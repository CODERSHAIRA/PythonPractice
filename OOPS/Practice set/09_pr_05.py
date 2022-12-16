class Train:
    def __init__(slf,name,fare,seats):
        slf.name=name
        slf.fare=fare
        slf.seats=seats

            
    def getStatus(slf):
        print(f"Name of the train is {slf.name}")  
        print(f"Number of seats are {slf.seats}")  
    
    def fareInfo(slf):
        print(f"Fare of {slf.name} train is {slf.fare}")
       
    def bookTicket(slf):
        if(slf.seats>0):
            print(f"Your tickets has been booked! Your seat number is {slf.seats}")
            slf.seats=slf.seats-1
        else:
            print("Sorry this train is full! Kindly try in tatkal")
    
    def cancelTicket(slf,seatNo):
        pass
intercity= Train("Intercity Express: 14815",100,287)
intercity.getStatus()
intercity.fareInfo()
for i in range(288):
 intercity.bookTicket()
