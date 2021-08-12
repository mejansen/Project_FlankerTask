import panel as pn
import FlankerExperiment
import DataWrangling
import PersonalSummary

# button texts -> primary panel
EXPERIMENT_TEXT = "Run the FLanker Task experiment and collect your own data points"
DATA_ANALYSIS = "Have a glimpse at some plots constructed with the yet collected data"
PERSONAL_RESULTS = "Look at plots using the data you collected yourself or contribute data points to the collection"

# button texts -> secondary panel
BAR_PLOT = "Look at the basic distribution of reaction times"
VIOLIN_PLOT = "Is there maybe an effect of practice between blocks? Reaction Times distributed according to their block affiliation"
SCATTER_PLOT = "Let's just scatter all reaction times and see what happens..."
STACKED_BARPLOT = "We have some average reaction times in comparison for you here"
CONTRIBUTION = "Help us update our data collection with your results and click here, to contribute your data!"

# plot texts -> general data analysis
BAR = "As we can see, most of the reaction times are concentrated on an interval between 450 and 700ms. The average reaction time is located in this interval. It can be seen, that there are still a few quite fast outliers to the lower end of the plot und some reaction times even exceed 1 second."
VIOLIN_ONE = "Since we have several blocks, there could be an effect of practice."
VIOLIN_TWO = "The summary statistic (blue point in the middle) is slightly lower for block two which indicates an effect of practice between the two blocks. It is not possible to say though that this may not only be due to growing accustomed to the setting. It is further possible to see that the violin for block one s slightly wider on top, while block two pulls further towards the quicker reaction times on the bottom. Overall, we can definitely see an increase of speed over the course of the two blocks."
SCATTER_ONE = "Including a wider variety of data into the plots can be helpful to find some value interactions."
STACKED_BAR_ONE = "We want to see the relation between the mean reaction times of the two conditions (congruent and incongruent) distributed over the two practice blocks. In order to construct that, we first have to gain our data though."
STACKED_BAR_TWO = "We see that between the blocks, the average reaction times in the congruent condition do not differ significantly and so do the mean reaction times in both conditions in the second block. What differs though, are the mean reaction times in the incongruent condition between the two block. The average reaction time differs by nearly 100ms which means a significant increase of reaction speed in the second block that could be due to practice and habituation."

# plot texts -> specific data analysis
BAR_COMPARISON_TEXT = "Comparing reaction times is often quite a useful tool to see, where onself is at, but also to understand the results of a data analysis and see what is the mean / usual reaction time."
VIOLIN_COMPARISON_TEXT = "Below, you can see the basic violin plot that you can also have a glimpse at in the file DataSummary.ipynb. The red data points that are scattered all over, are from when you yourself ran the experiment on your local machine."

# defaults:
css = '''
.bk.panel-widget-box {
  border-radius: 5px;
  border: 1px black solid;
}
'''
pn.extension(raw_css=[css])

# primary panel:
button_1 = pn.widgets.Button(name = 'Experiment', button_type = 'success', height = 150)
button_2 = pn.widgets.Button(name = 'Visualize official data', button_type = 'primary', height = 150)
button_3 = pn.widgets.Button(name = 'Show my data in comparison', button_type = 'warning', height = 150)

# secondary panel:
button_2a = pn.widgets.Button(name = "Bar Plot", height = 75)
button_2b = pn.widgets.Button(name = "Violin Plot", height = 75)
button_2c = pn.widgets.Button(name = "Scatter Plot", height = 75)
button_2d = pn.widgets.Button(name = "Stacked Barplot", height = 75)

# secondary panel:
button_3a = pn.widgets.Button(name = "Bar Plot", height = 150)
button_3b = pn.widgets.Button(name = "Violin Plot", height = 150)
button_3c = pn.widgets.Button(name = "Contribute my Data", height = 150)

# functions defining the events that shall happen when clicking a button:
# primary panel ("homescreen", so to say):
def experiment(event):
    """Conducts the entire Flanker Task experiment."""
    FlankerExperiment.main()
def data_analysis(event):
    """Opens a secondary panel to choose which plot to show."""
    pn.serve(second_panel_general) 
def personal_data(event):
    """Opens a secondary panel to choose in which plot to see compared results."""
    pn.serve(second_panel_specific)
    
# secondary panel (for general data analysis):
def bar_plot(event):
    """Shows the bar plot that can also be seen in DataSummary.ipynb"""
    # save the figure returned by corresponding function
    fig = DataWrangling.bar()
    # create a new panel that is going to be served in a new tab
    mpl_pane = pn.Column(pn.pane.Matplotlib(fig, dpi = 480, tight = True), BAR)
    pn.serve(mpl_pane)
    
def violin_plot(event):
    """Shows the violin plot that can also be seen in DataSummary.ipynb"""
    fig = DataWrangling.violin()
    mpl_pane = pn.Column(VIOLIN_ONE, pn.pane.Matplotlib(fig, dpi = 480, tight = True), VIOLIN_TWO)
    pn.serve(mpl_pane)
    
def scatter_plot(event):
    """Shows the scatter plot that can also be seen in DataSummary.ipynb"""
    fig = DataWrangling.scatter()
    mpl_pane = pn.Column(SCATTER_ONE, pn.pane.Matplotlib(fig, dpi = 480, tight = True))
    pn.serve(mpl_pane)
    
def stacked_barplot(event):
    """Shows the stacked bar plot that can also be seen in DataSummary.ipynb"""
    fig, ax = DataWrangling.stacked()
    mpl_pane = pn.Column(STACKED_BAR_ONE, pn.pane.Matplotlib(fig, dpi = 480, tight = True), STACKED_BAR_TWO)
    pn.serve(mpl_pane)
def contribute(event):
    """Shows reseults of the linear model as they can also be seen in DataSummary.ipynb"""
    PersonalSummary.merge_datasets()
    
# secondary panel (for specific data analysis):
def bar_comparison(event):
    """Shows two bar plots summing up reaction time in a new panel."""
    data_general, data_specific = PersonalSummary.create_datasets()
    one, two = PersonalSummary.rt_plots(data_general, data_specific)
    mpl_pane = pn.Column(pn.Row(pn.pane.Matplotlib(one, dpi = 480), pn.pane.Matplotlib(two, dpi = 480)), BAR_COMPARISON_TEXT)
    pn.serve(mpl_pane)
    
def violin_comparison(event):
    """Shows plot with individual data points scattered over the plots for general data analysis."""
    data_general, data_specific = PersonalSummary.create_datasets()
    fig = PersonalSummary.violin(data_general, data_specific)
    mpl_pane = pn.Column(VIOLIN_COMPARISON_TEXT, pn.pane.Matplotlib(fig, dpi = 480))
    pn.serve(mpl_pane)
    

    
# define, which button activates which function:
button_1.on_click(experiment)
button_2.on_click(data_analysis)
button_3.on_click(personal_data)

# secondary panel:
button_2a.on_click(bar_plot)
button_2b.on_click(violin_plot)
button_2c.on_click(scatter_plot)
button_2d.on_click(stacked_barplot)

button_3a.on_click(bar_comparison)
button_3b.on_click(violin_comparison)
button_3c.on_click(contribute)

row = pn.pane.Str(background = "#FFF5EE", sizing_mode = "scale_both")

# static_text = pn.widgets.StaticText(name = "Static Text", value = "A string")

# setting the layouts in form of rows and cols (as on a checkerboard)
menue = pn.Column(pn.Row(button_1, EXPERIMENT_TEXT), 
                  pn.Row(button_2, DATA_ANALYSIS), 
                  pn.Row(button_3, PERSONAL_RESULTS),
                  css_classes = ["panel-widget-box"],
                  background = "#FFF5EE",
                  sizing_mode = "scale_both")

second_panel_general = pn.Column(pn.Row(button_2a, BAR_PLOT), 
                         pn.Row(button_2b, VIOLIN_PLOT), 
                         pn.Row(button_2c, SCATTER_PLOT),
                         pn.Row(button_2d, STACKED_BARPLOT),
                         css_classes = ["panel-widget-box"],
                         background = "#FFF5EE",
                         sizing_mode = "scale_both")


second_panel_specific = pn.Column(pn.Row(button_3a, BAR_PLOT), 
                         pn.Row(button_3b, VIOLIN_PLOT),
                         pn.Row(button_3c, CONTRIBUTION),
                         css_classes = ["panel-widget-box"],
                         background = "#FFF5EE",
                         sizing_mode = "scale_both")

pn.serve(menue)