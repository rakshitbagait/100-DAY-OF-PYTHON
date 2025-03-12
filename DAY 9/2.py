# nested dictionaries

capitals ={
    "France" : "Paris",
    "Germany": "Berlin"
}
travel_log ={
    "France": ["Paris","Lille","Djon"],
    "Germany" :["Stuttgart","Berlin"]

}

print(travel_log["France"][1])

nested_list =[1,2,3,[23,45]]

print(nested_list[3][1])

travel_log2 = {
    "france":{
        "cities visited":["Paris","Lile","Dijon"],
        "total visits":12
    },
        "france":{
        "cities visited":["Paris","Lile","Dijon"],
        "total visits":12
    }

}
print(travel_log["France"])

print(travel_log["Germany"])