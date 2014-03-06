from sys import argv

script, from_file, to_file = argv

output = open(to_file, 'w')
input = open(from_file)

output.write(input.read())

input.close()
output.close()


