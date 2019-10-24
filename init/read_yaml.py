import yaml

def read_yam(data):
    with open('D:\\telephone\Data'+'\\'+data+'.yaml') as f:
        return yaml.load(f,Loader=yaml.FullLoader)


if __name__ == '__main__':
    dt = read_yam('data1').get('Data')
    dt_list = []
    for i in dt.values():
        dt_list.append(i.values())
    print(dt_list)