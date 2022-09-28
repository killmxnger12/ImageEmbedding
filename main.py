#!/usr/bin/python
import modules


def main():
	# Gives the user the choice on how to input the values to embed
	choice = str(input("How do you wish to add text, over .txt file or through terminal? (txt/term): "))

	if choice.lower() == "txt":
		# Method using the text file	
		modules.textFileMethod()
		values = modules.ReadFromFile()
		print(values + "\n\n")
	elif choice.lower() == "term":
		# Method using the terminal
		modules.terminalMethod()
		values = modules.ReadFromFile()
		print(values + "\n\n")
	else:
		print("\nPlease select one of the available options\n")
		main()



	# Checks if there is the selected image file and returns its name
	image = modules.CheckIfTheFileExists()

	# Appends the information to the image file
	modules.CreateAnImageFile(image)
	# Clears the values from the modularTextForm.txt file
	modules.ClearTextFile()
	print("Goodbye!")
	exit()

if __name__ == '__main__':
	main()