# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec for Age Of History 2 Bot

a = Analysis(
    ['overlay.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('titlebar_icon.png', '.'),
        ('app_icon.ico', '.'),
    ],
    hiddenimports=['keyboard'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='AgeOfHistory2Bot',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    uac_admin=True,
    icon='app_icon.ico',
)
