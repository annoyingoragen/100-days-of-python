import pandas

squirrel_Data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_color=squirrel_Data['Primary Fur Color']
fur_data=(fur_color).value_counts()
fur_data_dict=fur_data.to_dict()
furcolors=[]
numberofsquirres=[]
for key in fur_data_dict:
    furcolors.append(key)
    numberofsquirres.append(fur_data_dict[key])

fur_data_dict_2d={
    "Fur Color": furcolors,
    "Count":numberofsquirres
}

print(fur_data_dict_2d)

DF=pandas.DataFrame(fur_data_dict_2d)
DF.to_csv("fur_colors.csv")