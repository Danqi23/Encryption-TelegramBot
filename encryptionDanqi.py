from random import randrange as rand
def convert(type,text):
    bin=""
    out=""
    if type==1:
        text = int(text)
        
        while text > 0:
            bin = str(text % 2) + bin
            text = text // 2
        
        for i in range(0,len(bin)-1):
            if bin[i]=="1":
                out =out + str(rand(5,9,1))
            if bin[i]=='0':
                out =out + str(rand(0,4,1))
    elif type==2:
        text0=""
        bin0=""
        for a in range(0,len(text)):
            num=ord(text[a])
            while num > 0:
                bin0 = str(num % 2) + bin0
                num = num // 2
            text0=text0+str(bin0)+chr(rand(97,122,1))
            bin0=""
        for i in range(0,len(text0)-1):
            if text0[i]=="1":
                out =out + str(rand(5,9,1))
            elif text0[i]=='0':
                out =out + str(rand(0,4,1))
            else:
                out=out+text0[i]
    elif type==3:
        print(323)
    else: print('error(errortype="Error-Type")')
    return(out)
def unconvert(type,text):
    bin=""
    out=""
    if type==1:
        for i in range(0,len(text)):
            if int(text[i])<=4:
                bin =bin+"0"
            if int(text[i])>=5:
                bin =bin+"1"
        out=str(int(bin,2))
    elif type==2:
        for i in range(0,len(text)):
            if text[i].isdigit():
                if int(text[i])<=4:
                    bin =bin+"0"
                elif int(text[i])>=5:
                    bin =bin+"1"
            else:
                bin=bin+' '
        j=0
        j0=j
        text0=""
        while j !=len(bin):
            if bin[j]!=" ":
                j+=1
            else:
                text0=text0+str(int(bin[j0:j],2))+" "
                j0=j+1
                j+=1
        text0=text0+str(int(bin[j0:j],2))
        j=0
        j0=0
        while j !=len(text0):
            if text0[j]!=" ":
                j+=1
            else:
                out=out+chr(int(text0[j0:j]))
                j0=j+1
                j+=1
        out=out+chr(int(text0[j0:j]))
    elif type==3:
        print(323)
    else: print('error(errortype="Error-Type")')
    return(out)
