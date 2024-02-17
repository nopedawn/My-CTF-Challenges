file = open("UNI", "r").read()

repl = file.replace("字0漢", " ")

flag = ''

for i in repl.split():
	flag += chr(int(i))

print(flag)
