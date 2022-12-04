import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Reading the data
    df1 = pd.read_csv("/Users/riad_rustum/Desktop/Data_for_diagram/4-15.csv", encoding='UTF-8', sep=';')
    df2 = pd.read_csv("/Users/riad_rustum/Desktop/Data_for_diagram/4-16.csv", encoding='UTF-8', sep=';')
    df3 = pd.read_csv("/Users/riad_rustum/Desktop/Data_for_diagram/4-14.csv", encoding='UTF-8', sep=';')

    # Sorting the data
    df1 = df1.sort_values(ignore_index=True, by="MinFeret")
    df2 = df2.sort_values(ignore_index=True, by="MinFeret")
    df3 = df3.sort_values(ignore_index=True, by="MinFeret")

    # Getting MineFeret and Circ together
    feret_circ_df1 = df1.loc[:, ('MinFeret', 'Circ.')]
    feret_circ_df2 = df2.loc[:, ('MinFeret', 'Circ.')]
    feret_circ_df3 = df3.loc[:, ('MinFeret', 'Circ.')]

    # creating zero rows
    zero_list = []
    for i in range(1, (feret_circ_df1.shape[1] + 1)):
        i = 0
        zero_list.append(i)
    print(zero_list)

    feret_circ_df1.loc[0] = zero_list
    feret_circ_df2.loc[0] = zero_list
    feret_circ_df3.loc[0] = zero_list

    # creating the count column
    column_values_df1 = []
    for i in range(len(feret_circ_df1.index)):
        column_values_df1.append(i)

    column_values_df2 = []
    for i in range(len(feret_circ_df2.index)):
        column_values_df2.append(i)

    column_values_df3 = []
    for i in range(len(feret_circ_df3.index)):
        column_values_df3.append(i)

    feret_circ_df1['count'] = column_values_df1
    feret_circ_df2['count'] = column_values_df2
    feret_circ_df3['count'] = column_values_df3

    # Creating the procent column
    last_value_index_df1 = feret_circ_df1['count'].iat[-1]
    last_value_index_df2 = feret_circ_df2['count'].iat[-1]
    last_value_index_df3 = feret_circ_df3['count'].iat[-1]

    feret_circ_df1["procent"] = (feret_circ_df1["count"] / last_value_index_df1)
    feret_circ_df2["procent"] = (feret_circ_df2["count"] / last_value_index_df2)
    feret_circ_df3["procent"] = (feret_circ_df3["count"] / last_value_index_df3)

    # Converting the data to float again
    feret_circ_df1["MinFeret"] = feret_circ_df1["MinFeret"].str.replace(",", ".").astype(float)
    feret_circ_df1["Circ."] = feret_circ_df1["Circ."].str.replace(",", ".").astype(float)

    feret_circ_df2["MinFeret"] = feret_circ_df2["MinFeret"].str.replace(",", ".").astype(float)
    feret_circ_df2["Circ."] = feret_circ_df2["Circ."].str.replace(",", ".").astype(float)

    feret_circ_df3["MinFeret"] = feret_circ_df3["MinFeret"].str.replace(",", ".").astype(float)
    feret_circ_df3["Circ."] = feret_circ_df3["Circ."].str.replace(",", ".").astype(float)

    # And finally plotting the data

    # make an own Diagramm
    f, ax = plt.subplots(1)
    # plotting
    ax.plot(feret_circ_df1["MinFeret"], feret_circ_df1["procent"])
    ax.plot(feret_circ_df2["MinFeret"], feret_circ_df2["procent"])
    ax.plot(feret_circ_df3["MinFeret"], feret_circ_df3["procent"])
    # Setting to start with 0
    ax.set_ylim(ymin=0)
    ax.set_xlim(xmin=0)
    # getting rid of the Ticks
    ax.tick_params(left=False, bottom=False)
    # gettin ride of the Axes
    for border in ['right', 'top']:
        ax.spines[border].set_visible(False)
    # set ticks range
    ax.set_xticks([0, 0.5, 1.0, 1.5, 2.0, 2.5, 3])
    ax.set_yticks([0.25, 0.5, 0.75, 1])
    # changing the colors of x and y
    ax.tick_params(axis='x', colors='grey')
    ax.tick_params(axis='y', colors='grey')
    # grids
    ax.grid(True)
    # ax.xaxis.grid(True)
    # ax.yaxis.grid(True)

    # setting texts
    ax.legend(['15', '16', '14'])
    ax.xaxis.set_label_text('Partikelgröße χ in mm')
    ax.yaxis.set_label_text('Summenverteilung Q₁ in %')

    # show the Diagram
    plt.show()




