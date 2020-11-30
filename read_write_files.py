#reading files

with open("brushup_topics.txt", 'r') as reader:
	for line in reader:
		print(line, end = '')

with open("brushup_topics.txt", 'r') as reader:
	line = reader.readline()
	while line != '':
		print(line, end = '')
		line = reader.readline()

with open("brushup_topics.txt", 'r') as reader:
	l = reader.readlines()
	print(l)

with open("brushup_topics.txt", 'r') as reader:
	print(reader.read())


#writing files
with open("brushup_topics.txt", 'r') as reader:
	l = reader.readlines()


with open("brushup_topics_reversed.txt", 'w') as writer:
	for topic in reversed(l):
		writer.write(topic)

with open("brushup_topics_reversed.txt", 'w') as writer:
	writer.writelines(reversed(l))	
