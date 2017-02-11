import csv

errors_All = dict()

def throwError(error, name, date, field, calc):
    if (error, name, date, field) in errors_All:
        errors_All[error, name, date, field] += 1
    else:
        errors_All[error, name, date, field] = 1
    
def closeErrorFile():
    error_file = open("error.csv", "w")
    error_file.write("Error,Name,Date,Field,Count\n")
    for error, name, date, field in errors_All:
        c = errors_All[error, name, date, field]
        error_file.write("{},{},{},{},{}\n".format(error, name, date, field, c))
    error_file.close()
