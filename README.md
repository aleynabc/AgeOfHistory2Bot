# Age Of History 2 Bot

> Professional, multilingual desktop overlay for **Age of History 2** single-player cheat/console commands.

The application provides a small always-on-top panel that focuses the Age of History 2 window and sends the game's own keyboard commands. It does not modify game files or process memory.

## Highlights

- **8 interface languages**
  - Türkçe
  - English
  - Русский
  - Italiano
  - Français
  - العربية
  - Қазақша
  - Azərbaycanca
- C1-level UI translations with consistent terminology.
- Settings are persisted in `%APPDATA%\AgeOfHistory2Bot\settings.json`.
- Simple settings screen with:
  - language
  - game-window title
  - console key
  - repeat count
  - command delay
  - cheat-input position
  - console-input position
- `F9` global shortcut to show/hide the panel.
- ASCII-only command strings, so Turkish `ı` is never accidentally sent to the game.
- PyInstaller one-file executable.
- Inno Setup installer with a **real Windows `.lnk` desktop shortcut**.
- UAC elevation is enabled because the game may itself run elevated.

## Command architecture

Commands are defined centrally in `overlay.py` rather than being scattered across button callbacks.

Each command has:

```text
(command_id, command_template, uses_console, parameters)
```

This makes it straightforward to audit, translate and update commands without duplicating UI logic.

The command strings intentionally remain in the game's original ASCII form, for example:

```text
army
money
technology +1000
setarmy +500
buildtower
```

The interface language changes only the visible label and description; it never translates the actual game command.

## Command groups

### Cheat/input field

Includes the commonly documented Age of History 2 commands such as:

- `hi`
- `addciv`
- `addplayer`
- `army`
- `money`
- `population`
- `civs`
- `diplomacy`
- `movement`
- `scale`
- `fps`
- `war`
- `peace`
- `buildport`
- `buildfort`
- `buildtower`
- `civ`
- `province`
- `showids`
- `showarmy`
- `technology`
- `setarmy`
- `noliberty`
- `id`
- `economy`

### F1 console

Includes:

- `close`
- `bye`
- `help`
- `info`
- `debug`
- `center`
- `centerciv`
- `spin`
- `flags`
- `clear`
- `reloadprovince`
- `party`

The exact behavior can depend on the Age of History 2 version/mod in use.

## First-time setup

1. Install the application.
2. Start Age of History 2.
3. Open the game's cheat/message input.
4. Open **Settings** in the bot.
5. Use **Save cheat input position** and place the mouse over the game's input field during the countdown.
6. Open the F1 console and repeat the process with **Save console input position**.
7. Select a command.

If the game window size, UI scale, resolution, or position changes, save the input positions again.

## Shortcut problem: fixed properly

The installer creates shortcuts through Inno Setup's `[Icons]` section. These are actual Windows `.lnk` shortcuts pointing directly to:

```text
{install folder}\AgeOfHistory2Bot.exe
```

The shortcut also has an explicit working directory and uses the application's icon.

If an old shortcut asks Windows to choose an application from the Microsoft Store, delete that old shortcut and create a fresh one using the new installer. Do not rename an `.exe` or `.bat` file to `.lnk`.

## Build from source

### Automatic

Double-click:

```text
OTOMATIK_OLUSTUR.bat
```

The script:

1. checks/installs Python when necessary,
2. installs Python dependencies,
3. builds the executable with PyInstaller,
4. checks/installs Inno Setup when necessary,
5. creates:

```text
installer_output\AgeOfHistory2Bot_Kurulum.exe
```

### Manual

```powershell
python -m pip install -r requirements.txt
python -m PyInstaller --clean --noconfirm AgeOfHistory2Bot.spec
```

The executable will be:

```text
dist\AgeOfHistory2Bot.exe
```

Then compile `installer.iss` with Inno Setup to create the distributable installer.

## Project structure

```text
AgeOfHistory2Bot/
├─ overlay.py
├─ AgeOfHistory2Bot.spec
├─ requirements.txt
├─ build.bat
├─ OTOMATIK_OLUSTUR.bat
├─ otomatik_olustur.ps1
├─ installer.iss
├─ app_icon.ico
├─ titlebar_icon.png
├─ README.md
└─ LICENSE
```

## Technical notes

- Python standard-library Tkinter is used for the UI.
- `pydirectinput` handles keyboard/mouse automation.
- `pygetwindow` locates and focuses the game window.
- `keyboard` provides the global F9 shortcut.
- Settings are stored under the user's AppData folder instead of the installation directory, avoiding write-permission problems under `Program Files`.
- The application does not need an internet connection after installation.

## Safety / scope

This project is intended for the game's own single-player cheat/console functionality. It does not inject code, modify memory, patch executable files, or provide online-game automation.

Use it only where the game's rules and your local setup permit it.

## License

MIT. See `LICENSE`.


## Otomatik Build / Kurulum

`build.bat` tek tıklamayla build sürecini yönetir. Önceden elle `pip install` yapmanız gerekmez.

- Python yoksa Windows Package Manager (`winget`) üzerinden Python 3.14 otomatik denenir; `winget` yoksa python.org kurucusu otomatik indirilip sessizce çalıştırılır.
- `requirements.txt` içindeki Python paketleri otomatik kurulur/güncellenir.
- Python 3.14 ile uyumlu PyInstaller 6.22.2 kullanılır. PyInstaller 6.15.0 ile Python 3.14 desteği eklenmiştir.
- Inno Setup yoksa otomatik kurulumu denenir; ardından gerçek Windows kurulum paketi oluşturulur. Build scripti gerekirse Windows UAC ile yönetici yetkisini otomatik ister.
- Sonuç `installer_output\AgeOfHistory2Bot_Kurulum.exe` olur.
- Son kullanıcı tarafında Python veya Python kütüphaneleri gerekmez; PyInstaller bağımlılıkları EXE içine paketler.

> Not: Build makinesinde internet erişimi gerekir; otomatik Python/Inno Setup indirmeleri yalnızca eksik olduklarında yapılır.
