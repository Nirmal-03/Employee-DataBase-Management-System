from manage import Manager
class Main:
    def __init__(self):
        self.manage=Manager()
    def start(self):
        opt={1:"showall",2:"search and update",3:"remove",4:"show level",5:"summary",6:"exit"}
        while True:
            print("Employee DataBase Management")
            for i,j in opt.items():
                print(f"{i}: {j}")
            ch=int(input("select the choose: "))
            if ch==1:
                self.manage.showall()
            elif ch==2:
                self.manage.searchandupdate()
            elif ch==3:
                self.manage.remove()
            elif ch==4:
                self.manage.showtree()
            elif ch==5:
                self.manage.summary()
s=Main()
s.start()