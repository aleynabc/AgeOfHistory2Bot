; ============================================================
; Age Of History 2 Bot - Professional Installer
; ============================================================

#define MyAppName "Age Of History 2 Bot"
#define MyAppVersion "1.1.2"
#define MyAppExeName "AgeOfHistory2Bot.exe"
#define MyAppPublisher "Age Of History 2 Bot"
#define MyAppURL "https://github.com/"

[Setup]
AppId={{B7E2B7B4-7C7D-4A3E-9B5B-0A0201100001}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
DisableProgramGroupPage=yes
OutputDir=installer_output
OutputBaseFilename=AgeOfHistory2Bot_Kurulum
SetupIconFile=app_icon.ico
UninstallDisplayIcon={app}\{#MyAppExeName}
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=admin
ArchitecturesInstallIn64BitMode=x64compatible
VersionInfoVersion={#MyAppVersion}
VersionInfoDescription={#MyAppName}
VersionInfoProductName={#MyAppName}
VersionInfoCompanyName={#MyAppPublisher}
CloseApplications=yes
RestartApplications=no

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "turkish"; MessagesFile: "compiler:Languages\Turkish.isl"

[Tasks]
Name: "desktopicon"; Description: "Masaüstünde kısayol oluştur"; GroupDescription: "Ek görevler:"; Flags: checkedonce
Name: "startmenuicon"; Description: "Başlat menüsünde kısayol oluştur"; GroupDescription: "Ek görevler:"; Flags: checkedonce

[Files]
Source: "dist\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "README.md"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
; Bunlar gerçek Windows .lnk kısayollarıdır. Eski bozuk kısayolları kullanmayın.
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; WorkingDir: "{app}"; IconFilename: "{app}\{#MyAppExeName}"; Tasks: desktopicon
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; WorkingDir: "{app}"; IconFilename: "{app}\{#MyAppExeName}"; Tasks: startmenuicon
Name: "{group}\{#MyAppName} Kaldır"; Filename: "{uninstallexe}"

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{#MyAppName} uygulamasını şimdi çalıştır"; WorkingDir: "{app}"; Flags: nowait postinstall skipifsilent
