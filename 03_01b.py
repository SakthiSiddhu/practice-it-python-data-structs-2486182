from collections import namedtuple
def main():
    #add code here
    #create a driver with a name, car type, and car capacity
    #an example you can use to practice: "Iris", "Toyota Prius", 7
    #check if they can take a certain order, given their car's capacity.

    Driver = namedtuple('Driver',['name','type','cap'])
    d1 = Driver(name='A', type='Car', cap=5)
    d2 = Driver(name='B', type='Bike', cap=2)
    d3 = Driver(name='C', type='Scooter', cap=1)
    d4 = Driver(name='D', type='Motorcycle', cap=7)
    d5 = Driver(name='E', type='Van', cap=9)
    l=[]
   
    l.extend([d1,d2,d3,d4,d5])
    
    x = int(input('enter total capacity: ' ))

    for i in l:
        if i.cap>=x:
            print(i.name,' can hold ')
        else:
            print(i.name,' cannot hold')
    return

if __name__ == "__main__":
    main()