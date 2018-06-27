from queue import Queue
import glob, os
from InstagramAPI import InstagramAPI
from modules import getUnsplasLinks

def main():
  queue = Queue()
  urls = getUnsplasLinks('https://api.unsplash.com/collections/1538150/photos')
  print(urls)

  # for i in range(len(urls)):
    # t = Dowlander(queue, './images')
    # t.setDaemon(True)
    # t.start()
  # for url in urls:
    # queue.put(url)
# 
  # queue.join()

if __name__ == '__main__':
<<<<<<< HEAD
  main()
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
=======
  apiUrl = 'https://api.pinterest.com/v3/pidgets/boards/highquality/travel/pins/'
  urls = createScopeLink(apiUrl)
  main(urls)
  files = glob.glob('./images/*.jpg')
  if (len(files) >= len(urls)):
    InstagramAPI = InstagramAPI('****', '****')
    InstagramAPI.login()
    for file in glob.glob('./images/*.jpg'):
      caption = "Подписывайся и ставь лайки"
      InstagramAPI.uploadPhoto(file, caption=caption)
>>>>>>> b5f6a4e17b0e7aa012eef6913d36773851fa7e3d

