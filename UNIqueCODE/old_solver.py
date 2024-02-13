file = open("UNI", "r")

file = file.read()

repl = file.replace("字0漢", " ")

arr = repl.split()

output_list = []

for element in arr:
	value = int(element)
	output_list.append(value)

flag = ''

for i in range(len(output_list)):
        flag += chr(output_list[i])

print(flag)
