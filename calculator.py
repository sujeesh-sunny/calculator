class calculator:
    def __init__(self,first_num,second_num,select_opreator):
        self.first_num = first_num
	self.second_num = second_num
	self.select_opreator = select_opreator

    def numinput(self):
	self.first_num = int(input("enter first number: "))
	self.second_num = int(input("enter second number: "))
	self.select_opreator = int(input("select + for add - for sub * for multi / for div: "))

    def calculation(self):
	if self.select_opreator == + :
	    print (self.first_num + self.second_num)
	elif self.select_opreator == - :
            print (self.first_num - self.second_num)
	elif self.select_opreator == * :
            print (self.first_num * self.second_num)
	elif self.select_opreator == / :
            print (self.first_num / self.second_num)

cal1 = calculator("","","")
cal1 = numinput()
cal1 = calculation()


