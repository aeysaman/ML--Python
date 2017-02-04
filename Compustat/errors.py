import csv

error_file = open("error.csv", "w")
error_file.write("Error,Name,Date,Field,Calc\n")
print("error file")

def throwError(error, name, date, field, calc):
    error_file.write("{},{},{},{},{}\n".format(error, name, date, field, calc))

def closeErrorFile():
    error_file.close()
