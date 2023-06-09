# we will be using dearpygui library for GUI
# math is imported to generate data for plotting
import dearpygui.dearpygui as dpg
import math

# The following codes create two lists to store data for plotting
sindatax = []
sindatay = []

def print_me(sender, data):
    """ print the selected menu item
    This function is used to print the sender and data of the callback.
    Here the sender is the menu item and the data is the label of the menu item.
    When the user clicks a menu item, the callback function will be called and the
    sender and data will be passed to the callback function. The label of the menu item
    will be printed.
    Args:
        sender: the sender of the callback
        data: the data of the callback
    """
    print(sender, data)

def generate_data():
    """ generate_data
    This function is used to generate demo data for plotting.
    The data is generated using the following equation:
    y = 0.5 + 0.5 * sin(50 * x)
    """
    for i in range(0, 500):
        sindatax.append(i / 1000)
        sindatay.append(0.5 + 0.5 * math.sin(50 * i / 1000))

def create_window1():
    """ create a window
    This function is used to create a window
    This window contains several widgets like buttons, checkboxes, texts... 
	as well as an static plot to illustrate the capabilities of dearpygui.
	
	For each widget, parameter pos=[x,y] (x is the horizontal position and 
	y is the vertical position) can be used to set the position of the widget. 
	If not set, the widget will be placed automatically. In this case, the 
	radio button will be set below the checkbox widgets rather than side by side.
    """

    """
    In Python, the with statement is used for working with objects that support a context manager protocol. 
    It ensures that resources are properly managed and cleaned up when they are no longer needed. Here,
    the with statement is used to create a window and all the widgets added to the window will be automatically
    added to the window. The same for when you create a menu bar and plot widget.
    """
    with dpg.window(label="Window1", width=700, height=700,pos=[0,0]):
        # All the following widgets are added to Window1
        dpg.add_text("Text widget")
        dpg.add_button(label="Button widget")
        dpg.add_input_text(label="Input text widget", default_value="Input text box widgets")
        dpg.add_slider_float(label="Slider widget", default_value=0.273, max_value=1)
        dpg.add_text("Text widget")
        dpg.add_checkbox(label="Checkbox widget - option 1")
        dpg.add_checkbox(label="Checkbox widget - option 2")
        dpg.add_checkbox(label="Checkbox widget - option 3")
        """
        For each widget, parameter pos=[x,y] (x is the horizontal position and y is the vertical position)
        can be used to set the position of the widget. If not set, the widget will be placed automatically.
        In this case, the radio button will be set below the checkbox widgets rather than side by side.
        You can have a try by deleting the pos=[220,140] parameter.
        """
        dpg.add_radio_button(["Radio button widget - option 1", "Radio button widget - option 2", "Radio button widget - option 3"], horizontal=False,pos=[220,140])
    
        # The following codes create a plot widget
        with dpg.plot(label="Line Series", height=300, width=400):
        # optionally create legend
            dpg.add_plot_legend()
            # REQUIRED: create x and y axes
            dpg.add_plot_axis(dpg.mvXAxis, label="x")
            dpg.add_plot_axis(dpg.mvYAxis, label="y", tag="y_axis")
            # series belong to a y axis
            dpg.add_line_series(sindatax, sindatay, label="0.5 + 0.5 * sin(x)", parent="y_axis") 

def create_window2():
    """ create a window
    This function is used to create a window
    This window contains several widgets like buttons, checkboxes, texts... 
	as well as an static plot to illustrate the capabilities of dearpygui.
	
	For each widget, parameter pos=[x,y] (x is the horizontal position and 
	y is the vertical position) can be used to set the position of the widget. 
	If not set, the widget will be placed automatically. In this case, the 
	radio button will be set below the checkbox widgets rather than side by side.
    """

    """
    In Python, the with statement is used for working with objects that support a context manager protocol. 
    It ensures that resources are properly managed and cleaned up when they are no longer needed. Here,
    the with statement is used to create a window and all the widgets added to the window will be automatically
    added to the window. The same for when you create a menu bar and plot widget.
    """
    with dpg.window(label="Window2", width=700, height=700,pos=[700,0]):
        dpg.add_text("Text widget")

def create_menu_bar():
    """ create a menu bar
    This function is used to create a menu bar.
    The menu bar contains several menus, each menu contains several menu items.
    The menu can be considered as a container of menu items.
    """
    with dpg.viewport_menu_bar():
        with dpg.menu(label="File"):
            dpg.add_menu_item(label="Save", callback=print_me)
            dpg.add_menu_item(label="Save As", callback=print_me)

            with dpg.menu(label="Settings"):
                dpg.add_menu_item(label="Setting 1", callback=print_me, check=True)
                dpg.add_menu_item(label="Setting 2", callback=print_me)

        dpg.add_menu_item(label="Help", callback=print_me)

        with dpg.menu(label="Widget Items"):
            dpg.add_checkbox(label="Pick Me", callback=print_me)
            dpg.add_button(label="Press Me", callback=print_me)
            dpg.add_color_picker(label="Color Me", callback=print_me)

if __name__ == "__main__":
    # The following codes start the GUI
    # All dearpygui apps start with create_context()
    dpg.create_context()
    # The viewport is the window created by the operating system to display the GUI. 
    # The viewport is created using the create_viewport() function
    dpg.create_viewport(title='demonstration of dearpygui widgets', width=1000, height=700) 

    # The following codes are custom functions to create windows, menu bar and generate data for plotting
    generate_data()
    create_window1()
    create_window2()
    create_menu_bar()

    # The setup_dearpygui() function is used to setup the viewport.
    dpg.setup_dearpygui()
    # The viewport is shown using the show_viewport() function.
    dpg.show_viewport()
    #  The render loop is completely handled by the start_dearpygui() command.
    dpg.start_dearpygui()
    # All dearpygui apps end with destroy_context()
    dpg.destroy_context()