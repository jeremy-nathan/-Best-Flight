# # path = [(30.343769, 77.999559),
# #         (30.307977, 78.048457),
# #         (35.343769, 90.999559)]
# # print(path[0:2])
# cities=['Kuala Lumpur','Shanghai','New York','Singapore','New Delhi','Manila','Washington DC','Tokyo','Paris']
#
#
# a={}
#
# def calc(start):
#     for i in range(len(cities)-1):
#         a[cities[start]][cities[i]]=i*10
#
# for i in range(len(cities)):
#     a[cities[i]]={}
#     calc(i)
#     # calc(i)
#     # a[cities[i]][cities[i+1]]=i*10
#
#
# # print(a[cities[0]][cities[2]])
#
# # for i in range(len(cities)):
# #     a[cities[i]]={}
# #     a[cities[i]]['lat']=789
# #     a[cities[i]]['lon']=789
# #
# #
# print(a['Kuala Lumpur'])
# del a["Kuala Lumpur"]["New York"]
# print(a['Kuala Lumpur'])
import itertools
