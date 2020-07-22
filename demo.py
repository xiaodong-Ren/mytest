##爬虫:模拟浏览器向服务器发送请求
import requests
import re
def send_request():
    url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2020-07-22&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=SHH&purpose_codes=ADULT'
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0',
    'Cookie': '_uab_collina=159539181879785034520682; JSESSIONID=8B980590640874E014594F09285BC0BD; RAIL_EXPIRATION=1595700663638; RAIL_DEVICEID=VoxZ9fe80vFPGS__zXSTeX7fwdnFONL-yRvJZNXMbcZcLISIKylU9rHh4wTooYtBFjL55KAUTObGgMdAhSWSIajeWd9lEpDt5cYjQ2CV2hr0mIEA0EZUNkOScWdKHyhQrVkVMF1eNDcsAMW4fqcVSk7fVfQe1jxG; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_fromDate=2020-07-22; _jc_save_toDate=2020-07-22; _jc_save_wfdc_flag=dc; _jc_save_toStation=%u5929%u6D25%2CTJP; BIGipServerotn=1072693770.38945.0000; BIGipServerpool_passport=300745226.50215.0000; route=6f50b51faa11b987e576cdb301e545c4'}

    resp=requests.get(url,headers=headers)
    resp.encoding='UTF-8'
    return resp

def parse_json(resp,city):
    json_ticket=resp.json()
    data=json_ticket['data']['result']
    print(data)
    for item in data:
        d=item.split('|')
        print(d[3],city[d[6]],city[d[7]],d[31],d[30],d[13])

def get_city():
    url='https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9151'
    #headers={}
    resp=requests.get(url)
    resp.encoding='UTF-8'
    #编码表中所有中文的范围为：\u4e00-\u9fa5
    stations=re.findall('([\u4e00-\u9fa5]+)\|([A-Z]+)',resp.text)                    
    sta_data=dict(stations)
    sta_d={}
    for item in sta_data: #将值换成键，键换成值
        sta_d[sta_data[item]]=item
    #print(sta_d)
    return sta_d
def start():
    parse_json(send_request(),get_city())

if __name__=='__main__':
    res=send_request()
    print(res.text)
    res1=get_city()
    print(res1)
    start()
