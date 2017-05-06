inp = raw_input("Enter the temp in number ")
try:
    fahr =  float(inp)
    cel = (fahr - 32.0) *5.0/9.0
    print cel
except:
    print "You have not entered the number. Quitting........."
