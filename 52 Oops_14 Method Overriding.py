#==========================================================================================================
                                        # METHOD OVERRIDING
#==========================================================================================================
''''
    Method Overriding ----> (supported) ---> same method , same parameters and different classes
'''
class ITVedant():
    def Faculty (self):
        print ("Main Faculty ")
    def Placement (self):
        print("Main Placement ")

class ITV_E_Clas(ITVedant):
    def Faculty (self):
        print ("Main E_Faculty ")
    def Placement (self):
        print("Main E_Placement ")

class ITV_Thane(ITVedant):
    def Faculty (self):
        print ("Main Thane Faculty ")
    def Placement (self):
        print("Main Thane Placement ")

i = ITVedant()
ie = ITV_E_Clas()
it = ITV_Thane()

for x in (i,ie,it):
    x.Placement()
    x.Faculty()
