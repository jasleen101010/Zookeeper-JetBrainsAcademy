# put your python code here
hour =int(input())
min = int(input())
secs = int(input())
time1 = int((hour*3600)+(min*60)+(secs))
hr = int(input())
m = int(input())
s = int(input())
time2 = int((hr*3600) + (m*60) + (s))
diff = int(time2 - time1)
print(diff)
