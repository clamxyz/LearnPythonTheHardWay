from sys import argv

script, file_name = argv

def print_all(f):
	print f.read()

def rewind(f):
	print f.seek(0)

def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(file_name)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"
line_count = 1
print_a_line(line_count, current_file)

line_count += 1
print_a_line(line_count, current_file)

line_count += 1
print_a_line(line_count, current_file)

current_file.close()
