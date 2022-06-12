print("*******************ASSIGNMENT*****************")
alphabets="A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
NAME="MUHAMMAD USMAN KHAN"
key=4
print("Name: MUHAMMAD USMAN KHAN")
print("Key: 4")
def encrypt(alphabets,arr,key):
    li=list(alphabets.split(" "))
    arr=arr.replace(" ", "")
    li2=list(arr)
    for v in range(key):
        for x in range(len(li2)):
            for y in range(0,len(li)):
                if(li2[x]==li[y]):
                    if(y==25):
                        y=0
                        #y=y-1
                        li2[x]=li[y]
                        break
                    else:
                        y=y+1
                        li2[x]=li[y]
                        break
            listToStr = ' '.join(map(str, li2))
    print(listToStr)
def decrpt(alphabets,arr):
    li=list(alphabets.split(" "))
    arr=arr.replace(" ", "")
    li2=list(arr)
    for v in range(25):
        for x in range(len(li2)):
            for y in range(0,len(li)):
                if(li2[x]==li[y]):
                    if(y==0):
                        y=26    
                        y=y-1
                        li2[x]=li[y]
                        break
                    else:
                        y=y-1
                        li2[x]=li[y]
                        break
            listToStr = ' '.join(map(str, li2))
        print(listToStr)
print("****************ENCRYPTION*******************")
encrypt(alphabets,NAME,4)
print("****************DECRYPTION*******************")
decrpt(alphabets,"Q Y L E Q Q E H Y W Q E R O L E R")
print("**********************************************")
print("PLAIN TEXT: MUHAMMAD USMAN KHAN ")
print("**********************************************")