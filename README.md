**Wallpaper Engine for KDE** is a plugin that integrates Steam's Wallpaper Engine with KDE, allowing users to set dynamic wallpapers (including scenes, videos, and web-based content) directly from KDE's wallpaper settings. It supports various types of wallpapers but comes with some limitations such as issues with certain scenes, lack of screen locking support, and other minor bugs.

This repository hosts the RPM SPEC used for my copr repository here: https://copr.fedorainfracloud.org/coprs/jackgreiner/wallpaper-engine-kde-plugin/

Commits from the upstream project: https://github.com/catsout/wallpaper-engine-kde-plugin are fetched every hour.

### **Installation Instructions:**

1. **Enable COPR Repository and Install Plugin:**
   To install the `wallpaper-engine-kde-plugin` via COPR:
   ```sh
   sudo dnf copr enable jackgreiner/wallpaper-engine-kde-plugin
   sudo dnf install wallpaper-engine-kde-plugin
   ```
2. **Restart KDE:**
   After reinstalling the plugin, restart the KDE Plasma shell:
   ```sh
   systemctl --user restart plasma-plasmashell.service
   ```
   
3. **Usage:**
   - Ensure *Wallpaper Engine* is installed via Steam and subscribe to wallpapers on the Steam Workshop.
   - In the plugin, select the *Steam library* folder containing the *steamapps* folder (usually `~/.local/share/Steam`).
   
### **Troubleshooting:**

1. **KDE Crashes Due to Scene Wallpapers:**
   - If your KDE crashes with certain scene wallpapers, remove the `WallpaperSource` line from `~/.config/plasma-org.kde.plasma.desktop-appletsrc` and restart KDE.

2. **Mouse Long Press Issues:**
   - The mouse long press (used for entering panel edit mode) might not work on the desktop. No immediate fix, but it's a known limitation.

3. **Screen Locking Not Supported:**
   - Do not use this plugin if you rely on KDE's screen-locking functionality, as it does not support screen locking.

4. **Video Playback:**
   - If videos fail to play, ensure you have the required QtMultimedia GStreamer backend, or alternatively, use MPV for better hardware-accelerated playback.

