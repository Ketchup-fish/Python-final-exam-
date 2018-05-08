# -*- coding: utf-8 -*-

height = 1.75
weight = 80.5
bmi = float(weight)/(float(height)*float(height))
print("小明的BMI指数是:",bmi)
if bmi<18.5:
    print("过轻")
elif 18.5<bmi<25 or bmi==18.5:
    print("正常")
elif 25<bmi<28 or bmi==25:
    print("过重")
elif 28<bmi<32 or bmi==28:
    print("肥胖")
else:
    print("严重肥胖")
	
#方法二：
h=input('身高:')
w=input('体重:')
bmi =float(w)/(float(h)**2)
print("小明的BMI指数是：",bmi)
if float(bmi) < 18.5 :
    print('过轻') 
elif 18.5<= float(bmi) < 25 : 
    print('正常') 
elif 25<= float(bmi) < 28 : 
    print('过重') 
else: 
    print('严重肥胖')