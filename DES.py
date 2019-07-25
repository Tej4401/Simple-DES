def permutation(p10=[],ten_key=[]):
    p10_key=[]
    a=0
    for i in range(0,len(p10)):
        b=p10[i]-1
        a=ten_key[b]
        p10_key.append(a)
    return p10_key
def EX_OR(plain_ep=[],K1=[]):
    x=[]
    for i in range(0,len(plain_ep)):
        if plain_ep[i]==K1[i]:
            a='0'
        else:
            a='1'
        x.append(a)
    return x
def main():
    command=input("SELECT OPERATION \n\t 1.ENCRYPT 2.DECRYPT : ")
    if command=='1':
        plain_text=input(" > Enter Plain Text : ")
        plain=list(plain_text)
        Ten_key=input(" > Enter 10-Bit Key : ")
        ten_key=list(Ten_key)
        def dec(binary): 
            binary1 = binary 
            decimal, i, n = 0, 0, 0
            while(binary != 0): 
                dec = binary % 10
                decimal = decimal + dec * pow(2, i) 
                binary = binary//10
                i += 1
            return decimal   
        p10=[3,5,2,7,4,10,1,9,8,6]
        p8=[6,3,7,4,8,5,1,9]
        p10_key=permutation(p10,ten_key)
        p10_key_1=[]
        p10_key_2=[]
        for i in range(0,5):
            b=p10_key[i]
            p10_key_1.append(b)
        for i in range(5,10):
            b=p10_key[i]
            p10_key_2.append(b)
        a=p10_key_1[0]
        b=p10_key_2[0]
        for i in range(0,4):
            p10_key_1[i]=p10_key_1[i+1]
            p10_key_2[i]=p10_key_2[i+1]
        p10_key_1[4]=a
        p10_key_2[4]=b
        p8_key=[]
        for i in range(0,5):
            b=p10_key_1[i]
            p8_key.append(b)
        for i in range(0,5):
            b=p10_key_2[i]
            p8_key.append(b)
        P8_key=[]
        for i in range(0,len(p8)):
            b=p8[i]-1
            a=p8_key[b]
            P8_key.append(a)
        K1=P8_key
        a=p10_key_1[0]
        b=p10_key_2[0]
        for i in range(0,4):
            p10_key_1[i]=p10_key_1[i+1]
            p10_key_2[i]=p10_key_2[i+1]
        p10_key_1[4]=a
        p10_key_2[4]=b
        a=p10_key_1[0]
        b=p10_key_2[0]
        for i in range(0,4):
            p10_key_1[i]=p10_key_1[i+1]
            p10_key_2[i]=p10_key_2[i+1]
        p10_key_1[4]=a
        p10_key_2[4]=b
        p8_key=[]
        for i in range(0,5):
            b=p10_key_1[i]
            p8_key.append(b)
        for i in range(0,5):
            b=p10_key_2[i]
            p8_key.append(b)
        P8_key=[]
        for i in range(0,len(p8)):
            b=p8[i]-1
            a=p8_key[b]
            P8_key.append(a)
        K2=P8_key
        IP=[2,6,3,1,4,8,5,7]
        plain_ip=permutation(IP,plain)
        for i in range(0,len(IP)):
            b=IP[i]-1
            a=plain[b]
            plain_ip.append(a)
        EP=[4,1,2,3,2,3,4,1]
        plain_ip1=[]
        plain_ip2=[]
        for i in range(0,4):
            b=plain_ip[i]
            plain_ip1.append(b)
        for i in range(4,8):
            b=plain_ip[i]
            plain_ip2.append(b)
        plain_ep=permutation(EP,plain_ip2)
        x=EX_OR(plain_ep,K1)
        x1=[]
        x2=[]
        for i in range(0,4):
            b=x[i]
            x1.append(b)
        for i in range(4,8):
            b=x[i]
            x2.append(b)
        y=[]
        S0=[[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
        S1=[[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]
        a=x1[0]
        b=x1[3]
        y=str(a)+str(b)
        g=int(y)
        y=dec(g)
        y=int(y)
        c=x1[1]
        d=x1[2]
        z=str(c)+str(d)  
        g=int(z)
        z=dec(g)
        z=int(z)
        k=[]
        l=S0[y][z]
        k.append(l)
        a=x2[0]
        b=x2[3]
        y=str(a)+str(b)
        g=int(y)
        y=dec(g)
        y=int(y)
        c=x2[1]
        d=x2[2]
        z=str(c)+str(d)  
        g=int(z) 
        z=dec(g)
        z=int(z)
        l=S1[y][z]
        k.append(l)
        a=k[0]
        b=k[1]
        if a==0:
            a='00'
        elif a==1:
            a='01'
        elif a==2:
            a='10'
        else:
            a='11'
        if b==0:
            b='00'
        elif b==1:
            b='01'
        elif b==2:
            b='10'
        else:
            b='11'
        k=[]
        k.append(a)
        k.append(b)
        K=k[0]+k[1]
        K=list(K)
        P4=[2,4,3,1]
        p4=permutation(P4,K)
        fk=EX_OR(p4,plain_ip1)
        plain_ip1=[]
        plain_ip1=plain_ip2
        plain_ip2=[]
        plain_ip2=fk
        fk=[]
        plain_ep=permutation(EP,plain_ip2)
        x=EX_OR(plain_ep,K2)
        x1=[]
        x2=[]
        for i in range(0,4):
            b=x[i]
            x1.append(b)
        for i in range(4,8):
            b=x[i]
            x2.append(b)
        y=[]
        S0=[[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
        S1=[[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]
        a=x1[0]
        b=x1[3]
        y=str(a)+str(b)
        g=int(y)
        y=dec(g)
        y=int(y)
        c=x1[1]
        d=x1[2]
        z=str(c)+str(d)  
        g=int(z)
        z=dec(g)
        z=int(z)
        k=[]
        l=S0[y][z]
        k.append(l)
        a=x2[0]
        b=x2[3]
        y=str(a)+str(b)
        g=int(y)
        y=dec(g)
        y=int(y)
        c=x2[1]
        d=x2[2]
        z=str(c)+str(d)  
        g=int(z) 
        z=dec(g)
        z=int(z)
        l=S1[y][z]
        k.append(l)
        a=k[0]
        b=k[1]
        if a==0:
            a='00'
        elif a==1:
            a='01'
        elif a==2:
            a='10'
        else:
            a='11'
        if b==0:
            b='00'
        elif b==1:
            b='01'
        elif b==2:
            b='10'
        else:
            b='11'
        k=[]
        k.append(a)
        k.append(b)
        K=k[0]+k[1]
        K=list(K)
        P4=[2,4,3,1]
        p4=permutation(P4,K)
        fk=EX_OR(p4,plain_ip1)
        cipher=''.join(fk)
        text=''.join(plain_ip2)
        cipher_text=cipher+text
        ciphertext=list(cipher_text)
        IP_INV=[4,1,3,5,7,2,8,6]
        ipinv=[]
        for i in range(0,8):
            b=IP_INV[i]-1
            a=ciphertext[b]
            ipinv.append(a)
        cipher_text=''.join(ipinv)
        print(" > Encrypted Text : ",end="")
        print(cipher_text)
    elif command=='2':
        plain_text=input(" > Enter Cipher Text : ")
        plain=list(plain_text)
        Ten_key=input(" > Enter 10-Bit Key : ")
        ten_key=list(Ten_key)
        def dec(binary): 
            binary1 = binary 
            decimal, i, n = 0, 0, 0
            while(binary != 0): 
                dec = binary % 10
                decimal = decimal + dec * pow(2, i) 
                binary = binary//10
                i += 1
            return decimal   
        p10=[3,5,2,7,4,10,1,9,8,6]
        p8=[6,3,7,4,8,5,1,9]
        p10_key=permutation(p10,p10_key)
        p10_key_1=[]
        p10_key_2=[]
        for i in range(0,5):
            b=p10_key[i]
            p10_key_1.append(b)
        for i in range(5,10):
            b=p10_key[i]
            p10_key_2.append(b)
        a=p10_key_1[0]
        b=p10_key_2[0]
        for i in range(0,4):
            p10_key_1[i]=p10_key_1[i+1]
            p10_key_2[i]=p10_key_2[i+1]
        p10_key_1[4]=a
        p10_key_2[4]=b
        p8_key=[]
        for i in range(0,5):
            b=p10_key_1[i]
            p8_key.append(b)
        for i in range(0,5):
            b=p10_key_2[i]
            p8_key.append(b)
        P8_key=[]
        for i in range(0,len(p8)):
            b=p8[i]-1
            a=p8_key[b]
            P8_key.append(a)
        K2=P8_key
        a=p10_key_1[0]
        b=p10_key_2[0]
        for i in range(0,4):
            p10_key_1[i]=p10_key_1[i+1]
            p10_key_2[i]=p10_key_2[i+1]
        p10_key_1[4]=a
        p10_key_2[4]=b
        a=p10_key_1[0]
        b=p10_key_2[0]
        for i in range(0,4):
            p10_key_1[i]=p10_key_1[i+1]
            p10_key_2[i]=p10_key_2[i+1]
        p10_key_1[4]=a
        p10_key_2[4]=b
        p8_key=[]
        for i in range(0,5):
            b=p10_key_1[i]
            p8_key.append(b)
        for i in range(0,5):
            b=p10_key_2[i]
            p8_key.append(b)
        P8_key=[]
        for i in range(0,len(p8)):
            b=p8[i]-1
            a=p8_key[b]
            P8_key.append(a)
        K1=P8_key
        IP=[2,6,3,1,4,8,5,7]
        plain_ip=permutation(IP,plain)
        EP=[4,1,2,3,2,3,4,1]
        plain_ip1=[]
        plain_ip2=[]
        for i in range(0,4):
            b=plain_ip[i]
            plain_ip1.append(b)
        for i in range(4,8):
            b=plain_ip[i]
            plain_ip2.append(b)
        plain_ep=permutation(EP,plain_ip2)
        x=EX_OR(plain_ep,K1)
        x1=[]
        x2=[]
        for i in range(0,4):
            b=x[i]
            x1.append(b)
        for i in range(4,8):
            b=x[i]
            x2.append(b)
        y=[]
        S0=[[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
        S1=[[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]
        a=x1[0]
        b=x1[3]
        y=str(a)+str(b)
        g=int(y)
        y=dec(g)
        y=int(y)
        c=x1[1]
        d=x1[2]
        z=str(c)+str(d)  
        g=int(z)
        z=dec(g)
        z=int(z)
        k=[]
        l=S0[y][z]
        k.append(l)
        a=x2[0]
        b=x2[3]
        y=str(a)+str(b)
        g=int(y)
        y=dec(g)
        y=int(y)
        c=x2[1]
        d=x2[2]
        z=str(c)+str(d)  
        g=int(z) 
        z=dec(g)
        z=int(z)
        l=S1[y][z]
        k.append(l)
        a=k[0]
        b=k[1]
        if a==0:
            a='00'
        elif a==1:
            a='01'
        elif a==2:
            a='10'
        else:
            a='11'
        if b==0:
            b='00'
        elif b==1:
            b='01'
        elif b==2:
            b='10'
        else:
            b='11'
        k=[]
        k.append(a)
        k.append(b)
        K=k[0]+k[1]
        K=list(K)
        P4=[2,4,3,1]
        p4=permutation(P4,K)
        fk=EX_OR(p4,plain_ip1)
        plain_ip1=[]
        plain_ip1=plain_ip2
        plain_ip2=[]
        plain_ip2=fk
        fk=[]
        plain_ep=permutation(EP,plain_ip2)
        x=EX_OR(plain_ep,K2)
        x1=[]
        x2=[]
        for i in range(0,4):
            b=x[i]
            x1.append(b)
        for i in range(4,8):
            b=x[i]
            x2.append(b)
        y=[]
        S0=[[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
        S1=[[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]
        a=x1[0]
        b=x1[3]
        y=str(a)+str(b)
        g=int(y)
        y=dec(g)
        y=int(y)
        c=x1[1]
        d=x1[2]
        z=str(c)+str(d)  
        g=int(z)
        z=dec(g)
        z=int(z)
        k=[]
        l=S0[y][z]
        k.append(l)
        a=x2[0]
        b=x2[3]
        y=str(a)+str(b)
        g=int(y)
        y=dec(g)
        y=int(y)
        c=x2[1]
        d=x2[2]
        z=str(c)+str(d)  
        g=int(z) 
        z=dec(g)
        z=int(z)
        l=S1[y][z]
        k.append(l)
        a=k[0]
        b=k[1]
        if a==0:
            a='00'
        elif a==1:
            a='01'
        elif a==2:
            a='10'
        else:
            a='11'
        if b==0:
            b='00'
        elif b==1:
            b='01'
        elif b==2:
            b='10'
        else:
            b='11'
        k=[]
        k.append(a)
        k.append(b)
        K=k[0]+k[1]
        K=list(K)
        P4=[2,4,3,1]
        p4=permutation(P4,K)
        fk=EX_OR(p4,plain_ip1)
        cipher=''.join(fk)
        text=''.join(plain_ip2)
        cipher_text=cipher+text
        ciphertext=list(cipher_text)
        IP_INV=[4,1,3,5,7,2,8,6]
        ipinv=[]
        for i in range(0,8):
            b=IP_INV[i]-1
            a=ciphertext[b]
            ipinv.append(a)
        cipher_text=''.join(ipinv)
        print(" > Decrypted Text : ",end="")
        print(cipher_text)
    else:
        print(" [-] Wrong Input ")
main()
state=input("press any key to resume and 'Q' to quit : ")
while(state!='Q'):
    main()
    state=input("press any key to resume and 'Q' to quit : ")