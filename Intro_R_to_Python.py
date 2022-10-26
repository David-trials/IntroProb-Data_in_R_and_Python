# 25-10-2022
# Converting "Introduction to R and RSTudio" to Python
# Done using PyCharm. Note the imported data files were placed in the project directory for easy import.

# Note: R uses the following libraries:
# statsr: for data files and functions used in statistical analysis. Maybe standard Python library is enough...?
# dplyr: for data wrangling. Usage of lists along with the math library should be enough to manipulate data in Python
# ggplot2: for data vizualization. Note: these are the most common in Python: numpy, pandas, matplotlib


import pandas as pd # Pandas allows CSV file import into a dataframe, among other tools
import matplotlib.pyplot as plt # Allows plotting of graphs
import numpy as np # Very useful library to work with arrays

#test = pd.read_csv("C:/Users/David Aurelio/Desktop/niftydata.csv")
#print(test.head()) #Printing just the head of the file
#print(test)

test2 = pd.read_csv("test_arbuthmot.csv") # File is in project directory so no path needed
#print(test2)
#print(test2.head(3)) #see only first 3 lines of the data
#print(test2.columns) # Appears as a Index list of the first row
#print(test2["year"]) # Prints only the year column
#print(test2.iloc[0:2]) #Read first 2 rows and prints it plus header row

# A way to see the dimensions of the data passed to test2 #
print(len(test2.columns)) #Prints number of columns in test2
print(len(test2))   # Prints number of rows in test2

# How many variable are on the imported data file test_arbuthmot.csv?
# We can just print the first 3 lines of the data and see them.
print(test2.head(3)) #see only first 3 lines of the data
# We see the unnamed indexing number, where 0 is the line with the variable names; year, boys and girls

# If we do just a normal print of all data we should see the firs and last lines of the data in test2
print(test2)
# Since the years of number of births is sequentially organized we can see the study
#was from 1629 to 1710

# Seeing the data of just the boys birth number column.
print(test2["boys"]) # Prints only the boys column
# The same as before can be done to access the girls column of data
print(test2["girls"]) # Prints only the boys column

#Ploting the girls births over the years of the study
# Note. Will import the matplotlib.pyplot library to be able to plot the graphs

#First, just a general plot from a list of numbers ofr x-axis and y-axis
x=[1,2,3]
y=[4,5,6]
plt.plot(x,y)
plt.show()

#Now for the girls births vs year plot
plt.plot(test2["year"],test2["girls"]) #In Pycharm this graph will appear after you close the previous pop-up one
plt.title("Girls births over years of study") # Giving it a title
plt.xlabel("Year") # Adding a label to x-axis
plt.ylabel("Number of girls births") #Adding a label to y-axis
plt.show()

# By default it will draw it as a line so lets put some markers for a scatter plot type and add some colour.
plt.plot(test2["year"],test2["girls"], label='Girls', color="pink", linewidth=2, marker=".", markersize=10, linestyle="")
plt.legend() # This allow the label of the curve to be plotted
plt.show()
# See https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html for more details on what can go in the plot

# Determining the total number of births over the years and saving it to a tuple structure named total
total = (test2["boys"]+test2["girls"]) # Saving it as a tuple data structure to make it immutable
print(total)

# Let us make now a data frame with the original data plus the total births determined just before
# The pandas library allows this as follows
print("---Making data frame.---")
df=pd.DataFrame(test2) #Creating a data which is just a copy of test2
print(df) # Printing to confirm it is the same as test2
df2=df.assign(Total=total) #Adding/assigning the total variable as a column in the new data frame df2
print(df2)
# Plotting total births of the years of study
plt.plot(df2["year"],df2["Total"],label='total', color="red", marker=".", markersize=10) #In Pycharm this graph will appear after you close the previous pop-up one
plt.title(" Total births over years of study") # Giving it a title
plt.xlabel("Year") # Adding a label to x-axis
plt.ylabel("Number of total births") #Adding a label to y-axis
plt.legend() # This allow the label of the curve to be plotted
plt.show()

#Plot of boys proportion born over time
plt.plot(df2["year"],df2["boys"]/df2["Total"],label='Boys/total', color="blue", marker=".", markersize=10) #In Pycharm this graph will appear after you close the previous pop-up one
plt.title(" Boys proportion of births over years of study") # Giving it a title
plt.xlabel("Year") # Adding a label to x-axis
plt.ylabel("Boys/total ") #Adding a label to y-axis
plt.legend() # This allow the label of the curve to be plotted
plt.show()

# Adding to a data frame a new column with a TRUE boolean variable if that year more boys were born
for i in range(0,len(df2)): # Loop to run through all 82 rows of the dataframe
    if df2["boys"][i] > df2["girls"][i]: #Comparing the number of boys to girls in each row "i" and if it is larger
        more_boys = True            # set the boolean variable to true in that row of the df2 dataframe
    else:
        more_boys = False

df2=df.assign(MoreBoys=more_boys) #Adding/assigning the a Boolean variable as a column in the data frame df2
print(df2)

## Loading a new dataset named "present" ##

print("--- Loading new data for present births ---")
test3 = pd.read_csv("test_present.csv") # File is in project directory so no path needed
# A way to see the dimensions of the data passed to test3 #
print("Number of variables corresponds to the columns number: ",len(test3.columns)) #Prints number of columns in test3
print("Number of rows of imported data: ", len(test3))   # Prints number of rows in test3
# How many variable are on the imported data file test_arbuthmot.csv?
# We can just print the first 3 lines of the data and see them.
print("First 3 rows of the imported data.")
print(test3.head(3)) #see only first 3 lines of the data

#Printing first and last year rows.

print("1st row-> \n", test3.iloc[0]) #Note: data of each column will appear of different rows on output
print("last row-> \n", test3.iloc[len(test3)-1]) #Remember data starts at 0

# Again making a new dataframe not to alter original test3 data
print("---Making data frame.---")
df3=pd.DataFrame(test3) #Creating a data which is just a copy of test2
print(df3) # Printing to confirm it is the same as test2
total3 = (test3["boys"]+test3["girls"]) # Saving it as a tuple data structure to make it immutable
df3=df3.assign(Total=total3) #Adding/assigning the total variable as a column in the new data frame df2
prop_boys = (df3["boys"]/df3["Total"])
df3=df3.assign(PropBoys=prop_boys)
print(df3)
#Let's graph the new data of the dataframe df3
print("Next the graph for present data of prop_boys vs year:")
plt.plot(df3["year"],df3["PropBoys"],label='Boys/total', color="purple", marker=".", markersize=10) #In Pycharm this graph will appear after you close the previous pop-up one
plt.title(" Boys proportion for present data.") # Giving it a title
plt.xlabel("Year") # Adding a label to x-axis
plt.ylabel("Prop_boys") #Adding a label to y-axis
plt.legend() # This allow the label of the curve to be plotted
plt.show()
# Adding a True boolean variable to df3 if there are more boys than girls each year
for i in range(1,len(df3)): # Note that the data for "present" start at index 1 not 0 like before.
    if df3["boys"][i] > df3["girls"][i]: #Comparing the number of boys to girls in each row "i" and if it is larger
        more_boys3 = True            # set the boolean variable to true in that row of the df2 dataframe
    else:
        more_boys3 = False
df3=df3.assign(MoreBoys=more_boys3) #Adding/assigning the a Boolean variable as a column in the data frame
print(df3)

# Plot for the proportion of boys to girls
prop_boy_girl = df3["boys"] / df3["girls"]
df3=df3.assign(PropBoyGirl=prop_boy_girl) #Adding/assigning the a Boolean variable as a column in the data frame
print(df3.head(3)) # Showing just the first 3 rows

plt.plot(df3["year"],df3["PropBoyGirl"],label='Boys/Girls', color="yellow", marker="*", markersize=6) #In Pycharm this graph will appear after you close the previous pop-up one
plt.title(" Boys to girls proportion", fontdict={'fontname': 'Comic Sans MS', 'fontsize': 15}) # Giving it a title
plt.xlabel("Year") # Adding a label to x-axis
plt.ylabel("Prop_boy_girl") #Adding a label to y-axis
plt.yticks(np.arange(1.04,1.06, step=0.005)) #Seeting values for axis. Note the use on numpy library
plt.xticks(np.arange(1935,2025, step=10))
plt.legend() # This allow the label of the curve to be plotted
plt.show()

# Printing data in df3 in descending order
print(df3.sort_values("Total", ascending=False)) # Note, as it is not saved it does not change the original
print(df3.head(5))                              # order as shown in the print of first 5 values
# More direct way to find maximum of births, year
# Get the maximum of total births and the from the index of that maximum the year of that same line
print("Maximum births is ", max(df3["Total"]), " in year ", df3["year"][df3["Total"].idxmax()])
