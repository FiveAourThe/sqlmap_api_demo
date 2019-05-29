#!/usr/bin/python
# -*- coding:utf-8 -*-
# wirter:En_dust
from Service import Client
import time
from threading import Thread

def main():
    '''实例化Client对象时需要传递sqlmap api 服务端的ip、port、admin_token和HTTP包的绝对路径'''
    print("————————————————Start Working！—————————————————")
    target = input("url:")
    task1 = Thread(target=set_start_get_result,args=(target,))
    task1.start()



def time_deal(mytime):
     first_deal_time = time.localtime(mytime)
     second_deal_time = time.strftime("%Y-%m-%d %H:%M:%S", first_deal_time)
     return  second_deal_time


def set_start_get_result(url):
    #/home/cheng/Desktop/sqldump/1.txt
    current_taskid =  my_scan.create_new_task()
    print("taskid: " + str(current_taskid))
    my_scan.set_task_options(url=url)
    print("扫描id:" + str(my_scan.start_target_scan(url=url)))
    print("扫描开始时间：" + str(time_deal(my_scan.scan_start_time)))
    while True:
        if my_scan.get_scan_status() == True:
            print(my_scan.get_result())
            print("当前数据库:" + str(my_scan.get_result()[-1]['value']))
            print("当前数据库用户名:" + str(my_scan.get_result()[-2]['value']))
            print("数据库版本:" + str(my_scan.get_result()[-3]['value']))
            print("扫描结束时间：" + str(time_deal(my_scan.scan_end_time)))
            print("扫描日志：\n" + str(my_scan.get_scan_log()))
            break




if __name__ == '__main__':
    my_scan = Client("127.0.0.1", "8775", "c88927c30abb1ef6ea78cb81ac7ac6b0")
    main()
