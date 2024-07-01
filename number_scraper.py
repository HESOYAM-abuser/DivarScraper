#      ~~~ IMPORTS ~~~      #
import requests 
from json import loads



#      ~~~ VARIABLES ~~~      #
DEFAULT_LINK = "https://api.divar.ir/v5/posts/", "/contact/"



#      ~~~ FUNCTIONS ~~~      #
def link(data):
          for i in data:
                    try:
                              url = DEFAULT_LINK[0]+data[data.index(i)]['token']
                              url = url + DEFAULT_LINK[1]
                              response = requests.get(url)
                              number = (loads(response.content))['widgets']['contact']['phone']
                              data[data.index(i)]['number'] = number
                              print(data.index(i))
                    except:
                              print(response.content, data.index(i))
                              exit()
          return data



#      ~~~ MAIN ~~~      #
if __name__ == '__main__':
          with open('scraped_data/data121.txt', 'r') as f:
                    data = eval(f.read())
                    data = link(data)
          with open('scraped_data/data121.txt', 'w') as f:
                    f.write('[\n')
                    for i in data:
                              f.write((' '*4)+str(i)+','+'\n')
                    f.write(']')



