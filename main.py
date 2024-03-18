# We define a variable for the part of the text that should be replaced/personalised within the letter content:
PLACEHOLDER = "[name]"

# We put all the names written in the invited_names.txt file in a manageable list format:
with open("Input/Names/invited_names.txt") as names_file:
	names = names_file.readlines()

# We open the letter
with open("Input/Letters/starting_letter.txt") as letter_file:
	letter_content = letter_file.read()
	# # and for each name in the list:
	for name in names:
		# # # we remove the "\n" at the end of each name, using the .strip() method:
		stripped_name = name.strip()
		# # # and we generate a new letter content where we replace the PLACEHODLER with the actual name:
		new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
		# # # then we save the newly generated content in a new text file in the desired location:
		with open(f"Output/ReadyToSend/Letter_To_{stripped_name}.txt", mode="w") as completed_letter:
			completed_letter.write(new_letter)

# # # # JOB DONE !