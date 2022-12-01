#Title: assignment 7
#Description: A script detailing pickling and error handling
#Date created: 11/28/22
#Date edited and completed 11/29/22
#Andrew Meng, 11/29/22, Edited script

import pickle

file_name_str = "AppData.dat"
table_lst = []
#processing section
#An example of pickling
def saving_data_with_pickle(file_name, list_of_data): #this function is in charge of saving data using pickling
    file = open(file_name, 'ab') #This will open the file (AppData.dat) will also open in append mode
    pickle.dump(list_of_data, file) #this command will dump the contents of this list into the designated file
    file.close() #closes the file

def reading_Data(file_name): #2nd function that reads the data saved by the other function
    file = open(file_name, 'rb') #will open the same file but read the contents of the binary file
    list_of_data = pickle.load(file) #this command will retrieve and unpickle the binary data
    file.close()
    return list_of_data

#presentation section
print("Please input a name and ID")
name = input("please enter a name:")
try: #structural exception handling
    userId = int(input("assign an ID to this name:"))
except: #this kicks in when the input isn't an integer
    print("This input requires an integer value")

userId = int(input("Please re-enter a numerical ID "))
table_lst = [name, userId]
#calls the previous functions
saving_data_with_pickle(file_name_str, table_lst)
print(reading_Data(file_name_str))

