"Relative path, if file is in Desktop"

with open("../../../../../../../Otros/Escritorio/my_file.txt") as file:
    contents = file.read()
    print(contents)



"Absolute path, if file is in Desktop"

with open("/Users/jrodriji/OneDrive - NTT DATA EMEAL/Otros/Escritorio/my_file.txt") as file:
    contents = file.read()
    print(contents)

