f = open("question3.txt", "r")
f1 = f.readlines()

for x in f1:
    a = x.strip("\n")
    if "delhi" in x:
        delhi_file=open("delhi.txt","a")
        delhi_file.write(a)
        delhi_file.write("\n")
        delhi_file.close()
    elif "shimla" in x:
        shimla_file=open("shimla.txt", "a")
        shimla_file.write(a) 
        shimla_file.write("\n")
        shimla_file.close()
    else:
        others_file=open("others.txt", "a")
        others_file.write(a)
        others_file.write("\n")
        others_file.close()
df=open("delhi.txt","r")  
r =  df.read()    
print(r)
df.close()
sf=open("shimla.txt","r")  
s =  sf.read() 
print(s)
sf.close()   
of=open
("others.txt","r")  
o=of.read()    
# print(o)
of.close()
