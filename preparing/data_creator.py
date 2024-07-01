import re

def data_main():
          data = {}
          file0 = open('locations.txt' , 'r')
          lines = list(file0)
          file0.close()
          for i  in lines:
                    data[re.sub('\n', '', i)] = []
          return data
if __name__ == '__main__':
          print(data_main())