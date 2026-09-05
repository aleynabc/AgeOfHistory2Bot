# -*- coding: utf-8 -*-
"""
Age Of History 2 Bot
--------------------
Age of History 2 (tek oyunculu) için, oyunun üzerinde çalışan profesyonel
bir yardımcı panel. Panel, oyunun kendi konsol/hile sistemine klavye komutları
gönderir; oyun dosyalarına, belleğe veya çevrim içi servislere müdahale etmez.

Özellikler:
- Türkçe, İngilizce, Rusça, İtalyanca, Fransızca, Arapça, Kazakça ve
  Azerbaycanca arayüz.
- Ayarların %APPDATA% altında kalıcı olarak saklanması.
- Oyun ve konsol yazı kutusu konumlarının tek seferlik kaydı.
- F9 ile göster/gizle.
- Hile/konsol komutlarının merkezi ve hataya daha az açık tanımları.
"""

import json
import os
import sys
import threading
import time
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

import pydirectinput
import pygetwindow as gw

pydirectinput.FAILSAFE = False

APP_NAME = "AgeOfHistory2Bot"
DEFAULT_WINDOW_TITLE = "Age of History"
DEFAULT_CONSOLE_KEY = "f1"
DEFAULT_REPEAT = 1
DEFAULT_DELAY = 0.25
CONFIG_DIR = os.path.join(os.environ.get("APPDATA", os.path.expanduser("~")), APP_NAME)
CONFIG_FILE = os.path.join(CONFIG_DIR, "settings.json")

# ---------------------------------------------------------------------------
# TEMA
# ---------------------------------------------------------------------------
COL_BG = "#2b1c12"
COL_BAR = "#1c120c"
COL_TAB = "#3d281a"
COL_TAB_SEL = "#5a3a24"
COL_BTN = "#4a2f1f"
COL_BTN_HOVER = "#6b4529"
COL_ACCENT = "#c69c4a"
COL_ACCENT_LIGHT = "#e8c98a"
COL_TEXT = "#f0e0c0"
COL_TEXT_MUTED = "#c9a876"
COL_SUCCESS = "#d8b46a"
COL_ERROR = "#e0745a"


# ---------------------------------------------------------------------------
# DİL SİSTEMİ
# ---------------------------------------------------------------------------
LANGUAGES = {
    "tr": "Türkçe",
    "en": "English",
    "ru": "Русский",
    "it": "Italiano",
    "fr": "Français",
    "ar": "العربية",
    "kk": "Қазақша",
    "az": "Azərbaycanca",
}

T = {
    "tr": {
        "app_title": "Age Of History 2 Bot",
        "ready": "Hazır. Oyunu açık tutun ve bir komut seçin.",
        "cheats": "Hileler",
        "console": "Konsol",
        "settings": "Ayarlar",
        "language": "Dil",
        "general": "Genel",
        "game_window": "Oyun penceresi",
        "console_key": "Konsol tuşu",
        "repeat": "Tekrar sayısı",
        "delay": "Komut arası bekleme (sn)",
        "save": "Ayarları Kaydet",
        "input_positions": "Yazı kutusu konumları",
        "chat_position": "Hile kutusu konumunu kaydet (3 sn)",
        "console_position": "Konsol kutusu konumunu kaydet (3 sn)",
        "not_saved": "Kayıtlı konum yok",
        "cursor": "İmleç",
        "hint": "İpucu: Önce oyunda ilgili yazı kutusunu açın. Ardından konum kaydetme düğmesine basın ve geri sayım sırasında fareyi kutunun üzerine getirin.",
        "shortcut": "Paneli göster/gizle: F9",
        "about": "Hakkında",
        "about_text": "Age Of History 2 Bot\nTek oyunculu kullanım için oyun içi komut yardımcısı.\n\nOyun dosyalarına veya belleğe müdahale etmez.",
        "sent": "Gönderildi",
        "sending": "Gönderiliyor",
        "game_not_found": "Oyun penceresi bulunamadı",
        "settings_saved": "Ayarlar kaydedildi.",
        "position_saved": "Konum kaydedildi",
        "cancelled": "İptal edildi.",
        "position_missing": "Konum ayarlanmadı",
        "position_missing_text": "{box} kutusunun konumu henüz kaydedilmedi. Ayarlar bölümünden ilgili konumu kaydedin.",
        "enter_value": "Değer gir",
        "error": "Hata",
        "warning": "Uyarı",
        "invalid_value": "Geçersiz değer. Lütfen tekrar deneyin.",
        "count": "Miktar",
        "country_id": "Ülke ID",
        "country_id_1": "1. ülke ID",
        "country_id_2": "2. ülke ID",
        "country_tag": "Ülke etiketi (TAG)",
        "technology_amount": "Teknoloji miktarı",
        "army_amount": "Ordu miktarı",
        "scale": "Harita ölçeği (1-5)",
        "province_id": "Eyalet ID",
        "command_sent": "Gönderildi: {command}",
        "command_error": "Komut gönderilirken hata: {error}",
        "countdown": "{seconds}... Fareyi hedef kutunun üzerine götürün.",
        "chat_box": "Hile",
        "console_box": "Konsol",
        "singleplayer": "Yalnızca tek oyunculu kullanım önerilir.",
        "command_section": "Komutlar",
        "info": "Bilgi",
        "info_text": "Komutların açıklamasını görmek için fareyi butonun üzerinde kısa süre bekletin.",
        "tooltip": "Komut: {command}\n{description}",
    },
    "en": {
        "app_title": "Age Of History 2 Bot",
        "ready": "Ready. Keep the game open and choose a command.",
        "cheats": "Cheats",
        "console": "Console",
        "settings": "Settings",
        "language": "Language",
        "general": "General",
        "game_window": "Game window",
        "console_key": "Console key",
        "repeat": "Repeat count",
        "delay": "Delay between commands (sec)",
        "save": "Save settings",
        "input_positions": "Input positions",
        "chat_position": "Save cheat input position (3 sec)",
        "console_position": "Save console input position (3 sec)",
        "not_saved": "No position saved",
        "cursor": "Cursor",
        "hint": "Tip: Open the relevant input field in the game first. Then press the position button and move the mouse over the field during the countdown.",
        "shortcut": "Show/hide panel: F9",
        "about": "About",
        "about_text": "Age Of History 2 Bot\nIn-game command assistant for single-player use.\n\nIt does not modify game files or memory.",
        "sent": "Sent",
        "sending": "Sending",
        "game_not_found": "Game window not found",
        "settings_saved": "Settings saved.",
        "position_saved": "Position saved",
        "cancelled": "Cancelled.",
        "position_missing": "Position not set",
        "position_missing_text": "The {box} input position has not been saved yet. Save it in Settings first.",
        "enter_value": "Enter value",
        "error": "Error",
        "warning": "Warning",
        "invalid_value": "Invalid value. Please try again.",
        "count": "Amount",
        "country_id": "Country ID",
        "country_id_1": "Country ID 1",
        "country_id_2": "Country ID 2",
        "country_tag": "Country tag (TAG)",
        "technology_amount": "Technology amount",
        "army_amount": "Army amount",
        "scale": "Map scale (1-5)",
        "province_id": "Province ID",
        "command_sent": "Sent: {command}",
        "command_error": "Command error: {error}",
        "countdown": "{seconds}... Move the mouse over the target input.",
        "chat_box": "Cheat input",
        "console_box": "Console",
        "singleplayer": "Single-player use is recommended.",
        "command_section": "Commands",
        "info": "Info",
        "info_text": "Hover over a button briefly to see its command and description.",
        "tooltip": "Command: {command}\n{description}",
    },
    "ru": {
        "app_title": "Age Of History 2 Bot",
        "ready": "Готово. Оставьте игру открытой и выберите команду.",
        "cheats": "Читы",
        "console": "Консоль",
        "settings": "Настройки",
        "language": "Язык",
        "general": "Основные",
        "game_window": "Окно игры",
        "console_key": "Клавиша консоли",
        "repeat": "Количество повторов",
        "delay": "Задержка между командами (сек.)",
        "save": "Сохранить настройки",
        "input_positions": "Позиции полей ввода",
        "chat_position": "Сохранить позицию поля читов (3 сек.)",
        "console_position": "Сохранить позицию консоли (3 сек.)",
        "not_saved": "Позиция не сохранена",
        "cursor": "Курсор",
        "hint": "Совет: сначала откройте нужное поле ввода в игре. Затем нажмите кнопку сохранения позиции и наведите мышь на поле во время обратного отсчёта.",
        "shortcut": "Показать/скрыть панель: F9",
        "about": "О программе",
        "about_text": "Age Of History 2 Bot\nПомощник для игровых команд в одиночной игре.\n\nНе изменяет файлы или память игры.",
        "sent": "Отправлено",
        "sending": "Отправка",
        "game_not_found": "Окно игры не найдено",
        "settings_saved": "Настройки сохранены.",
        "position_saved": "Позиция сохранена",
        "cancelled": "Отменено.",
        "position_missing": "Позиция не задана",
        "position_missing_text": "Позиция поля «{box}» ещё не сохранена. Сначала сохраните её в настройках.",
        "enter_value": "Введите значение",
        "error": "Ошибка",
        "warning": "Предупреждение",
        "invalid_value": "Недопустимое значение. Попробуйте снова.",
        "count": "Количество",
        "country_id": "ID страны",
        "country_id_1": "ID страны 1",
        "country_id_2": "ID страны 2",
        "country_tag": "Тег страны (TAG)",
        "technology_amount": "Количество технологий",
        "army_amount": "Размер армии",
        "scale": "Масштаб карты (1–5)",
        "province_id": "ID провинции",
        "command_sent": "Отправлено: {command}",
        "command_error": "Ошибка отправки команды: {error}",
        "countdown": "{seconds}... Наведите мышь на нужное поле.",
        "chat_box": "Поле читов",
        "console_box": "Консоль",
        "singleplayer": "Рекомендуется использовать только в одиночной игре.",
        "command_section": "Команды",
        "info": "Информация",
        "info_text": "Наведите курсор на кнопку, чтобы увидеть команду и её описание.",
        "tooltip": "Команда: {command}\n{description}",
    },
    "it": {
        "app_title": "Age Of History 2 Bot",
        "ready": "Pronto. Mantieni aperto il gioco e scegli un comando.",
        "cheats": "Trucchi",
        "console": "Console",
        "settings": "Impostazioni",
        "language": "Lingua",
        "general": "Generali",
        "game_window": "Finestra del gioco",
        "console_key": "Tasto della console",
        "repeat": "Numero di ripetizioni",
        "delay": "Attesa tra i comandi (sec.)",
        "save": "Salva impostazioni",
        "input_positions": "Posizioni dei campi di input",
        "chat_position": "Salva posizione campo trucchi (3 sec.)",
        "console_position": "Salva posizione console (3 sec.)",
        "not_saved": "Nessuna posizione salvata",
        "cursor": "Cursore",
        "hint": "Suggerimento: apri prima il campo di input nel gioco. Poi premi il pulsante di salvataggio e porta il mouse sul campo durante il conto alla rovescia.",
        "shortcut": "Mostra/nascondi pannello: F9",
        "about": "Informazioni",
        "about_text": "Age Of History 2 Bot\nAssistente ai comandi di gioco per la modalità giocatore singolo.\n\nNon modifica file o memoria del gioco.",
        "sent": "Inviato",
        "sending": "Invio",
        "game_not_found": "Finestra del gioco non trovata",
        "settings_saved": "Impostazioni salvate.",
        "position_saved": "Posizione salvata",
        "cancelled": "Annullato.",
        "position_missing": "Posizione non impostata",
        "position_missing_text": "La posizione del campo {box} non è stata salvata. Salvala prima nelle impostazioni.",
        "enter_value": "Inserisci valore",
        "error": "Errore",
        "warning": "Avviso",
        "invalid_value": "Valore non valido. Riprova.",
        "count": "Quantità",
        "country_id": "ID paese",
        "country_id_1": "ID paese 1",
        "country_id_2": "ID paese 2",
        "country_tag": "Tag paese (TAG)",
        "technology_amount": "Quantità tecnologia",
        "army_amount": "Dimensione esercito",
        "scale": "Scala mappa (1-5)",
        "province_id": "ID provincia",
        "command_sent": "Inviato: {command}",
        "command_error": "Errore nell'invio del comando: {error}",
        "countdown": "{seconds}... Porta il mouse sul campo di input.",
        "chat_box": "Campo trucchi",
        "console_box": "Console",
        "singleplayer": "Si consiglia l'uso esclusivamente in modalità giocatore singolo.",
        "command_section": "Comandi",
        "info": "Info",
        "info_text": "Passa brevemente il mouse su un pulsante per vedere comando e descrizione.",
        "tooltip": "Comando: {command}\n{description}",
    },
    "fr": {
        "app_title": "Age Of History 2 Bot",
        "ready": "Prêt. Gardez le jeu ouvert et choisissez une commande.",
        "cheats": "Triches",
        "console": "Console",
        "settings": "Paramètres",
        "language": "Langue",
        "general": "Général",
        "game_window": "Fenêtre du jeu",
        "console_key": "Touche de la console",
        "repeat": "Nombre de répétitions",
        "delay": "Délai entre les commandes (s)",
        "save": "Enregistrer les paramètres",
        "input_positions": "Positions des champs de saisie",
        "chat_position": "Enregistrer la position du champ de triche (3 s)",
        "console_position": "Enregistrer la position de la console (3 s)",
        "not_saved": "Aucune position enregistrée",
        "cursor": "Curseur",
        "hint": "Conseil : ouvrez d’abord le champ de saisie dans le jeu. Appuyez ensuite sur le bouton d’enregistrement et placez la souris sur le champ pendant le compte à rebours.",
        "shortcut": "Afficher/masquer le panneau : F9",
        "about": "À propos",
        "about_text": "Age Of History 2 Bot\nAssistant de commandes pour le mode solo.\n\nNe modifie ni les fichiers ni la mémoire du jeu.",
        "sent": "Envoyé",
        "sending": "Envoi",
        "game_not_found": "Fenêtre du jeu introuvable",
        "settings_saved": "Paramètres enregistrés.",
        "position_saved": "Position enregistrée",
        "cancelled": "Annulé.",
        "position_missing": "Position non définie",
        "position_missing_text": "La position du champ {box} n’a pas encore été enregistrée. Enregistrez-la dans les paramètres.",
        "enter_value": "Saisir une valeur",
        "error": "Erreur",
        "warning": "Avertissement",
        "invalid_value": "Valeur invalide. Veuillez réessayer.",
        "count": "Quantité",
        "country_id": "ID du pays",
        "country_id_1": "ID du pays 1",
        "country_id_2": "ID du pays 2",
        "country_tag": "Tag du pays (TAG)",
        "technology_amount": "Quantité de technologie",
        "army_amount": "Taille de l’armée",
        "scale": "Échelle de la carte (1-5)",
        "province_id": "ID de province",
        "command_sent": "Envoyé : {command}",
        "command_error": "Erreur d’envoi de la commande : {error}",
        "countdown": "{seconds}... Placez la souris sur le champ cible.",
        "chat_box": "Champ de triche",
        "console_box": "Console",
        "singleplayer": "Utilisation en mode solo uniquement recommandée.",
        "command_section": "Commandes",
        "info": "Info",
        "info_text": "Survolez brièvement un bouton pour voir sa commande et sa description.",
        "tooltip": "Commande : {command}\n{description}",
    },
    "ar": {
        "app_title": "Age Of History 2 Bot",
        "ready": "جاهز. أبقِ اللعبة مفتوحة واختر أمرًا.",
        "cheats": "الغش",
        "console": "وحدة التحكم",
        "settings": "الإعدادات",
        "language": "اللغة",
        "general": "عام",
        "game_window": "نافذة اللعبة",
        "console_key": "مفتاح وحدة التحكم",
        "repeat": "عدد التكرارات",
        "delay": "التأخير بين الأوامر (بالثواني)",
        "save": "حفظ الإعدادات",
        "input_positions": "مواضع حقول الإدخال",
        "chat_position": "حفظ موضع حقل الغش (3 ثوانٍ)",
        "console_position": "حفظ موضع وحدة التحكم (3 ثوانٍ)",
        "not_saved": "لم يتم حفظ موضع",
        "cursor": "المؤشر",
        "hint": "نصيحة: افتح حقل الإدخال المطلوب داخل اللعبة أولًا، ثم اضغط زر حفظ الموضع وحرك الفأرة إلى الحقل أثناء العد التنازلي.",
        "shortcut": "إظهار/إخفاء اللوحة: F9",
        "about": "حول البرنامج",
        "about_text": "Age Of History 2 Bot\nمساعد لأوامر اللعبة في نمط اللعب الفردي.\n\nلا يغيّر ملفات اللعبة أو ذاكرتها.",
        "sent": "تم الإرسال",
        "sending": "جارٍ الإرسال",
        "game_not_found": "لم يتم العثور على نافذة اللعبة",
        "settings_saved": "تم حفظ الإعدادات.",
        "position_saved": "تم حفظ الموضع",
        "cancelled": "تم الإلغاء.",
        "position_missing": "لم يتم ضبط الموضع",
        "position_missing_text": "لم يتم حفظ موضع حقل {box} بعد. احفظه من الإعدادات أولًا.",
        "enter_value": "أدخل قيمة",
        "error": "خطأ",
        "warning": "تحذير",
        "invalid_value": "قيمة غير صالحة. حاول مرة أخرى.",
        "count": "الكمية",
        "country_id": "معرّف الدولة",
        "country_id_1": "معرّف الدولة 1",
        "country_id_2": "معرّف الدولة 2",
        "country_tag": "وسم الدولة (TAG)",
        "technology_amount": "مقدار التكنولوجيا",
        "army_amount": "حجم الجيش",
        "scale": "مقياس الخريطة (1-5)",
        "province_id": "معرّف المقاطعة",
        "command_sent": "تم الإرسال: {command}",
        "command_error": "حدث خطأ أثناء إرسال الأمر: {error}",
        "countdown": "{seconds}... حرّك الفأرة فوق حقل الإدخال المطلوب.",
        "chat_box": "حقل الغش",
        "console_box": "وحدة التحكم",
        "singleplayer": "يوصى بالاستخدام في نمط اللعب الفردي فقط.",
        "command_section": "الأوامر",
        "info": "معلومات",
        "info_text": "مرّر المؤشر فوق الزر قليلًا لرؤية الأمر ووصفه.",
        "tooltip": "الأمر: {command}\n{description}",
    },
    "kk": {
        "app_title": "Age Of History 2 Bot",
        "ready": "Дайын. Ойынды ашық қалдырып, пәрменді таңдаңыз.",
        "cheats": "Читтер",
        "console": "Консоль",
        "settings": "Баптаулар",
        "language": "Тіл",
        "general": "Жалпы",
        "game_window": "Ойын терезесі",
        "console_key": "Консоль пернесі",
        "repeat": "Қайталау саны",
        "delay": "Пәрмендер арасындағы кідіріс (сек.)",
        "save": "Баптауларды сақтау",
        "input_positions": "Енгізу өрістерінің орындары",
        "chat_position": "Чит енгізу орнына сақтау (3 сек.)",
        "console_position": "Консоль енгізу орнына сақтау (3 сек.)",
        "not_saved": "Орын сақталмаған",
        "cursor": "Меңзер",
        "hint": "Кеңес: алдымен ойындағы қажетті енгізу өрісін ашыңыз. Содан кейін сақтау батырмасын басып, кері санау кезінде меңзерді өрістің үстіне апарыңыз.",
        "shortcut": "Панельді көрсету/жасыру: F9",
        "about": "Бағдарлама туралы",
        "about_text": "Age Of History 2 Bot\nБір ойыншы режиміне арналған ойын пәрмендерінің көмекшісі.\n\nОйын файлдарына немесе жадына өзгеріс енгізбейді.",
        "sent": "Жіберілді",
        "sending": "Жіберілуде",
        "game_not_found": "Ойын терезесі табылмады",
        "settings_saved": "Баптаулар сақталды.",
        "position_saved": "Орын сақталды",
        "cancelled": "Бас тартылды.",
        "position_missing": "Орын бапталмаған",
        "position_missing_text": "{box} өрісінің орны әлі сақталмаған. Алдымен оны баптаулардан сақтаңыз.",
        "enter_value": "Мән енгізіңіз",
        "error": "Қате",
        "warning": "Ескерту",
        "invalid_value": "Мән жарамсыз. Қайта енгізіңіз.",
        "count": "Мөлшер",
        "country_id": "Ел ID-і",
        "country_id_1": "1-ел ID-і",
        "country_id_2": "2-ел ID-і",
        "country_tag": "Ел тегі (TAG)",
        "technology_amount": "Технология мөлшері",
        "army_amount": "Әскер саны",
        "scale": "Карта масштабы (1-5)",
        "province_id": "Провинция ID-і",
        "command_sent": "Жіберілді: {command}",
        "command_error": "Пәрменді жіберу қатесі: {error}",
        "countdown": "{seconds}... Меңзерді қажетті өрістің үстіне апарыңыз.",
        "chat_box": "Чит өрісі",
        "console_box": "Консоль",
        "singleplayer": "Тек бір ойыншы режимінде пайдалану ұсынылады.",
        "command_section": "Пәрмендер",
        "info": "Ақпарат",
        "info_text": "Пәрмен мен сипаттаманы көру үшін батырманың үстіне меңзерді аз уақыт қойыңыз.",
        "tooltip": "Пәрмен: {command}\n{description}",
    },
    "az": {
        "app_title": "Age Of History 2 Bot",
        "ready": "Hazırdır. Oyunu açıq saxlayın və əmr seçin.",
        "cheats": "Çitlər",
        "console": "Konsol",
        "settings": "Parametrlər",
        "language": "Dil",
        "general": "Ümumi",
        "game_window": "Oyun pəncərəsi",
        "console_key": "Konsol düyməsi",
        "repeat": "Təkrar sayı",
        "delay": "Əmrlər arasındakı gecikmə (san.)",
        "save": "Parametrləri saxla",
        "input_positions": "Daxiletmə sahələrinin mövqeləri",
        "chat_position": "Çit sahəsinin mövqeyini saxla (3 san.)",
        "console_position": "Konsol sahəsinin mövqeyini saxla (3 san.)",
        "not_saved": "Mövqe saxlanmayıb",
        "cursor": "Kursor",
        "hint": "Məsləhət: əvvəlcə oyunda uyğun daxiletmə sahəsini açın. Sonra mövqe düyməsinə basın və geri sayım zamanı siçanı həmin sahənin üzərinə gətirin.",
        "shortcut": "Paneli göstər/gizlət: F9",
        "about": "Haqqında",
        "about_text": "Age Of History 2 Bot\nTək oyunçu rejimi üçün oyun əmrləri köməkçisi.\n\nOyun fayllarını və ya yaddaşını dəyişdirmir.",
        "sent": "Göndərildi",
        "sending": "Göndərilir",
        "game_not_found": "Oyun pəncərəsi tapılmadı",
        "settings_saved": "Parametrlər saxlanıldı.",
        "position_saved": "Mövqe saxlanıldı",
        "cancelled": "Ləğv edildi.",
        "position_missing": "Mövqe təyin edilməyib",
        "position_missing_text": "{box} sahəsinin mövqeyi hələ saxlanmayıb. Əvvəlcə Parametrlər bölməsindən saxlayın.",
        "enter_value": "Dəyər daxil edin",
        "error": "Xəta",
        "warning": "Xəbərdarlıq",
        "invalid_value": "Yanlış dəyər. Yenidən cəhd edin.",
        "count": "Miqdar",
        "country_id": "Ölkə ID-si",
        "country_id_1": "1-ci ölkə ID-si",
        "country_id_2": "2-ci ölkə ID-si",
        "country_tag": "Ölkə teqi (TAG)",
        "technology_amount": "Texnologiya miqdarı",
        "army_amount": "Ordu sayı",
        "scale": "Xəritə miqyası (1-5)",
        "province_id": "Əyalət ID-si",
        "command_sent": "Göndərildi: {command}",
        "command_error": "Əmr göndərilərkən xəta: {error}",
        "countdown": "{seconds}... Siçanı hədəf sahənin üzərinə gətirin.",
        "chat_box": "Çit sahəsi",
        "console_box": "Konsol",
        "singleplayer": "Yalnız tək oyunçu rejimində istifadə tövsiyə olunur.",
        "command_section": "Əmrlər",
        "info": "Məlumat",
        "info_text": "Əmri və təsvirini görmək üçün kursoru düymənin üzərində qısa müddət saxlayın.",
        "tooltip": "Əmr: {command}\n{description}",
    },
}

COMMAND_TEXT = {
    "tr": {
        "addciv": ("Uygarlık ekle", "Seçili eyalete belirtilen TAG ile bir uygarlık ekler."),
        "addplayer": ("Oyuncu ekle", "Seçili ülkeye yeni bir oyuncu ekler."),
        "army": ("Ordu +300", "Seçili bölgeye 300 asker ekler."),
        "money": ("Para +450", "450 para ekler."),
        "population": ("Nüfus +750", "Seçili eyalete 750 nüfus ekler."),
        "civs": ("Ülke etiketleri", "Tüm ülkelerin TAG etiketlerini gösterir."),
        "diplomacy": ("Diplomasi +0.7", "Seçilen ülkeye 0.7 hareket puanı ekler."),
        "movement": ("Hareket +0.4", "Hareket puanı ekler."),
        "scale": ("Harita ölçeği", "Harita ölçeğini 1 ile 5 arasında değiştirir."),
        "fps": ("FPS göstergesi", "FPS sayacını açar veya kapatır."),
        "war": ("Savaş başlat", "İki ülke ID'si arasında savaş başlatır."),
        "peace": ("Barış yap", "İki ülke ID'si arasında barış sağlar."),
        "buildport": ("Liman inşa et", "Seçili eyalete liman inşa eder."),
        "buildfort": ("Kale inşa et", "Seçili eyalete kale inşa eder."),
        "buildtower": ("Kule inşa et", "Seçili eyalete kule inşa eder."),
        "civ": ("Ülke bilgisi", "Seçili uygarlığın ID ve TAG bilgisini gösterir."),
        "province": ("Eyalet bilgisi", "Seçili eyalet hakkında bilgi gösterir."),
        "showids": ("Eyalet ID'leri", "Eyalet ID'lerini harita üzerinde gösterir."),
        "showarmy": ("Orduyu göster", "Ordu göstergesini açar."),
        "technology": ("Teknoloji +X", "Seçilen ülkeye X kadar teknoloji ekler; X yerine istediğiniz değeri girin."),
        "setarmy": ("Orduyu ayarla", "Seçili eyaletin mevcut ordu miktarını verilen değere ayarlar."),
        "noliberty": ("Özgürlük yok", "Yönetiminizdeki ülkelerin özgürlük isteğini azaltır."),
        "id": ("ID bilgisi", "Seçili bölgenin ve sahibinin ID bilgisini gösterir."),
        "economy": ("Ekonomi +600", "Anında 600 altın ekler."),
        "hi": ("Hileleri etkinleştir", "Konsolu/hile sistemini etkinleştirmek için Hello yanıtı verir."),
        "close": ("Konsolu kapat", "Konsolu kapatır."),
        "bye": ("Konsolu kapat (bye)", "Konsolu bye komutuyla kapatır."),
        "help": ("Yardım", "Kullanılabilir komutlar hakkında yardım gösterir."),
        "info": ("Genel bilgi", "Oyun, performans ve grafik bilgilerini gösterir."),
        "debug": ("Debug", "Hata ayıklama modunu açar/kapatır."),
        "center": ("Haritayı ortala", "Kamerayı haritanın merkezine getirir."),
        "centerciv": ("Ülkeye odaklan", "Kamerayı belirtilen ülkenin üzerine getirir."),
        "spin": ("Kamerayı döndür", "Kamerayı döndürür."),
        "flags": ("Bayrakları göster", "Ekranda bayrakları gösterir."),
        "clear": ("Konsolu temizle", "Konsol içeriğini temizler."),
        "reloadprovince": ("Eyaleti yenile", "Belirtilen eyaleti yeniden yükler."),
        "party": ("Parti / bayraklar", "Ekranda oyun bayraklarını gösteren eğlence komutudur."),
    },
    "en": {
        "addciv": ("Add civilization", "Adds a civilization with the specified TAG to the selected province."),
        "addplayer": ("Add player", "Adds a new player to the selected country."),
        "army": ("Army +300", "Adds 300 soldiers to the selected region."),
        "money": ("Money +450", "Adds 450 money."),
        "population": ("Population +750", "Adds 750 population to the selected province."),
        "civs": ("Country tags", "Shows the TAGs of all countries."),
        "diplomacy": ("Diplomacy +0.6", "Adds diplomacy points."),
        "movement": ("Movement +0.4", "Adds movement points."),
        "scale": ("Map scale", "Changes the map scale from 1 to 5."),
        "fps": ("FPS counter", "Toggles the FPS counter."),
        "war": ("Start war", "Starts a war between two country IDs."),
        "peace": ("Make peace", "Makes peace between two country IDs."),
        "buildport": ("Build port", "Builds a port in the selected province."),
        "buildfort": ("Build fort", "Builds a fort in the selected province."),
        "buildtower": ("Build tower", "Builds a tower in the selected province."),
        "civ": ("Country information", "Shows the ID and TAG of the selected civilization."),
        "province": ("Province information", "Shows information about the selected province."),
        "showids": ("Show province IDs", "Shows province IDs on the map."),
        "showarmy": ("Show army", "Shows the army indicator."),
        "technology": ("Add technology", "Adds technology points; 1000 corresponds to 1.0 technology."),
        "setarmy": ("Set army", "Sets the selected province's army to the specified amount."),
        "noliberty": ("No liberty", "Reduces the desire for freedom of subjects under your control."),
        "id": ("ID information", "Shows the ID of the selected region and its owner."),
        "economy": ("Economy +600", "Adds 600 economy/money."),
        "hi": ("Enable cheats", "Activates the cheat/console system and returns a Hello response."),
        "close": ("Close console", "Closes the console."),
        "bye": ("Close console (bye)", "Closes the console using the bye alias."),
        "help": ("Help", "Shows help for available commands."),
        "info": ("General information", "Shows game, performance and graphics information."),
        "debug": ("Debug", "Toggles debug mode."),
        "center": ("Center map", "Centers the camera on the map."),
        "centerciv": ("Focus country", "Centers the camera on the specified country."),
        "spin": ("Spin camera", "Rotates the camera."),
        "flags": ("Show flags", "Displays flags on screen."),
        "clear": ("Clear console", "Clears the console."),
        "reloadprovince": ("Reload province", "Reloads the specified province."),
        "party": ("Party / flags", "Displays game flags as a fun visual command."),
    },
}

# The remaining languages use the same command identifiers and high-quality
# labels/descriptions. Command strings themselves are deliberately kept ASCII.
COMMAND_TEXT.update({
    "ru": {
        "addciv": ("Добавить цивилизацию", "Добавляет цивилизацию с указанным TAG в выбранную провинцию."),
        "addplayer": ("Добавить игрока", "Добавляет нового игрока в выбранную страну."),
        "army": ("Армия +300", "Добавляет 300 солдат в выбранный регион."),
        "money": ("Деньги +450", "Добавляет 450 денег."),
        "population": ("Население +750", "Добавляет 750 жителей в выбранную провинцию."),
        "civs": ("Теги стран", "Показывает TAG всех стран."),
        "diplomacy": ("Дипломатия +0.6", "Добавляет очки дипломатии."),
        "movement": ("Движение +0.4", "Добавляет очки движения."),
        "scale": ("Масштаб карты", "Изменяет масштаб карты от 1 до 5."),
        "fps": ("Счётчик FPS", "Включает или выключает счётчик FPS."),
        "war": ("Начать войну", "Начинает войну между двумя ID стран."),
        "peace": ("Заключить мир", "Заключает мир между двумя ID стран."),
        "buildport": ("Построить порт", "Строит порт в выбранной провинции."),
        "buildfort": ("Построить крепость", "Строит крепость в выбранной провинции."),
        "buildtower": ("Построить башню", "Строит башню в выбранной провинции."),
        "civ": ("Информация о стране", "Показывает ID и TAG выбранной цивилизации."),
        "province": ("Информация о провинции", "Показывает информацию о выбранной провинции."),
        "showids": ("Показать ID провинций", "Показывает ID провинций на карте."),
        "showarmy": ("Показать армию", "Показывает индикатор армии."),
        "technology": ("Добавить технологии", "Добавляет очки технологий; 1000 соответствует 1,0."),
        "setarmy": ("Задать армию", "Устанавливает размер армии выбранной провинции."),
        "noliberty": ("Без свободы", "Снижает стремление подчинённых стран к свободе."),
        "id": ("Информация об ID", "Показывает ID выбранного региона и его владельца."),
        "economy": ("Экономика +600", "Добавляет 600 единиц экономики/денег."),
        "hi": ("Включить читы", "Активирует систему читов/консоль и возвращает ответ Hello."),
        "close": ("Закрыть консоль", "Закрывает консоль."),
        "bye": ("Закрыть консоль (bye)", "Закрывает консоль с помощью алиаса bye."),
        "help": ("Помощь", "Показывает помощь по доступным командам."),
        "info": ("Общая информация", "Показывает сведения об игре, производительности и графике."),
        "debug": ("Отладка", "Включает или выключает режим отладки."),
        "center": ("Центрировать карту", "Центрирует камеру на карте."),
        "centerciv": ("Фокус на стране", "Центрирует камеру на указанной стране."),
        "spin": ("Повернуть камеру", "Вращает камеру."),
        "flags": ("Показать флаги", "Показывает флаги на экране."),
        "clear": ("Очистить консоль", "Очищает содержимое консоли."),
        "reloadprovince": ("Перезагрузить провинцию", "Перезагружает указанную провинцию."),
        "party": ("Праздник / флаги", "Показывает игровые флаги как развлекательную команду."),
    },
    "it": {
        "addciv": ("Aggiungi civiltà", "Aggiunge una civiltà con il TAG indicato alla provincia selezionata."),
        "addplayer": ("Aggiungi giocatore", "Aggiunge un nuovo giocatore al paese selezionato."),
        "army": ("Esercito +300", "Aggiunge 300 soldati alla regione selezionata."),
        "money": ("Denaro +450", "Aggiunge 450 unità di denaro."),
        "population": ("Popolazione +750", "Aggiunge 750 abitanti alla provincia selezionata."),
        "civs": ("Tag dei paesi", "Mostra i TAG di tutti i paesi."),
        "diplomacy": ("Diplomazia +0,6", "Aggiunge punti diplomazia."),
        "movement": ("Movimento +0,4", "Aggiunge punti movimento."),
        "scale": ("Scala della mappa", "Modifica la scala della mappa da 1 a 5."),
        "fps": ("Contatore FPS", "Attiva o disattiva il contatore FPS."),
        "war": ("Inizia guerra", "Avvia una guerra tra due ID di paese."),
        "peace": ("Fai la pace", "Stipula la pace tra due ID di paese."),
        "buildport": ("Costruisci porto", "Costruisce un porto nella provincia selezionata."),
        "buildfort": ("Costruisci fortezza", "Costruisce una fortezza nella provincia selezionata."),
        "buildtower": ("Costruisci torre", "Costruisce una torre nella provincia selezionata."),
        "civ": ("Informazioni paese", "Mostra ID e TAG della civiltà selezionata."),
        "province": ("Informazioni provincia", "Mostra informazioni sulla provincia selezionata."),
        "showids": ("Mostra ID province", "Mostra gli ID delle province sulla mappa."),
        "showarmy": ("Mostra esercito", "Mostra l'indicatore dell'esercito."),
        "technology": ("Aggiungi tecnologia", "Aggiunge punti tecnologia; 1000 corrisponde a 1,0."),
        "setarmy": ("Imposta esercito", "Imposta la dimensione dell'esercito della provincia selezionata."),
        "noliberty": ("Niente libertà", "Riduce il desiderio di libertà dei paesi sotto il tuo controllo."),
        "id": ("Informazioni ID", "Mostra l'ID della regione selezionata e del suo proprietario."),
        "economy": ("Economia +600", "Aggiunge 600 unità di economia/denaro."),
        "hi": ("Attiva trucchi", "Attiva il sistema di trucchi/console e restituisce una risposta Hello."),
        "close": ("Chiudi console", "Chiude la console."),
        "bye": ("Chiudi console (bye)", "Chiude la console usando l'alias bye."),
        "help": ("Aiuto", "Mostra l'aiuto sui comandi disponibili."),
        "info": ("Informazioni generali", "Mostra informazioni sul gioco, prestazioni e grafica."),
        "debug": ("Debug", "Attiva o disattiva la modalità debug."),
        "center": ("Centra mappa", "Centra la telecamera sulla mappa."),
        "centerciv": ("Focalizza paese", "Centra la telecamera sul paese indicato."),
        "spin": ("Ruota telecamera", "Ruota la telecamera."),
        "flags": ("Mostra bandiere", "Mostra le bandiere sullo schermo."),
        "clear": ("Pulisci console", "Cancella il contenuto della console."),
        "reloadprovince": ("Ricarica provincia", "Ricarica la provincia indicata."),
        "party": ("Party / bandiere", "Mostra le bandiere del gioco come comando divertente."),
    },
    "fr": {
        "addciv": ("Ajouter une civilisation", "Ajoute une civilisation avec le TAG indiqué à la province sélectionnée."),
        "addplayer": ("Ajouter un joueur", "Ajoute un nouveau joueur au pays sélectionné."),
        "army": ("Armée +300", "Ajoute 300 soldats à la région sélectionnée."),
        "money": ("Argent +450", "Ajoute 450 unités d’argent."),
        "population": ("Population +750", "Ajoute 750 habitants à la province sélectionnée."),
        "civs": ("Tags des pays", "Affiche les TAG de tous les pays."),
        "diplomacy": ("Diplomatie +0,6", "Ajoute des points de diplomatie."),
        "movement": ("Mouvement +0,4", "Ajoute des points de mouvement."),
        "scale": ("Échelle de la carte", "Modifie l’échelle de la carte de 1 à 5."),
        "fps": ("Compteur FPS", "Active ou désactive le compteur FPS."),
        "war": ("Déclarer une guerre", "Déclenche une guerre entre deux ID de pays."),
        "peace": ("Faire la paix", "Établit la paix entre deux ID de pays."),
        "buildport": ("Construire un port", "Construit un port dans la province sélectionnée."),
        "buildfort": ("Construire un fort", "Construit un fort dans la province sélectionnée."),
        "buildtower": ("Construire une tour", "Construit une tour dans la province sélectionnée."),
        "civ": ("Informations sur le pays", "Affiche l’ID et le TAG de la civilisation sélectionnée."),
        "province": ("Informations sur la province", "Affiche les informations de la province sélectionnée."),
        "showids": ("Afficher les ID", "Affiche les ID des provinces sur la carte."),
        "showarmy": ("Afficher l’armée", "Affiche l’indicateur de l’armée."),
        "technology": ("Ajouter de la technologie", "Ajoute des points de technologie ; 1000 correspond à 1,0."),
        "setarmy": ("Définir l’armée", "Définit la taille de l’armée de la province sélectionnée."),
        "noliberty": ("Sans liberté", "Réduit le désir de liberté des pays sous votre contrôle."),
        "id": ("Informations ID", "Affiche l’ID de la région sélectionnée et de son propriétaire."),
        "economy": ("Économie +600", "Ajoute 600 unités d’économie/d’argent."),
        "hi": ("Activer les triches", "Active le système de triches/console et renvoie une réponse Hello."),
        "close": ("Fermer la console", "Ferme la console."),
        "bye": ("Fermer la console (bye)", "Ferme la console avec l’alias bye."),
        "help": ("Aide", "Affiche l’aide sur les commandes disponibles."),
        "info": ("Informations générales", "Affiche des informations sur le jeu, les performances et les graphismes."),
        "debug": ("Débogage", "Active ou désactive le mode débogage."),
        "center": ("Centrer la carte", "Centre la caméra sur la carte."),
        "centerciv": ("Cibler un pays", "Centre la caméra sur le pays indiqué."),
        "spin": ("Faire tourner la caméra", "Fait pivoter la caméra."),
        "flags": ("Afficher les drapeaux", "Affiche les drapeaux à l’écran."),
        "clear": ("Effacer la console", "Efface le contenu de la console."),
        "reloadprovince": ("Recharger la province", "Recharge la province indiquée."),
        "party": ("Fête / drapeaux", "Affiche les drapeaux du jeu comme commande amusante."),
    },
    "ar": {
        "addciv": ("إضافة حضارة", "يضيف حضارة بالوسم المحدد إلى المقاطعة المختارة."),
        "addplayer": ("إضافة لاعب", "يضيف لاعبًا جديدًا إلى الدولة المختارة."),
        "army": ("جيش +300", "يضيف 300 جندي إلى المنطقة المختارة."),
        "money": ("مال +450", "يضيف 450 من المال."),
        "population": ("سكان +750", "يضيف 750 نسمة إلى المقاطعة المختارة."),
        "civs": ("وسوم الدول", "يعرض وسوم TAG لجميع الدول."),
        "diplomacy": ("دبلوماسية +0.6", "يضيف نقاطًا دبلوماسية."),
        "movement": ("حركة +0.4", "يضيف نقاط حركة."),
        "scale": ("مقياس الخريطة", "يغيّر مقياس الخريطة من 1 إلى 5."),
        "fps": ("عداد FPS", "يفعّل عداد FPS أو يعطّله."),
        "war": ("بدء حرب", "يبدأ حربًا بين معرّفي دولتين."),
        "peace": ("إحلال السلام", "يعقد السلام بين معرّفي دولتين."),
        "buildport": ("بناء ميناء", "يبني ميناءً في المقاطعة المختارة."),
        "buildfort": ("بناء حصن", "يبني حصنًا في المقاطعة المختارة."),
        "buildtower": ("بناء برج", "يبني برجًا في المقاطعة المختارة."),
        "civ": ("معلومات الدولة", "يعرض معرّف ووسم الحضارة المختارة."),
        "province": ("معلومات المقاطعة", "يعرض معلومات عن المقاطعة المختارة."),
        "showids": ("إظهار معرّفات المقاطعات", "يعرض معرّفات المقاطعات على الخريطة."),
        "showarmy": ("إظهار الجيش", "يعرض مؤشر الجيش."),
        "technology": ("إضافة تقنية", "يضيف نقاط تقنية؛ 1000 تعادل 1.0."),
        "setarmy": ("تعيين الجيش", "يعيّن حجم جيش المقاطعة المختارة بالقيمة المحددة."),
        "noliberty": ("منع الحرية", "يقلل رغبة الدول التابعة الخاضعة لسيطرتك في الاستقلال."),
        "id": ("معلومات المعرّف", "يعرض معرّف المنطقة المختارة ومالكها."),
        "economy": ("اقتصاد +600", "يضيف 600 وحدة من الاقتصاد/المال."),
        "hi": ("تفعيل الغش", "يفعّل نظام الغش/وحدة التحكم ويُرجع استجابة Hello."),
        "close": ("إغلاق وحدة التحكم", "يغلق وحدة التحكم."),
        "bye": ("إغلاق وحدة التحكم (bye)", "يغلق وحدة التحكم باستخدام الاسم البديل bye."),
        "help": ("مساعدة", "يعرض المساعدة الخاصة بالأوامر المتاحة."),
        "info": ("معلومات عامة", "يعرض معلومات اللعبة والأداء والرسوميات."),
        "debug": ("تصحيح", "يفعّل وضع التصحيح أو يعطّله."),
        "center": ("توسيط الخريطة", "يضع الكاميرا في مركز الخريطة."),
        "centerciv": ("التركيز على دولة", "يضع الكاميرا فوق الدولة المحددة."),
        "spin": ("تدوير الكاميرا", "يدير الكاميرا."),
        "flags": ("إظهار الأعلام", "يعرض الأعلام على الشاشة."),
        "clear": ("مسح وحدة التحكم", "يمسح محتوى وحدة التحكم."),
        "reloadprovince": ("إعادة تحميل المقاطعة", "يعيد تحميل المقاطعة المحددة."),
        "party": ("احتفال / أعلام", "يعرض أعلام اللعبة كأمر ترفيهي."),
    },
    "kk": {
        "addciv": ("Өркениет қосу", "Көрсетілген TAG арқылы таңдалған провинцияға өркениет қосады."),
        "addplayer": ("Ойыншы қосу", "Таңдалған елге жаңа ойыншы қосады."),
        "army": ("Әскер +300", "Таңдалған аймаққа 300 сарбаз қосады."),
        "money": ("Ақша +450", "450 ақша қосады."),
        "population": ("Халық +750", "Таңдалған провинцияға 750 тұрғын қосады."),
        "civs": ("Ел тегтері", "Барлық елдердің TAG белгілерін көрсетеді."),
        "diplomacy": ("Дипломатия +0.6", "Дипломатия ұпайларын қосады."),
        "movement": ("Қозғалыс +0.4", "Қозғалыс ұпайларын қосады."),
        "scale": ("Карта масштабы", "Карта масштабын 1-ден 5-ке дейін өзгертеді."),
        "fps": ("FPS есептегіші", "FPS есептегішін қосады немесе өшіреді."),
        "war": ("Соғыс бастау", "Екі ел ID-і арасында соғыс бастайды."),
        "peace": ("Бітім жасау", "Екі ел ID-і арасында бітім жасайды."),
        "buildport": ("Порт салу", "Таңдалған провинцияға порт салады."),
        "buildfort": ("Бекініс салу", "Таңдалған провинцияға бекініс салады."),
        "buildtower": ("Мұнара салу", "Таңдалған провинцияға мұнара салады."),
        "civ": ("Ел туралы ақпарат", "Таңдалған өркениеттің ID және TAG ақпаратын көрсетеді."),
        "province": ("Провинция ақпараты", "Таңдалған провинция туралы ақпаратты көрсетеді."),
        "showids": ("Провинция ID-ін көрсету", "Провинция ID-лерін картада көрсетеді."),
        "showarmy": ("Әскерді көрсету", "Әскер көрсеткішін көрсетеді."),
        "technology": ("Технология қосу", "Технология ұпайларын қосады; 1000 = 1,0."),
        "setarmy": ("Әскерді орнату", "Таңдалған провинция әскерінің санын берілген мәнге орнатады."),
        "noliberty": ("Еркіндіксіз", "Басқаруыңыздағы елдердің еркіндікке ұмтылысын азайтады."),
        "id": ("ID ақпараты", "Таңдалған аймақ пен оның иесінің ID-ін көрсетеді."),
        "economy": ("Экономика +600", "600 экономика/ақша қосады."),
        "hi": ("Читтерді қосу", "Чит/консоль жүйесін іске қосып, Hello жауабын қайтарады."),
        "close": ("Консольді жабу", "Консольді жабады."),
        "bye": ("Консольді жабу (bye)", "Консольді bye балама пәрмені арқылы жабады."),
        "help": ("Анықтама", "Қолжетімді пәрмендер туралы анықтаманы көрсетеді."),
        "info": ("Жалпы ақпарат", "Ойын, өнімділік және графика туралы ақпаратты көрсетеді."),
        "debug": ("Debug", "Жөндеу режимін қосады немесе өшіреді."),
        "center": ("Картаны орталау", "Камераны картаның ортасына орналастырады."),
        "centerciv": ("Елге фокус жасау", "Камераны көрсетілген елге бағыттайды."),
        "spin": ("Камераны айналдыру", "Камераны айналдырады."),
        "flags": ("Жалауларды көрсету", "Экранда жалауларды көрсетеді."),
        "clear": ("Консольді тазалау", "Консоль мазмұнын өшіреді."),
        "reloadprovince": ("Провинцияны қайта жүктеу", "Көрсетілген провинцияны қайта жүктейді."),
        "party": ("Мереке / жалаулар", "Ойын жалауларын көңіл көтеру мақсатындағы пәрмен ретінде көрсетеді."),
    },
    "az": {
        "addciv": ("Sivilizasiya əlavə et", "Seçilmiş əyalətə göstərilən TAG ilə sivilizasiya əlavə edir."),
        "addplayer": ("Oyunçu əlavə et", "Seçilmiş ölkəyə yeni oyunçu əlavə edir."),
        "army": ("Ordu +300", "Seçilmiş bölgəyə 300 əsgər əlavə edir."),
        "money": ("Pul +450", "450 pul əlavə edir."),
        "population": ("Əhali +750", "Seçilmiş əyalətə 750 əhali əlavə edir."),
        "civs": ("Ölkə teqləri", "Bütün ölkələrin TAG-lərini göstərir."),
        "diplomacy": ("Diplomatiya +0,6", "Diplomatiya xalları əlavə edir."),
        "movement": ("Hərəkət +0,4", "Hərəkət xalları əlavə edir."),
        "scale": ("Xəritə miqyası", "Xəritə miqyasını 1-dən 5-ə qədər dəyişir."),
        "fps": ("FPS sayğacı", "FPS sayğacını açır və ya bağlayır."),
        "war": ("Müharibə başlat", "İki ölkə ID-si arasında müharibə başladır."),
        "peace": ("Sülh et", "İki ölkə ID-si arasında sülh yaradır."),
        "buildport": ("Liman tik", "Seçilmiş əyalətdə liman tikir."),
        "buildfort": ("Qala tik", "Seçilmiş əyalətdə qala tikir."),
        "buildtower": ("Qüllə tik", "Seçilmiş əyalətdə qüllə tikir."),
        "civ": ("Ölkə məlumatı", "Seçilmiş sivilizasiyanın ID və TAG məlumatını göstərir."),
        "province": ("Əyalət məlumatı", "Seçilmiş əyalət haqqında məlumat göstərir."),
        "showids": ("Əyalət ID-lərini göstər", "Əyalət ID-lərini xəritədə göstərir."),
        "showarmy": ("Ordunu göstər", "Ordu göstəricisini göstərir."),
        "technology": ("Texnologiya əlavə et", "Texnologiya xalları əlavə edir; 1000 = 1,0."),
        "setarmy": ("Ordunu təyin et", "Seçilmiş əyalətin ordu sayını verilən dəyərə təyin edir."),
        "noliberty": ("Azadlıq yoxdur", "Nəzarətinizdə olan ölkələrin azadlıq istəyini azaldır."),
        "id": ("ID məlumatı", "Seçilmiş bölgənin və sahibinin ID-sini göstərir."),
        "economy": ("İqtisadiyyat +600", "600 iqtisadiyyat/pul əlavə edir."),
        "hi": ("Çitləri aktivləşdir", "Çit/konsol sistemini aktivləşdirir və Hello cavabı qaytarır."),
        "close": ("Konsolu bağla", "Konsolu bağlayır."),
        "bye": ("Konsolu bağla (bye)", "Konsolu bye alternativi ilə bağlayır."),
        "help": ("Kömək", "Mövcud əmrlər haqqında kömək göstərir."),
        "info": ("Ümumi məlumat", "Oyun, performans və qrafika məlumatlarını göstərir."),
        "debug": ("Debug", "Sazlama rejimini açır və ya bağlayır."),
        "center": ("Xəritəni mərkəzlə", "Kameranı xəritənin mərkəzinə gətirir."),
        "centerciv": ("Ölkəyə fokuslan", "Kameranı göstərilən ölkənin üzərinə gətirir."),
        "spin": ("Kameranı döndər", "Kameranı fırladır."),
        "flags": ("Bayraqları göstər", "Bayraqları ekranda göstərir."),
        "clear": ("Konsolu təmizlə", "Konsolun məzmununu təmizləyir."),
        "reloadprovince": ("Əyaləti yenilə", "Göstərilən əyaləti yenidən yükləyir."),
        "party": ("Parti / bayraqlar", "Oyun bayraqlarını əyləncə məqsədli əmr kimi göstərir."),
    },
})

# Komut tanımları: komutların kendisi her dilde DEĞİŞMEZ ve ASCII tutulur.
# Bu, pydirectinput.write() ile Türkçe "ı" gibi karakterlerin gönderilmesi
# sorununu önler. Örneğin "diplomasi" değil, oyunun gerçek komutu "diplomacy"dir.
COMMANDS = [
    # Hile/oyun kutusu
    ("hi", "hi", False, []),
    ("addciv", "addciv {0}", False, ["country_tag"]),
    ("addplayer", "addplayer", False, []),
    ("army", "army", False, []),
    ("money", "money", False, []),
    ("population", "population", False, []),
    ("civs", "civs", False, []),
    ("diplomacy", "diplomacy", False, []),
    ("movement", "movement", False, []),
    ("scale", "scale +{0}", False, ["scale"]),
    ("fps", "fps", False, []),
    ("war", "war +{0} +{1}", False, ["country_id_1", "country_id_2"]),
    ("peace", "peace +{0} +{1}", False, ["country_id_1", "country_id_2"]),
    ("buildport", "buildport", False, []),
    ("buildfort", "buildfort", False, []),
    ("buildtower", "buildtower", False, []),
    ("civ", "civ", False, []),
    ("province", "province", False, []),
    ("showids", "showids", False, []),
    ("showarmy", "showarmy", False, []),
    ("technology", "technology +{0}", False, ["technology_amount"]),
    ("setarmy", "setarmy +{0}", False, ["army_amount"]),
    ("noliberty", "noliberty", False, []),
    ("id", "id", False, []),
    ("economy", "economy", False, []),

    # F1 konsolu
    ("close", "close", True, []),
    ("bye", "bye", True, []),
    ("help", "help", True, []),
    ("info", "info", True, []),
    ("debug", "debug", True, []),
    ("center", "center", True, []),
    ("centerciv", "centerciv +{0}", True, ["country_id"]),
    ("spin", "spin", True, []),
    ("flags", "flags", True, []),
    ("clear", "clear", True, []),
    ("reloadprovince", "reloadprovince +{0}", True, ["province_id"]),
    ("party", "party", True, []),
]

# Oyun komutları kesinlikle ASCII olmalıdır. Özellikle Türkçe "ı" karakteri
# hiçbir komutun gönderim veya ekranda gösterim metnine giremez.
for _key, _template, _console, _params in COMMANDS:
    if not _template.isascii():
        raise ValueError(f"Non-ASCII game command: {_key} -> {_template!r}")

PARAM_KEY_MAP = {
    "country_tag": "country_tag",
    "country_id": "country_id",
    "country_id_1": "country_id_1",
    "country_id_2": "country_id_2",
    "technology_amount": "technology_amount",
    "army_amount": "army_amount",
    "scale": "scale",
    "province_id": "province_id",
}


# ---------------------------------------------------------------------------
# KALICI AYARLAR
# ---------------------------------------------------------------------------
class Settings:
    def __init__(self):
        self.language = "tr"
        self.window_title = DEFAULT_WINDOW_TITLE
        self.console_key = DEFAULT_CONSOLE_KEY
        self.repeat = DEFAULT_REPEAT
        self.delay = DEFAULT_DELAY
        self.chat_pos = None
        self.console_pos = None
        self.load()

    def load(self):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.language = data.get("language", "tr") if data.get("language", "tr") in LANGUAGES else "tr"
            self.window_title = data.get("window_title", DEFAULT_WINDOW_TITLE)
            self.console_key = data.get("console_key", DEFAULT_CONSOLE_KEY)
            self.repeat = max(1, int(data.get("repeat", DEFAULT_REPEAT)))
            self.delay = max(0.05, float(data.get("delay", DEFAULT_DELAY)))
            self.chat_pos = tuple(data["chat_pos"]) if data.get("chat_pos") else None
            self.console_pos = tuple(data["console_pos"]) if data.get("console_pos") else None
        except (OSError, ValueError, TypeError, json.JSONDecodeError):
            pass

    def save(self):
        os.makedirs(CONFIG_DIR, exist_ok=True)
        data = {
            "language": self.language,
            "window_title": self.window_title,
            "console_key": self.console_key,
            "repeat": self.repeat,
            "delay": self.delay,
            "chat_pos": list(self.chat_pos) if self.chat_pos else None,
            "console_pos": list(self.console_pos) if self.console_pos else None,
        }
        tmp = CONFIG_FILE + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        os.replace(tmp, CONFIG_FILE)


settings = Settings()


# ---------------------------------------------------------------------------
# YARDIMCILAR
# ---------------------------------------------------------------------------
def tr(key, **kwargs):
    text = T[settings.language].get(key, T["en"].get(key, key))
    return text.format(**kwargs)


def cmd_text(key):
    return COMMAND_TEXT.get(settings.language, COMMAND_TEXT["en"]).get(
        key, COMMAND_TEXT["en"].get(key, (key, ""))
    )


def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def ensure_admin():
    """Windows'ta gerekirse UAC ile programı yönetici olarak yeniden başlatır."""
    if os.name != "nt":
        return
    try:
        import ctypes
        if ctypes.windll.shell32.IsUserAnAdmin():
            return
    except Exception:
        return

    try:
        import ctypes
        if getattr(sys, "frozen", False):
            executable = sys.executable
            args = sys.argv[1:]
        else:
            executable = sys.executable
            args = [os.path.abspath(__file__)] + sys.argv[1:]
        params = " ".join(f'"{a}"' for a in args)
        result = ctypes.windll.shell32.ShellExecuteW(
            None, "runas", executable, params, None, 1
        )
        if int(result) > 32:
            sys.exit(0)
    except Exception:
        pass


def focus_game_window():
    try:
        matches = [
            w for w in gw.getAllWindows()
            if settings.window_title.lower() in w.title.lower() and w.title.strip()
        ]
        if not matches:
            return None
        win = matches[0]
        if win.isMinimized:
            win.restore()
        win.activate()
        time.sleep(0.15)
        return win
    except Exception:
        return None


def _send_once(command, use_console):
    if use_console:
        pydirectinput.press(settings.console_key)
        time.sleep(0.25)
        if settings.console_pos:
            pydirectinput.click(*settings.console_pos)
        else:
            pydirectinput.click()
    else:
        if settings.chat_pos:
            pydirectinput.click(*settings.chat_pos)
        else:
            pydirectinput.click()
    time.sleep(0.2)
    # Komutlar ASCII'dir: özellikle Türkçe "ı" hiçbir zaman gönderilmez.
    pydirectinput.write(command, interval=0.025)
    time.sleep(0.1)
    pydirectinput.press("enter")
    time.sleep(settings.delay)


def send_command_async(command, use_console=True, status_cb=None):
    def worker():
        win = focus_game_window()
        if win is None:
            if status_cb:
                status_cb(f"⚠ {tr('game_not_found')}", True)
            return
        try:
            for _ in range(max(1, settings.repeat)):
                _send_once(command, use_console)
            if status_cb:
                status_cb(tr("command_sent", command=command), False)
        except Exception as e:
            if status_cb:
                status_cb(tr("command_error", error=e), True)

    threading.Thread(target=worker, daemon=True).start()


# ---------------------------------------------------------------------------
# ARAYÜZ
# ---------------------------------------------------------------------------
class Tooltip:
    def __init__(self, widget, text_getter):
        self.widget = widget
        self.text_getter = text_getter
        self.tip = None
        widget.bind("<Enter>", self.show)
        widget.bind("<Leave>", self.hide)

    def show(self, _event=None):
        self.hide()
        try:
            text = self.text_getter()
            self.tip = tk.Toplevel(self.widget)
            self.tip.wm_overrideredirect(True)
            self.tip.attributes("-topmost", True)
            x = self.widget.winfo_rootx() + self.widget.winfo_width() + 8
            y = self.widget.winfo_rooty() + 4
            self.tip.geometry(f"+{x}+{y}")
            tk.Label(
                self.tip, text=text, justify="left",
                bg="#17100b", fg=COL_TEXT,
                padx=8, pady=6, relief="solid", bd=1,
                font=("Segoe UI", 8), wraplength=330
            ).pack()
        except Exception:
            pass

    def hide(self, _event=None):
        if self.tip is not None:
            try:
                self.tip.destroy()
            except Exception:
                pass
            self.tip = None


class OverlayApp:
    def __init__(self, root):
        self.root = root
        self.collapsed = False
        self._ui_built = False
        self._scroll_canvases = []
        self._drag_data = {"x": 0, "y": 0}
        self._hotkey_registered = False
        self._build_ui()
        self._register_hotkey()
        self.root.bind_all("<MouseWheel>", self._on_global_mousewheel, add="+")
        self.root.bind_all("<Button-4>", self._on_global_mousewheel, add="+")
        self.root.bind_all("<Button-5>", self._on_global_mousewheel, add="+")
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def L(self, key, **kwargs):
        return tr(key, **kwargs)

    def _register_hotkey(self):
        try:
            import keyboard
            keyboard.add_hotkey("f9", lambda: self.root.after(0, self.toggle_visibility))
            self._hotkey_registered = True
        except Exception:
            self._hotkey_registered = False

    def _build_ui(self, geometry=None):
        root = self.root
        root.title(self.L("app_title"))
        root.overrideredirect(True)
        root.attributes("-topmost", True)
        root.configure(bg=COL_BG)
        if geometry:
            root.geometry(geometry)
        elif not self._ui_built:
            root.geometry("390x560+80+80")
        try:
            root.iconbitmap(resource_path("app_icon.ico"))
        except Exception:
            pass
        try:
            root.attributes("-alpha", 0.97)
        except Exception:
            pass

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TNotebook", background=COL_BG, borderwidth=0)
        style.configure(
            "TNotebook.Tab", background=COL_TAB, foreground=COL_TEXT,
            padding=(12, 5), font=("Segoe UI", 9, "bold")
        )
        style.map(
            "TNotebook.Tab",
            background=[("selected", COL_TAB_SEL)],
            foreground=[("selected", COL_ACCENT_LIGHT)]
        )
        style.configure("TFrame", background=COL_BG)
        style.configure(
            "Cmd.TButton", padding=7, background=COL_BTN,
            foreground=COL_TEXT, borderwidth=1, focusthickness=0,
            bordercolor=COL_ACCENT, font=("Segoe UI", 9)
        )
        style.map(
            "Cmd.TButton",
            background=[("active", COL_BTN_HOVER)],
            bordercolor=[("active", COL_ACCENT_LIGHT)]
        )
        style.configure(
            "Save.TButton", padding=8, background=COL_ACCENT,
            foreground="#21140c", borderwidth=0, font=("Segoe UI", 9, "bold")
        )
        style.map("Save.TButton", background=[("active", COL_ACCENT_LIGHT)])

        bar = tk.Frame(root, bg=COL_BAR, height=34)
        bar.pack(fill="x", side="top")
        bar.bind("<ButtonPress-1>", self._start_drag)
        bar.bind("<B1-Motion>", self._on_drag)

        try:
            self._icon_img = tk.PhotoImage(file=resource_path("titlebar_icon.png"))
            tk.Label(bar, image=self._icon_img, bg=COL_BAR).pack(side="left", padx=(8, 2), pady=2)
        except Exception:
            self._icon_img = None

        title_lbl = tk.Label(
            bar, text=self.L("app_title"), bg=COL_BAR,
            fg=COL_ACCENT_LIGHT, font=("Segoe UI", 10, "bold")
        )
        title_lbl.pack(side="left", padx=4)
        title_lbl.bind("<ButtonPress-1>", self._start_drag)
        title_lbl.bind("<B1-Motion>", self._on_drag)

        close_btn = tk.Label(
            bar, text="✕", bg=COL_BAR, fg=COL_ERROR,
            font=("Segoe UI", 10, "bold"), cursor="hand2"
        )
        close_btn.pack(side="right", padx=8)
        close_btn.bind("<Button-1>", lambda _e: self.close())

        min_btn = tk.Label(
            bar, text="—", bg=COL_BAR, fg=COL_TEXT,
            font=("Segoe UI", 10, "bold"), cursor="hand2"
        )
        min_btn.pack(side="right", padx=4)
        min_btn.bind("<Button-1>", lambda _e: self.toggle_visibility())

        self.status_var = tk.StringVar(value=self.L("ready"))
        self.status_label = tk.Label(
            root, textvariable=self.status_var, bg=COL_BG,
            fg=COL_SUCCESS, font=("Segoe UI", 8),
            wraplength=370, justify="left"
        )
        self.status_label.pack(fill="x", padx=10, pady=(6, 2))

        nb = ttk.Notebook(root)
        nb.pack(fill="both", expand=True, padx=7, pady=7)

        cheat_tab = self._make_scroll_tab(nb, use_console=False)
        console_tab = self._make_scroll_tab(nb, use_console=True)
        settings_tab = self._make_settings_tab(nb)

        nb.add(cheat_tab, text=self.L("cheats"))
        nb.add(console_tab, text=self.L("console"))
        nb.add(settings_tab, text=self.L("settings"))

        self.body_widgets = [nb, self.status_label]
        self._ui_built = True

    def _make_scroll_tab(self, parent, use_console):
        frame = ttk.Frame(parent)
        canvas = tk.Canvas(frame, bg=COL_BG, highlightthickness=0, bd=0)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        inner = ttk.Frame(canvas)

        inner.bind("<Configure>", lambda _e: canvas.configure(scrollregion=canvas.bbox("all")))
        window_id = canvas.create_window((0, 0), window=inner, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        def resize_inner(event):
            canvas.itemconfigure(window_id, width=event.width)

        canvas.bind("<Configure>", resize_inner)
        self._scroll_canvases.append(canvas)

        for key, template, console, params in COMMANDS:
            if console != use_console:
                continue
            label, description = cmd_text(key)
            btn = ttk.Button(
                inner, text=label, style="Cmd.TButton",
                command=lambda k=key, t=template, p=params, c=console: self._on_click(k, t, p, c)
            )
            btn.pack(fill="x", padx=4, pady=2)
            Tooltip(
                btn,
                lambda k=key, t=template: self.L(
                    "tooltip", command=t, description=cmd_text(k)[1]
                )
            )
        return frame

    def _make_settings_tab(self, parent):
        outer = ttk.Frame(parent)
        canvas = tk.Canvas(outer, bg=COL_BG, highlightthickness=0, bd=0)
        scrollbar = ttk.Scrollbar(outer, orient="vertical", command=canvas.yview)
        frame = ttk.Frame(canvas)

        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.bind("<Configure>", lambda _e: canvas.configure(scrollregion=canvas.bbox("all")))
        window_id = canvas.create_window((0, 0), window=frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        canvas.bind("<Configure>", lambda event: canvas.itemconfigure(window_id, width=event.width))
        self._scroll_canvases.append(canvas)

        self._populate_settings_frame(frame)
        return outer

    def _on_global_mousewheel(self, event):
        if not self.root.winfo_exists():
            return
        try:
            px = self.root.winfo_pointerx()
            py = self.root.winfo_pointery()
        except Exception:
            return

        for canvas in reversed(self._scroll_canvases):
            try:
                x0 = canvas.winfo_rootx()
                y0 = canvas.winfo_rooty()
                x1 = x0 + canvas.winfo_width()
                y1 = y0 + canvas.winfo_height()
                if x0 <= px <= x1 and y0 <= py <= y1:
                    if getattr(event, "num", None) == 4:
                        units = -5
                    elif getattr(event, "num", None) == 5:
                        units = 5
                    else:
                        delta = getattr(event, "delta", 0)
                        if delta == 0:
                            return "break"
                        units = -max(1, int(abs(delta) / 120)) * (1 if delta > 0 else -1) * 5
                    canvas.yview_scroll(units, "units")
                    return "break"
            except tk.TclError:
                continue
        return None

    def _populate_settings_frame(self, frame):
        heading = tk.Label(
            frame, text=self.L("general"), bg=COL_BG, fg=COL_ACCENT_LIGHT,
            font=("Segoe UI", 10, "bold")
        )
        heading.grid(row=0, column=0, columnspan=2, sticky="w", padx=8, pady=(8, 6))

        def add_row(r, label, var, width=21):
            tk.Label(
                frame, text=label, bg=COL_BG, fg=COL_TEXT,
                font=("Segoe UI", 9)
            ).grid(row=r, column=0, sticky="w", padx=8, pady=4)
            entry = tk.Entry(
                frame, textvariable=var, width=width,
                bg=COL_BTN, fg=COL_TEXT, insertbackground=COL_TEXT,
                relief="flat", highlightthickness=1,
                highlightbackground=COL_ACCENT, highlightcolor=COL_ACCENT_LIGHT
            )
            entry.grid(row=r, column=1, sticky="ew", padx=8, pady=4)
            return entry

        self.language_var = tk.StringVar(value=LANGUAGES[settings.language])
        tk.Label(
            frame, text=self.L("language"), bg=COL_BG, fg=COL_TEXT,
            font=("Segoe UI", 9)
        ).grid(row=1, column=0, sticky="w", padx=8, pady=4)

        self.language_combo = ttk.Combobox(
            frame, textvariable=self.language_var,
            values=list(LANGUAGES.values()), state="readonly", width=19
        )
        self.language_combo.grid(row=1, column=1, sticky="ew", padx=8, pady=4)
        self.language_combo.bind("<<ComboboxSelected>>", self._change_language)

        self.title_var = tk.StringVar(value=settings.window_title)
        self.key_var = tk.StringVar(value=settings.console_key)
        self.repeat_var = tk.StringVar(value=str(settings.repeat))
        self.delay_var = tk.StringVar(value=str(settings.delay))

        add_row(2, self.L("game_window"), self.title_var)
        add_row(3, self.L("console_key"), self.key_var)
        add_row(4, self.L("repeat"), self.repeat_var)
        add_row(5, self.L("delay"), self.delay_var)

        ttk.Button(
            frame, text=self.L("save"), style="Save.TButton",
            command=self._save_settings
        ).grid(row=6, column=0, columnspan=2, sticky="ew", padx=8, pady=(8, 10))

        tk.Frame(frame, bg=COL_ACCENT, height=1).grid(
            row=7, column=0, columnspan=2, sticky="ew", padx=8, pady=5
        )

        tk.Label(
            frame, text=self.L("input_positions"), bg=COL_BG,
            fg=COL_ACCENT_LIGHT, font=("Segoe UI", 9, "bold")
        ).grid(row=8, column=0, columnspan=2, sticky="w", padx=8, pady=(5, 2))

        self.cursor_var = tk.StringVar(value=f"{self.L('cursor')}: -")
        tk.Label(
            frame, textvariable=self.cursor_var, bg=COL_BG,
            fg=COL_TEXT_MUTED, font=("Segoe UI", 8)
        ).grid(row=9, column=0, columnspan=2, sticky="w", padx=8, pady=(2, 4))

        self.chat_pos_var = tk.StringVar(value=self._pos_text(settings.chat_pos))
        ttk.Button(
            frame, text=self.L("chat_position"), style="Cmd.TButton",
            command=lambda: self._capture_position("chat_pos", self.chat_pos_var)
        ).grid(row=10, column=0, columnspan=2, sticky="ew", padx=8, pady=2)
        tk.Label(
            frame, textvariable=self.chat_pos_var, bg=COL_BG,
            fg=COL_TEXT_MUTED, font=("Segoe UI", 8)
        ).grid(row=11, column=0, columnspan=2, sticky="w", padx=8)

        self.console_pos_var = tk.StringVar(value=self._pos_text(settings.console_pos))
        ttk.Button(
            frame, text=self.L("console_position"), style="Cmd.TButton",
            command=lambda: self._capture_position("console_pos", self.console_pos_var)
        ).grid(row=12, column=0, columnspan=2, sticky="ew", padx=8, pady=(7, 2))
        tk.Label(
            frame, textvariable=self.console_pos_var, bg=COL_BG,
            fg=COL_TEXT_MUTED, font=("Segoe UI", 8)
        ).grid(row=13, column=0, columnspan=2, sticky="w", padx=8)

        tk.Label(
            frame, text=self.L("hint"), bg=COL_BG, fg=COL_TEXT_MUTED,
            font=("Segoe UI", 8), justify="left", wraplength=350
        ).grid(row=14, column=0, columnspan=2, sticky="w", padx=8, pady=(8, 4))

        tk.Label(
            frame, text=self.L("shortcut"), bg=COL_BG, fg=COL_ACCENT_LIGHT,
            font=("Segoe UI", 8, "bold")
        ).grid(row=15, column=0, columnspan=2, sticky="w", padx=8, pady=(2, 8))

        return frame

    def _change_language(self, _event=None):
        selected = self.language_var.get()
        settings.language = next((k for k, v in LANGUAGES.items() if v == selected), "tr")
        settings.save()

        # Dil değişirken pencerenin mevcut ekran konumu ve boyutu aynen korunur.
        current_geometry = self.root.geometry()
        for widget in self.root.winfo_children():
            widget.destroy()
        self._scroll_canvases.clear()
        self._build_ui(current_geometry)
        self._set_status(self.L("settings_saved"))

    def _pos_text(self, pos):
        if pos:
            return f"({pos[0]}, {pos[1]})"
        return self.L("not_saved")

    def _update_cursor_readout(self):
        try:
            x, y = pydirectinput.position()
            self.cursor_var.set(f"{self.L('cursor')}: ({x}, {y})")
        except Exception:
            pass
        if self.root.winfo_exists():
            self.root.after(300, self._update_cursor_readout)

    def _capture_position(self, attr_name, display_var):
        def worker():
            for seconds in (3, 2, 1):
                self._set_status(self.L("countdown", seconds=seconds))
                time.sleep(1)
            x, y = pydirectinput.position()
            setattr(settings, attr_name, (x, y))
            settings.save()

            self.root.after(0, lambda: display_var.set(self._pos_text((x, y))))
            self._set_status(f"{self.L('position_saved')}: ({x}, {y})")

        threading.Thread(target=worker, daemon=True).start()

    def _save_settings(self):
        settings.window_title = self.title_var.get().strip() or DEFAULT_WINDOW_TITLE
        settings.console_key = self.key_var.get().strip().lower() or DEFAULT_CONSOLE_KEY
        try:
            settings.repeat = max(1, int(self.repeat_var.get()))
        except ValueError:
            settings.repeat = DEFAULT_REPEAT
        try:
            settings.delay = max(0.05, float(self.delay_var.get().replace(",", ".")))
        except ValueError:
            settings.delay = DEFAULT_DELAY
        settings.save()
        self._set_status(self.L("settings_saved"))

    def _on_click(self, key, template, params, use_console):
        values = []
        for param in params:
            prompt = self.L(PARAM_KEY_MAP[param])
            while True:
                value = simpledialog.askstring(self.L("enter_value"), prompt, parent=self.root)
                if value is None:
                    self._set_status(self.L("cancelled"))
                    return
                value = value.strip()
                if not value:
                    messagebox.showwarning(self.L("warning"), self.L("invalid_value"), parent=self.root)
                    continue
                if param == "scale":
                    try:
                        if not 1 <= int(value) <= 5:
                            raise ValueError
                    except ValueError:
                        messagebox.showwarning(self.L("warning"), self.L("invalid_value"), parent=self.root)
                        continue
                values.append(value)
                break

        try:
            command = template.format(*values)
        except (IndexError, KeyError) as e:
            messagebox.showerror(self.L("error"), str(e), parent=self.root)
            return

        pos = settings.console_pos if use_console else settings.chat_pos
        if pos is None:
            box = self.L("console_box" if use_console else "chat_box")
            messagebox.showwarning(
                self.L("position_missing"),
                self.L("position_missing_text", box=box),
                parent=self.root
            )

        self._set_status(f"{self.L('sending')}: {command} ...")
        send_command_async(command, use_console=use_console, status_cb=self._set_status)

    def _set_status(self, text, error=False):
        def update():
            self.status_var.set(text)
            # Hata/başarı renklerini durum bazında ayır.
            try:
                self.status_label.configure(fg=COL_ERROR if error else COL_SUCCESS)
            except Exception:
                pass
        try:
            self.root.after(0, update)
        except Exception:
            pass

    def toggle_visibility(self):
        if self.collapsed:
            self.root.deiconify()
            self.collapsed = False
        else:
            self.root.withdraw()
            self.collapsed = True

    def _start_drag(self, event):
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def _on_drag(self, event):
        x = self.root.winfo_pointerx() - self._drag_data["x"]
        y = self.root.winfo_pointery() - self._drag_data["y"]
        self.root.geometry(f"+{x}+{y}")

    def close(self):
        try:
            if self._hotkey_registered:
                import keyboard
                keyboard.unhook_all_hotkeys()
        except Exception:
            pass
        try:
            settings.save()
        except Exception:
            pass
        try:
            self.root.unbind_all("<MouseWheel>")
            self.root.unbind_all("<Button-4>")
            self.root.unbind_all("<Button-5>")
        except Exception:
            pass
        self.root.destroy()


def main():
    ensure_admin()
    root = tk.Tk()
    app = OverlayApp(root)
    root.after(300, app._update_cursor_readout)
    root.mainloop()


if __name__ == "__main__":
    main()
