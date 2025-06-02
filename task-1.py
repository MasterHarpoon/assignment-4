# TASK 1
try:
    openFile = open('sample.txt', 'r')
    readLine1 = openFile.readline()
    readLine2 = openFile.readline()
    print("Reading file content\nLine 1: " + readLine1 + "Line 2: " + readLine2)
    openFile.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")