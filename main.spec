# -*- mode: python ; coding: utf-8 -*-
import os
import sys

from pathlib import Path

from pylibdmtx import pylibdmtx
from pyzbar import pyzbar

block_cipher = None

sys.modules['FixTk'] = None

a = Analysis(['main.py'],
             pathex=[],
             binaries=[],
             datas=[
                ('temp', 'temp'),
                ('venv\Lib\site-packages\plyer', 'plyer'),
             ],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

ICON = 'temp/print.ico'

# dylibs not detected because they are loaded by ctypes
a.binaries += TOC([
    (Path(dep._name).name, dep._name, 'BINARY')
    for dep in pylibdmtx.EXTERNAL_DEPENDENCIES + pyzbar.EXTERNAL_DEPENDENCIES
])

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='silent_print',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None,
          icon=ICON)
