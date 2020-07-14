log_file = open("um-server-01.txt")   # assined variable to open (use data) from specific document


def sales_reports(log_file): #start function named sales_report with log_file parameter
    for line in log_file:   # start to itterate over data in main file  
        line = line.rstrip() #during every itterarion, our string from main 
                             #document will be return the string without any symbols, only chars
        
        day = line[0:3]     # chose the directory where days collected and get 3 chars from line
        if day == "Mon":    # chose the day for showing
            print(line)     # showing the data from choose day


sales_reports(log_file)     # call the function with argument log-file
