participant_file = open("participants.txt", 'r')
parts = participant_file.read()
participant_file.close()

title_input = raw_input("Please enter the title of the table: ")

parts = parts.split("\n")

i = 0
while i < len(parts):
	parts[i] = parts[i].split("\t")
	i += 1

part_str = ("\t" * 5) + "<article>\n" + ("\t" * 6) + "<h3>" + title_input + "</h3>\n" + ("\t" * 6) + "<div class='table-wrapper'>\n" + ("\t" * 7) + "<table>\n" + ("\t" * 8) + "<tbody>\n"
for part in parts:
	part_str += ("\t" * 9) + "<tr>\n"
	part_str += ("\t" * 10) + "<td>" + part[0] + "</td>\n"
	part_str += ("\t" * 10) + "<td>" + part[1] + "</td>\n"
	part_str += ("\t" * 9) + "<tr>\n"

part_str += ("\t" * 8) + "</tbody>\n" + ("\t" * 7) + "</table>\n" + ("\t" * 6) + "</div>\n" + ("\t" * 5) + "</article>"

participant_file = open("participants.txt", 'w')
participant_file.write(part_str)
participant_file.close()

