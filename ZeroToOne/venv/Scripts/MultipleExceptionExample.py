import sys

try:
    file = open('myfile.txt')
    s = file.readline()
    i = int(s.strip())
except  IOError as e:
    print("I/O Error({0}): {1}".format(e.errno, e.strerror)) #these values at the end insert the error specifics into the error message
except ValueEroor:
    print("Could not convert data to integer")
except:
    print ("unexpected error", sys.exc_info()[0])
    raise
finally:    #Finally will be executed after any try block. This is crucial for any clean up actions (close files/ databases)
    print("goodbye cruel world!")
