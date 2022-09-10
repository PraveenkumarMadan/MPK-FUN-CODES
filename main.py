import sys
import time
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.10)
s="MPK FLAMES CALCULATOR"
g=""
print(g.center(50),end="");
delay_print(s);print();
print("Enter your name: ")
a=input().strip();
print("Enter your crush's name: ");
b=input().strip();
a=a.lower();b=b.lower();
s="";
for i in range(97,123):
    x=a.count(chr(i));
    y=b.count(chr(i));
    z=abs(x-y);
    s+=chr(i)*z;
t="FLAMES";
while(len(t)>1):
    h=len(t);g=len(s);
    while(g>h):
        g-=h;
    f=t[g:];f+=t[:g- 1];
    t=f;
if(t=='F'):
    print("FRIENDS");
elif(t=='L'):
    print("LOVE");
elif(t=='A'):
    print("AFFECTION");
elif(t=='M'):
    print("MARRIAGE");
elif(t=='E'):
    print("ENEMY");
else:
    print("SIBLING");

