# Installation

## Download

Grab the latest `.lrplugin` bundle from your purchase confirmation email or the
[releases page](https://github.com/LunarLanded/lunarlanded.github.io/releases).

## Install

=== "macOS"

    1. Unzip the download. You'll get a folder ending in `.lrplugin`.
    2. Move it to:
       ```
       ~/Library/Application Support/Adobe/Lightroom/Modules/
       ```
       Create the `Modules` folder if it doesn't exist.
    3. Restart Lightroom Classic.

    !!! warning "Gatekeeper"

        macOS may quarantine the download. If Lightroom refuses to load it, run:

        ```bash
        xattr -dr com.apple.quarantine ~/Library/Application\ Support/Adobe/Lightroom/Modules/YourPlugin.lrplugin
        ```

=== "Windows"

    1. Unzip the download.
    2. Move the `.lrplugin` folder to:
       ```
       %APPDATA%\Adobe\Lightroom\Modules\
       ```
    3. Restart Lightroom Classic.

## Verify

1. Open **File → Plug-in Manager**
2. Your plugin should appear in the left-hand list with a green status dot

If it isn't listed, click **Add**, navigate to the `.lrplugin` folder, and
select it manually.

## Activate

1. **File → Plug-in Extras → Enter Licence**
2. Paste the key from your confirmation email
3. Click **Activate**

Keys are valid for :material-numeric-3-circle: three machines. Deactivate an
old machine from the same dialog before installing on a fourth.
