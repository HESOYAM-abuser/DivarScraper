#      ~~~ VARIABLES ~~~      #
DEFAULT_LINK = "https://divar.ir/v/"



#      ~~~ FUNCTIONS ~~~      #
def link(data):
          for i in data:
                    token = data[data.index(i)]['token']
                    link = DEFAULT_LINK + token
                    data[data.index(i)]['link_address'] = link 
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