file = "chall"
output = "out.png"

with open(file, "rb") as input_file:
    data = input_file.read()

reversed_data = data[::-1]

with open(output, "wb") as output:
    output.write(reversed_data)
