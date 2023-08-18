from f_separate_str import separate_str

str = "This is a test"

file = open("./test_file", "a+")
separated_str = separate_str(str, " ")

for i in separated_str:
    file.write(i + "\n")
file.close()
