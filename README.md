# Age Of History 2 Bot

[![Release](https://img.shields.io/badge/Release-v1.1.2-blue?style=for-the-badge)](../../releases/latest)
[![Downloads](https://img.shields.io/github/downloads/aleynabc/AgeOfHistory2Bot/total?style=for-the-badge)](../../releases)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

> Age of History 2 için hızlı, kullanışlı ve çok dilli cheat command / console botu.
>
> A fast, convenient and multilingual cheat command / console bot for Age of History 2.

---

## 📥 Download / İndirme

### 🇹🇷 Türkçe

En güncel hazır sürümü GitHub Releases bölümünden indirebilirsiniz.

**[⬇️ En Güncel Sürümü İndir / Download Latest Release](../../releases/latest)**

Hazır sürümü kullanmak için Python, pip, PyInstaller veya Visual Studio kurulmasına gerek yoktur.

Botun kaynak ve proje dosyaları `AgeOfHistory2Bot_Professional_v1.1.2.zip` arşivinde bulunmaktadır.

### 🇬🇧 English

You can download the latest ready-to-use version from the GitHub Releases section.

**[⬇️ Download Latest Release](../../releases/latest)**

Python, pip, PyInstaller, or Visual Studio is not required to use the ready-to-use version.

The bot's source and project files are included in the `AgeOfHistory2Bot_Professional_v1.1.2.zip` archive.

---

## 🧰 Technologies Used / Kullanılan Teknolojiler

### 🇹🇷 Türkçe

Proje, aşağıdaki teknoloji ve araçlar kullanılarak geliştirilmiştir:

- 🐍 **Python** — Botun ana mantığı ve overlay arayüzü (`overlay.py`) Python ile yazılmıştır.
- 📦 **requirements.txt** — Projenin bağımlılıkları bu dosya üzerinden yönetilmektedir; kesin kütüphane listesi için dosyanın kendisine bakabilirsiniz.
- 🛠️ **PyInstaller** (`AgeOfHistory2Bot.spec`) — Python kaynak kodunu bağımsız çalışabilir bir Windows `.exe` dosyasına dönüştürmek için kullanılır.
- 🪟 **Inno Setup** (`installer.iss`) — Windows için profesyonel bir kurulum (installer) paketi oluşturmak amacıyla kullanılır.
- ⚙️ **Batch / PowerShell** (`build.bat`, `OTOMATIK_OLUSTUR.bat`, `otomatik_olustur.ps1`) — Derleme (build) sürecini otomatikleştiren komut dosyalarıdır; Python bağımlılıklarını kurar, PyInstaller ile derler ve Inno Setup ile installer üretir.
- 🎨 **Özel simgeler** (`app_icon.ico`, `titlebar_icon.png`) — Uygulamanın görsel kimliği için özel olarak hazırlanmış ikonlardır.
- 📜 **MIT License** — Proje açık kaynak MIT lisansı ile paylaşılmıştır.

Kısacası proje, Python ile yazılmış bir masaüstü overlay uygulamasını, kullanıcıya Python kurulumu gerektirmeden tek bir `.exe` kurulum dosyası halinde sunacak şekilde paketlemektedir.

### 🇬🇧 English

The project was built using the following technologies and tools:

- 🐍 **Python** — The bot's core logic and overlay interface (`overlay.py`) are written in Python.
- 📦 **requirements.txt** — Project dependencies are managed through this file; check it directly for the exact library list.
- 🛠️ **PyInstaller** (`AgeOfHistory2Bot.spec`) — Used to bundle the Python source code into a standalone Windows `.exe` executable.
- 🪟 **Inno Setup** (`installer.iss`) — Used to build a professional Windows installer package.
- ⚙️ **Batch / PowerShell** (`build.bat`, `OTOMATIK_OLUSTUR.bat`, `otomatik_olustur.ps1`) — Automation scripts that handle the build pipeline: installing Python dependencies, compiling with PyInstaller, and packaging with Inno Setup.
- 🎨 **Custom icons** (`app_icon.ico`, `titlebar_icon.png`) — Custom-made icons for the application's visual identity.
- 📜 **MIT License** — The project is open-sourced under the MIT license.

In short, the project packages a Python-based desktop overlay application into a single `.exe` installer, so end users don't need Python installed to run it.

---

## 🚀 Installation / Kurulum

### 🇹🇷 Türkçe

1. [Latest Release](../../releases/latest) sayfasına gidin.
2. `AgeOfHistory2Bot_Professional_v1.1.2.zip` dosyasını indirin.
3. ZIP arşivini çıkartın.
4. İçerisindeki `AgeOfHistory2Bot_Kurulum.exe` dosyasını çalıştırın.
5. Kurulum tamamlandıktan sonra masaüstünde oluşturulan kısayoldan botu başlatın.
6. Age of History 2'yi açın ve botu kullanmaya başlayın.

### 🇬🇧 English

1. Go to the [Latest Release](../../releases/latest) page.
2. Download `AgeOfHistory2Bot_Professional_v1.1.2.zip`.
3. Extract the ZIP archive.
4. Run `AgeOfHistory2Bot_Kurulum.exe`.
5. After installation, launch the bot using the desktop shortcut.
6. Open Age of History 2 and start using the bot.

---

## ▶️ How to Use / Nasıl Kullanılır

### 🇹🇷 Türkçe

1. Botu masaüstü kısayolundan başlatın; karşınıza küçük bir overlay penceresi gelecektir.
2. Overlay penceresinden kullanmak istediğiniz dili seçin (8 dil desteklenmektedir).
3. Age of History 2 oyununu açın ve oyun içinde komut göndermek istediğiniz ekranda olun.
4. Overlay üzerindeki komut listesinden veya metin kutusundan istediğiniz cheat ya da konsol komutunu seçin/yazın.
5. Komutu gönderin; bot, komutu oyuna ASCII tabanlı güvenli bir şekilde iletecektir.
6. Dili değiştirseniz bile pencere konumu korunur, böylece overlay'i tekrar konumlandırmanıza gerek kalmaz.
7. İşiniz bittiğinde overlay'i kapatabilir veya `close` / `bye` konsol komutlarını kullanarak konsolu kapatabilirsiniz.

> 💡 İpucu: Aşağıdaki **Cheat Commands** ve **Console Commands** tablolarından hangi komutun ne işe yaradığını inceleyebilirsiniz.

### 🇬🇧 English

1. Launch the bot from the desktop shortcut; a small overlay window will appear.
2. Select your preferred language from the overlay (8 languages supported).
3. Open Age of History 2 and be on the screen where you want to send a command.
4. Choose or type the cheat or console command you want from the overlay's command list or text box.
5. Send the command; the bot will deliver it to the game using a safe, ASCII-based method.
6. The window position is preserved even if you switch languages, so you won't need to reposition the overlay.
7. When you're done, close the overlay, or use the `close` / `bye` console commands to exit the console.

> 💡 Tip: Check the **Cheat Commands** and **Console Commands** tables below to see what each command does.

---

## ✨ Features / Özellikler

### 🇹🇷 Türkçe

- 🎮 Age of History 2 cheat komutları
- 🖥️ Konsol komutları
- 🌍 8 farklı dil desteği
- 📜 Tüm sayfalarda dikey kaydırma
- ⚡ Hızlı komut gönderme
- 🔄 Dil değiştirildiğinde pencere konumunu koruma
- 🪟 Windows kısayol desteği
- 🔐 ASCII tabanlı güvenli komut gönderimi
- 🎨 Modern ve kullanışlı arayüz

### 🇬🇧 English

- 🎮 Age of History 2 cheat commands
- 🖥️ Console commands
- 🌍 Support for 8 languages
- 📜 Vertical scrolling on all pages
- ⚡ Fast command sending
- 🔄 Preserves the window position when changing language
- 🪟 Windows shortcut support
- 🔐 ASCII-based command sending
- 🎨 Modern and user-friendly interface

---

## 🌍 Supported Languages / Desteklenen Diller

### 🇹🇷 Türkçe

Uygulama aşağıdaki 8 dili desteklemektedir:

- 🇹🇷 Türkçe
- 🇬🇧 English
- 🇷🇺 Русский
- 🇮🇹 Italiano
- 🇫🇷 Français
- 🇸🇦 العربية
- 🇰🇿 Қазақша
- 🇦🇿 Azərbaycanca

### 🇬🇧 English

The application supports the following 8 languages:

- 🇹🇷 Turkish
- 🇬🇧 English
- 🇷🇺 Russian
- 🇮🇹 Italian
- 🇫🇷 French
- 🇸🇦 Arabic
- 🇰🇿 Kazakh
- 🇦🇿 Azerbaijani

---

# 🎮 Cheat Commands / Hile Komutları

| Command / Komut   | Açıklama / Description                                                              |
| ------------------ | ------------------------------------------------------------------------------------ |
| `addciv [TAG]`    | 🇹🇷 Seçili eyalete medeniyet verir. / 🇬🇧 Gives the selected province a civilization. |
| `addplayer`       | 🇹🇷 Seçili ülkeye oyuncu verir. / 🇬🇧 Gives the selected country a player.            |
| `army`            | 🇹🇷 +300 asker verir. / 🇬🇧 Adds +300 soldiers.                                       |
| `money`           | 🇹🇷 +450 altın verir. / 🇬🇧 Adds +450 gold.                                           |
| `technology +X`   | 🇹🇷 X miktarında teknoloji ekler. / 🇬🇧 Adds X technology.                            |
| `population`      | 🇹🇷 +750 nüfus verir. / 🇬🇧 Adds +750 population.                                     |
| `civs`            | 🇹🇷 Tüm ülke etiketlerini gösterir. / 🇬🇧 Shows all country tags.                     |
| `diplomacy`       | 🇹🇷 +0.7 hareket puanı verir. / 🇬🇧 Adds +0.7 movement points.                        |
| `scale +X`        | 🇹🇷 Ölçeği X olarak değiştirir (1–5). / 🇬🇧 Changes the scale by X (1–5).             |
| `fps`             | 🇹🇷 FPS sayacını gösterir. / 🇬🇧 Displays the FPS counter.                            |
| `war +ID1 +ID2`   | 🇹🇷 İki ülke arasında savaş başlatır. / 🇬🇧 Starts a war between two countries.       |
| `peace +ID1 +ID2` | 🇹🇷 İki ülke arasındaki savaşı bitirir. / 🇬🇧 Ends the war between two countries.     |
| `buildport`       | 🇹🇷 Liman inşa eder. / 🇬🇧 Builds a port.                                             |
| `buildfort`       | 🇹🇷 Kale inşa eder. / 🇬🇧 Builds a fort.                                              |
| `buildtower`      | 🇹🇷 Kule inşa eder. / 🇬🇧 Builds a tower.                                             |
| `civ`             | 🇹🇷 Seçili ülkenin etiketini gösterir. / 🇬🇧 Shows the selected country's tag.        |
| `province`        | 🇹🇷 Eyalet bilgilerini gösterir. / 🇬🇧 Shows province information.                    |
| `showids`         | 🇹🇷 ID bilgilerini gösterir. / 🇬🇧 Shows ID information.                              |
| `showarmy`        | 🇹🇷 Ordu bilgilerini gösterir. / 🇬🇧 Shows army information.                          |
| `setarmy +X`      | 🇹🇷 Ordu miktarını X olarak ayarlar. / 🇬🇧 Sets the army amount to X.                 |
| `noliberty`       | 🇹🇷 Liberty özelliğini devre dışı bırakır. / 🇬🇧 Disables the liberty feature.        |
| `economy`         | 🇹🇷 +600 ekonomi verir. / 🇬🇧 Adds +600 economy.                                      |

---

# 🖥️ Console Commands / Konsol Komutları

| Command / Komut | Açıklama / Description                                                 |
| ---------------- | ------------------------------------------------------------------------ |
| `close`         | 🇹🇷 Konsolu kapatır. / 🇬🇧 Closes the console.                           |
| `bye`           | 🇹🇷 Konsoldan çıkar. / 🇬🇧 Exits the console.                            |
| `help`          | 🇹🇷 Yardım menüsünü gösterir. / 🇬🇧 Shows the help menu.                 |
| `info`          | 🇹🇷 Bilgi ekranını gösterir. / 🇬🇧 Shows information.                    |
| `debug`         | 🇹🇷 Debug modunu açar. / 🇬🇧 Enables debug mode.                         |
| `center`        | 🇹🇷 Haritayı merkeze getirir. / 🇬🇧 Centers the map.                     |
| `centerciv +ID` | 🇹🇷 Belirtilen ülkeye merkezler. / 🇬🇧 Centers on the specified country. |
| `spin`          | 🇹🇷 Haritayı döndürür. / 🇬🇧 Spins the map.                              |
| `flags`         | 🇹🇷 Bayrakları gösterir. / 🇬🇧 Displays flags.                           |
| `clear`         | 🇹🇷 Konsolu temizler. / 🇬🇧 Clears the console.                          |

---

# 💻 System Requirements / Sistem Gereksinimleri

### 🇹🇷 Türkçe

- Windows 10 veya Windows 11
- Age of History 2
- Hazır sürümü kullanmak için Python gerekmez.
- pip gerekmez.
- PyInstaller gerekmez.
- Visual Studio gerekmez.

### 🇬🇧 English

- Windows 10 or Windows 11
- Age of History 2
- Python is not required for the ready-to-use version.
- pip is not required.
- PyInstaller is not required.
- Visual Studio is not required.

---

# 🛠️ Build From Source / Kaynak Koddan Derleme

### 🇹🇷 Türkçe

Projeyi kaynak koddan geliştirmek veya yeniden derlemek istiyorsanız:

1. Repository'yi klonlayın.
2. `AgeOfHistory2Bot` klasörüne girin.
3. `OTOMATIK_OLUSTUR.bat` dosyasını çalıştırın.
4. Build sistemi gerekli Python bağımlılıklarını ve derleme araçlarını hazırlayacaktır.
5. İşlem tamamlandığında Windows installer oluşturulacaktır.

### 🇬🇧 English

If you want to develop or rebuild the project from source:

1. Clone the repository.
2. Open the `AgeOfHistory2Bot` directory.
3. Run `OTOMATIK_OLUSTUR.bat`.
4. The build system will prepare the required Python dependencies and build tools.
5. When the process is complete, a Windows installer will be created.

---

# 📁 Project Structure / Proje Yapısı

```text
AgeOfHistory2Bot/
│
├── README.md
├── LICENSE
├── CHANGELOG.md
├── .gitignore
│
└── AgeOfHistory2Bot/
    ├── overlay.py
    ├── AgeOfHistory2Bot.spec
    ├── requirements.txt
    ├── build.bat
    ├── OTOMATIK_OLUSTUR.bat
    ├── otomatik_olustur.ps1
    ├── installer.iss
    ├── app_icon.ico
    └── titlebar_icon.png
```

---

## 📄 License / Lisans

### 🇹🇷 Türkçe

Bu proje **MIT Lisansı** altında lisanslanmıştır. Ayrıntılar için [LICENSE](LICENSE) dosyasına bakabilirsiniz.

### 🇬🇧 English

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
