# import requests
# from datetime import datetime
#
# time_start = datetime.now()
# THE_url='https://www.binaryjazz.us/wp-json/genrenator/v1/genre/'
# res = []
#
# for i in range(10):
#     response = requests.get(THE_url)
#     res.append(response.json())
# time_end = datetime.now()
# time_res = time_end - time_start
# print(res)
# print(time_res)

# Second variant
from threading import Thread
from datetime import datetime
import requests

THE_url = 'https://www.binaryjazz.us/wp-json/genrenator/v1/genre/'
res = []


def func(url):
    response = requests.get(THE_url)
    page_response = response.json()
    res.append(page_response)

thr_first = Thread(target=func, args=(THE_url,))
thr_second = Thread(target=func, args=(THE_url,))
thr_third = Thread(target=func, args=(THE_url,))

time_start = datetime.now()
thr_first.start()
thr_second.start()
thr_third.start()

thr_first.join()
thr_second.join()
thr_third.join()
time_end = datetime.now()
time_res = time_end - time_start
print(res)
print(time_res)