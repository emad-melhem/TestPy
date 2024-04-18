class Hand:
    _id =0
    def __init__(self, id):
        self._id=id

    def handName(self): # Return the name of hand id
        name=""
        if self._id == 0:
            name = "rock"
        elif self._id == 1:
            name = "paper"
        elif self._id == 2:
            name = "scissors"
        return name
        
    def isPowerfullThan(self, hand): # Detect if user select hand that is power than computer 0:Draw; 1:wins ; -1:lost
        quality = 0
        if self._id==0:
            if hand ==1:
                quality =-1
            elif hand == 2:
                quality =1
        elif self._id==1:
            if hand ==0:
                quality =1
            elif hand == 2:
                quality =-1
        elif self._id==2:
            if hand ==0:
                quality =-1
            elif hand == 1:
                quality =1
        return quality