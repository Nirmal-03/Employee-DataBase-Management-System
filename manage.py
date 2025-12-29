from employeedetails import employee
class Manager:
    def __init__(self):
        self.employee=employee
        self.filtered=[]
    def showall(self):
        print(f"{'ID':<5}{'Name':<10}{'Age':<5}{'Department':<12}{'Designation':<12}{'Reporting To':<12}")
        for emp in self.employee:
            print(f"{emp.id:<5}{emp.name:<10}{emp.age:<5}{emp.department:<12}{emp.designation:<12}{str(emp.reportingto):<12}")
    def printdb(self):
        print(f"{'ID':<5}{'Name':<10}{'Age':<5}{'Department':<12}{'Designation':<12}{'Reporting To':<12}")
        for emp in self.filtered:
            print(f"{emp.id:<5}{emp.name:<10}{emp.age:<5}{emp.department:<12}{emp.designation:<12}{str(emp.reportingto):<12}")
    def search(self, s, value=None):
        ch = input("give input value: ").strip()
        searchlist = self.filtered if self.filtered else self.employee
    
        if s in ("<", ">", "==", "!="):
            num = int(ch)
            ops = {
                "<":  lambda a, b: a < b,
                ">":  lambda a, b: a > b,
                "==": lambda a, b: a == b,
                "!=": lambda a, b: a != b
            }
            self.filtered = [
                emp for emp in searchlist
                if ops[s](emp.age, num)
            ]
    
        elif s == "between":
            v1, v2 = map(int, ch.split())
            self.filtered = [
                emp for emp in searchlist
                if v1 < emp.age < v2
            ]
    
        else:
            ch = ch.lower()
            conditions = {
                "equal":        lambda v: v == ch,
                "not equal":    lambda v: v != ch,
                "start with":   lambda v: v.startswith(ch),
                "end with":     lambda v: v.endswith(ch),
                "contains":     lambda v: ch in v,
                "not contains": lambda v: ch not in v
            }
    
            self.filtered = [
                emp for emp in searchlist
                if (val := getattr(emp, value)) and
                   conditions[s](val.lower())
            ]
    
        self.printdb()
        self.addcriteria()

    def change(self,emp_attr,value):
        for i in self.filtered:
            for j in self.employee:
                if i.id == j.id:
                    setattr(j,emp_attr,value)
        self.filtered=[]
    def changeover(self,d,ch,user_ch):
        for i in d:
            for j in self.employee:
                if ch==1:
                    if getattr(j,"reportingto") is not None:
                        v=getattr(j,"reportingto")  
                        if v.lower() in d:
                            setattr(j,"reportingto",user_ch)
                elif ch==5: 
                    if getattr(j,"name") is not None:
                        v=getattr(j,"name") 
                        if v.lower() in d:
                            setattr(j,"name",user_ch)
    def update(self):
        opt={1:"name",2:"age",3:"department",4:"designation",5:"reportingto"}
        for i,j in opt.items():
            print(f"{i}: {j}")
        ch=int(input("select the choice to update: "))
        if ch==2:
            user_ch=int(input("enter the value: "))
            for i in self.filtered:
                setattr(i,opt[ch],user_ch)
            self.printdb()
            self.change(opt[ch],user_ch)
        else:
            d=[]
            user_ch=input("enter the value: ")
            for i in self.filtered:
                if ch==1:
                    if getattr(i,"name") is not None:
                        d.append(getattr(i,"name").lower())
                else:
                    if getattr(i,"reportingto") is not None:
                        d.append(getattr(i,"reportingto").lower())
                setattr(i,opt[ch],user_ch)
            self.printdb()
            self.change(opt[ch],user_ch)
            if ch==1 or ch==5:
                self.changeover(d,ch,user_ch)
        return

    def addcriteria(self):
        opt={1:"add criteria",2:"update",3:"exit"}
        for i,j in opt.items():
            print(f"{i}: {j}")
        ch=int(input("select the choose: "))
        if ch==1:
            self.searchandupdate()
        elif ch==2:
            self.update()
        else:
            exit()
    def agesearch(self):
        opt={1:"<",2:">",3:"==",4:"!=",5:"between"}
        for i,j in opt.items():
            print(f"{i}: {j}")
        ch=int(input("select the criteria: "))
        self.search(opt[ch])
    def stringsearch(self,value):
        opt={1:"equal",2:"not equal",3:"start with",4:"end with",5:"contains",6:"not contains"}
        for i,j in opt.items():
            print(f"{i}: {j}")
        ch=int(input("select the criteria: "))
        self.search(opt[ch],value)
    def searchandupdate(self):
        opt={1:"name",2:"age",3:"department",4:"designation",5:"reportingto"}
        for i,j in opt.items():
            print(f"{i}: {j}")
        ch=int(input("select option to search: "))
        if ch==2:
            self.agesearch()
        else :
            self.stringsearch(opt[ch])
    def remove(self):
        emp_id=int(input("enter emp id: "))
        emp_name=input("enter the emp name")
        ind=0
        reporting_name=emp_name.lower()
        change_name=""
        for i in self.employee:
            if i.id==emp_id and i.name.lower()==emp_name.lower():
                change_name=i.reportingto
                self.employee.pop(ind)
                break
            ind+=1
        for i in self.employee:
            if i.reportingto is not None and i.reportingto.lower()==reporting_name:
                setattr(i,"reportingto",change_name)
        return
    def showtree(self):
        user_ch=input("enter emp name: ").lower()
        print(user_ch,end="->")
        cur=user_ch.lower()
        while True:
            v=None
            for i in self.employee:
                if i.name.lower()==cur:
                    v=i.reportingto
                    break
            if not v:
                break
            print(v,end="->")
            cur=v.lower()
        print("None")
    def summary(self):
        while True:
            opt={1:"total no of emp",2:"no of emp in departmeny",3:"no of emp under manager",4:"main menu"}
            for i,j in opt.items():
                print(f"{i}: {j}")
            ch=int(input("select the choice: "))
            if ch==1:
                print(len(self.employee))
            elif ch==2:
                d=set()
                for i in self.employee:
                    if i.department not in d:
                        d.add(i.department)
                l=list(d)
                for i in l:
                    c=0
                    for j in self.employee:
                        if i==j.department:
                            c+=1
                    print(f"{i}->{c}")
            elif ch==3:
                d=set()
                for i in self.employee:
                    if i.reportingto is not None and i.reportingto not in d:
                        d.add(i.reportingto)
                l=list(d)
                for i in l:
                    c=0
                    for j in self.employee:
                        if i==j.reportingto:
                            c+=1
                    print(f"{i}->{c}")
            elif ch==4:
                return



        


        
