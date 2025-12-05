


a = 50 

z=0
arr = [
#   "L50",
#   "R1"
]



with open("D:/adventOfcode/day_1/input.txt", "r") as file:

    arr=file.readlines()
    

for i in range(len(arr)):
    arr[i] = arr[i].replace("\n", "")

for s in arr:

    dir = s[0]
   
    val = int(s[1:])
    add =0

    if dir == 'L':
        
        pointer = (a-val) % 100
        # if a-val != pointer:
        if (a-val) <= 0 and a!=0:
            add+= int(abs((a-val)/100)) +1
            z=z+add
        else:
            add+= int(abs((a-val)/100))
            z+=add
        print(dir,val,a, a-val, (a-val)%100, add, z)
        a = (a-val)%100
        
    
    else:
        
        pointer = (a+val) % 100
        if a+val != (a+val) % 100:
            z+= int((a+val)/100)
        print(dir,val,a, a+val, (a+val)%100, int((a+val)/100),z)
        a = (a+val)%100
        

print(dir, val, z)

