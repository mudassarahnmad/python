i = 1
 while i <= 100 :
         #print "number is : ", i  
         if (i  % 3 == 0) and (i % 5 != 0):
                 print i," fizznumber"
         elif (i % 5 == 0) and (i % 3 != 0)  :
                 print i ," buzznumber"
         elif (i % 3 == 0) and (i % 5 == 0) :
                 print i, "number is fizzbuzz" 
         else :
                 print i, " number is not a fizz or buzz number"
         i = i + 1
