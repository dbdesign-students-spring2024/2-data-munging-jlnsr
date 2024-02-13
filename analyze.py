# Place code below to do the analysis part of the assignment.
with open("clean_data.csv","r") as file:
    full_data = file.readlines()
    full_data = [i.split("\t") for i in full_data]
    for i in full_data: #remove the first line 
        for j in i:
            if str.lower(j) == 'year':
                full_data.remove(i)
    full_data = [i[:13] for i in full_data] #extract just the relevant values (Jan - Dec)
    full_data.pop()
    records_as_dict = {i[0]:i[1:] for i in full_data}

    for record in records_as_dict.values():
        for index,value in enumerate(record):
            if value != "\n":
                try:
                    record[index] = float( record[index] )
                except:
                    continue
            else:
                record.remove(value)
    total = 0   #total count for all months in each year of EACH decade
                #starting at 1880
    counter = 0 #keep track of how many years, stop at 9
    
    averages_list = [] #list holding JUST averages
    decades_list = [] #list of decades
    for key,record in records_as_dict.items():
        if counter == 0:
            decades_list += [ key+ "-" + str( int(key)+9 )]    #create a key for the beginning year of each decade e.g. 1890,1900,etc. that will hold the average value
        if counter < 9:
            total += sum(record)
            counter += 1
        else:
            averages_list += [format(total/120, '.2f')] #total / amount of months in a decade = average
            counter = 0 #rest variables
            total = 0 
        
    for decade,average in zip(decades_list, averages_list): #output the averages according to decade
        print(decade,": ",average,sep="")
