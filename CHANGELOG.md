# Changelog

All notable changes to this project are documented in this file.

Bu dosya, projede yapılan önemli değişiklikleri sürüm bazında açıklar.

---

## [1.1.2] - 2026-09-05

### 🇹🇷 Türkçe

#### Yeni Özellikler
- `Hileler`, `Konsol` ve `Ayarlar` sekmelerine dikey kaydırma desteği eklendi.
- Fare tekerleği ile kaydırma doğrudan ve gecikmesiz hale getirildi.
- Windows ve Linux fare tekerleği davranışları desteklendi.
- Dil değiştirildiğinde bot penceresinin mevcut konumu korunuyor.
- Dil değişikliğinde pencerenin boyutu ve ekran üzerindeki konumu sıfırlanmıyor.
- 8 dil desteği:
  - Türkçe
  - English
  - Русский
  - Italiano
  - Français
  - العربية
  - Қазақша
  - Azərbaycan dili

#### Hile Komutları
- Hile komutları merkezi bir komut yapısında düzenlendi.
- Oyun tarafından kullanılan komutların ASCII karakterlerle gönderilmesi güvence altına alındı.
- Türkçe `ı` karakterinin oyun komutlarında kullanılmasını engelleyen kontrol eklendi.
- `addciv [TAG]` komutu için açıklama güncellendi.
- `addplayer` komutu için açıklama güncellendi.
- `army` komutu `+300` asker olarak güncellendi.
- `money` komutu `+450` altın olarak güncellendi.
- `technology +X` komutu X değerinin kullanıcı tarafından girilebilmesini destekleyecek şekilde düzenlendi.
- `population` komutu `+750` nüfus olarak güncellendi.
- `civs` komutunun ülke etiketlerini gösterdiği belirtildi.
- `diplomacy` komutunun `+0.7` hareket puanı eklediği belirtildi.
- `scale +X` komutu için 1–5 aralığı belirtildi.
- `fps` komutunun FPS göstergesini açtığı belirtildi.
- `war +ID1 +ID2` komutu güncellendi.
- `peace +ID1 +ID2` komutu güncellendi.
- `buildport`, `buildfort` ve `buildtower` komutları güncellendi.
- `province` ve `showids` komutlarının açıklamaları güncellendi.
- `info`, `debug`, `center`, `centerciv`, `close`, `spin`, `help`, `flags` ve `clear` konsol komutları düzenlendi.
- `economy` komutu `+600` ekonomi olarak güncellendi.
- `population` komutu `+750` olarak güncellendi.
- `setarmy +X` komutu güncellendi.
- `noliberty` komutu korundu.

#### Kod ve Proje
- Komut şablonlarının ASCII uyumluluğunu kontrol eden çalışma zamanı doğrulaması eklendi.
- Proje yapısı korunarak kod daha düzenli hale getirildi.
- Mevcut bot işlevleri korunmuştur.

---

## [1.1.1] - 2026-09-04

### 🇹🇷 Türkçe

#### Arayüz
- Ayarlar arayüzü sadeleştirildi.
- Dil seçenekleri yeniden düzenlendi.
- Çoklu dil desteği geliştirildi.
- Hile ve konsol komutlarının açıklamaları güncellendi.
- Uygulama arayüzünün daha profesyonel ve kullanıcı dostu olması sağlandı.

#### Windows
- Windows kısayol oluşturma sistemi geliştirildi.
- Microsoft Store'a yönlendirme sorununa karşı gerçek Windows `.lnk` kısayolları kullanılmaya başlandı.
- Masaüstü ve Başlat Menüsü kısayolları için çalışma dizini (`WorkingDir`) tanımlandı.
- Kurulum sonrası uygulamanın otomatik başlatılması sağlandı.

#### Kurulum
- Inno Setup ile kurulum desteği geliştirildi.
- Kurulum dosyasının otomatik oluşturulması sağlandı.
- Python ve gerekli bağımlılıkların otomatik kurulması için build sistemi geliştirildi.
- PyInstaller ile tek dosyalık EXE oluşturma sistemi geliştirildi.

---

## [1.0.0] - Initial Release

### 🇹🇷 Türkçe

- Age of History 2 için ilk bot sürümü yayınlandı.
- Hile komutlarının grafik arayüz üzerinden kullanılabilmesi sağlandı.
- Konsol komutları için arayüz oluşturuldu.
- Ayarlar bölümü eklendi.
- Çoklu dil altyapısının temeli oluşturuldu.
- Windows EXE oluşturma altyapısı eklendi.
- Inno Setup ile kurulum desteği eklendi.

---

### 🇬🇧 English

## [1.1.2] - 2026-09-05

#### New Features
- Added vertical scrolling support to the `Cheats`, `Console`, and `Settings` tabs.
- Made mouse-wheel scrolling immediate and responsive.
- Added support for Windows and Linux mouse-wheel behavior.
- Preserved the bot window position when changing the language.
- Window size and screen position are no longer reset after changing language.
- Added support for 8 languages:
  - Turkish
  - English
  - Russian
  - Italian
  - French
  - Arabic
  - Kazakh
  - Azerbaijani

#### Cheat Commands
- Centralized the cheat command definitions.
- Ensured that game commands are sent using ASCII characters.
- Added runtime protection against the Turkish `ı` character appearing in game commands.
- Updated the description of `addciv [TAG]`.
- Updated the description of `addplayer`.
- Updated `army` to add `+300` soldiers.
- Updated `money` to add `+450` gold.
- Updated `technology +X` to allow the user to enter the X value.
- Updated `population` to add `+750` population.
- Updated `civs` to show country tags.
- Updated `diplomacy` to add `+0.7` movement points.
- Updated `scale +X` with a 1–5 range.
- Updated `fps` to show the FPS counter.
- Updated `war +ID1 +ID2`.
- Updated `peace +ID1 +ID2`.
- Updated `buildport`, `buildfort`, and `buildtower`.
- Updated `province` and `showids` descriptions.
- Updated console commands including `info`, `debug`, `center`, `centerciv`, `close`, `spin`, `help`, `flags`, and `clear`.
- Updated `economy` to add `+600` economy.
- Updated `population` to `+750`.
- Updated `setarmy +X`.
- Preserved the `noliberty` command.

#### Code and Project
- Added runtime validation to ensure command templates contain only ASCII characters.
- Improved internal project organization while preserving the existing bot architecture.
- Existing bot functionality has been preserved.

---

## [1.1.1] - 2026-09-04

#### Interface
- Simplified the Settings interface.
- Reorganized language options.
- Improved multilingual support.
- Updated cheat and console command descriptions.
- Improved the overall professional and user-friendly experience.

#### Windows
- Improved Windows shortcut creation.
- Added real Windows `.lnk` shortcuts to prevent Microsoft Store redirection issues.
- Added an explicit working directory to shortcuts.
- Added desktop and Start Menu shortcuts.
- Added automatic application launch after installation.

#### Installation
- Improved Inno Setup installation support.
- Added automatic installer generation.
- Improved automatic Python and dependency installation.
- Improved PyInstaller single-file EXE generation.

---

## [1.0.0] - Initial Release

- Initial Age of History 2 Bot release.
- Added a graphical interface for cheat commands.
- Added a graphical interface for console commands.
- Added a Settings section.
- Added the foundation for multilingual support.
- Added Windows EXE build support.
- Added Inno Setup installer support.
