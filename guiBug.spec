# -*- mode: python -*-
a = Analysis(['guiBug.py'],
             pathex=['C:\\Users\\dedign2\\Desktop\\buGUI'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='guiBug.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True , icon='bug.ico')
