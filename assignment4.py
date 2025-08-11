req_file = "sample.txt"
try:
    with open(req_file, 'r') as file:
        print("Reading file content:\n")
        for index, line in enumerate(file):
            print(f"Line {index+1}: {line.strip()}")

except: FileNotFoundError, print("Error: The file "+req_file+" was not found.")



text_st = input("Enter text to write to the file: ")
t = open("output.txt","w")
t.write(text_st+"\n")
print("Data successfully written to output.txt")
t.close()

text_ap = input("Enter additional text to append: ")
e = open("output.txt","a")
e.write(text_ap+"\n")
print("Data successfully appended")
e.close()


r = open("output.txt","r")
c = r.read()
print(c)
r.close()