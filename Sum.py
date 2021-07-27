import os

def work_add(a,b):
    c=int(a)+int(b);
    print(c);
    print(a+"与"+b+"的和为"+str(c));
first_num= os.getenv("first_num");
second_num = os.getenv("second_num");
work_add(first_num,second_num)
