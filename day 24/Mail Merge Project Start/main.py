with open("Input/Letters/starting_letter.txt") as letter_content:
    content = letter_content.read()

name_list = []
with open("Input/Names/invited_names.txt") as names:
    for line in names:
        name_list.append(line.strip("\n"))
print(name_list)
for name in name_list:
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as new_letter:
        new_letter.write(content.replace("[name]", name))
