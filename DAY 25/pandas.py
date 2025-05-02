# # to input the value in the 

# # file = open("D:/100 Days Of Python/DAY 25/weather_data.csv")
# # contents=file.read()
# # print(contents)

# # with open("D:/100 Days Of Python/DAY 25/weather_data.csv") as file:
# #     data =file.readlines()
# #     print(data)
# # with open("D:/100 Days Of Python/DAY 25/weather_data.csv") as file:
# #     data =file.readline(1000)
# #     print(data)

# # csv library 
# # D:/100 Days Of Python/DAY 25/
# # import csv

# # with open("D:/100 Days Of Python/DAY 25/weather_data.csv") as data_file:
# #     data= csv.reader(data_file)
# #     temprature =[]
# #     for row in data:
# #         if row[1]!="temp":
# #             temprature.append(int(row[1]))
# #     print(temprature)
        

# import pandas as pd

# # data = pd.read_csv("D:/100 Days Of Python/DAY 25/weather_data.csv")
# # print(data)
# # print(data["temp"])
# # temp_data=data["temp"].to_list()
# # temprature = pd.Series(temp_data)
# # print(temprature)
# # print(temprature.max())
# # print(temprature.min())
# # print(temprature.mean())
# # print(temprature.mode())
# # print(temprature.median())
# # print(data.temp)
# # print(data[data.day=="Monday"])
# # print(data[data.temp==data.temp.max()])
# # rain=(data[data.condition=="Rain"])
# # print(rain.temp)
# # rain_temp= rain.temp[2]
# # print(rain_temp*9/5+32)


# data_dict ={
#     "students" :["Ajay","Riva","James"],
#     "marks":[40,23,35]
# }
# data = pd.DataFrame(data_dict)
# data.to_csv("DAY 25/new_data.csv")


import pandas as pd 
data = pd.read_csv("D:/100 Days Of Python/DAY 25/squirrel_data.csv")
grey_squirrels=len(data[data["Primary Fur Color"]=="Gray"])
print(grey_squirrels)
red_squirrels=len(data[data["Primary Fur Color"]=="Cinnamon"])
print(red_squirrels)
black_squirrels=len(data[data["Primary Fur Color"]=="Black"])
print(black_squirrels)

squirrel_df = pd.DataFrame({"Color":["Gray","Cinnamon","Black"],
               "Count": [grey_squirrels,red_squirrels,black_squirrels]}
               )
squirrel_df.to_csv("D:/100 Days Of Python/DAY 25/Squirrel_count.csv")