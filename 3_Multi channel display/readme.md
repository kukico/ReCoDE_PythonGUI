## Python GUI programming Day 3
With what you have learned from Day2, you can create a GUI that displays multiple channels of data. The widget we need is plotting widget, which is used to display the data.

### **Create three channels based on single channel in Day2**
The only change we need to make is to add more plot widgets to the GUI. The code is the same as Day2. We just need to add more plot widgets to the GUI. Usually we dulinicate the code for one plot widget and change the name of the widget. However, this can make the codes look messy. A better way is to use a loop to create the widgets. In order to use a loop, we need to use ```zip``` function. The ```zip``` function is used to combine two lists. For example, if we have two lists, ```list1 = [1,2,3]``` and ```list2 = [4,5,6]```, we can use ```zip``` function to combine them into a list of tuples: ```[(1,4),(2,5),(3,6)]```. By doing so, you can index the first element of each tuple by ```[0]``` and the second element by ```[1]```. That's it. One more thing before you proceed is that you need to genete data for each channel. The code is shown in ```Python_GUI_day3_simple.py```.

### **Display data of three channels from file**
Now try to display the data in three channles from the file you processed in Day 2. There are three channels in the file. You can use the following code to read the data from the file:
```python
filename = 'Data/charis4.dat'
with open(filename, 'rb') as datafile:
    data = np.fromfile(datafile, np.dtype('int16'))
ABP  = (data[0::3]+2644)/91.5061
ECG  = (data[1::3]+392)/6081.8245    
ICP  = (data[2::3]+5)/84.0552
```

The full codes are shown in ```Python_GUI_day3_file.py```. Try to code by yourself before you check the codes.