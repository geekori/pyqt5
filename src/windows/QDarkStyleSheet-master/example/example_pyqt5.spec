# -*- mode: python -*-

block_cipher = None


a = Analysis(['example_pyqt5.py'],
             pathex=['/MyStudio/resources/PyQt5/src/window_graghics_effect/QDarkStyleSheet-master/example'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='example_pyqt5',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name='example_pyqt5.app',
             icon=None,
             bundle_identifier=None)
