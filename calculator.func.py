#Calculator Program

print " This program is a calculator program"
def table():
#       print "Please enter the integer for the table"
        table = int(raw_input("enter table :"))
        last = int(raw_input("enter last :"))
        print last
        start = 1
        while start <= last:
                 print table, "*", start, "=", int(table) *  int(start)
                 start = int(start) + 1
        loop2 = 1
        choice2 = 0
        while loop2 != 0:
                 print "do you want to continue:"
                 print " "
                 print "1)  yes"
                 print "2) no"
                 choice2 =int(raw_input("please enter your choice: "))
                 if choice2 == 1:
                           print "Please enter the integer for the table"
                           table = int(raw_input("enter table :"))
                           start = 1
                           last = int(raw_input("enter last :"))
                           while start <= last:
                                   print table, "*", start, "=", int(table) *  int(start)
                                   start = int(start) + 1
                 elif choice2 == 2:
                        loop2 = 0
def main():
        print "Please enter the integer for the table calling from function"
        table() 

#main()
loop = 1

choice = 0

while loop != 0:
        print "your options are:"
        print " "
        print "1)  Addition"
        print "2) Subtraction"
        print "3) Multiplication"
        print "4) Divison"
        print "5) Tables"
        print "6) Quit"

        choice =int(raw_input("please enter your choice: "))

        if choice == 1:
                num1 = int(raw_input("enter num1 :"))
                num2 = int(raw_input("enter num2 :"))
                print num1, "+", num2, "=", int(num1) + int(num2)
        elif choice == 2:
                num1 = int(raw_input("enter num1 :"))
                num2 = int(raw_input("enter num2 :"))
                print num1, "-", num2, "=", int(num1) -  int(num2)
        elif choice == 3:
                num1 = int(raw_input("enter num1 :"))
                num2 = int(raw_input("enter num2 :"))
                print num1, "*", num2, "=", int(num1) *  int(num2)
        elif choice == 4:
                num1 = int(raw_input("enter num1 :"))
                num2 = int(raw_input("enter num2 :"))
                print num1, "/", num2, "=", int(num1) /  int(num2)
        elif choice == 5:
                main()
        elif choice == 6:
                loop = 0

print " Thank you for using calculator.py"
