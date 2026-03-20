import re
import sys
import json
import datetime

if len(sys.argv) < 2:
    sys.exit(0)
tag = sys.argv[1]

with open("build.json", encoding="utf-8") as f:
    build_data = json.load(f)
with open("README.md", encoding="utf-8") as f:
    readme = f.read()

for app, info in build_data.items():
    version = info["version"]
    rv_brand = info["rv_brand"]
    app_name = info["app_name"]

    badge_version = version.replace("-", ".").replace(" ", "")
    link_version = re.sub(r"\.+", ".", re.sub(r"[^a-zA-Z0-9@+\-_.]", ".", version.replace(" ", "")))
    summary_pattern = rf'<summary id="{app}"[^>]*>.*?</summary>'
    match = re.search(summary_pattern, readme, re.IGNORECASE | re.DOTALL)
    if not match:
        continue

    arch_pattern = r'(-(?:arm64-v8a|arm-v7a|all))'
    old_summary = match.group(0)
    new_summary = re.sub(
        rf'(href="[^"]*?/download/)[^"]*?{arch_pattern}\.apk',
        rf'\g<1>{tag}/{app_name}-{rv_brand}-v{link_version}\g<2>.apk',
        old_summary
    )
    new_summary = re.sub(
        rf'(href="[^"]*?/download/)[^"]*?{arch_pattern}\.zip',
        rf'\g<1>{tag}/{app_name}-{rv_brand}-module-v{link_version}\g<2>.zip',
        new_summary
    )
    new_summary = re.sub(r'(src="[^"]*?-v)\d[^"]*?(-gray\?)', rf'\g<1>{badge_version}\g<2>', new_summary)
    if new_summary != old_summary:
        readme = readme.replace(old_summary, new_summary)

    match = re.search(summary_pattern, readme, re.IGNORECASE | re.DOTALL)
    if not match:
        continue
    blockquote_match = re.search(r'<blockquote>\s*\n(.*?)\n</blockquote>', readme[match.end():], re.DOTALL)
    if not blockquote_match:
        continue

    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    new_content = f"\n\n[Release {current_date}](../../releases/tag/{tag})<br>\nPatches: {info.get('patches', '')}"
    if info.get("applied_patches"):
        for patch in info["applied_patches"]:
            if patch.strip():
                new_content += f"\n- {patch.strip()}"

    pos = match.end() + blockquote_match.start()
    readme = readme[:pos] + f"<blockquote>{new_content}\n</blockquote>" + readme[pos + len(blockquote_match.group(0)):]

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

print("✓ README updated")
