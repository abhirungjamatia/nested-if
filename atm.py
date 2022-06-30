atm=input("enter card")
if atm=='card inserted':
    language=input("enter language")
    if language=='english' or language=='ENGLISH':
        pin=int(input("enter pin"))
        if pin>999 and pin<10000:
         key=input("enter ok")
        if key=='ok' or key=='OK':
            transaction=input("enter transaction type")
            if transaction=='withdrawal' or transaction=='WITHDRAWAL':
                account=input("enter account type")
                if account=='saving' or account=='SAVING' or account=='current' or account=='CURRENT' or account=='joint' or account=='JOINT':
                    amt=int(input("enter amount"))
                    if amt>=500 and amt<=20000 and amt%500==0:
                        a=amt//2000
                        m=amt%2000
                        o=m//500
                        u=m%500
                        print("notes of2000=",a,"notes of 500=",o)
                        receipt=input("enter yes or no")
                        if receipt=='yes' or receipt=='YES':
                            print("show the receipt")
                        else:
                           print("amount is not sufficient")
                    else:
                        print("limit exceeded")
                else:
                    print("error")
            elif transaction=='balance enquiry' or transaction=='BALANCE ENQUIRY':
             account=input("enter account type")
            if account=='saving' or account=='SAVING' or account=='current' or account=='CURRENT' or account=='joint' or account=='JOINT':
                pin=int(input("enter pin"))
                key=input("enter ok")
            if key=='ok' or key=='OK':
               print("amount")

