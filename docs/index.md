# Python Pickling and Structured Error Handling 
**Dev:**  *AMeng*  
**Date:** *11.29.2022*
## Introduction
  In this assignment, we utilized python pickling and structured error handling in a python script. We were asked to find sources detailing these topics and demonstrate our understanding. 
## Method
I decided to create a python script that resembles our previous assignments of editing a to do list, and given the numerical aspect that pickling involves, I changed priority from a string variable to an integer. 
The new topics covered this week were python pickling and structured error handling.
## Pickling
Python pickling involves serializing and/or deserializing a python object structure. Pickling can be used to convert a python object and turn it into a character stream, that can be further transformed the object in another script. This process can be used to transport data/ share objects, and in this assignment, we will be storing data, pickling it into a binary file, which must be unpickled afterwards. This website https://www.synopsys.com/blogs/software-security/python-pickling/#:~:text=Pickle%20in%20Python%20is%20primarily,transport%20data%20over%20the%20network. Helped in initially showing what the purpose any function of pickling was, and I supplemented that knowledge with this website, https://www.geeksforgeeks.org/understanding-python-pickling-example/ a more practical example. 
## Structured Error Handling
Structured error handling is the process of defining a possible error using a try/except command. This can trap these errors without causing the program/script to stop running. I used this website https://docs.python.org/3/tutorial/errors.html to provide further insight into this process. I liked how this website described this process as it was very logical and formulaic.This process is important to determine how errors can interact with your created script and to ensure that the script can still function in the event of an error. 
## Script Rundown
In this week’s assignment, I defined two different functions, save data with pickle, and read data. I used the file AppData.dat to record the data in binary. I started this assignment with the import pickle command import the pickle module. Then I defined function save data with pickle, and in it, I opened the file using file = open(file_name) and used the new command pickle.dump to dump the contents of the list into the file defined above. See figure 1.
![image](https://user-images.githubusercontent.com/118324497/204984009-eb9bf9d6-bd53-478f-8016-829cf1ab887b.png)

In the second function, reading_data, I did a similar process except this function unpacks the binary code dumped into the list by the previous function, and then reads and unpickles the data. The important command was pickle.load as opposed to pickle.dump. See figure 1.
After defining my functions, I created prompts asking for user input to determine both name and ID. The ID has been set as an integer, and I used structural exception handling in the form of the try/except commands to designate a possible error. In this case, if the user inputs any non-integer value, the script will prompt them to re-input a new value. See fig 2:
![image](https://user-images.githubusercontent.com/118324497/204984043-aae4ac3e-4de5-4a6f-81d8-c09313cf578c.png)
## Errors:
I was more prone to errors in this assignment given that the knowledge and information required to perform this task was self-provided. I had to find sources that could convey the necessary information in a digestible manner. Some sources were great sources of information, but too complex for a rookie python programmer. I didn’t fully comprehend some of the processes at first, struggling with the binary file, but looking at various websites and some classmate examples, I was able to troubleshoot and solve my issues. 
## Summary 
This assignment uniquely tested my ability to find crucial information online, as opposed to being provided with the sources to succeed. The material wasn’t as challenging as some previous assignments but being able to critically analyze and comprehend unknown sources of information is a fundamental aspect to learning new things. The topics covered included pickling and structured exception handling, which were both fascinating topics to learn about. Errors are quite a common occurrence for a newer programmer such as myself, and being able to account for and essentially target errors to ensure functionality was valuable to learn.  
## Results
![image](https://user-images.githubusercontent.com/118324497/204984188-057be890-2d61-4fdc-baa7-8d8097b17e4e.png)
Figure 3: process running on command prompt, when I input and for ID, it rejected and asked for a numerical value.
![image](https://user-images.githubusercontent.com/118324497/204984257-fb0dfc9f-b9c1-4770-9751-947382bb465e.png)
Figure 4: Same process but in PyCharm
![image](https://user-images.githubusercontent.com/118324497/204984320-f6b89a0d-55c8-4261-90e8-8853a71af733.png)
Figure 5: The results in a binary file. 
