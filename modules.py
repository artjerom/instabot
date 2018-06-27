from urllib.request import Request, urlopen, urlretrieve
import os, json, threading, glob
from queue import Queue
from InstagramAPI import InstagramAPI
from config import AUTH_HEADER_UNSPLASH, INSTAGRAM_LOGIN, INSTAGRAM_PASSWORD

def setInterval(func,time, argument):
  e = threading.Event()
  while not e.wait(time):
    func(argument)

# Return array of link unsplash
def getUnsplasLinks(url):
  result = []
  q = Request(url)
  q.add_header('Authorization', AUTH_HEADER_UNSPLASH)
  with urlopen(q) as response:
    data = json.loads(response.read().decode())
  for pin in data:
    result.append(pin['urls']['regular'])
  return result

class UploadPhotoToInstagram():
  def __init__(self, img):
    self.img = img

  def run(self):
    print('run ins')
    self.uploadImg()
    self.removeImg()
  def removeImg(self):
    os.remove(self.img)
  def uploadImg(self):
    instagramAPI = InstagramAPI(INSTAGRAM_LOGIN, INSTAGRAM_PASSWORD)
    instagramAPI.login()
    caption = "Подписывайся и ставь лайки"
    instagramAPI.uploadPhoto(self.img, caption=caption)

# dowland images from url
class Dowlander(threading.Thread):
  def __init__(self, queue, outFolderName):
    threading.Thread.__init__(self)
    self.queue = queue
    self.outFolderName = outFolderName

    if not os.path.exists(self.outFolderName):
      os.makedirs(self.outFolderName)

  def run(self):
    while True:
      url = self.queue.get()
      self.dowland_file(url)
      self.queue.task_done()

  def dowland_file(self, url):
    count = len(glob.glob(self.outFolderName + '/*'))
    handle = urlopen(url)
    fname = os.path.basename(self.outFolderName + '/' + url)
    with open(self.outFolderName + '/' + fname, 'wb') as f:
      while True:
        chunk = handle.read(1024)
        if not chunk:
          break
        f.write(chunk)