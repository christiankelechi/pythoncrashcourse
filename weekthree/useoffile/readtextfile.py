from pathlib import Path

pythontextpath=Path('D:\\codeblazebackendcourse\\weekthree\\useoffile\\javatext.txt')

# openmytext=pythontextpath.open(mode='r', encoding='utf-8')

# print("for reading only\n "+str(openmytext.read()))
# openmytext=pythontextpath.open(mode='a', encoding='utf-8')
# textappend=input("Enter a text to append to the inital text\n")
# openmytext.write(textappend)
# openmytext=pythontextpath.open(mode='r', encoding='utf-8')
# print(openmytext.read())
openmytext=pythontextpath.open(mode='w', encoding='utf-8')
openmytext.write("Flutter is a very nice framework for mobile app development")

openmytext.close()
