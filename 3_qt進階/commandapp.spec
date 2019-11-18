# -*- mode: python -*-
import glob

block_cipher = None

defaultdata = [(fn, "./test") for fn in glob.glob("./test/*.ci")]

a = Analysis(['commandapp.py'],
             pathex=['/Users/Elwing/PycharmProjects/qtdemo'],
             binaries=[],
             datas=[('command.ui', '.')] + defaultdata,
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
          name='commandapp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name='commandapp.app',
             icon='icon.icns',
             bundle_identifier=None)
