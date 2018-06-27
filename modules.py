from urllib.request import Request, urlopen, urlretrieve
import os, json, threading, glob
from queue import Queue
from config import AUTH_HEADER_UNSPLASH

# Return array of link unsplash
def getUnsplasLinks(url):
  result = []
  q = Request(url)
  q.add_header('Authorization', AUTH_HEADER_UNSPLASH)
  with urlopen(q) as response:
    data = json.loads(response.read().decode())
  for pin in data:
    result.append(pin['urls']['thumb'])
  return result

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
    urlretrieve(url, self.outFolderName + '/pic_' + str(count) + '.jpeg')
    # handle = urlopen(url)
    # fname = os.path.basename(self.outFolderName + '/' + url)
    # with open(self.outFolderName + '/' + fname, 'wb') as f:
      # while True:
        # chunk = handle.read(1024)
        # if not chunk:
          # break
        # f.write(chunk)