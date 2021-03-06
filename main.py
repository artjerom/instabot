from queue import Queue
import glob, os
from modules import getUnsplasLinks, Dowlander, UploadPhotoToInstagram, setInterval
import urllib

def main(urls):
  queue = Queue()
  for i in range(len(urls)):
    t = Dowlander(queue, './images')
    t.setDaemon(True)
    t.start()
  for url in urls:
    queue.put(url)

  queue.join()
  files = glob.glob('./images/*')
  for file in files:
    print(file)
    inst = UploadPhotoToInstagram(file)
    inst.run()

if __name__ == '__main__':
  urls = getUnsplasLinks('https://api.unsplash.com/collections/1538150/photos')

  main(urls)
  # apiUrl = 'https://api.pinterest.com/v3/pidgets/boards/highquality/travel/pins/'
  # urls = createScopeLink(apiUrl)
  # main(urls)
  # files = glob.glob('./images/*.jpg')
  # if (len(files) >= len(urls)):
    # InstagramAPI = InstagramAPI('sapaDart', 'xaNokia81aB420x')
    # InstagramAPI.login()
    # for file in glob.glob('./images/*.jpg'):
      # caption = "Подписывайся и ставь лайки"
      # InstagramAPI.uploadPhoto(file, caption=caption)

