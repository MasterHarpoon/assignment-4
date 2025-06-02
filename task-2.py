# TASK 2

try:
    inpt1 = str(input("Enter text to write to the file: "))
    openFile = open('output.txt', 'w')
    writeText = openFile.write(inpt1 + '\n')
    openFile.close()
finally:
    print("Data successfully written to output.txt")

try:
    inpt2 = str(input("Enter additional text to append: "))
    openFile = open('output.txt', 'a')
    appendText = openFile.write( inpt2)
    openFile.close()
finally:
    print("Data successfully apended")

print("Final content of output.txt:\n")
openFile = open('output.txt', 'r')    
readText = openFile.read()
print(readText)
openFile.close()
    