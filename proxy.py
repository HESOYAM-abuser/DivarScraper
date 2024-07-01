#      ~~~ IMPORTS ~~~      #
import threading
import requests
from datetime import datetime
from json import loads
from requests_html import HTMLSession


#      ~~~ VARIABLES ~~~      #
API_URL = 'https://api.openproxy.space/' 
URL = 'https://openproxy.space/'


#      ~~~ FUNCTIONS ~~~      #
def TheTime():
          time = int((datetime.now()).timestamp()) * 1000
          return time

def ChunkLoader(time_stamp):
          '''
          '''
          chunk = 0
          json_data = []
          ts = time_stamp
          while True:
                    options = f'list?skip={chunk}&ts={ts}' 
                    response = requests.get(url=API_URL+options)
                    chunk += 18
                    chunk_data = loads(response.content)
                    if len(chunk_data) == 0:
                              break
                    for i in chunk_data:
                              json_data.append(i['code'])
          print('chunk loader finished')
          return json_data
          
def ChunkScraper(codes, results):
          proxies = []
          print('+')
          for code in codes:
                    options = f'list/{code}'
                    session = HTMLSession()
                    response = session.get(URL+options)
                    response.html.render(keep_page=False)
                    text = response.html.find('textarea')
                    text = text[0].text
                    proxy_chunk = text.split(' ')
                    for x in proxy_chunk:
                              proxies.append(x)
                    print(code, len(codes), codes.index(code))
          results = proxies

def ProxyScraper(code_list, thread_number=1):
          '''
          '''
          code_list = list(set(code_list))
          grouped_codes = []
          if thread_number <= len(code_list):
                    group_len = len(code_list) // thread_number
                    leftover = len(code_list) % thread_number
                    leftover_items = code_list[-leftover:len(code_list)]
                    code_list = list(set(code_list)-set(leftover_items))
                    for i in range(0, len(code_list), group_len):
                              grouped_codes.append(code_list[i:i+group_len])
                    if leftover != 0:
                              for i in leftover_items:
                                        grouped_codes[leftover_items.index(i)].append(i)
                    else:
                              pass
          else:
                    grouped_codes = [[code] for code in code_list]
          threads = []
          results = [[] for i in range(len(grouped_codes))]
          print(len(grouped_codes))
          print('=========================================')
          for i in range(len(grouped_codes)-1):
                    t = threading.Thread(target=ChunkScraper, args=(grouped_codes[i], results[i]))
                    t.start()
                    threads.append(t)
          print(threading.active_count(), len(grouped_codes))
          print("+++++++++++++++++++++++++++++++++++++++++")
          
          for thread in threads:

                    print(thread.getName(), thread.is_alive())
          
          output = []
          for chunk in results:
                    for i in chunk:
                              output.append(i)
          return output


#      ~~~ MAIN ~~~      #
if __name__ == '__main__':
          data = ProxyScraper(ChunkLoader(TheTime()), thread_number=16)
          print(len(data))
          with open('proxy_data.txt', 'w') as f:
                    for i in data:
                              f.write(f'{i}\n')