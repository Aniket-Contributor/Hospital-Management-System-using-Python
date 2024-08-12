import time

def intro():
        
        print(' \t\t\t||||          ||||          ')
        print(' \t\t\t||||          ||||                 ')
        print(' \t\t\t||||          ||||   |||||||||||||||  |||||||||||||   ||||||||||||||    |||||    ||||||||||||||||    |||||||||||||||    ||||                                                            ')
        print(' \t\t\t||||||||||||||||||   ||||       ||||  ||||            |||         ||    |||||          ||||          ||||       ||||    ||||  ')
        print(' \t\t\t||||          ||||   ||||       ||||  ||||||||||||    ||||||||||||||    |||||          ||||          |||||||||||||||    ||||                 ')
        print(' \t\t\t||||          ||||   ||||       ||||          ||||    |||               |||||          ||||          ||||       ||||    ||||                 '                                         )
        print(' \t\t\t||||          ||||   |||||||||||||||  ||||||||||||    |||               |||||          ||||          ||||       ||||    |||||||||||||||           ')
        print ("\n\n\t\t\t\t\t\t\t\tPRESENTED BY : ")
        print("\t\t\t\t\t\t\t\t\t ANIKET SHARMA ")
        print("\t\t\t\t\t\t\t\t\t ELECTRICAL ENGINEERING ")
        print("\t\t\t\t\t\t\t\t\t NATIONAL INSTITUTE OF TECHNOLOGY,JAMSHEDPUR")
       
        print("\n")
        
        print("\n\n==>>>PRESS ENTER TO CONTINUE")
        input()
intro()        
        
while 1==1:
    u=input("ENTER USER ID----")
    p=input("ENTER PASSWORD---")
    p=p.upper()
    if p=="ANIKET":
        print ("Analysing your input."),
        time.sleep(.6)
        print ("."),
        time.sleep(.6)
        print ("."),
        time.sleep(.6)
        print ("."),
        time.sleep(.6)
        print ("."),
        time.sleep(.6)
        print (".")
        print("\n\n\n~~~~~~~~~~~~~~~~~~~~ACCESS GRANTED!!!~~~~~~~~~~~~~~~~~~~\n\n\n")
        
        import time    
        import pickle
        import os
        class Hospital():
            def _init_(self):
                self.sno=0
                self.name=' '
                self.age=0
                self.sex=""
                self.email=" "
                self.fname=" "
                self.address=''
                self.city=''
                self.state=''
                self.height=0
                self.weight=0
                self.doctor=''
                self.med=''
                self.bill=0
                self.paymethod=''
                self.pno=0
                self.bgroup=''
                self.dname=''

            def Input(self):
                self.sno=input("Enter Serial number:")
                self.name=input("Enter Patinet's Name:")
                self.age=input("Enter Patinet's Age:")
                self.sex=input("Enter Patinet's Sex (Male/Female):")
                self.height=input("Enter Patinet's Height:")
                self.weight=input("Enter Patinet's Weight(In Kgs):")
                self.bgroup=input("Enter Patient's Blood Group:")
                self.fname=input("Enter Fathers Name:")
                self.address=input("Enter Address:")
                self.city=input("Enter City:")
                self.state=input("Enter State:")
                self.pno=input("Enter Phone number:")
                self.email=input("Enter E-Mail:")
                self.doctor=input("Enter Doctor's Name:")
                self.dname=input("Enter Disease Name:")
                self.med=input("Enter Prescribed Medicine:")
                self.bill=input("Enter Bill Amount: Rs.")
                self.paymethod=input("Enter Payment Method(Cash/Cheque/Card):")
            def Output(self):
                print ("SERIAL NUMBER:-",self.sno)
                print ("PATIENT'S NAME:-",self.name)
                print ("PATIENT'S AGE:-",self.age)
                print ("PATIENT'S SEX:-",self.sex)
                print ("PATIENT'S HEIGHT:-",self.height)
                print ("PATIENT'S WEIGHT:-",self.weight)
                print ("PATIENT'S BLOOD GROUP:-",self.bgroup)
                print ("FATHERS NAME:-",self.fname)
                print ("ADDRESS:-",self.address)
                print ("CITY:-",self.city)
                print ("STATE:-",self.state)
                print ("CONTACT NUMBER:-",self.pno)
                print ("E-MAIL ADDRESS:-",self.email)
                print ("DISEASE NAME:-",self.dname)
                print ("DOCTOR'S NAME:-",self.doctor)
                print ("PRESCRIBED MEDICINES:-",self.med)
                print ("BILL AMOUNT:-",self.bill)
                print ("PAYMENT METHOD:-",self.paymethod)
        
    #FUNCTION
        import time
        import pickle
        import os
        f=open("Hospital1.DAT","w")
        f.close()
        def WriteHospital():
            fout=open("Hospital1.DAT","ab")
            ob=Hospital()
            print ("Enter Details::\n")
            ob.Input()
            pickle.dump(ob,fout)
            print ("\nRecord Saved................")
            fout.close()
        def ReadHospital():
            fin=open("Hospital1.DAT","rb")
            ob=Hospital()
            try:
                print ("Hospital Details are::\n")
                while True:
                    ob=pickle.load(fin)
                    ob.Output()
                    print
            except EOFError:
                fin.close
        def SearchHospitalSno(n):       
            fin=open("Hospital1.DAT","rb")
            ob=Hospital()
            flag=False
            try:
                print
                print("\nHospital Details Are:--\n")
                while True:
                    ob=pickle.load(fin)
                    if ob.sno==n:
                        ob.Output()
                        flag=True
            except EOFError:    
                if not flag:
                    print ("\n")
                    print ("\n")
                    print ("               ____________________________________________ " )
                    print ("               |  ... RECORD... DOES... NOT... EXIST ...  | ")
                    print ("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
                fin.close()
        def SearchHospitalemail(n):       
            fin=open("Hospital1.DAT","rb")
            ob=Hospital()
            flag=False
            try:
                print("\nHospital Details Are:--\n")
                while True:
                    ob=pickle.load(fin) 
                    if ob.email==n:
                        ob.Output()
                        flag=True
                        break
            except EOFError:
                if not flag:
                    print ("\n")
                    print ("\n")
                    print ("               ____________________________________________ " )
                    print ("               |  ... RECORD... DOES... NOT... EXIST ...  | " )
                    print ("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ " )
                fin.close() 
        def SearchHospitalcontact(n):     
            fin=open("Hospital1.DAT","rb")
            ob=Hospital()
            flag=False
            try:
                print("\nHospital Details Are:--\n")
                while True:
                    ob=pickle.load(fin)
                    if ob.pno==n:
                        ob.Output()
                        flag=True
                    
            except EOFError:
                    if not flag:
                        print ("\n")
                        print ("\n")
                        print ("               ____________________________________________ " )
                        print ("               |  ... RECORD... DOES... NOT... EXIST ...  | " )
                        print ("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ " )
                    fin.close()
        
        def SearchBloodgroup(n):             
            fin=open("Hospital1.DAT","rb")
            ob=Hospital()
            flag=False
            try:
                print("\nHospital Details are:\n")
                while True:
                    ob=pickle.load(fin)
                    if ob.bgroup==n:
                        ob.Output()
                        flag=True
                        
            except EOFError:
                    if not flag:
                        print ("\n")
                        print ("\n")
                        print ("               ____________________________________________ ") 
                        print ("               |  ... RECORD... DOES... NOT... EXIST ...  | ")
                        print ("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
                    fin.close()
        
        def SearchAge(n):                        
            fin=open("Hospital1.DAT","rb")
            ob=Hospital()
            flag=False
            try:
                print("\nHospital Details are:\n")
                while True:
                    ob=pickle.load(fin)
                    if ob.age==n:
                        ob.Output()
                        flag=True
                        
            except EOFError:
                    if not flag:
                        print ("\n")
                        print ("\n")
                        print ("               ____________________________________________ ") 
                        print ("               |  ... RECORD... DOES... NOT... EXIST ...  | ")
                        print ("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
                    fin.close()
                    
        def SearchSex(n):                         
            fin=open("Hospital1.DAT","rb")
            ob=Hospital()
            flag=False
            try:
                print("\nHospital Details are:\n")
                while True:
                    ob=pickle.load(fin)
                    if ob.sex==n:
                        ob.Output()
                        flag=True
                        
            except EOFError:
                    if not flag:
                        print ("\n")
                        print ("\n")
                        print ("               ____________________________________________ ") 
                        print ("               |  ... RECORD... DOES... NOT... EXIST ...  | ")
                        print ("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
                    fin.close()
        
        def SearchDName(n):                        
            fin=open("Hospital1.DAT","rb")
            ob=Hospital()
            flag=False
            try:
                print("\nHospital Details are:\n")
                while True:
                    ob=pickle.load(fin)
                    if ob.dname==n:
                        ob.Output()
                        flag=True
                        
            except EOFError:
                    if not flag:
                        print ("\n")
                        print ("\n")
                        print ("               ____________________________________________ ") 
                        print ("               |  ... RECORD... DOES... NOT... EXIST ...  | ")
                        print ("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
                    fin.close()
        
        def SearchDoctor(n):                         
            fin=open("Hospital1.DAT","rb")
            ob=Hospital()
            flag=False
            try:
                print("\nHospital Details are:\n")
                while True:
                    ob=pickle.load(fin)
                    if ob.doctor==n:
                        ob.Output()
                        flag=True
                        
            except EOFError:
                    if not flag:
                        print ("\n")
                        print ("\n")
                        print ("               ____________________________________________ " )
                        print ("               |  ... RECORD... DOES... NOT... EXIST ...  | " )
                        print ("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ " )
                    fin.close()
    
        def SearchPayment(n):                          
            fin=open("Hospital1.DAT","rb")
            ob=Hospital()
            flag=False
            try:
                print("\nHospital Details are:\n")
                while True:
                    ob=pickle.load(fin)
                    if ob.paymethod==n:
                        ob.Output()
                        flag=True
                        
            except EOFError:
                    if not flag:
                        print ("\n")
                        print ("\n")
                        print ("               ____________________________________________ " )
                        print ("               |  ... RECORD... DOES... NOT... EXIST ...  | " )
                        print ("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ " )
                    fin.close()

        
        def ModiHospital(b):#to modify details
            fin=open("Hospital1.DAT","rb")
            fout = open ("TEMP.DAT","ab")
            ob=Hospital()
            flag = False
            try:
                while True :
                    ob=pickle.load(fin)
                    if ob.sno==b:
                        flag=True
                        n=int(input("ENTER YOUR CHOICE!!!!"))
                        if n==1:
                            a=input("ENTER NEW PATIENT'S NAME::")
                            ob.name=a
                            pickle.dump(ob,fout)
                            print("\nRECORD MODIFIED\n")
                        elif n==2: 
                            a=input("ENTER NEW PATIENT'S AGE:-->")
                            ob.age=a
                            pickle.dump(ob,fout)
                            print("\nRECORD MODIFIED\n")
                        elif n==3:
                            a=input("ENTER NEW PATIENT'S SEX(Male/Female):-->")
                            ob.sex=a
                            pickle.dump(ob,fout)
                            print("\nRECORD MODIFIED\n")
                        elif n==4:
                            a=input("ENTER NEW PATIENT'S HEIGHT:-->")
                            ob.height=a
                            pickle.dump(ob,fout)
                            print("\nRECORD MODIFIED\n")
                        elif n==5:
                            a=input("ENTER NEW PATIENT'S WEIGHT(In Kgs):-->")
                            ob.weight=a
                            pickle.dump(ob,fout)
                            print("\nRECORD MODIFIED\n")
                        elif n==6:
                            a=input("ENTER NEW PATIENT'S BLOOD GROUP:-->")
                            ob.bgroup=a
                            pickle.dump(ob,fout)
                            print("\nRECORD MODIFIED\n")
                        elif n==7:
                            a=input("ENTER NEW FATHERS NAME:-->")
                            ob.fname=a
                            pickle.dump(ob,fout)
                            print("\nRECORD MODIFIED\n")
                        elif n==8:
                            a=input("ENTER NEW ADDRESS:-->")
                            ob.address=a
                            pickle.dump(ob,fout)
                        elif n==9:
                            a=input("ENTER NEW CITY:-->")
                            ob.city=a
                            pickle.dump(ob,fout)
                            print("\nRECORD MODIFIED\n")
                        elif n==10:
                            a=input("ENTER NEW STATE:-->")
                            ob.state=a
                            pickle.dump(ob,fout)
                            print("\nRECORD MODIFIED\n")
                        elif n==11:
                            a=input("ENTER NEW CONTACT NUMBER:-->")
                            ob.pno=a
                            pickle.dump(ob,fout)
                            print("\nRECORD MODIFIED\n")
                        elif n==12:
                            a=input("ENTER NEW E-MAIL ADDRESS:-->")
                            ob.email=a
                            pickle.dump(ob,fout)
                            print("\nRECORD MODIFIED\n")
                        elif n==13:
                            a=input("ENTER NEW DISEASE NAME:-->")
                            ob.dname=a
                            pickle.dump(ob,fout)
                            print("\nRECORD MODIFIED\n")
                        elif n==14:
                            a=input("ENTER NEW DOCTOR'S NAME:-->")
                            ob.doctor=a
                            pickle.dump(ob,fout)
                            print("\nRECORD MODIFIED\n")
                        elif n==15:
                            a=input("ENTER NEW PRESCRIBED MEDICINE:-->")
                            ob.med=a
                            pickle.dump(ob,fout)
                            print("\nRECORD MODIFIED\n")
                        elif n==16:
                            a=input("ENTER NEW BILL AMOUNT:--> Rs.")
                            ob.bill=a
                            pickle.dump(ob,fout)
                            print("\nRECORD MODIFIED\n")
                        elif n==17:
                            a=input("ENTER NEW PAYMENT METHOD(Cash\Cheque\Card):-->")
                            ob.paymethod=a
                            pickle.dump(ob,fout)
                            print("\nRECORD MODIFIED\n")
                    
                        elif n==18:
                            print ("__________________ENTER THE NEW DETAILS__________________")
                            ob.Input() 
                            pickle.dump(ob,fout)
                            print("\nRECORD MODIFIED\n")
                        else:
                            print("Enter Valid Choice!")
                    else:
                        pickle.dump(ob,fout)
            
            except EOFError:
                if not flag:
                    print ("\n")
                    print ("\n")
                    print ("               ____________________________________________ " )
                    print ("               |  ... RECORD... DOES... NOT... EXIST ...  | " )
                    print ("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ " )
                fin.close()
        
            fout.close()
            os.remove("Hospital1.DAT")
            os.rename("TEMP.DAT","Hospital1.DAT")
        
        def DelHospital(n):
            fin=open("Hospital1.DAT","rb")
            fout=open("TEMP.DAT","wb")
            ob=Hospital()
            Flag=False
            try:
                while True:
                    ob=pickle.load(fin)
                    if ob.sno==n:
                        Flag=True
                        print("Rcord Deleted")
                    else:
                        
                        pickle.dump(ob,fout)
            except EOFError:
                if not Flag:
                    print("Record Does Not Exit")
                fin.close()
                fout.close()
                os.remove("Hospital1.DAT")
                os.rename("TEMP.DAT","Hospital1.DAT")
        

        while True:
            print("\n")
            print("\t..........______________________________Hospital Management System_____________________________________.............. \n")
            #print("\n")
            print("1.WRITE RECORD\n2.SHOW ALL RECORDS\n3.SEARCH DETAILS")
            print("4.MODIFY RECORD\n5.DELETE RECORD\n6.EXIT\n")
            ch=int(input("ENTER YOUR CHOICE---"))
            print("\n")
            if ch==1:
                WriteHospital()
            elif ch==2:
                fin=open("Hospital1.DAT","rb")
                print("SERIAL NUMBER","\t" ,"PATIENT'S NAME","\t","PATIENT'S SEX","\t","FATHERS NAME","\t\t","BILL AMOUNT")
                try:
                      while True:
                         s=pickle.load(fin)
                         print("\n",s.sno,"\t\t",s.name,"\t",s.sex,"\t\t",s.fname,"\t",s.bill)
                except EOFError:
                        pass
                fin.close()
                         
            elif ch==3:
                print ("\t____________________________________________________________ " )
                print ("\t|------------SEARCH OPTIONS ARE AS FOLLOWS.................| " )
                print ("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" )
                print ("\n")
                print("1.SEARCH BY SERIAL NUMBER\n2.SEARCH BY CONTACT NUMBER\n3.SEARCH BY BLOOD GROUP\n4.SEARCH BY AGE\n5.SEARCH BY SEX")
                print("6.SEARCH BY DISEASE NAME\n7.SEARCH BY DOCTORS NAME\n8.SEARCH BY PAYMENT METHOD\n9.SEARCH BY E-MAIL\n10.MAIN MENU\n")
                i=int(input("ENTER YOUR CHOICE : "))
                if i==1:
                    n=input("PLEASE ENTER SERIAL NUMBER TO SEARCH:--")
                    SearchHospitalSno(n)
                elif i==2:
                    n=input("PLEASE ENTER CONTACT NUMBER TO SEARCH:--")
                    SearchHospitalcontact(n)
                elif i==3:
                    n=input("PLEASE ENTER BLOOD GROUP TO SEARCH:--")
                    SearchBloodgroup(n)
                elif i==4:
                    n=input("PLEASE ENTER AGE TO SEARCH:--")
                    SearchAge(n)
                elif i==5:
                    n=input("PLEASE ENTER SEX TO SEARCH:--")
                    SearchSex(n)
                elif i==6:
                    n=input("PLEASE ENTER DISEASE NAME TO SEARCH:--")
                    SearchDName(n)
                elif i==7:
                    n=input("PLEASE ENTER DOCTORS NAME TO SEARCH:--")
                    SearchDoctor(n)
                elif i==8:
                    n=input("PLEASE ENTER PAYMENT METHOD TO SEARCH:--")
                    SearchPayment(n)
                elif i==9:
                    n=input("PLEASE ENTER E-MAIL ADDRESS TO SEARCH:--")
                    SearchHospitalemail(n)
                elif i==10:
                    continue
            elif ch==4:
                m=input("ENTER SERIAL NUMBER TO MODIFY:--")
                print ("\n")
                print ("____________________________________________ " )
                print ("|  ......... ENTER YOUR CHOICE ..........  | " )
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ " )
                print ("\n")
                print ("WHAT DO YOU WANT TO MODIFY:")
                print 
                print ("1.PATIENT'S NAME")
                print ("2.PATIENT'S AGE")
                print ("3.PATIENT'S SEX")
                print ("4.PATIENT'S HEIGHT")
                print ("5.PATIENT'S WEIGHT")
                print ("6.PATIENT'S BLOOD GROUP:-")
                print ("7.FATHERS NAME:-")
                print ("8.ADDRESS:-")
                print ("9.CITY:-")
                print ("10.STATE:-")
                print ("11.CONTACT NUMBER:-")
                print ("12.E-MAIL ADDRESS:-")
                print ("13.DISEASE NAME:-")
                print ("14.DOCTOR'S NAME:-")
                print ("15.PRESCRIBED MEDICINES:-")
                print ("16.BILL AMOUNT:-")
                print ("17.PAYMENT METHOD:-")
                print ("18.ALL")
                ModiHospital(m)
            elif ch==5:
                n=input("ENTER SERIAL NUMBER TO DELETE:-")
                DelHospital(n)
            elif ch==6:
                print ("\n")
                print ("EXITING"),
                time.sleep(.8)
                print ("."),
                time.sleep(.8)
                print ("."),
                time.sleep(.8)
                print ("."),
                time.sleep(.8)
                print ("."),
                time.sleep(.8)
                print (".")
                break
            else:
                print ("Analysing your input."),
                time.sleep(.6)
                print ("."),
                time.sleep(.6)
                print ("."),
                time.sleep(.6)
                print ("."),
                time.sleep(.6)
                print ("."),
                time.sleep(.6)
                print (".")
                print("\n\n\n~~~~~~~~~~~~~~~~~~~~WRONG CHOICE!!!~~~~~~~~~~~~~~~~~~~\n\n\n")
            
    else:
        print ("Analysing your input."),
        time.sleep(.6)
        print ("."),
        time.sleep(.6)
        print ("."),
        time.sleep(.6)
        print ("."),
        time.sleep(.6)
        print ("."),
        time.sleep(.6)
        print (".")
        print("\n\n\n~~~~~~~~~~~~~~~~~~~~ACCESS DENIED!!!~~~~~~~~~~~~~~~~~~~\n\n\n")
        
    z=input("ENTER Y to re-enter or N to exit")
    z=z.upper()
    if z=="Y":
        continue
    else:
        break
        



        
        


    
