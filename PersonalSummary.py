# importing the packages necessary
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *
from expyriment import misc


# for more explanation on z-method and what is done in this section, see DataSummary.py
def clean(data):
    """This function cleans the data handed to it via z-method and returns it with correct indexing."""
    while True:
        mean = np.mean(data["RT"])
        sd = np.std(data["RT"])
        rows, cols = data.shape
        data["z_value"] = np.zeros(rows)
        for row in data.itertuples(index = True, name = "Row"):
            index = row[0]
            value = row[6]
            data.at[index, "z_value"] = abs(value - mean)/ sd
        z_max = data["z_value"].idxmax()
        if data.at[z_max, "z_value"] > 3:
            data = data.drop(z_max)
        else:
            break
    rows, cols = data.shape
    data = data.set_index(np.arange(rows))

    return data


def create_datasets(tidy = True):
    # import official data and turn Condition, Response, StimVar, as well as Block into a categorical value (for usage in plots)
    data_general = pd.read_csv("data/data.csv")
    data_general["Block"] = data_general["Block"].astype("category")
    data_general["Condition"] = data_general["Condition"].astype("category")
    data_general["Response"] = data_general["Response"].astype("category")
    data_general["StimVar"] = data_general["StimVar"].astype("category")
    
    # in case the user wants to be shown his own data without having run the experiment, there will be an error raised
    try:
        misc.data_preprocessing.write_concatenated_data("./data", "menu_01.xpd", output_file = "data_converted.csv")  # converting the log-file to csv-format:
        df = pd.read_csv("data_converted.csv")    # reading the dataframe
        df.to_csv(path_or_buf = "data_converted.csv")   # rewrite the csv-file
        data_specific = pd.read_csv("data_converted.csv")   # re-read the csv-file
        data_specific.columns = data_specific.iloc[0]   # reset the column names
        data_specific = data_specific[1:]   # exclude the first column
        
        # change the d.types of the variables to make working with it feasible
        data_specific = data_specific.astype({"subject_id": 'int32'})
        data_specific = data_specific.astype({"Response": 'int32'})
        data_specific = data_specific.astype({"StimVar": 'int32'})
        data_specific = data_specific.astype({"Onset": 'int32'})
        data_specific = data_specific.astype({"RT": 'int32'})
        data_specific = data_specific.astype({"Block": 'int32'})

        # make some variables categorical to enable better working 
        data_specific["Block"] = data_specific["Block"].astype("category")
        data_specific["Condition"] = data_specific["Condition"].astype("category")
        data_specific["Response"] = data_specific["Response"].astype("category")
        data_specific["StimVar"] = data_specific["StimVar"].astype("category")
        
        # check whether to call upon cleaning the datasets
        if tidy:
            data_general = clean(data_general)
            data_specific = clean(data_specific)

        return data_general, data_specific
    
    # if there is an error during the execution of the code, raise a FileNotFound-error
    except:
        raise Exception(u"No data files found. Please run the experiment first.")
    
    return



def rt_plots(data_general, data_specific):
    """This function constructs two plots in the same manner, but binding a different data set to each version."""
    # first plot: uses the official dataset
    fig_general = (ggplot(data_general, aes(x = "RT"))
        + geom_histogram(binwidth = 50, color = "#FFA500", fill = "#FFA500", alpha = 0.4)
        + labs(
            x = "Reaction Time",
            y = "Number of Occurrences",
            title = "Distribution of Reaction Times"
        )
    ).draw()
    # second plot: uses the participant's data
    fig_specific = (ggplot(data_specific, aes(x = "RT"))
        + geom_histogram(binwidth = 10, color = "#FFA500", fill = "#FFA500", alpha = 0.4)
        + labs(
            x = "Reaction Time",
            y = "Number of Occurrences",
            title = "Distribution of Reaction Times"
        )
    ).draw()
    return fig_general, fig_specific

def violin(data_general, data_specific):
    """This function created a violin plot with the general data as it is also done in DataSummary.py and scatters the individual data points on top."""
    # apart from one line, the code is exactly the same as in DataSummary.ipynb
    fig = (ggplot(data_general, aes(x='Block', y='RT')) 
     + geom_violin(fill = "#FFA500", color = "#FFA500", alpha = 0.4)
     + stat_summary(color = "#4F94CD")
     + geom_jitter(data = data_specific, color = "red") # jitters the participant's data points over the plot
     + labs(
         x = "Trial Block",
         y = "Reaction Time in ms",
         title = "Learning effect between blocks - mean Reaction Times shrink with practice"
     )
    ).draw()
    
    return fig

def merge_datasets():
    """In case the user wants to contribute their data, this function will be called upon by the corresponding button."""
    data_general, data_specific = create_datasets(tidy = False)
    
    # criterions for data_general
    rows_g, cols_g = data_general.shape
    rowGeneral = (rows_g >= 1248)
    colGeneral = (data_general.columns == ["SubjectID", "Response", "StimVar", "Condition", "Onset", "RT", "Block"]).all()
    
    data_specific = data_specific.rename(columns = {"subject_id" : "SubjectID"})
    # criterions for data_specific:
    rows_s, cols_s = data_specific.shape
    rowSpecific = (rows_s == 48)
    colSpecific = (data_specific.columns == ["SubjectID", "Response", "StimVar", "Condition", "Onset", "RT", "Block"]).all()
    
    #prepare second dataset:
    last_subject = data_general.at[rows_g - 1, "SubjectID"]
    data_specific["SubjectID"] = last_subject + 1
    
    # check, whether all criterions are met before merging
    if rowGeneral & colGeneral:
        if rowSpecific & colSpecific:
            # append the data from second df:
            data_combined = data_general.append(data_specific)
            data_combined = data_combined.set_index(np.arange(rows_g + rows_s))
            data_combined.to_csv(path_or_buf = "data/data.csv")
        else:
            print("There must have been a mistake with your experiment data. Try again")   # error message, if there is sth wrong with the participant's file
    else:
        print("There is a problem with the general data file. Try again")   # error message, if there is sth wrong with the data collection
        
    print("Thank you for contributing your data!")
    
    return
