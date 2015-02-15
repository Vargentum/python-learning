x = "There is %d types of people." % 10  # interpolate 10 to string with decimal conversion
binary = "binary" # assign string value to variable
do_not = "don't" # assign string value to variable
y = "Those who knows %s and those who %s." % (binary, do_not) # interpolate two variables inside string with string conversion

print(x) #print variable x value
print(y) #print variable y value

print("I said %r." % x) # print string with interpolated variable converted as printable representation repr()
print("I also said: '%s'." % y) # print string with interpolated variable converted as string

hilarious = False # assign False bool to varable
joke_evaluation = "Isn't that joke so funny?! %s" # assign string with interpolated value converted to string

print(joke_evaluation % hilarious) # print first variable value with interpolated inside it value of second one

w = "This is the left side of..."  # assign string to variable
e = "a string with a right side." # assign string to variable

print(w + e) # print result of concat first and second variables