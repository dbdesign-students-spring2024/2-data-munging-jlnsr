""" Workspace Module."""
#/NYU DOCUMENTS/2-data-munging-jlnsr/data/nasa.txt

#J-D average for entire year (Jan-December)
#D-N average between Dec of PREVIOUS year to current Nov
#DJF average of Dec of previous year through Feb of current year
#MAM average of Mar-May
#JJA average of Jun-Aug
#SON average of Sep-Nov
with open("data/nasa.txt","r") as file:
    all_data = file.readlines() #a list containing each line of the file as a string
    raw_data = []
    start_read = ''

    for index,line in enumerate(all_data): #the first lines up to the first lines of data
        if (str.lower(line)).startswith('year'):
            all_data = all_data[index+1:]
            break
    all_data.reverse() #temporarily reverse the data set to remove excess lines from the bottom up 
    for index,line in enumerate(all_data): #iterate through the list backwards and remove excess lines at the bottom
        if (str.lower(line)).startswith('year'):
            all_data = all_data[index+1:]
            break       
    all_data.reverse()
    
    all_data = [line.strip() for line in all_data] #remove \n
    all_data = [line[:-4] for line in all_data if line.endswith( line[0:4])] #removing any reoccurences of the column/row fields
        
    records_as_dict = {} #a dictionary where every 'key' is the year and every 'value' is a list of temps of that year
    values = [] #a temporary list that will acumulate all the acceptable values in each line of data in 'cleaned_data'
    for line in all_data: 
        for i in line.split(" "): #iterate through each line as a list
            if (i != "") and (i != line[:4]): #remove excess spaces AND remove the year to isolate just the temperature values
                values += [i]
        records_as_dict[line[:4]] = values
        values = [] #clear the list for new values
    
    for key in records_as_dict.copy(): #remove anything other than a year
        if key.isnumeric() is False:
            records_as_dict.pop(key)

    records_as_dict_converted = {key:[] for key in records_as_dict.keys()} #dictionary holding the converted values

    for key,record in records_as_dict.items():
        for value in record:
            try:
                records_as_dict_converted[key] += [format((( int(value)/100 ) * 1.8),".1f" )] #convert from celsius to Fahrenheit, and FORMAT result
            except:
                records_as_dict_converted[key] += [value]

line = '' #a variable to write every line for the new CSV file

with open("clean_data.csv","w") as file2:
    for key,record in records_as_dict_converted.items():
        for value in record:
            line += value+"\t"
        file2.write(key+"\t"+line+"\n")
        line = ""
