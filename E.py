print(1);
try:
    read=open("abc.txt","r");
    values=read.read();
    print(values);
except Exception as raised:
    print(raised)
print(3)
print("End")

a=[10,20,30]
print(a[2]);

try:
    print(a[3]);
except Exception as reff:
    print(reff)


print("End 2")