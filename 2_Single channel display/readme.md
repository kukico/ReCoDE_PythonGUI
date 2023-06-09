## Python GUI programming Day 2
In this session we are going to create a GUI that displays a single channel of data. You will learn both how to plot data generated by program and how to plot data from file.

`Python_GUI_day2_simple.py` is the template to plot data generated by program in a single channel.

`Python_GUI_day2_file.py` is the template to plot data from file in a single channel.

The codes are modularized. You can copy the codes from the template and paste them to your own codes. The codes are explained in the following sections.

You have created a plot widgte that can show data statically. However, in most cases, we need to plot data dynamically. That is, the data is changing with time. In this case, we need to update the plot widget with new data. The function `start_dearpygui()` is used to start the GUI. However, it is a blocking function. That is, the program will be blocked at this function. Therefore, we cannot update the plot widget. Therefore, we are going to replace `start_dearpygui()` with a while loop. The while loop will keep running until the GUI is closed. The function `render_dearpygui_frame()` is used to update the GUI after we make updates to the widgets. 
```python
while dpg.is_dearpygui_running():
    ### function to update the plot widgets ###
    dpg.render_dearpygui_frame()
```

Now try to Design a GUI program with just one plot widget and display data dynamically. The codes are given in the following python files.
* `python_gui_day2_simple.py` is to plot data generated by program.
* `python_gui_day2_file.py` is to plot data from file.


### Steps for plot data generated by program
1. We will use the virtual enviroment created in Day1. Activate the environment using the following command:
```conda activate GUI```
2. Import libraries. In addition to Dearpygui imported in Day1, we need to import ```numpy``` library to generate data and read data from file. The ```numpy``` library is not a built-in Python module. Therefore, we need to install it. The command is as follows:
```python
conda install numpy
```
Then we can import ```numpy``` library.
```python
import numpy as np
```

3. Create a GUI window with a plot widget. The code is the same as Day1. Create a window using the window() function and copy the following code after ```with dpg.window()``` to create a plot widget to the window.
```python
 # The following codes create a plot widget
with dpg.plot(label="Line Series", height=300, width=400):
# optionally create legend
    dpg.add_plot_legend()
    # REQUIRED: create x and y axes
    dpg.add_plot_axis(dpg.mvXAxis, label="x")
    dpg.add_plot_axis(dpg.mvYAxis, label="y", tag="y_axis")
    # series belong to a y axis
    # you need to change datax and datay to your data
    dpg.add_line_series(datax, datay, label="0.5 + 0.5 * sin(x)", parent="y_axis") 
```
4. Create a function to generate data. 
```python
def update_series(j):
    cosdatax = []
    cosdatay = []
    for i in range(0, 500):
        cosdatax.append(i / 1000)
        cosdatay.append(0.5 + 0.5 * cos(50 * (i+j) / 1000))
```
5. Send the data to the plot widget for display. Here, we set the tag for the plot widgte as ```tag="series_tag```. Then we can use the tag to update the data in the plot widget. The code is as follows:
```python
dpg.set_value("series_tag", [cosdatax, cosdatay])
```
The full codes can be found in `python_gui_day2_simple.py`.

### **Steps for plot data from file**
The steps for plotting data from file are exactly the same as plotting data generated by program. The only difference is that we need to read data from file. We provide a sample data from CHARIS database. The data is from [PhysioNet](https://physionet.org/content/charisdb/1.0.0/). The CHARIS database contains multi-channel recordings of ECG, arterial blood pressure (ABP), and intracranial pressure (ICP) of patients diagnosed with traumatic brain injury (TBI). 

A record from Physionet comes with two files, one is data.hea and the other is data.dat. The data.hea file contains information about the data, so called header file. The data.dat file contains the data. The format of header file can be found in the [Documentation from Physionet](https://physionet.org/physiotools/wag/header-5.htm).  
In this example, we are going to use ADC gain (ADC units per physical unit) and ADC baseline from the header file. ADC gain is a floating-point number that specifies the difference in sample values that would be observed if a step of one physical unit occurred in the original analog signal. For example, the **ADC gain** for **ABP** is **91.5061**. Therefore, we need to divide the data by 91.5061 to get the real data. ADC baseline is surrounded by parentheses after ADC gain. The baseline is an integer that specifies the sample value corresponding to 0 physical units.  
For example, from charis4.hea we can find 91.5061(-2644)/mmHg for ABP. Therefore, we need to add 2644 and then divide the data by 91.5061 to get the real data, and the unit is mmHg.  
Another important parameter is sampling frequency, which is the number of samples per second. For example, the sampling frequency is **50 Hz** in this record (the third parameter in the first line). Therefore, the time interval between two samples is 1/50 = 0.02 s.


The following codes are used to read data from file:
```python
datafile =open(filename, 'rb')
dtype = np.dtype('int16')
data = np.fromfile(datafile,dtype)
# The data are stored in the following order: ABP,ECG,ICP
ABP  = [(data[i]+2644)/91.5061 for i in range(0, len(data), 3)]
ECG  = [(data[i]+392)/6081.8245 for i in range(1, len(data), 3)]
ICP  = [(data[i]+5)/84.0552 for i in range(2, len(data), 3)]
```
