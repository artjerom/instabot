import urllib.request, json
import os
from queue import Queue
import threading

# create array of url
def createScopeLink(apiUrl):
  links = []
  with urllib.request.urlopen(apiUrl) as url:
    data = json.loads(url.read().decode())
  for pin in data['data']['pins']:
    links.append(pin['images']['237x']['url'])
    if len(links) > 5:
      break
  return links

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
    handle = urllib.request.urlopen(url)
    fname = os.path.basename(self.outFolderName + '/' + url)
    with open(self.outFolderName + '/' + fname, 'wb') as f:
      while True:
        chunk = handle.read(1024)
        if not chunk:
          break
        f.write(chunk)