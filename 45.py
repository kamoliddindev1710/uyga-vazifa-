def cash_game(l:list,t:list):
        a1=3
        a2=3
        for x in range(len(l)):
            if l[x]==t[x] and l[x]=="share" and (a1>0 and a2>0):
                a1=a1+2
                a2=a2+2
            elif l[x]==t[x] and l[x]=="steal" and (a1>0 and a2>0):
                a1=a1+0
                a2=a2+0
            elif l[x]=="steal" and t[x]=="share" and (a1>0 and a2>0):
                a1=a1+3
                a2=a2-1
            elif l[x]=="share" and t[x]=="steal" and (a1>0 and a2>0):
                a1=a1-1
                a2=a2+3
        print([a1,a2])

try:
    text1=input("Enter your choices <> [share] or [steal]: ")
    text2=input("Enter your choices <> [share] or [steal]: ")
except Exception as ex:
     print(ex)
fir_op=text1.split(" ")
sec_op=text2.split(" ")
cash_game(fir_op,sec_op)