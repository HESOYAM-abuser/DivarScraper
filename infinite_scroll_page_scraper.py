#      ~~~ IMPORTS ~~~      #
from json import loads
from requests import post
from datetime import datetime, timedelta
from time import sleep



#      ~~~ FUNCTIONS ~~~      #
def theTime(k=0):
          '''
          '''
          if k == 0 or k == 1:
                    time = int((datetime.now()-timedelta(seconds=(300*k))).timestamp())
                    time = str(time)[1:]+('0'*6)
                    time = int(time)
          elif k == 2 or k ==3:
                    k = (1800*k)-18000
                    time = int((datetime.now()-timedelta(seconds=(k))).timestamp())
                    time = str(time)[1:]+('0'*6)
                    time = int(time)
          elif k >= 5:
                    time = int((datetime.now()-timedelta(days=(k-4))).timestamp())
                    time = str(time)[1:]+('0'*6)
                    time = int(time)
          return time

def chunkProductLoader(url, json_data, date):
          '''
          '''
          data_chunk = []
          json_data['last-post-date'] = date
          response = post(url, json=json_data)
          json_data =response.content
          try:
                    if json_data != b'':
                              data = loads(json_data)
                              for i in range(len(data['widget_list'])):
                                        data_chunk.append(data['web_widgets']['post_list'][i]['data'])
                              time = data['last_post_date'] 
                              return data_chunk, time, None 
                    else:
                              return None , date, None
          except Exception as error0:
                    return False, False, error0

def allProductLoader(url, json_data):
          '''
          '''
          attempts = [0, 0]
          all_data = []
          time = first_time = theTime()
          while True:
                    data_chunk, time, error1= chunkProductLoader(url, json_data, time)
                    print(time)
                    if data_chunk == None:
                              if attempts[0] == 36:
                                        print('Done!')
                                        break
                              else:
                                        attempts[0] = attempts[0] + 1
                                        if first_time == time:
                                                  time = first_time = theTime(attempts[0])
                                        else:
                                                  pass           
                                        sleep(0.1)
                                        continue
                    if data_chunk == False:
                              if attempts[1] == 6:
                                        print(f'An error occurred\n{error1}')
                                        break
                              else:
                                        attempts[1] = attempts[1] + 1
                                        sleep(5)
                                        continue
                    if data_chunk != False and data_chunk != None:
                              for i in data_chunk:
                                        all_data.append(i)
          return all_data



#      ~~~ MAIN ~~~      #
if __name__ == '__main__':
          url = 'https://api.divar.ir/v8/search/777/ROOT'
          post_data = {"json_schema":{"category":{"value":"ROOT"}},"last-post-date":None}
          main0 = allProductLoader(url, post_data)
          with open('scraped_data/data121.txt', 'w') as f:
                    f.write('[\n')
                    for i in main0:
                              f.write((' '*4)+str(i)+','+'\n')
                    f.write(']')
          


