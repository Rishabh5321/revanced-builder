# [nvbangg/revanced-morphe-builder](https://github.com/nvbangg/revanced-morphe-builder)

> [!NOTE]
> Automated builds using GitHub Actions, with patch details and download links updated in README for ReVanced, Morphe & many other patches. Builds both modules and APKs. Updated daily.     
> ⭐ First build per app is recommended. Expand to view patch details.    
> 🔒 All release files are immutable, meaning they cannot be modified once published — even by me.   

<div align="center">

[![CI](https://img.shields.io/github/actions/workflow/status/nvbangg/revanced-morphe-builder/ci.yml?label=CI&logo=githubactions&logoColor=white)](https://github.com/nvbangg/revanced-morphe-builder/actions/workflows/ci.yml)　[![Releases](https://img.shields.io/github/downloads/nvbangg/revanced-morphe-builder/total?logo=data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjZmZmZmZmIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij48cGF0aCBkPSJNNSAyMGgxNHYtMkg1djJ6TTE5IDloLTRWM0g5djZINWw3IDcgNy03eiIvPjwvc3ZnPg==&label=Downloads)](https://github.com/nvbangg/revanced-morphe-builder/releases)　[![Stars](https://img.shields.io/github/stars/nvbangg/revanced-morphe-builder?label=Star%20this%20repo%20if%20useful%20⭐&logo=github)](https://github.com/nvbangg/revanced-morphe-builder)　[![Donate](https://img.shields.io/badge/Support-pink?style=social&logo=github-sponsors)](https://nvbangg.github.io/#donate)　[![Other Tools](https://img.shields.io/badge/%F0%9F%91%89%20Other%20Tools-nvbangg--tools-blue)](https://github.com/nvbangg/nvbangg-tools)
</div> 

<details>
<summary><b>✨ Features</b></summary>

- **🧩 Patches used in this repository:** 

[![MorpheApp](https://img.shields.io/github/license/MorpheApp/morphe-patches?label=MorpheApp)](https://github.com/MorpheApp/morphe-patches) [![ReVanced](https://img.shields.io/github/license/ReVanced/revanced-patches?label=ReVanced)](https://github.com/ReVanced/revanced-patches) [![hoo-dles](https://img.shields.io/github/license/hoo-dles/morphe-patches?label=hoo-dles)](https://github.com/hoo-dles/morphe-patches) [![RookieEnough](https://img.shields.io/github/license/RookieEnough/De-ReVanced?label=RookieEnough)](https://github.com/RookieEnough/De-ReVanced) [![anddea](https://img.shields.io/github/license/anddea/revanced-patches?label=anddea)](https://github.com/anddea/revanced-patches) [![Aunali321](https://img.shields.io/github/license/Aunali321/ReVancedExperiments?label=Aunali321)](https://github.com/Aunali321/ReVancedExperiments) [![crimera](https://img.shields.io/github/license/crimera/piko?label=crimera)](https://github.com/crimera/piko) [![jkennethcarino](https://img.shields.io/github/license/jkennethcarino/adobo?label=jkennethcarino)](https://github.com/jkennethcarino/adobo) [![AmpleReVanced](https://img.shields.io/github/license/AmpleReVanced/revanced-patches?label=AmpleReVanced)](https://github.com/AmpleReVanced/revanced-patches) 

- **💻 CLI used in this repository:** 
 
[![Morphe CLI](https://img.shields.io/github/license/MorpheApp/morphe-cli?label=Morphe%20CLI)](https://github.com/MorpheApp/morphe-cli) [![ReVanced CLI](https://img.shields.io/github/license/revanced/revanced-cli?label=ReVanced%20CLI)](https://github.com/revanced/revanced-cli) 

- ✅ Based on trusted code from [j-hc/revanced-magisk-module](https://github.com/j-hc/revanced-magisk-module) with transparent changes ([see diff](https://github.com/j-hc/revanced-magisk-module/compare/main...nvbangg:revanced-morphe-builder:main)), including main changes:
  - Automatically updates patch details and download links in the README
  - Automatically syncs with upstream
  - Supports automatic architecture selection and GitHub Releases download source
  - Fixes some issues with UI/config improvements
- Optimizes APKs and modules for size
- Modules  
  - recompile invalidated odex for faster usage
  - receive updates from Magisk app
  - do not break safetynet or trigger root detections
  - handle installation of the correct version of the stock app and all that
  - support Magisk and KernelSU

</details>

<details>
<summary><b>⬇️ Easily install and update apps (APK) with <a href="https://github.com/ImranR98/Obtainium/releases">Obtainium</a></b></summary>

- Download and install [Obtainium](https://github.com/ImranR98/Obtainium/releases)
- Add apps from this repository:

<img height="450" alt="image" src="https://github.com/user-attachments/assets/5a4b0c89-2a1e-41fb-a679-9104e9c9f294" />

- In step 2, Enter `https://github.com/nvbangg/revanced-morphe-builder`

  - MicroG-RE: `https://github.com/MorpheApp/MicroG-RE`
  - MicroG: `https://github.com/ReVanced/GmsCore`

- In step 3, enter the expression below for the app you want (except MicroG/MicroG-RE):

  - YouTube: `youtube-nvbangg`
  - YouTube Morphe: `youtube-morpheapp`
  - YouTube ReVanced: `youtube-revanced`
  - YouTube Anddea: `youtube-anddea`
  - YouTube Music Morphe: `youtube-music-morpheapp`
  - YouTube Music ReVanced: `youtube-music-revanced`
  - YouTube Music Anddea: `youtube-music-anddea`
  - Google Photos: `google-photos`

  <details>
  <summary>Other apps:</summary>

  - Facebook: `facebook`
  - Instagram: `instagram`
  - Threads: `threads`
  - Messenger: `messenger`
  - Viber: `viber`
  - TikTok: `tiktok`
  - Telegram: `telegram-aunali321`
  - Telegram Web: `telegram-web-aunali321`
  - X (Twitter): `x-crimera`
  - Amazon Shopping: `amazon-shopping`
  - Prime Video: `prime-video`
  - Disney+: `disney-plus`
  - Duolingo: `duolingo`
  - WPS Office: `wps-office`
  - SoundCloud HooDles: `soundcloud-hoo-dles`
  - SoundCloud DeReVanced: `soundcloud-rookieenough`
  - Twitch: `twitch`
  - Pandora: `pandora`
  - Reddit Morphe: `reddit-morpheapp`
  - Reddit Anddea: `reddit-anddea`
  - Google News: `google-news`
  - Gboard: `gboard`
  - Google Recorder: `google-recorder`
  - Photomath: `photomath`
  - KakaoTalk: `kakaotalk`
  - Crunchyroll: `crunchyroll`
  - Cricbuzz: `cricbuzz`
  - Tumblr: `tumblr`
  - MyFitnessPal: `myfitnesspal`
  - Strava: `strava`
  - ibis Paint X: `ibis-paint-x`
  - RAR: `rar`
  - Wallcraft: `wallcraft`
  - Nova Launcher: `nova-launcher`
  - Smart Launcher 6: `smart-launcher`
  - Proton VPN: `proton-vpn`
  - Sofascore: `sofascore`
  - Peacock TV: `peacock-tv`
  - Windy: `windy`
  - Cake: `cake`
  - Merriam Webster Dictionary: `merriam-webster`
  - Busuu: `busuu`

  </details>
</details>

<details>
<summary><b>📖 Guide</b></summary>

- **📦 Modules**
  - (Optional) Use [zygisk-detach](https://github.com/j-hc/zygisk-detach) to detach YouTube and YT Music from Play Store.
  - If you are having trouble with the classic mount method of the modules
    - **"Reflash needed"** error after reboots
    - **"Suspicious mount detected"** warnings from root detector apps

    You can consider using [rvmm-zygisk-mount](https://github.com/j-hc/rvmm-zygisk-mount)

- **⚙️ To include/exclude patches or patch other apps:**
  - Star the repo :eyes:
  - Fork this repo or use it as a [template](https://github.com/nvbangg/revanced-morphe-builder/generate)
  - Customize [`config.toml`](./config.toml) (see [`CONFIG.md`](./CONFIG.md) for more detailed explanations)
  - Run the build [workflow](../../actions/workflows/build.yml)
  - Grab your modules and APKs from [releases](../../releases) or download from the README

- **🏷️ App template for automated README updates:**
  - Fields automatically updated by the script:
    - Download links: `/releases/download/.../...-<arch>.<ext>`
    - Badge version: `-v<number>...-gray?`
    - Patch details: inside `<blockquote>...</blockquote>`
  - The script scans all `<details>` blocks with `id="App-Name"` in the README and updates them.

```md
<details>
<summary id="App-Name">...</summary>
...
<blockquote>
...
</blockquote>
</details>
```

- **🛠️ Building Locally**
  - On Termux
  ```console
  bash <(curl -sSf https://raw.githubusercontent.com/nvbangg/revanced-morphe-builder/main/build-termux.sh)
  ```

  - On Linux
  ```console
  $ git clone https://github.com/nvbangg/revanced-morphe-builder --depth 1
  $ cd revanced-morphe-builder
  $ ./build.sh
  ```

</details>

---
### MicroG

> [!IMPORTANT]
> You need to install **MicroG-RE** (recommended) or **MicroG**, then sign in to your **Google account** to use **YouTube**, **YouTube Music**, and **Google Photos**.

[![MicroG-RE](https://img.shields.io/github/v/release/MorpheApp/MicroG-RE?label=MicroG-RE)](https://github.com/MorpheApp/MicroG-RE/releases)　[![MicroG](https://img.shields.io/github/v/release/ReVanced/GmsCore?label=MicroG)](https://github.com/ReVanced/GmsCore/releases)

---
### [YouTube](https://play.google.com/store/apps/details?id=com.google.android.youtube)

- A Morphe-based build with only essential patches, keeping YouTube close to the original while adding ad blocking, SponsorBlock, and other essential features.
Great for beginners. 

<details>
<summary id="YouTube">&emsp;<a href="../../releases/download/46/youtube-nvbangg-v20.45.36-arm64-v8a.apk"><img src="https://img.shields.io/badge/YouTube-v20.45.36-gray?labelColor=FF0000&logo=YouTube&logoColor=white"></a></summary>

[Module (.zip)](../../releases/download/46/youtube-nvbangg-module-v20.45.36-arm64-v8a.zip)
<blockquote>

[Release 2026-04-10](../../releases/tag/46)<br>
Patches: [MorpheApp/patches-1.23.0.mpp](https://github.com/MorpheApp/morphe-patches/releases/tag/v1.23.0)
- Bypass URL redirects
- Disable Shorts resuming on startup
- Downloads
- GmsCore support
- Hide Shorts components
- Hide ads
- Open links externally
- Override YouTube Music actions
- Playback speed
- Remove background playback restrictions
- Sanitize sharing links
- Shorts autoplay
- SponsorBlock
- Swipe controls
- Video ads
- Video quality
</blockquote>
</details>

**Other builds:**

<details>
<summary id="YouTube-Morphe">&emsp;<a href="../../releases/download/46/youtube-morpheapp-v20.45.36-arm64-v8a.apk"><img src="https://img.shields.io/badge/Morphe-v20.45.36-gray?labelColor=FF0000&logo=YouTube&logoColor=white"></a></summary>
     
[Module (.zip)](../../releases/download/46/youtube-morpheapp-module-v20.45.36-arm64-v8a.zip)
<blockquote>

[Release 2026-04-10](../../releases/tag/46)<br>
Patches: [MorpheApp/patches-1.23.0.mpp](https://github.com/MorpheApp/morphe-patches/releases/tag/v1.23.0)
- Alternative thumbnails
- Ambient mode
- Bypass URL redirects
- Bypass image region restrictions
- Captions
- Change form factor
- Change header
- Change start page
- Check watch history domain name resolution
- Copy video URL
- Custom branding
- Custom player overlay opacity
- Disable DRC audio
- Disable QUIC protocol
- Disable Shorts resuming on startup
- Disable double tap actions
- Disable haptic feedback
- Disable layout updates
- Disable player popup panels
- Disable rolling number animations
- Disable sign in to TV popup
- Disable video codecs
- Double tap to seek
- Downloads
- Enable debugging
- Exit fullscreen mode
- Force original audio
- GmsCore support
- Hide Shorts components
- Hide ads
- Hide autoplay preview
- Hide end screen cards
- Hide end screen suggested video
- Hide info cards
- Hide layout components
- Hide player flyout menu components
- Hide player overlay buttons
- Hide related video overlay
- Hide related videos
- Hide timestamp
- Hide video action buttons
- Loop video
- Miniplayer
- Navigation bar
- Open Shorts in regular player
- Open links externally
- Open system share sheet
- Open videos fullscreen
- Override YouTube Music actions
- Play all
- Playback speed
- Reload video
- Remove background playback restrictions
- Remove viewer discretion dialog
- Return YouTube Dislike
- Sanitize sharing links
- Seekbar
- Shorts autoplay
- SponsorBlock
- Spoof app version
- Spoof device dimensions
- Spoof video streams
- Swipe controls
- Theme
- Video ads
- Video quality
</blockquote>
</details>

<details>
<summary id="YouTube-ReVanced">&emsp;<a href="../../releases/download/31/youtube-revanced-v20.40.45-arm64-v8a.apk"><img src="https://img.shields.io/badge/ReVanced-v20.40.45-gray?labelColor=FF0000&logo=YouTube&logoColor=white"></a></summary>
<blockquote>

[Release 2026-03-20](../../releases/tag/31)<br>
Patches: ReVanced/patches-6.1.0.rvp
- Add more double tap to seek length options
- Alternative thumbnails
- Announcements
- Bypass URL redirects
- Bypass image region restrictions
- Change form factor
- Change header
- Change start page
- Check watch history domain name resolution
- Copy video URL
- Custom player overlay opacity
- Disable auto captions
- Disable double tap actions
- Disable fullscreen ambient mode
- Disable haptic feedback
- Disable player popup panels
- Disable resuming Shorts on startup
- Disable rolling number animations
- Disable sign in to TV popup
- Disable video codecs
- Downloads
- Enable debugging
- Exit fullscreen
- Force original audio
- GmsCore support
- Hide Shorts components
- Hide ads
- Hide autoplay preview
- Hide end screen cards
- Hide end screen suggested video
- Hide info cards
- Hide layout components
- Hide player flyout menu items
- Hide player overlay buttons
- Hide related video overlay
- Hide timestamp
- Hide video action buttons
- Loop video
- Miniplayer
- Navigation bar
- Open Shorts in regular player
- Open links externally
- Open videos fullscreen
- Pause on audio interrupt
- Playback speed
- Remove background playback restrictions
- Remove viewer discretion dialog
- Return YouTube Dislike
- Sanitize sharing links
- Seekbar
- Shorts autoplay
- SponsorBlock
- Spoof app version
- Spoof device dimensions
- Spoof video streams
- Swipe controls
- Theme
- Video ads
- Video quality
- Custom branding
</blockquote>
</details>

<details>
<summary id="YouTube-Anddea">&emsp;<a href="../../releases/download/45/youtube-anddea-v20.05.46-arm64-v8a.apk"><img src="https://img.shields.io/badge/Anddea-v20.05.46-gray?labelColor=FF0000&logo=YouTube&logoColor=white"></a></summary>

[Module (.zip)](../../releases/download/45/youtube-anddea-module-v20.05.46-arm64-v8a.zip)
<blockquote>

[Release 2026-04-09](../../releases/tag/45)<br>
Patches: [anddea/patches-4.0.0.mpp](https://github.com/anddea/revanced-patches/releases/tag/v4.0.0)
- Alternative thumbnails
- Ambient mode control
- Bypass URL redirects
- Bypass image region restrictions
- Change form factor
- Change player flyout menu toggles
- Change share sheet
- Change start page
- Custom Shorts action buttons
- Custom double tap length
- Description components
- Disable QUIC protocol
- Disable forced auto audio tracks
- Disable forced auto captions
- Disable haptic feedback
- Disable layout updates
- Disable resuming Miniplayer on startup
- Disable resuming Shorts on startup
- Disable sign in to TV popup
- Disable splash animation
- Enable debug logging
- Enable gradient loading screen
- Force player buttons background
- Fullscreen components
- GmsCore support
- Hide accessibility controls dialog
- Hide action buttons
- Hide ads
- Hide comments components
- Hide feed components
- Hide feed flyout menu
- Hide layout components
- Hide player buttons
- Hide player flyout menu
- Hook YouTube Music actions
- Hook download actions
- Miniplayer
- Navigation bar components
- Open links externally
- Overlay buttons
- Player components
- Remove background playback restrictions
- Remove viewer discretion dialog
- Return YouTube Dislike
- Return YouTube Username
- Sanitize sharing links
- Seekbar components
- Set transcript cookies
- Shorts components
- Snack bar components
- SponsorBlock
- Spoof app version
- Spoof watch history
- Swipe controls
- Toolbar components
- Translations for YouTube
- Video playback
- Voice Over Translation
- Visual preferences icons for YouTube
- Reload video
- Settings for YouTube
</blockquote>
</details>

---
### [YouTube Music](https://play.google.com/store/apps/details?id=com.google.android.apps.youtube.music)

<details>
<summary id="YouTube-Music-Morphe">&emsp;<a href="../../releases/download/46/youtube-music-morpheapp-v8.44.54-arm64-v8a.apk"><img src="https://img.shields.io/badge/Morphe-v8.44.54-gray?labelColor=FF0000&logo=youtube-music&logoColor=white"></a></summary>

[Module (.zip)](../../releases/download/46/youtube-music-morpheapp-module-v8.44.54-arm64-v8a.zip)
<blockquote>

[Release 2026-04-10](../../releases/tag/46)<br>
Patches: [MorpheApp/patches-1.23.0.mpp](https://github.com/MorpheApp/morphe-patches/releases/tag/v1.23.0)
- Bypass certificate checks
- Change header
- Change miniplayer color
- Change start page
- Check watch history domain name resolution
- Custom branding
- Disable DRC audio
- Disable QUIC protocol
- Enable debugging
- Enable exclusive audio playback
- Enable forced miniplayer
- Force original audio
- GmsCore support
- Hide 'Get Music Premium'
- Hide buttons
- Hide category bar
- Hide music video ads
- Miniplayer previous and next buttons
- Navigation bar
- Permanent repeat
- Remove background playback restrictions
- Sanitize sharing links
- Spoof video streams
- Theme
</blockquote>
</details>

**Other builds:**

<details>
<summary id="YouTube-Music-ReVanced">&emsp;<a href="../../releases/download/31/youtube-music-revanced-v8.40.54-arm64-v8a.apk"><img src="https://img.shields.io/badge/ReVanced-v8.40.54-gray?labelColor=FF0000&logo=youtube-music&logoColor=white"></a></summary>
<blockquote>

[Release 2026-03-20](../../releases/tag/31)<br>
Patches: ReVanced/patches-6.1.0.rvp
- Change miniplayer color
- Check watch history domain name resolution
- Enable debugging
- Enable exclusive audio playback
- Force original audio
- GmsCore support
- Hide 'Get Music Premium'
- Hide buttons
- Hide category bar
- Hide layout components
- Hide music video ads
- Navigation bar
- Permanent repeat
- Remove background playback restrictions
- Sanitize sharing links
- Spoof video streams
- Theme
- Unlock Android Auto Media Browser
</blockquote>
</details>

<details>
<summary id="YouTube-Music-Anddea">&emsp;<a href="../../releases/download/45/youtube-music-anddea-v8.30.54-arm64-v8a.apk"><img src="https://img.shields.io/badge/Anddea-v8.30.54-gray?labelColor=FF0000&logo=youtube-music&logoColor=white"></a></summary>

[Module (.zip)](../../releases/download/45/youtube-music-anddea-module-v8.30.54-arm64-v8a.zip)
<blockquote>

[Release 2026-04-09](../../releases/tag/45)<br>
Patches: [anddea/patches-4.0.0.mpp](https://github.com/anddea/revanced-patches/releases/tag/v4.0.0)
- Bitrate default value
- Bypass image region restrictions
- Certificate spoof
- Change share sheet
- Change start page
- Dark theme
- Disable Cairo splash animation
- Disable QUIC protocol
- Disable dislike redirection
- Disable forced auto audio tracks
- Disable forced auto captions
- Enable landscape mode
- Flyout menu components
- GmsCore support
- Hide account components
- Hide action bar components
- Hide ads
- Hide layout components
- Navigation bar components
- Player components
- Remove background playback restrictions
- Remove viewer discretion dialog
- Restore old style library shelf
- Return YouTube Dislike
- Return YouTube Username
- Sanitize sharing links
- SponsorBlock
- Spoof app version for lyrics
- Translations for YouTube Music
- Video playback
- Watch history
- Visual preferences icons for YouTube Music
- Settings for YouTube Music
</blockquote>
</details>

---
### [Google Photos](https://play.google.com/store/apps/details?id=com.google.android.apps.photos)

<details>
<summary id="Google-Photos">&emsp;<a href="../../releases/download/48/google-photos-rookieenough-v7.68.0.884121604-all.apk"><img src="https://img.shields.io/badge/Google_Photos-v7.68.0.884121604-gray?labelColor=FBBC04&logo=google-photos&logoColor=000000"></a></summary>

[Module (.zip)](../../releases/download/48/google-photos-rookieenough-module-v7.68.0.884121604-all.zip)
<blockquote>

[Release 2026-04-12](../../releases/tag/48)<br>
Patches: [RookieEnough/patches-1.0.3.mpp](https://github.com/RookieEnough/De-ReVanced/releases/tag/v1.0.3)
- GmsCore support
- Spoof features
</blockquote>
</details>

---
### [Facebook](https://play.google.com/store/apps/details?id=com.facebook.katana)

<details>
<summary id="Facebook">&emsp;<a href="../../releases/download/48/facebook-rookieenough-v490.0.0.63.82-arm64-v8a.apk"><img src="https://img.shields.io/badge/Facebook-v490.0.0.63.82-gray?labelColor=1877F2&logo=Facebook&logoColor=white"></a></summary>
 
[Module (.zip)](../../releases/download/48/facebook-rookieenough-module-v490.0.0.63.82-arm64-v8a.zip)
<blockquote>

[Release 2026-04-12](../../releases/tag/48)<br>
Patches: [RookieEnough/patches-1.0.3.mpp](https://github.com/RookieEnough/De-ReVanced/releases/tag/v1.0.3)
- Hide 'Sponsored Stories'
- Hide story ads
</blockquote>
</details>

---
### [Instagram](https://play.google.com/store/apps/details?id=com.instagram.android)

<details>
<summary id="Instagram">&emsp;<a href="../../releases/download/49/instagram-crimera-v423.0.0.47.66-arm64-v8a.apk"><img src="https://img.shields.io/badge/Instagram-v423.0.0.47.66-gray?labelColor=E4405F&logo=Instagram&logoColor=white"></a></summary>
   
[Module (.zip)](../../releases/download/49/instagram-crimera-module-v423.0.0.47.66-arm64-v8a.zip)
<blockquote>

[Release 2026-04-13](../../releases/tag/49)<br>
Patches: [crimera/patches-3.2.0-dev.5.mpp](https://github.com/crimera/piko/releases/tag/v3.2.0-dev.5)
- Add settings
- Change version code
- Customise story timestamp
- Disable ads
- Disable analytics
- Disable comments
- Disable discover people
- Disable explore
- Disable stories
- Disable story flipping
- Download media
- Follow back indicator
- Hide group creation button on sharesheet
- Hide navigation buttons
- Hide reshare button
- Hide stories tray
- Hide suggested content
- Improve image viewing
- Limit feed to following profiles
- Make ephemeral media permanent
- Open links externally
- Remove build expired popup
- Sanitize share links
- Unlock developer options
- View live anonymously
- View stories anonymously
- View story mentions
</blockquote>
</details>

---
### [Threads](https://play.google.com/store/apps/details?id=com.instagram.barcelona)

<details>
<summary id="Threads">&emsp;<a href="../../releases/download/48/threads-rookieenough-v382.0.0.51.85-arm64-v8a.apk"><img src="https://img.shields.io/badge/Threads-v382.0.0.51.85-gray?labelColor=0F1419&logo=Threads&logoColor=white"></a></summary>
 
[Module (.zip)](../../releases/download/48/threads-rookieenough-module-v382.0.0.51.85-arm64-v8a.zip)
<blockquote>

[Release 2026-04-12](../../releases/tag/48)<br>
Patches: [RookieEnough/patches-1.0.3.mpp](https://github.com/RookieEnough/De-ReVanced/releases/tag/v1.0.3)
- Hide ads
</blockquote>
</details>

---
### [Messenger](https://play.google.com/store/apps/details?id=com.facebook.orca)

<details>
<summary id="Messenger">&emsp;<a href="../../releases/download/36/messenger-rookieenough-v552.0.0.44.65-arm64-v8a.apk"><img src="https://img.shields.io/badge/Messenger-v552.0.0.44.65-gray?labelColor=00B2FF&logo=Messenger&logoColor=white"></a></summary>
 
[Module (.zip)](../../releases/download/36/messenger-rookieenough-module-v552.0.0.44.65-arm64-v8a.zip)
<blockquote>

[Release 2026-03-25](../../releases/tag/36)<br>
Patches: RookieEnough/patches-1.0.1.mpp
- Disable typing indicator
- Hide Facebook button
- Hide inbox ads
- Hide inbox subtabs
- Remove Meta AI
</blockquote>
</details>

---
### [Viber](https://play.google.com/store/apps/details?id=com.viber.voip)

<details>
<summary id="Viber">&emsp;<a href="../../releases/download/48/viber-rookieenough-v26.1.2.0-all.apk"><img src="https://img.shields.io/badge/Viber-v26.1.2.0-gray?labelColor=665CAC&logo=Viber&logoColor=white"></a></summary>
 
[Module (.zip)](../../releases/download/48/viber-rookieenough-module-v26.1.2.0-all.zip)
<blockquote>

[Release 2026-04-12](../../releases/tag/48)<br>
Patches: [RookieEnough/patches-1.0.3.mpp](https://github.com/RookieEnough/De-ReVanced/releases/tag/v1.0.3)
- Hide Ads
</blockquote>
</details>

---
### [TikTok](https://play.google.com/store/apps/details?id=com.ss.android.ugc.trill)

<details>
<summary id="TikTok">&emsp;<a href="../../releases/download/48/tiktok-rookieenough-v43.8.3-all.apk"><img src="https://img.shields.io/badge/TikTok-v43.8.3-gray?labelColor=252525&logo=TikTok&logoColor=white"></a></summary>

[Module (.zip)](../../releases/download/48/tiktok-rookieenough-module-v43.8.3-all.zip)
<blockquote>

[Release 2026-04-12](../../releases/tag/48)<br>
Patches: [RookieEnough/patches-1.0.3.mpp](https://github.com/RookieEnough/De-ReVanced/releases/tag/v1.0.3)
- Disable login requirement
- Downloads
- Feed filter
- Fix Google login
- Remember clear display
- Sanitize sharing links
- Show seekbar
</blockquote>
</details>

---
### [Telegram](https://play.google.com/store/apps/details?id=org.telegram.messenger)

<details>
<summary id="Telegram">&emsp;<a href="../../releases/download/43/telegram-aunali321-v12.6.3-arm64-v8a.apk"><img src="https://img.shields.io/badge/Telegram-v12.6.3-gray?labelColor=2CA5E0&logo=telegram&logoColor=white"></a></summary>

[Module (.zip)](../../releases/download/43/telegram-aunali321-module-v12.6.3-arm64-v8a.zip)
<blockquote>

[Release 2026-04-07](../../releases/tag/43)<br>
Patches: [Aunali321/patches-2.0.0.rvp](https://github.com/Aunali321/ReVancedExperiments/releases/tag/v2.0.0)
- Bypass Integrity
- Disable Auto Update
- Download Speed Boost
- Hide sponsored ads
- Hide typing indicator
- Unlock Pro
</blockquote>
</details>


[**Web version:**](https://telegram.org/android)

<details>
<summary id="Telegram-Web">&emsp;<a href="../../releases/download/43/telegram-web-aunali321-v12.6.3-arm64-v8a.apk"><img src="https://img.shields.io/badge/Telegram_Web-v12.6.3-gray?labelColor=2CA5E0&logo=telegram&logoColor=white"></a></summary>

[Module (.zip)](../../releases/download/43/telegram-web-aunali321-module-v12.6.3-arm64-v8a.zip)
<blockquote>

[Release 2026-04-07](../../releases/tag/43)<br>
Patches: [Aunali321/patches-2.0.0.rvp](https://github.com/Aunali321/ReVancedExperiments/releases/tag/v2.0.0)
- Bypass Integrity
- Disable Auto Update
- Download Speed Boost
- Hide sponsored ads
- Hide typing indicator
- Unlock Pro
</blockquote>
</details>

---
### [X (Twitter)](https://play.google.com/store/apps/details?id=com.twitter.android)

<details>
<summary id="X">&emsp;<a href="../../releases/download/49/x-crimera-v11.81.0-release.0-all.apk"><img src="https://img.shields.io/badge/Twitter-v11.81.0.release.0-gray?labelColor=0F1419&logo=X&logoColor=white"></a></summary>

[Module (.zip)](../../releases/download/49/x-crimera-module-v11.81.0-release.0-all.zip)
<blockquote>

[Release 2026-04-13](../../releases/tag/49)<br>
Patches: [crimera/patches-3.2.0-dev.5.mpp](https://github.com/crimera/piko/releases/tag/v3.2.0-dev.5)
- Add ability to copy media link
- Change app icon
- Change version code
- Clear tracking params
- Control video auto scroll
- Custom download folder
- Custom emoji font
- Custom font
- Custom sharing domain
- Customise post font size
- Customize Inline action Bar items
- Customize Navigation Bar items
- Customize default reply sorting
- Customize explore tabs
- Customize notification tabs
- Customize profile tabs
- Customize search suggestions
- Customize search tab items
- Customize side bar items
- Customize timeline top bar
- Delete from database
- Disable auto timeline scroll on launch
- Disable chirp font
- Download patch
- Enable PiP mode automatically
- Enable Undo Posts
- Enable debug menu for posts
- Enable force HD videos
- Force enable translate
- Handle custom twitter links
- Hide Banner
- Hide Community Notes
- Hide FAB
- Hide FAB Menu Buttons
- Hide Live Threads
- Hide Recommended Users
- Hide badges from navigation bar icons
- Hide bookmark icon in timeline
- Hide community badges
- Hide followed by context
- Hide hidden replies
- Hide immersive player
- Hide nudge button
- Hide post metrics
- Hide promote button
- Hide recommendation items
- Hook feature flag
- Import/Export login token
- Legacy share links
- Log server response
- Native downloader
- Native reader mode
- Native translator
- No shortened URL
- Pause search suggestions
- Remove Ads
- Remove premium upsell
- Remove search suggestions
- Remove view count
- Round off numbers
- Selectable Text
- Share Tweet as Image
- Show changelogs
- Show poll results
- Show post source label
- Show sensitive media
</blockquote>
</details>

---
### [Amazon Shopping](https://play.google.com/store/apps/details?id=com.amazon.mShop.android.shopping)

<details>
<summary id="Amazon-Shopping">&emsp;<a href="../../releases/download/48/amazon-shopping-rookieenough-v32.7.0.100-all.apk"><img src="https://img.shields.io/badge/Amazon_Shopping-v32.7.0.100-gray?labelColor=FF9900&logo=amazon&logoColor=000000"></a></summary>

[Module (.zip)](../../releases/download/48/amazon-shopping-rookieenough-module-v32.7.0.100-all.zip)
<blockquote>

[Release 2026-04-12](../../releases/tag/48)<br>
Patches: [RookieEnough/patches-1.0.3.mpp](https://github.com/RookieEnough/De-ReVanced/releases/tag/v1.0.3)
- Always allow deep-linking
</blockquote>
</details>

---
### [Prime Video](https://play.google.com/store/apps/details?id=com.amazon.avod.thirdpartyclient)

<details>
<summary id="Prime-Video">&emsp;<a href="../../releases/download/48/prime-video-hoo-dles-v3.0.447.757-all.apk"><img src="https://img.shields.io/badge/Prime_Video-v3.0.447.757-gray?labelColor=00A8E1&logo=Prime-Video&logoColor=white"></a></summary>

[Module (.zip)](../../releases/download/48/prime-video-hoo-dles-module-v3.0.447.757-all.zip)
<blockquote>

[Release 2026-04-12](../../releases/tag/48)<br>
Patches: [hoo-dles/patches-1.23.0.mpp](https://github.com/hoo-dles/morphe-patches/releases/tag/v1.23.0)
- Enable speed control
- Rename shared permissions
- Skip ads
</blockquote>
</details>

---
### [Disney+](https://play.google.com/store/apps/details?id=com.disney.disneyplus)

<details>
<summary id="Disney-Plus">&emsp;<a href="../../releases/download/48/disney-plus-rookieenough-v26.5.1+rc1-2026.04.08-all.apk"><img src="https://img.shields.io/badge/Disney+-v26.5.1+rc1.2026.04.08-gray?labelColor=113CCF&logo=Disney%2B&logoColor=white"></a></summary>

[Module (.zip)](../../releases/download/48/disney-plus-rookieenough-module-v26.5.1+rc1-2026.04.08-all.zip)
<blockquote>

[Release 2026-04-12](../../releases/tag/48)<br>
Patches: [RookieEnough/patches-1.0.3.mpp](https://github.com/RookieEnough/De-ReVanced/releases/tag/v1.0.3)
- Skip ads
</blockquote>
</details>

---
### [Duolingo](https://play.google.com/store/apps/details?id=com.duolingo)

<details>
<summary id="Duolingo">&emsp;<a href="../../releases/download/48/duolingo-hoo-dles-v6.74.4-all.apk"><img src="https://img.shields.io/badge/Duolingo-v6.74.4-gray?labelColor=4DC730&logo=Duolingo&logoColor=white"></a></summary>

[Module (.zip)](../../releases/download/48/duolingo-hoo-dles-module-v6.74.4-all.zip)
<blockquote>

[Release 2026-04-12](../../releases/tag/48)<br>
Patches: [hoo-dles/patches-1.23.0.mpp](https://github.com/hoo-dles/morphe-patches/releases/tag/v1.23.0)
- Disable Login Integrity
- Enable Premium
</blockquote>
</details>

---
### [WPS Office](https://play.google.com/store/apps/details?id=cn.wps.moffice_eng)

<details>
<summary id="WPS-Office">&emsp;<a href="../../releases/download/48/wps-office-hoo-dles-v18.12.1-all.apk"><img src="https://img.shields.io/badge/WPS_Office-v18.12.1-gray?labelColor=C03426&logo=wpsoffice&logoColor=white"></a></summary>

[Module (.zip)](../../releases/download/48/wps-office-hoo-dles-module-v18.12.1-all.zip)
<blockquote>

[Release 2026-04-12](../../releases/tag/48)<br>
Patches: [hoo-dles/patches-1.23.0.mpp](https://github.com/hoo-dles/morphe-patches/releases/tag/v1.23.0)
- Disable anti-tamper
- Enable Pro
</blockquote>
</details>

---
### [SoundCloud](https://play.google.com/store/apps/details?id=com.soundcloud.android)

<details>
<summary id="SoundCloud-HooDles">&emsp;<a href="../../releases/download/48/soundcloud-hoo-dles-v2026.03.20-release-all.apk"><img src="https://img.shields.io/badge/HooDles-v2026.03.20.release-gray?labelColor=FF5500&logo=SoundCloud&logoColor=white"></a></summary>

[Module (.zip)](../../releases/download/48/soundcloud-hoo-dles-module-v2026.03.20-release-all.zip)
<blockquote>

[Release 2026-04-12](../../releases/tag/48)<br>
Patches: [hoo-dles/patches-1.23.0.mpp](https://github.com/hoo-dles/morphe-patches/releases/tag/v1.23.0)
- Disable telemetry
- Enable SoundCloud Go+
</blockquote>
</details>

**Other builds:**

<details>
<summary id="SoundCloud-DeReVanced">&emsp;<a href="../../releases/download/48/soundcloud-rookieenough-v2025.05.27-release-all.apk"><img src="https://img.shields.io/badge/DeReVanced-v2025.05.27.release-gray?labelColor=FF5500&logo=SoundCloud&logoColor=white"></a></summary>

[Module (.zip)](../../releases/download/48/soundcloud-rookieenough-module-v2025.05.27-release-all.zip)
<blockquote>

[Release 2026-04-12](../../releases/tag/48)<br>
Patches: [RookieEnough/patches-1.0.3.mpp](https://github.com/RookieEnough/De-ReVanced/releases/tag/v1.0.3)
- Disable telemetry
- Enable offline sync
- Hide ads
</blockquote>
</details>

---
### [Twitch](https://play.google.com/store/apps/details?id=tv.twitch.android.app)

<details>
<summary id="Twitch">&emsp;<a href="../../releases/download/31/twitch-revanced-v16.9.1-arm64-v8a.apk"><img src="https://img.shields.io/badge/Twitch-v16.9.1-gray?labelColor=9146FF&logo=Twitch&logoColor=white"></a></summary>

[Module (.zip)](../../releases/download/0/twitch-revanced-module-v16.9.1-arm64-v8a.zip)
<blockquote>

[Release 2026-03-20](../../releases/tag/31)<br>
Patches: ReVanced/patches-6.1.0.rvp
- Auto claim channel points
- Block audio ads
- Block embedded ads
- Block video ads
- Show deleted messages
- Settings
</blockquote>
</details>

---
### [Pandora](https://play.google.com/store/apps/details?id=com.pandora.android)

<details>
<summary id="Pandora">&emsp;<a href="../../releases/download/48/pandora-hoo-dles-v2602.1-arm64-v8a.apk"><img src="https://img.shields.io/badge/Pandora-v2602.1-gray?labelColor=3668FF&logo=Pandora&logoColor=white"></a></summary>

[Module (.zip)](../../releases/download/48/pandora-hoo-dles-module-v2602.1-arm64-v8a.zip)
<blockquote>

[Release 2026-04-12](../../releases/tag/48)<br>
Patches: [hoo-dles/patches-1.23.0.mpp](https://github.com/hoo-dles/morphe-patches/releases/tag/v1.23.0)
- Disable ads
- Unlimited skips
</blockquote>
</details>

---
### [Reddit](https://play.google.com/store/apps/details?id=com.reddit.frontpage)

<details>
<summary id="Reddit-Morphe">&emsp;<a href="../../releases/download/46/reddit-morpheapp-v2026.04.0-arm64-v8a.apk"><img src="https://img.shields.io/badge/Morphe-v2026.04.0-gray?labelColor=FF4500&logo=Reddit&logoColor=white"></a></summary>

[Module (.zip)](../../releases/download/46/reddit-morpheapp-module-v2026.04.0-arm64-v8a.zip)
<blockquote>

[Release 2026-04-10](../../releases/tag/46)<br>
Patches: [MorpheApp/patches-1.23.0.mpp](https://github.com/MorpheApp/morphe-patches/releases/tag/v1.23.0)
- Disable modern home
- Disable screenshot popup
- Hide Trending Today shelf
- Hide ads
- Hide navigation buttons
- Hide recommended communities shelf
- Hide sidebar components
- Open links directly
- Remove subreddit dialog
- Sanitize sharing links
- Show view count
- Spoof signature
</blockquote>
</details>

**Other builds:**

<details>
<summary id="Reddit-Anddea">&emsp;<a href="../../releases/download/45/reddit-anddea-v2025.12.1-arm64-v8a.apk"><img src="https://img.shields.io/badge/Anddea-v2025.12.1-gray?labelColor=FF4500&logo=Reddit&logoColor=white"></a></summary>

[Module (.zip)](../../releases/download/45/reddit-anddea-module-v2025.12.1-arm64-v8a.zip)
<blockquote>

[Release 2026-04-09](../../releases/tag/45)<br>
Patches: [anddea/patches-4.0.0.mpp](https://github.com/anddea/revanced-patches/releases/tag/v4.0.0)
- Disable screenshot popup
- Hide Recently Visited shelf
- Hide Trending Today shelf
- Hide ads
- Hide navigation buttons
- Hide recommended communities shelf
- Open links directly
- Open links externally
- Premium icon
- Remove subreddit dialog
- Sanitize sharing links
- Settings for Reddit
- Translations for Reddit
</blockquote>
</details>

---
### [Google News](https://play.google.com/store/apps/details?id=com.google.android.apps.magazines)

<details>
<summary id="Google-News">&emsp;<a href="../../releases/download/48/google-news-rookieenough-v5.108.0.644447823-all.apk"><img src="https://img.shields.io/badge/Google_News-v5.108.0.644447823-gray?labelColor=4285F4&logo=Google&logoColor=white"></a></summary>

[Module (.zip)](../../releases/download/43/google-news-rookieenough-module-v5.108.0.644447823-arm64-v8a.zip)
<blockquote>

[Release 2026-04-12](../../releases/tag/48)<br>
Patches: [RookieEnough/patches-1.0.3.mpp](https://github.com/RookieEnough/De-ReVanced/releases/tag/v1.0.3)
- Enable CustomTabs
- GmsCore support
</blockquote>
</details>

---
### [Gboard](https://play.google.com/store/apps/details?id=com.google.android.inputmethod.latin)

<details>
<summary id="Gboard">&emsp;<a href="../../releases/download/43/gboard-jkennethcarino-v17.0.12.880768217-release-arm64-v8a-arm64-v8a.apk"><img src="https://img.shields.io/badge/Gboard-v17.0.12.880768217.release.arm64.v8a-gray?labelColor=4285F4&logo=Google&logoColor=white"></a></summary>
   
[Module (.zip)](../../releases/download/43/gboard-jkennethcarino-module-v17.0.12.880768217-release-arm64-v8a-arm64-v8a.zip)
<blockquote>

[Release 2026-04-07](../../releases/tag/43)<br>
Patches: [jkennethcarino/patches-1.0.0.mpp](https://github.com/jkennethcarino/adobo/releases/tag/v1.0.0)
- Always-incognito mode
- Enable OCR feature
- Enable Undo feature
- Enable clipboard in incognito
</blockquote>
</details>

---
### [Google Recorder](https://play.google.com/store/apps/details?id=com.google.android.apps.recorder)

<details>
<summary id="Google-Recorder">&emsp;<a href="../../releases/download/48/google-recorder-rookieenough-v4.2.20260307.895737626-arm64-v8a.apk"><img src="https://img.shields.io/badge/Google_Recorder-v4.2.20260307.895737626-gray?labelColor=F44336&logo=google&logoColor=white"></a></summary>
<blockquote>

[Release 2026-04-12](../../releases/tag/48)<br>
Patches: [RookieEnough/patches-1.0.3.mpp](https://github.com/RookieEnough/De-ReVanced/releases/tag/v1.0.3)
- Remove device restrictions
</blockquote>
</details>

---
### [Photomath](https://play.google.com/store/apps/details?id=com.microblink.photomath)

<details>
<summary id="Photomath">&emsp;<a href="../../releases/download/48/photomath-rookieenough-v8.47.1-all.apk"><img src="https://img.shields.io/badge/Photomath-v8.47.1-gray?labelColor=DA2323&logo=google&logoColor=white"></a></summary>

[Module (.zip)](../../releases/download/48/photomath-rookieenough-module-v8.47.1-all.zip)
<blockquote>

[Release 2026-04-12](../../releases/tag/48)<br>
Patches: [RookieEnough/patches-1.0.3.mpp](https://github.com/RookieEnough/De-ReVanced/releases/tag/v1.0.3)
- Hide update popup
- Spoof device ID
- Unlock plus
</blockquote>
</details>

---
### [KakaoTalk](https://play.google.com/store/apps/details?id=com.kakao.talk)

<details>
<summary id="KakaoTalk">&emsp;<a href="../../releases/download/48/kakaotalk-amplerevanced-v26.2.2-all.apk"><img src="https://img.shields.io/badge/KakaoTalk-v26.2.2-gray?labelColor=FEE500&logo=kakaotalk&logoColor=000000"></a></summary>

[Module (.zip)](../../releases/download/48/kakaotalk-amplerevanced-module-v26.2.2-all.zip)
<blockquote>

[Release 2026-04-12](../../releases/tag/48)<br>
Patches: [AmpleReVanced/patches-1.0.0-dev.11.mpp](https://github.com/AmpleReVanced/revanced-patches/releases/tag/v1.0.0-dev.11)
- Add settings resources
- Add settings tab
- Allow Hide on Any Chat
- Allow reply to feed
- Always Show Kick Button
- Bypass input mention limit in non-multichat
- Change model
- Default external browser
- Disable 300+ unread limit
- Disable 99 unread limit
- Disable ChatRoomAdController
- Disable Collapse Button
- Disable Community Tab
- Disable Friend Feed tab
- Disable Friend Lists ad
- Disable S2Event
- Disable SDK Tracker
- Disable Sentry
- Disable Talk Share Log
- Disable chat room list ad
- Disable verifying signature
- Enable Markdown
- Enable recording pause/resume feature
- Enable send big text
- Force enable debug mode
- Force enable emoticon plus feature
- Ghost Mode
- Hook Package Manager
- Override feature flag
- Play YouTube player in chat room
- Register settings activity
- Remove BizBoard ads
- Remove More tab ad
- Remove OpenLink chat room list ad
- Remove Short-form Tab
- Remove feed ad
- Remove focus ad
- Remove native ad
- Remove shop tab
- Show deleted or hidden messages
- Spoof App ID
- Spoof apk checksums
- Spoof signature
- Version info patch
</blockquote>
</details>

---
### [Crunchyroll](https://play.google.com/store/apps/details?id=com.crunchyroll.crunchyroid)

<details>
<summary id="Crunchyroll">&emsp;<a href="../../releases/download/31/crunchyroll-revanced-v3.104.0-arm64-v8a.apk"><img src="https://img.shields.io/badge/Crunchyroll-v3.104.0-gray?labelColor=F47521&logo=Crunchyroll&logoColor=white"></a></summary>
<blockquote>

[Release 2026-03-20](../../releases/tag/31)<br>
Patches: ReVanced/patches-6.1.0.rvp
- Hide ads
</blockquote>
</details>

---
### [Cricbuzz](https://play.google.com/store/apps/details?id=com.cricbuzz.android)

<details>
<summary id="Cricbuzz">&emsp;<a href="../../releases/download/48/cricbuzz-rookieenough-v6.24.01-all.apk"><img src="https://img.shields.io/badge/Cricbuzz-v6.24.01-gray?labelColor=009270&logo=Cricbuzz&logoColor=white"></a></summary>

[Module (.zip)](../../releases/download/48/cricbuzz-rookieenough-module-v6.24.01-all.zip)
<blockquote>

[Release 2026-04-12](../../releases/tag/48)<br>
Patches: [RookieEnough/patches-1.0.3.mpp](https://github.com/RookieEnough/De-ReVanced/releases/tag/v1.0.3)
- Hide ads
</blockquote>
</details>

---
### [Tumblr](https://play.google.com/store/apps/details?id=com.tumblr)

<details>
<summary id="Tumblr">&emsp;<a href="../../releases/download/48/tumblr-rookieenough-v44.0.0.107-all.apk"><img src="https://img.shields.io/badge/Tumblr-v44.0.0.107-gray?labelColor=36465D&logo=Tumblr&logoColor=white"></a></summary>

[Module (.zip)](../../releases/download/48/tumblr-rookieenough-module-v44.0.0.107-all.zip)
<blockquote>

[Release 2026-04-12](../../releases/tag/48)<br>
Patches: [RookieEnough/patches-1.0.3.mpp](https://github.com/RookieEnough/De-ReVanced/releases/tag/v1.0.3)
- Disable Ad-Free Banner
- Disable Tumblr TV
- Disable blog notification reminder
- Disable dashboard ads
- Disable gift message popup
- Disable in-app update
</blockquote>
</details>

---
### [MyFitnessPal](https://play.google.com/store/apps/details?id=com.myfitnesspal.android)

<details>
<summary id="MyFitnessPal">&emsp;<a href="../../releases/download/48/myfitnesspal-hoo-dles-v25.50.0-all.apk"><img src="https://img.shields.io/badge/MyFitnessPal-v25.50.0-gray?labelColor=0066EE&logo=MyFitnessPal&logoColor=white"></a></summary>

[Module (.zip)](../../releases/download/48/myfitnesspal-hoo-dles-module-v25.50.0-all.zip)
<blockquote>

[Release 2026-04-12](../../releases/tag/48)<br>
Patches: [hoo-dles/patches-1.23.0.mpp](https://github.com/hoo-dles/morphe-patches/releases/tag/v1.23.0)
- Enable Premium+
</blockquote>
</details>

---
### [Strava](https://play.google.com/store/apps/details?id=com.strava)

<details>
<summary id="Strava">&emsp;<a href="../../releases/download/48/strava-rookieenough-v458.12-all.apk"><img src="https://img.shields.io/badge/Strava-v458.12-gray?labelColor=FC4C02&logo=Strava&logoColor=white"></a></summary>

[Module (.zip)](../../releases/download/48/strava-rookieenough-module-v458.12-all.zip)
<blockquote>

[Release 2026-04-12](../../releases/tag/48)<br>
Patches: [RookieEnough/patches-1.0.3.mpp](https://github.com/RookieEnough/De-ReVanced/releases/tag/v1.0.3)
- Add 'Give Kudos' button to 'Group Activity'
- Add media download
- Block Snowplow tracking
- Disable Quick Edit
- Enable password login
- Hide distractions
- Overwrite media upload parameters
- Unlock subscription features
</blockquote>
</details>

---
### [ibis Paint X](https://play.google.com/store/apps/details?id=jp.ne.ibis.ibispaintx.app)

<details>
<summary id="ibis-Paint-X">&emsp;<a href="../../releases/download/48/ibis-paint-x-hoo-dles-v14.0.0-all.apk"><img src="https://img.shields.io/badge/ibis_Paint_X-v14.0.0-gray?labelColor=E64A8B&logo=ibispaintx&logoColor=white"></a></summary>
<blockquote>

[Release 2026-04-12](../../releases/tag/48)<br>
Patches: [hoo-dles/patches-1.23.0.mpp](https://github.com/hoo-dles/morphe-patches/releases/tag/v1.23.0)
- Enable Prime membership
</blockquote>
</details>

---
### [RAR](https://play.google.com/store/apps/details?id=com.rarlab.rar)

<details>
<summary id="RAR">&emsp;<a href="../../releases/download/48/rar-rookieenough-v7.20.build131-all.apk"><img src="https://img.shields.io/badge/RAR-v7.20.build131-gray?labelColor=FF6B00&logo=rar&logoColor=white"></a></summary>

[Module (.zip)](../../releases/download/48/rar-rookieenough-module-v7.20.build131-all.zip)
<blockquote>

[Release 2026-04-12](../../releases/tag/48)<br>
Patches: [RookieEnough/patches-1.0.3.mpp](https://github.com/RookieEnough/De-ReVanced/releases/tag/v1.0.3)
- Hide purchase reminder
</blockquote>
</details>

---
### [Wallcraft](https://play.google.com/store/apps/details?id=com.wallpaperscraft.wallpaper)

<details>
<summary id="Wallcraft">&emsp;<a href="../../releases/download/48/wallcraft-hoo-dles-v3.61.01-all.apk"><img src="https://img.shields.io/badge/Wallcraft-v3.61.01-gray?labelColor=1E88E5&logo=wallpaper&logoColor=white"></a></summary>

[Module (.zip)](../../releases/download/48/wallcraft-hoo-dles-module-v3.61.01-all.zip)
<blockquote>

[Release 2026-04-12](../../releases/tag/48)<br>
Patches: [hoo-dles/patches-1.23.0.mpp](https://github.com/hoo-dles/morphe-patches/releases/tag/v1.23.0)
- Enable Premium
</blockquote>
</details>

---
### [Nova Launcher](https://play.google.com/store/apps/details?id=com.teslacoilsw.launcher)

<details>
<summary id="Nova-Launcher">&emsp;<a href="../../releases/download/48/nova-launcher-hoo-dles-v81042-all.apk"><img src="https://img.shields.io/badge/Nova_Launcher-v81042-gray?labelColor=FF3C30&logo=nova_launcher&logoColor=white"></a></summary>
 
[Module (.zip)](../../releases/download/48/nova-launcher-hoo-dles-module-v81042-all.zip)
<blockquote>

[Release 2026-04-12](../../releases/tag/48)<br>
Patches: [hoo-dles/patches-1.23.0.mpp](https://github.com/hoo-dles/morphe-patches/releases/tag/v1.23.0)
- Enable Prime
</blockquote>
</details>

---
### [Smart Launcher 6](https://play.google.com/store/apps/details?id=ginlemon.flowerfree)

<details>
<summary id="Smart-Launcher-6">&emsp;<a href="../../releases/download/48/smart-launcher-6-hoo-dles-v6.6build002patch1-all.apk"><img src="https://img.shields.io/badge/Smart_Launcher_6-v6.6build002patch1-gray?labelColor=0F1419&logo=smart_launcher&logoColor=white"></a></summary>

[Module (.zip)](../../releases/download/48/smart-launcher-6-hoo-dles-module-v6.6build002patch1-all.zip)
<blockquote>

[Release 2026-04-12](../../releases/tag/48)<br>
Patches: [hoo-dles/patches-1.23.0.mpp](https://github.com/hoo-dles/morphe-patches/releases/tag/v1.23.0)
- Disable signature check
- Enable Pro
</blockquote>
</details>

---
### [Proton VPN](https://play.google.com/store/apps/details?id=ch.protonvpn.android)

<details>
<summary id="Proton-VPN">&emsp;<a href="../../releases/download/48/proton-vpn-hoo-dles-v5.16.83.0-all.apk"><img src="https://img.shields.io/badge/Proton_VPN-v5.16.83.0-gray?labelColor=6D4AFF&logo=protonvpn&logoColor=white"></a></summary>

[Module (.zip)](../../releases/download/48/proton-vpn-hoo-dles-module-v5.16.83.0-all.zip)
<blockquote>

[Release 2026-04-12](../../releases/tag/48)<br>
Patches: [hoo-dles/patches-1.23.0.mpp](https://github.com/hoo-dles/morphe-patches/releases/tag/v1.23.0)
- Remove delay
- Unlock custom DNS
- Unlock split tunneling
</blockquote>
</details>

---
### [Sofascore](https://play.google.com/store/apps/details?id=com.sofascore.results)

<details>
<summary id="Sofascore">&emsp;<a href="../../releases/download/48/sofascore-hoo-dles-v25.12.17-all.apk"><img src="https://img.shields.io/badge/Sofascore-v25.12.17-gray?labelColor=1A4BFF&logo=sofascore&logoColor=white"></a></summary>

[Module (.zip)](../../releases/download/48/sofascore-hoo-dles-module-v25.12.17-all.zip)
<blockquote>

[Release 2026-04-12](../../releases/tag/48)<br>
Patches: [hoo-dles/patches-1.23.0.mpp](https://github.com/hoo-dles/morphe-patches/releases/tag/v1.23.0)
- Disable ads
</blockquote>
</details>

---
### [Peacock TV](https://play.google.com/store/apps/details?id=com.peacocktv.peacockandroid)

<details>
<summary id="Peacock-TV">&emsp;<a href="../../releases/download/48/peacock-tv-rookieenough-v7.4.201-all.apk"><img src="https://img.shields.io/badge/Peacock_TV-v7.4.201-gray?labelColor=252525&logo=peacock&logoColor=white"></a></summary>

[Module (.zip)](../../releases/download/48/peacock-tv-rookieenough-module-v7.4.201-all.zip)
<blockquote>

[Release 2026-04-12](../../releases/tag/48)<br>
Patches: [RookieEnough/patches-1.0.3.mpp](https://github.com/RookieEnough/De-ReVanced/releases/tag/v1.0.3)
- Hide ads
</blockquote>
</details>

---
### [Windy](https://play.google.com/store/apps/details?id=com.windyty.android)

<details>
<summary id="Windy">&emsp;<a href="../../releases/download/48/windy-hoo-dles-v49.0.1-all.apk"><img src="https://img.shields.io/badge/Windy-v49.0.1-gray?labelColor=C62828&logo=windy&logoColor=white"></a></summary>

[Module (.zip)](../../releases/download/48/windy-hoo-dles-module-v49.0.1-all.zip)
<blockquote>

[Release 2026-04-12](../../releases/tag/48)<br>
Patches: [hoo-dles/patches-1.23.0.mpp](https://github.com/hoo-dles/morphe-patches/releases/tag/v1.23.0)
- Enable Premium
</blockquote>
</details>

---
### [Cake](https://play.google.com/store/apps/details?id=me.mycake)

<details>
<summary id="Cake">&emsp;<a href="../../releases/download/48/cake-hoo-dles-v6.4.0-arm64-v8a.apk"><img src="https://img.shields.io/badge/Cake-v6.4.0-gray?labelColor=FF6B35&logo=cake&logoColor=white"></a></summary>

[Module (.zip)](../../releases/download/48/cake-hoo-dles-module-v6.4.0-arm64-v8a.zip)
<blockquote>

[Release 2026-04-12](../../releases/tag/48)<br>
Patches: [hoo-dles/patches-1.23.0.mpp](https://github.com/hoo-dles/morphe-patches/releases/tag/v1.23.0)
- Enable Plus
</blockquote>
</details>

---
### [Merriam Webster Dictionary](https://play.google.com/store/apps/details?id=com.merriamwebster)

<details>
<summary id="Merriam-Webster-Dictionary">&emsp;<a href="../../releases/download/48/merriam-webster-dictionary-hoo-dles-v5.5.0-all.apk"><img src="https://img.shields.io/badge/Merriam_Webster_Dictionary-v5.5.0-gray?labelColor=B30000&logo=merriam_webster&logoColor=white"></a></summary>
 
[Module (.zip)](../../releases/download/48/merriam-webster-dictionary-hoo-dles-module-v5.5.0-all.zip)
<blockquote>

[Release 2026-04-12](../../releases/tag/48)<br>
Patches: [hoo-dles/patches-1.23.0.mpp](https://github.com/hoo-dles/morphe-patches/releases/tag/v1.23.0)
- Enable Premium
</blockquote>
</details>

---
### [Busuu](https://play.google.com/store/apps/details?id=com.busuu.android.enc)

<details>
<summary id="Busuu">&emsp;<a href="../../releases/download/48/busuu-hoo-dles-v32.30.0.1575420.-all.apk"><img src="https://img.shields.io/badge/Busuu-v32.30.0(1575420)-gray?labelColor=116EEE&logo=busuu&logoColor=white"></a></summary>

[Module (.zip)](../../releases/download/48/busuu-hoo-dles-module-v32.30.0.1575420.-all.zip)
<blockquote>

[Release 2026-04-12](../../releases/tag/48)<br>
Patches: [hoo-dles/patches-1.23.0.mpp](https://github.com/hoo-dles/morphe-patches/releases/tag/v1.23.0)
- Enable Premium
</blockquote>
</details>


---
## ⭐ Star History

<a href="https://www.star-history.com/?repos=nvbangg%2Frevanced-morphe-builder&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=nvbangg/revanced-morphe-builder&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=nvbangg/revanced-morphe-builder&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=nvbangg/revanced-morphe-builder&type=date&legend=top-left" />
 </picture>
</a>
