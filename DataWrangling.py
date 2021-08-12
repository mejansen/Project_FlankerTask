import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *

# colour codings:
# orange -> #FFA500
# blue -> #4F94CD


# import the needed data and turn Condition, as well as Block into a categorical value (helps with distinction in plots)
data = pd.read_csv("data/data.csv")
data["Block"] = data["Block"].astype("category")
data["Condition"] = data["Condition"].astype("category")
data["Response"] = data["Response"].astype("category")
data["StimVar"] = data["StimVar"].astype("category")

    
# removing outliers:
while True:
    # calculate the mean and standard deviation
    mean = np.mean(data["RT"])
    sd = np.std(data["RT"])

    # calculate z-values for all data points and append them in a separate column:
    rows, cols = data.shape
    data["z_value"] = np.zeros(rows)
    for row in data.itertuples(index = True, name = "Row"):
        index = row[0]
        value = row[6]
        data.at[index, "z_value"] = abs(value - mean)/ sd

    # find index of data point with largest z-value
    z_max = data["z_value"].idxmax()

    # check if said data point is an outlier
    if z_max > 3:
        # remove whiole line from the data
        data = data.drop(z_max)
    # stop if no more outliers are found
    else:
        break

# update the indices in the df and have a brief look at it:
rows, cols = data.shape
# indices = np.arange(rows)
data = data.set_index(np.arange(rows))


def bar():
    fig = (ggplot(data, aes(x = "RT"))
        + geom_histogram(binwidth = 50, color = "#FFA500", fill = "#FFA500", alpha = 0.4)
        + labs(
            x = "Reaction Time",
            y = "Number of Occurrences",
            title = "Distribution of Reaction Times"
        )
    ).draw()
    return fig
    
def violin():
    fig = (ggplot(data, aes(x='Block', y='RT')) 
         + geom_violin(fill = "#FFA500", color = "#FFA500", alpha = 0.4)
         + stat_summary(color = "#4F94CD")
         + labs(
             x = "Trial Block",
             y = "Reaction Time in ms",
             title = "Learning effect between blocks - mean Reaction Times shrink with practice"
         )
    ).draw()
    return fig

def scatter():
    fig = (ggplot(data, aes(x = "Onset", y = "RT", color = "Condition"))
         + geom_point()
         + geom_smooth(method = "lm", color = "black", se = False)
         + labs(
             x = "Onset in ms",
             y = "Reaction time in ms",
             title = "Reaction times depending on Condition plotted against stimulus onset"
         )
    ).draw()
    return fig

def stacked():
    data_block_one = data.loc[data['Block'] == 1]
    data_block_two = data.loc[data['Block'] == 2]
    congruent_one, incongruent_one = data_block_one.groupby('Condition')['RT'].mean()
    congruent_two, incongruent_two = data_block_two.groupby('Condition')['RT'].mean()
    std_congruent_one, std_incongruent_one = data_block_one.groupby("Condition")["RT"].std()
    std_congruent_two, std_incongruent_two = data_block_two.groupby("Condition")["RT"].std()

    dataframe = pd.DataFrame({"Block" : [1, 2],
                "RT_congruent" : [congruent_one, congruent_two],
                "std_congruent" : [std_congruent_one, std_congruent_two],
                "RT_incongruent" : [incongruent_one, incongruent_two],
                "std_incongruent" : [std_incongruent_one, std_incongruent_two]})


    fig, ax = plt.subplots(figsize = (9, 6))
    ax.bar([0.9, 1.9], 
        dataframe["RT_congruent"],
        label='Congruent',
        yerr = dataframe["std_congruent"], 
        color = "#FFA500",
        width = 0.2,
        alpha = 0.8)

    ax.bar([1.1, 2.1], 
        dataframe["RT_incongruent"], 
        label='Incongruent',
        yerr = dataframe["std_congruent"], 
        color = "#4F94CD", 
        width = 0.2, 
        alpha = 0.8)

    ax.set(
        xlabel = "Block",
        ylabel = "Mean Reaction Time",
        title = "Stacked Average Reaction Times between Practice Blocks of the Experiment"
    )
    ax.set_xticks([1, 2])
    ax.set_xticklabels(["Block 1", "Block 2"])
    ax.legend()
    
    

    return fig, ax

def lrm():
    #regression model!
    # prepare x and y:
    x = np.array(data["Onset"]).reshape(-1, 1)
    y = data["RT"]

    model_onset = LinearRegression().fit(x, y)

    # obtain the results:
    print('correlation coefficient:', model_onset.score(x, y))
    print('intercept:', model_onset.intercept_)
    print('slope:', model_onset.coef_)
    
    return






