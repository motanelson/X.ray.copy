print("\033c\033[47;31m")
print("give me a file to convert ...")
a=input().strip()
f1=open(a,"r")
aa=f1.read()
f1.close()
a=aa.replace("\n","\\")
a=a.replace("\r","\\")
print("give me a var name ...")
b=input().strip()
print("int "+b,end="[]={")
counter=0
backs=False
for aa in a:
  if aa=="\\":
      print(ord("\n"),end=",")
  else:
      print(ord(aa),end=",")
          
          
  counter=counter+1

print("0};")