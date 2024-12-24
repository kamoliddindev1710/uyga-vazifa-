def cash_game(l:list,t:list):
        a1=3
        a2=3
        for x in range(len(l)):
            if l[x]==t[x] and l[x]=="share":
                a1=a1+2
                a2=a2+2
            elif l[x]==t[x] and l[x]=="steal":
                a1=a1+0
                a2=a2+0
            elif l[x]=="steal" and t[x]=="share":
                a1=a1+3
                a2=a2-1
            elif l[x]=="share" and t[x]=="steal":
                a1=a1-1
                a2=a2+3
        print([a1,a2])

try:
    text=input("first opponent enter the words ")
    text2=input("Second opponent enter the words: ")
except Exception as ex:
     print(ex)
fir_text=text.split(" ")
sec_text=text2.split(" ")
cash_game(fir_text,sec_text)