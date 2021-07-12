# input
list_of_dictionaries = [
     {
        "name": "toyota",
        "model": "corolla",
        "price": "3300"
    },

     {
        "name": "honda",
        "model": "accord",
        "price": "2409"
    },

     {
        "name": "nissan",
        "model": "pathfinder",
        "price": "1800"
    },

     {
        "name": "mercedes",
        "model": "gWagon",
        "price": "4000"
    }
]
  
#print(cars[0])
sought_value = input ("Please enter name and model:")
needed_value = sought_value.split(" ")
used_value = []

for ele in needed_value:
      if ele.strip():
        used_value.append(ele)

# name, model = needed_value

name = used_value[0] 
model = used_value[1]

def car_price(name, model):
    for dictionary in list_of_dictionaries:
        if dictionary["name"].lower() == name and dictionary["model"].lower() == model:
            print("The price of the car is {}.".format(dictionary["price"]))
            break
    else:    
        print("This car does not exist in the inventory")         
         
        
              

              
car_price(name, model)


            
            
    
   
            
            
            
    