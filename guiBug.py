import os,sys,tempfile


guiFolderPath = "C:\Program Files\Unity\Editor\Data\UnityExtensions\Unity\GUISystem"
unityPath ="\"C:\Program Files\Unity\Editor\Unity.exe\""

def tmpFiles(arg):
    tmp = tempfile.gettempdir()
    os.rename(arg,tmp+"\\"+os.path.split(arg)[1])

def getFiles(arg):
    tmp = tempfile.gettempdir()
    os.rename(tmp+"\\"+os.path.split(arg)[1],arg)

def isAdmin():
    import ctypes, os
    is_admin = 0
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin


if isAdmin():
    print "***Abra o projeto***"
    tmpFiles(guiFolderPath)
    os.system(unityPath)
    print "***Feche o projeto***"
    getFiles(guiFolderPath)
    print "***Bug Corrigido \o/***"
    os.system(unityPath)
else:
    print "Esse comando deve ser executado como Admin"
    os.system("pause")

