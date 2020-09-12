class Cars:
    'This method speaks of different cars'

    def __init__(self,manufacturer,model,make,transmission,color):
        self.manufacturer = manufacturer
        self.model = model
        self.make = make
        self.transmission = transmission
        self.color = color

    def accelerate(self):
        print(self.manufacturer+" " +self.model+" is moving")
    
    
    def stop(self):
        print(self.manufacturer+" " +self.model+ " has stopped")

c1 = Cars("Maruti","Celerio",2015,"Manual","Silver")
c2 = Cars("Honda","City",2018,"Manual","Black")
c3 = Cars("Maruti","Creta",2017,"Automatic","white")

c3.accelerate()
c3.stop()
