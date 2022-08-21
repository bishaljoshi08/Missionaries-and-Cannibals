class Missinaries_cannibals:
    def __init__(self, right_missinaries, right_cannibals, is_boat_left, status='valid') -> None:
        self.left_missinaries = 3 - right_missinaries
        self.left_cannibals = 3 - right_cannibals
        self.right_missinaries = right_missinaries
        self.right_cannibals = right_cannibals
        self.is_boat_left = is_boat_left
        self.status = status
        self.choices = self.generate_choices()

    def __str__(self) -> str:
        return f"{self.right_missinaries}, {self.right_cannibals}, {1 if self.is_boat_left else 0}"


    def __eq__(self,com) -> bool:
        return self.right_cannibals == com.right_cannibals and self.right_missinaries == com.right_missinaries \
            and self.is_boat_left == com.is_boat_left
          
    
    def move_right_2_left(self,x,y,li):
    # x = missinaries and y = cannibals
        if (self.left_cannibals + y > self.left_missinaries+x and self.left_missinaries+x != 0) or \
            (self.right_cannibals-y > self.right_missinaries-x and self.right_missinaries-x != 0):
            return Missinaries_cannibals(self.right_missinaries-x, self.right_cannibals-y, True, 'dead')
        elif Missinaries_cannibals(self.right_missinaries-x, self.right_cannibals-y, True) in li:
            return Missinaries_cannibals(self.right_missinaries-x, self.right_cannibals-y, True, 'already')
        elif  Missinaries_cannibals(self.right_missinaries-x, self.right_cannibals-y, True).success():
            return Missinaries_cannibals(self.right_missinaries-x, self.right_cannibals-y, True, 'success')
        else:
            return Missinaries_cannibals(self.right_missinaries-x, self.right_cannibals-y, True, 'valid')

    def success(self):
        return self.left_missinaries == 3 and self.left_cannibals ==3 and self.is_boat_left == True

    def move_left_2_right(self, x, y, li):
    # x = missinaries and y = cannibals
        if (self.left_cannibals-y > self.left_missinaries-x and self.left_missinaries-x != 0) or \
            (self.right_cannibals+y > self.right_missinaries+x and self.right_missinaries+x != 0):
            return Missinaries_cannibals( self.right_missinaries+x, self.right_cannibals+y, False, 'dead')
        elif Missinaries_cannibals( self.right_missinaries+x, self.right_cannibals+y, False) in li:
            return Missinaries_cannibals( self.right_missinaries+x, self.right_cannibals+y, False, 'already')
        elif Missinaries_cannibals( self.right_missinaries+x, self.right_cannibals+y, False).success():
            return Missinaries_cannibals( self.right_missinaries+x, self.right_cannibals+y, False, 'success')
        else:
            return Missinaries_cannibals( self.right_missinaries+x, self.right_cannibals+y, False, 'valid')

    def generate_choices(self):
        choices = []
        if self.is_boat_left == True:
            m = self.left_missinaries
            c = self.left_cannibals
        else:
            m = self.right_missinaries
            c = self.right_cannibals
        for i in range(3 if (m == 3) else m+1):
            for j in range(3 if (c == 3) else c+1):
                if i+j > 0 and i+j < 3:
                    choices.append((i,j))
        return choices