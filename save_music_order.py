import os
import platform
from datetime import datetime
black_list=["(music7s.appspot.com)","[YT2mp3.info] ","X2Download.app ","X2Download.com ","y2mate.com - ","Y2mate.mx - ","y2meta.com - "]
def get_creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return os.path.getmtime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime
def generate_new_name(old_name):
    new_name=old_name
    for bad in black_list:
        if bad in old_name:
            try:
                new_name = str.replace(bad, '')
            except:
                print(bad,old_name)
    return new_name

def rename_musics(music_directory):
    os.chdir(music_directory)
    count=0
    for music in os.listdir():
        creation_date=creation_date(music)
        new_name=generate_new_name(music)
        os.rename(music,str(creation_date)+new_name)
        count+=1
        if count%10==0:
            print(f"{count}/{len(os.listdir())}")
    
music_directory="D:\флеха\содержимое флехи\Topsecret\песенки — копия"
print(os.listdir())
#rename_musics(music_directory)
os.chdir(music_directory)
count=0
for music in os.listdir():
    creation_date=datetime.utcfromtimestamp(get_creation_date(music)).strftime('%Y-%m-%d')
    new_name=generate_new_name(music)
    os.rename(music,creation_date+(new_name))
    count+=1
    if count%10==0:
        print(f"{count}/{len(os.listdir())}")
