# -*- mode: python ; coding: utf-8 -*-

import sys
import os
from PyInstaller.utils.hooks import collect_submodules, collect_data_files

# 明确列出所有需要的PyQt5模块
pyqt5_modules = [
    'PyQt5',
    'PyQt5.QtCore',
    'PyQt5.QtGui',
    'PyQt5.QtWidgets',
    'PyQt5.QtNetwork',
    'PyQt5.QtPrintSupport',
    'PyQt5.QtSvg',
    'PyQt5.QtWebEngineWidgets',
    'PyQt5.sip',
    'sip'
]

# 收集项目模块
ui_modules = collect_submodules('ui')
core_modules = collect_submodules('core')

# 组合所有隐藏导入
hiddenimports = pyqt5_modules + ui_modules + core_modules + [
    'requests',
    'urllib3',
    'chardet',
    'certifi',
    'idna',
    'charset_normalizer',
    'lxml',
    'lxml.etree',
    'lxml._elementpath',
    'lxml.html',
    'lxml.html.clean',
    'lxml.html.defs',
]

# 收集数据文件
datas = [
    ('ui', 'ui'),
    ('core', 'core'),
]

readme_path = 'README.md'
if os.path.exists(readme_path):
    datas.append((readme_path, '.'))

# 收集PyQt5的数据文件
datas += collect_data_files('PyQt5')

block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='WeLearnAuto',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    icon='icon.ico',
)