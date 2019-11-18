# -*- mode: python -*-

block_cipher = None


a = Analysis(['jiebaapp.py'],
             pathex=['/Users/Elwing/PycharmProjects/qtdemo'],
             binaries=[],
             datas=[('dict.txt.big', '.'), ('idf.txt', './jieba/analyse')],
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
          [],
          exclude_binaries=True,
          name='jiebaapp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='jiebaapp')
app = BUNDLE(coll,
             name='jiebaapp.app',
             icon=None,
             bundle_identifier=None)
