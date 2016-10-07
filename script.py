from socketIO_client import SocketIO, BaseNamespace
import os
import urllib2

class Namespace(BaseNamespace):
    def on_connect(self):
        print('[connected]')
        self.emit("setname", get_name())
        self.emit("cwd", cwd())
	def on_listdir(self, *args):
        print("[listdir]", args)
        self.emit("dirlist", list_dir(args))
    def on_listmusic(self, *args):
        self.emit("musiclist", list_musics())
        print("[listmusic]", list_musics())
    def on_ff(self, *args):
        print("on_ff", args)
        self.emit("serverlog","on_ff")
    def on_download(self, *args):
        print("[on_download] starting download function...")
        download(args)
    def on_playasong(self, *args):
        print("[on_playsong] starting 'playasong' function...")
        playasong(args)

socketIO = SocketIO("https://phpuploadfile-arjenbakur.c9users.io", 8080, Namespace)
dirname = "musics/"

def list_dir(dirpath):
    dirs = os.listdir(dirpath[0])
    return dirs
def list_musics():
    dirs = os.listdir(dirname)
    return dirs
def cwd():
    cwd = os.getcwd()
    return cwd
def get_name():
    name = os.environ['COMPUTERNAME']
    return name
def download(url):
    print("[download]", url)
    filename = url[0].split("/")[-1]
    print("[download] filename: ", filename)
    f = urllib2.urlopen(url[0])
    data = f.read()
    with open(dirname + "/" + filename, "wb") as code:
        code.write(data)
    print("[download] completed")
def playasong(mp3Name):
    mp3Name = dirname + mp3Name[0]

socketIO.wait()
