# from hello_python import chai   

# chai("Ginger Tea")
# Data type of python 

# print(repr('Sourabh'))

myset = {1,3,5,6}
myset2 = {3,5,6,8,9}

# result =  myset - myset2

# print(result)

player = {"virat" : "India", "gayle" : "West Indies", "starc":"Australia" , "shakib": "Bangladesh"}
# print(player["virat"])
# abc = player.get("starc")
# print(abc)

# for key, value in player.items():
    # print(key, value)

# del player["shakib"]
# print(player)
player_copy = player.copy()
# print(player_copy)

nation = {
    "india" : {"mh" : "shinde", "kar" : "shetty", "ap": "reddy"},
    "briton" : {"wales" : "thomas", "england": "mathew", "scot" : "miller"},
    "usa" : {"cal" : "pomp", "florida" : "sentis", "nevada": "trupm"} 
}

print(nation.get("usa").get("cal"))

