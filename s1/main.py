print("Hello there")

 a = input("Insert your name: ")
 b = input("Insert your age: ")
#
 print(type(a))
 a = b
 try:
    print(type(int(a)))
 except ValueError or Exception as e:
     print(e)
     print("Cannot convert {} to int".format(a))

 print("Hi " + a)
 print("Hi", a)
 print("Hi {}. You're {} years old".format(a, b))

 f = open("dataset.txt", 'w')
 f.write("""Results\n""")
 f.write(str(12))
 f.write("\n")
 f.write(str(20))
 print(f.closed)
 f.close()
 print(f.closed)

with open("dataset.txt") as f:
 for line in f:
     print(line)
