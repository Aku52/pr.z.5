#Арифметика
input_data = open('input.txt','r')
data = input_data.read()
data = data.split()

a = int(data[0])
b = int(data[1])
c = int(data[2])
if c == a*b:
    p = "Yes"
else:
    v = "No"

output_data = open('output.txt','w')
output_data.write()

input_data.close('input.txt','r')
output_data.close('output.txt','w')