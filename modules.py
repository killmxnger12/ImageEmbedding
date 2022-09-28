#!/usr/bin/python
import subprocess
import os


# Method used to start text file method of value input
def textFileMethod():
	print("Make sure that the file input.txt has proper values inside it")
	input("When you are ready press ENTER...")

	value = ""

	with open("input.txt", "r") as file:
		data = file.read()
		
		if data == "":
			print("There is no value inside the file...")
			print("Exiting the program...")
			exit()

		for x in range(2):
			value += "\n"

		value += "--- INFORMATION ---"
		value += "\n" + str(data)
	
	WriteToFile(value)


# Method used to start the terminal method of value input
def terminalMethod():
	try:
		value = ""
		for x in range(2):
			value += "\n"

		value += "--- INFORMATION ---"
		value += "\n"
		value += str(input("Please input the values: "))

		print("...\nValues successfully written to input.txt file!")

		WriteToFile(value)
	except:
		print("Something went wrong...")


# Method used to create and image file with embedded values
def CreateAnImageFile(path):
	if os.name == "nt":
		# Windows command to embed information
		append = subprocess.run(['copy', '/b', path, "+", "modularTextForm.txt", path], capture_output=True, text=True, shell=True)
		
		if append.returncode == 1:
			print("Image is successfully embedded!\nExiting now...")
			exit()

		print("Something went wrong...")


	if os.name == "posix":
		# Linux command to embed information
		append = subprocess.run('cat ' + str(path) + ' modularTextForm.txt >> ' + str(path), shell=True, text=True, capture_output=True)

		if append.returncode == 1:
			print("Image is successfully embedded!\nExiting the program now...")

		print("Something went wrong...")


# Method used to see if there is the specified file
def CheckIfTheFileExists():
	try:
		file_name = str(input("Please input the actual file name (with jpeg/jpg/png/etc.): "))

		f = open(file_name)
		# Gets the location of the specified file
		location = os.path.abspath(file_name)
		print("The file named " + str(file_name) + " has been found!")
		print("It's location is " + str(location))
		f.close()
		return file_name

	except:
		print("Image file is not accessible, either it does not exists in the folder or it's corrupted...")
		choice = str(input("Do you wish to exit? (yes/no): "))

		if choice.lower() == "yes":
			print("Goodbye!")
			exit()
		elif choice.lower() == "no":
			CheckIfTheFileExists()
		else:
			print("That option is not available...\n\nExiting now...")


# Method used to write values to the modularTextForm.txt file
def WriteToFile(values):
	with open("modularTextForm.txt", "w") as file:
		file.truncate(0)
		file.write(values)
		file.close()
	
	print("Values written successfully to modularTextForm.txt file!")


# Method used to read from modularTextForm.txt file
def ReadFromFile():
	with open("modularTextForm.txt", "r") as file:
		data = file.read()
		file.close()
	
	return data


# Method used to clear all text from modularTextForm.txt file
def ClearTextFile():
	with open("modularTextForm.txt", "w") as file:
		file.truncate()
		file.close()

