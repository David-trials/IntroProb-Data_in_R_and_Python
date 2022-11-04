# David Aurelio
# Converting "Introduction to R and RSTudio" to Python
# Done using PyCharm. Note the imported data files were placed in the project directory for easy import.

# Note: R uses the following libraries:
# statsr: for data files and functions used in statistical analysis. Maybe standard Python library is enough...?
# dplyr: for data wrangling. Usage of lists along with the math library should be enough to manipulate data in Python
# ggplot2: for data vizualization. Note: these are the most common in Python: numpy, pandas, matplotlib


import pandas as pd # Pandas allows CSV file import into a dataframe (df), among other tools
import matplotlib.pyplot as plt # Allows plotting of graphs
import numpy as np # Very useful library to work with arrays

#Importing the data about NYC flights
dfnycflg = pd.read_csv("test_nycflights.csv") # File is in project directory so no path needed

# A way to see the dimensions of the data passed to test2 #
print(len(dfnycflg.columns)) #Prints number of columns df
print(len(dfnycflg))   # Prints number of rows in df
print(dfnycflg.head(3)) #see only first 3 lines of the data

# Viewing the names of the variable on the dataframe
print(dfnycflg.columns)

print("--- Plotting histograms of dep_delay data ---")
#Plotting the distrubition of departure delays in a hystogram
plt.hist(dfnycflg.dep_delay) #Note: Default bins=10
plt.hist(dfnycflg["dep_delay"], color="violet", bins=11) #Alternative to dfnycflg.dep_delay
plt.show()
#Adjusting the hystogram to better see the distribution
bins = [-20,0,20,40,60,80,100,120,140,160,180,200,220] #Making a list of values for my x-axis hystogram
plt.hist(dfnycflg.dep_delay, bins=bins)
plt.xticks(bins) # values defined in list bins for the x-axis
plt.title("Delayed flights Hystogram", fontdict={'fontname': 'Comic Sans MS', 'fontsize': 15}) # Giving it a title
plt.ylabel("Number of delayed flights") # Adding a label to x-axis
plt.xlabel("Minutes of delay.(Negative times are early than expected flights)") #Adding a label to y-axis
plt.show()
#Alternatively, one can use the numpy librarly for ease in seeting the axis values
bins2 = np.arange(-20,220, step=20) #using numpy
plt.hist(dfnycflg.dep_delay, bins=bins2, color="red")
plt.xticks(bins2) # values defined in list bins for the x-axis
plt.title("Delayed flights Hystogram", fontdict={'fontname': 'Comic Sans MS', 'fontsize': 15}) # Giving it a title
plt.ylabel("Number of delayed flights") # Adding a label to x-axis
plt.xlabel("Minutes of delay.(Negative times are early than expected flights)") #Adding a label to y-axis
plt.show()
#Very samall bin width example
plt.hist(dfnycflg.dep_delay, bins=100, range =(-20,220),  color="green")# Note:Defining a specific range, no effect on bins.
plt.xticks([-20,20,80,140,220]) # values defined in list bins for the x-axis
plt.title("Small bin example") # Giving it a title
plt.ylabel("Number of delayed flights") # Adding a label to x-axis
plt.xlabel("Minutes of delay.") #Adding a label to y-axis
plt.show()

#Plotting the histogram delays just for the destination RDU.
print("--- For desitnation RDU only ---")
rdu_flights = dfnycflg.loc[dfnycflg["dest"]=="RDU"]# This acts as a filter. Look at column "dest" for the equals to RDU
print(rdu_flights["dest"].head(5)) #Showing just the top 5 destinations to prove that all data is for dest==RDU
print(rdu_flights.head(5)) #Prints the first 5 rows having just the RDU destination
print("Length of RDU data: ",len(rdu_flights)) #To see length of the data just of the RDU flights

plt.hist(rdu_flights.dep_delay, bins=26, color="cyan")
plt.title("Delayed flights to RDU", fontdict={'fontname': 'Comic Sans MS', 'fontsize': 15}) # Giving it a title
plt.ylabel("Number of delayed flights") # Adding a label to x-axis
plt.xlabel("Minutes of delay.\n(Negative->early than expected.)") #Adding a label to y-axis
plt.show()
#Pritting numerical statistical summary for just the RDU flights
print(rdu_flights.describe())
print("Or as shown in R program: \n Mean    std     n   \n", rdu_flights["dep_delay"].mean(),rdu_flights["dep_delay"].std(),len(rdu_flights))

#Now filtering for destination and month.
print("--- For desitnation SFO and February only ---")
sfo_flights = dfnycflg.loc[ (dfnycflg["dest"]=="SFO") & (dfnycflg["month"]==2)] #Two conditional for the ".loc" into the dataframe
print(sfo_flights[["dest","month"]].head(3))# Showing just top 3 wtih only SFO for month 2
print(sfo_flights.head(3))# Showing top 3 of all data in this dataframe
print("Length of  data dest=SFO for just february: ", len(sfo_flights))

#Histogram and summary statistics for arrival delays of sfo_flights february created previously
print("---Making histogram and summary statistics for SFO debruary data---\n **Arrival delays**")
plt.hist(sfo_flights.arr_delay, bins=26, color="gray", label='SFO_feb_arr-dly')
plt.title("Arrival delay SFO", fontdict={'fontname': 'Comic Sans MS', 'fontsize': 15}) # Giving it a title
plt.ylabel("Number of delayed flights") # Adding a label to x-axis
plt.xlabel("Minutes of delay.\n(Negative->early than expected.)") #Adding a label to y-axis
plt.legend() # This allow the label of the curve to be plotted
plt.show()
#Pritting numerical statistical summary for SFO
print(sfo_flights.describe())
print("As in R program for SFO: \n Mean    std      median    IQR    n   \n",
      sfo_flights["arr_delay"].mean(),sfo_flights["arr_delay"].std().round(3),sfo_flights["arr_delay"].median(),
      sfo_flights["arr_delay"].quantile(0.75)-sfo_flights["arr_delay"].quantile(0.25),len(sfo_flights)) #Note: Rounding std to 3 decimals.

#Gouping data by origin. Back to the RDU dataframe
print("--- Grouping and simple summary of RDU by its origin flights. ---")
print("Simple summary:\n Mean   std     num. elements\n",
      rdu_flights.groupby(["origin"])["dep_delay"].agg(["mean","std","count"]))
#Note on last line: Using pandas the dataframe is grouped by its origin for the dep_delay variable
#also .agg is used to aggregate the caculation for those grouped parameters of the mean, std and number of elements of each origin group.

#For the SFO-february determine median and IQR for arr_delay
print("")#Print empty line
print("For SOF-february arr_delay by carrier:\n             IQR  \n ",
      sfo_flights.groupby(["carrier"])["arr_delay"].quantile(0.75) -
      sfo_flights.groupby(["carrier"])["arr_delay"].quantile(0.25) )
print("\n ",sfo_flights.groupby(["carrier"])["arr_delay"].agg(["median","count"])) #Easier to make two separate prints for IQR  and median+count

#Which has the highest average delay departying from NYC airport?
print("")#Print empty line
print("--- NYC flights grouping by month and finding mean dep_delay in descending order ---")
df_month_mean = dfnycflg.groupby(["month"])["dep_delay"].agg(["mean"]) #Finding the mean for each month and saving it to a different dataframe
print(df_month_mean.sort_values(by="mean", ascending=False) ) #Printing and organizing the data in descending order.
#Now for the median
print("")#Print empty line
print("--- NYC flights grouping by month and finding median dep_delay in descending order ---")
df_month_median = dfnycflg.groupby(["month"])["dep_delay"].agg(["median"]) #Finding the mean for each month and saving it to a different dataframe
print(df_month_median.sort_values(by="median", ascending=False) ) #Printing and organizing the data in descending order.

#Using box plots to compare departure delays on each month.
print("")#Print empty line
print("--- Comparying box plots of dep_delays ---")
month1= dfnycflg.loc[dfnycflg["month"]== 1]["dep_delay"] #Test, selecting just the dep_delay fro month 1
print(month1.head(3))

#Creating a new dataframe where each column is the month of the year with the dep_delays for that month.
#Note: Since the columns have different sizes I used pd.concat so the df frame as the same size on all columns
# filling the empty spaces with NaN
mth = pd.concat([dfnycflg.loc[dfnycflg["month"]== 1]["dep_delay"],dfnycflg.loc[dfnycflg["month"]== 2]["dep_delay"]
                 ,dfnycflg.loc[dfnycflg["month"]== 3]["dep_delay"],dfnycflg.loc[dfnycflg["month"]== 4]["dep_delay"]
                 ,dfnycflg.loc[dfnycflg["month"]== 5]["dep_delay"],dfnycflg.loc[dfnycflg["month"]== 6]["dep_delay"]
                 ,dfnycflg.loc[dfnycflg["month"]== 7]["dep_delay"],dfnycflg.loc[dfnycflg["month"]== 8]["dep_delay"]
                 ,dfnycflg.loc[dfnycflg["month"]== 9]["dep_delay"],dfnycflg.loc[dfnycflg["month"]== 10]["dep_delay"]
                 ,dfnycflg.loc[dfnycflg["month"]== 11]["dep_delay"],dfnycflg.loc[dfnycflg["month"]== 12]["dep_delay"]], axis=1)

print(mth.head())
print(mth.columns) #Let's change the name of the columns since they are all dep_delay at this point.
mth.columns = [ "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dec"] # Renames columns with desired month abbreviation
print(mth.head())
test = mth["Jan"][~np.isnan(mth["Jan"])] #Removing the NaN values of the coulmn "Jan" test
print(test)
#Removing all nan values from the coulmns and making the side by side box plot of all months data of dep_delay
plt.boxplot( [ mth["Jan"][~np.isnan(mth["Jan"])],mth["Feb"][~np.isnan(mth["Feb"])]
               ,mth["Mar"][~np.isnan(mth["Mar"])],mth["Apr"][~np.isnan(mth["Apr"])]
               ,mth["May"][~np.isnan(mth["May"])],mth["Jun"][~np.isnan(mth["Jun"])]
               ,mth["Jul"][~np.isnan(mth["Jul"])],mth["Ago"][~np.isnan(mth["Ago"])]
               ,mth["Sep"][~np.isnan(mth["Sep"])],mth["Oct"][~np.isnan(mth["Oct"])]
               ,mth["Nov"][~np.isnan(mth["Nov"])],mth["Dec"][~np.isnan(mth["Dec"])]] )
plt.xlabel("Month") # Adding a label to x-axis
plt.ylabel("Dep-delay") #Adding a label to y-axis
plt.show()

#Classifying flight as on time is delayed by less than 5 minutes
print(" ")
print("--- On time departure rate for NYC airports")
print(dfnycflg.columns) #Current columns
# Adding to a data frame a new column with a TRUE boolean variable if that year more boys were born
dep_type=["Dep_Time"] #Creating a list to save departure type on_time or delayed. The index o contains str "Dep_Time"
for i in range(1,len(dfnycflg)+1): # Loop to run through all rows of the dataframe
    val = dfnycflg["dep_delay"][i]
    if val < 5:
        dep_type.append("on_time")
    else:
        dep_type.append("delayed")

df_dep_type = pd.DataFrame(dep_type) #Converting list to a dataframe to then add a new column to the dfnycflg
print(df_dep_type.head()) # Checking the first rows of the new dataframe
dfnycflg=dfnycflg.assign(DepTime=df_dep_type) #Adding/assigning a new column to the dataframe
print(dfnycflg.columns) #Current columns
print(dfnycflg[["month","dep_delay","DepTime"]])

print("\n --- Determining rate of on time flights in  descending order ---  ")
df_origin = dfnycflg.groupby(["origin"])["DepTime"].size()# alternative to .agg(["count"])
print("Airport origins tags and their total flights.\n", df_origin)

LGAcount, EWRcount,JFKcount = 0, 0 , 0 #Initializing each count variable at zero
#Determining the on time rate for NYC origin flights
for i in range(1,len(dfnycflg)+1): # Loop to run through all rows of the dataframe
    if dfnycflg["origin"][i] == "LGA" and dfnycflg["DepTime"][i] == "on_time":
        LGAcount += 1
    if dfnycflg["origin"][i] == "EWR" and dfnycflg["DepTime"][i] == "on_time":
        EWRcount += 1
    if dfnycflg["origin"][i] == "JFK" and dfnycflg["DepTime"][i] == "on_time":
        JFKcount += 1

df_ot_dep_rate = pd.DataFrame(df_origin) #Datframe to save the ontime data and then rate
df_ot_dep_rate = df_ot_dep_rate.assign( OnTimeCount=[EWRcount,JFKcount,LGAcount]) # Adding to the df the size of flights per origin and their ontime count
print(df_ot_dep_rate) # Look at current df
df_ot_dep_rate["Rate"] = df_ot_dep_rate.iloc[:,1] / df_ot_dep_rate.iloc[:,0]#Determining the Rate by accessing the correct df columns through index and adding the column Rate
print("\nRate of on time flights\n",df_ot_dep_rate.sort_values(by="Rate", ascending=False)) #Printing the df in descending order

#Segmented barplot of the on time departure rate
plt.bar(df_ot_dep_rate.index,df_ot_dep_rate["OnTimeCount"], color="orange")
plt.bar(df_ot_dep_rate.index,df_ot_dep_rate["DepTime"] - df_ot_dep_rate["OnTimeCount"],color="blue",bottom=df_ot_dep_rate["OnTimeCount"]) #bottom to stack on top of that data
plt.xlabel("Airport")
plt.ylabel("Number of flights")
plt.legend(["On time", "Delayed"])
plt.show()

#Determining the airplane with highest average speed
print("\n --- Plane with highest average speed determination ---")
dfnycflg = dfnycflg.assign(AveSpeed=dfnycflg["distance"]/(dfnycflg["air_time"]/60)) #Adding column with average speed in mph
print(dfnycflg[["tailnum","AveSpeed"]].head()) #Showing just the first 5 elements of just the columns "tainnum" and "AveSpeed"
print(dfnycflg[["tailnum","AveSpeed"]].sort_values(by="AveSpeed", ascending=False).head())# now sorting it in descending order

#Scatter plot
print("--- Scatter plot of avg-distance vs distance ---")
plt.scatter(dfnycflg["distance"],dfnycflg["AveSpeed"])
plt.xlabel("Distance in miles")
plt.ylabel("Ave. speed in mph")
plt.show()

#Data to determine if flights arrive on time
print("--- Arrival time data ---")
arr_type=["Arr_Time"] #Creating a list to save arrival type on_time or delayed.
ot_count = 0 #For later calculation of ontime rate
for i in range(1,len(dfnycflg)+1): # Loop to run through all rows of the dataframe
    if dfnycflg["arr_delay"][i] <= 0:
        arr_type.append("on_time")
        ot_count +=1 #For later calculation of ontime rate
    else:
        arr_type.append("delayed")

df_arr_type = pd.DataFrame(arr_type) #Converting list to a dataframe to then add a new column to the dfnycflg
print(df_arr_type.head()) # Checking the first rows of the new dataframe
dfnycflg=dfnycflg.assign(ArrTime=df_arr_type) #Adding/assigning a new column to the dataframe
print(dfnycflg.columns) #Current columns
print(dfnycflg[["month","arr_delay","ArrTime"]]) #printing to check results
print("Rate of on time arrivals " , round(ot_count/len(dfnycflg),7)) # Determining the rate and showing with 7 decimals

print(" --- Fraction that departed delayed but arrived on time ---")
N_depDly = sum( df_ot_dep_rate["DepTime"] - df_ot_dep_rate["OnTimeCount"]) #Number of delayed DEPARTURES
N_arrOT = ot_count #Number of on time ARRIVALS
print("Number of delayed departures: ", N_depDly ,
      "\nNumber of on time arrivals: ",  N_arrOT )
#Determining delayed and on time number of flights
N_dpDly_arrOT = 0
for i in range(1,len(dfnycflg)+1): # Loop to run through all rows of the dataframe
    if dfnycflg["DepTime"][i] == "delayed" and dfnycflg["ArrTime"][i] == "on_time":
        N_dpDly_arrOT +=1

print("Proportion of delayed flights that arrived on time: ", round(N_dpDly_arrOT/N_depDly,7))