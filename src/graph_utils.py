import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def create_two_bar_graph(a, b, x_pos, x_tick_labels="", title="", x_label="", y_label="", c=pd.Series(), width=0.35, tick_num=55,
                         a_legend="", b_legend="", c_legend="", autolabel1=False, autolabel1decimal=False, autolabel2=False):

    ind = np.arange(tick_num)  # the x locations for the groups
    bar_width = width  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x_pos, a, bar_width, color='tab:blue')
    rects2 = ax.bar(x_pos + bar_width, b, bar_width, color='tab:orange')

    # add some text for labels, title and axes ticks
    ax.set_title(title)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_xticks(ind + bar_width / 2)
    ax.set_xticklabels(x_tick_labels)

    # show extra plot (for rain)
    c_rects = None
    if not c.empty:
        c_rects = ax.plot(c, linewidth=2, color="turquoise")

    if (a_legend and b_legend and c_legend):
        ax.legend((rects1[0], rects2[0], c_rects[0]), (a_legend, b_legend, c_legend))
    elif (a_legend and b_legend):
        legend = ax.legend((rects1[0], rects2[0]), (a_legend, b_legend), loc='lower right', shadow=True)

    def autolabel(rects, decimal):
        # attach a text label above each bar displaying its height
        for rect in rects:
            height = rect.get_height()
            if (decimal):
                ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                        '%0.2f' % height,
                        ha='center', va='bottom', size=8, rotation=90)
            else:
                ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                        '%d' % int(height * 1000),
                        ha='center', va='bottom', size=8, rotation=90)

    if (autolabel1):
        autolabel(rects1, autolabel1decimal)
    if (autolabel2):
        autolabel(rects2)

    plt.show()

def dataframe_mean(df_list):
    mean_list = []
    for i in range(0, len(df_list[0])):
        local_mean = 0
        local_num = 0
        for x in range(0, len(df_list)):
            if (str(df_list[x][i]) != 'null'):
                local_mean = local_mean + float(str(df_list[x][i]).replace('−', '-'))
                local_num = local_num + 1
        if (local_num == 0):
            local_mean = 0
        else:
            local_mean = local_mean / local_num
        mean_list.append(local_mean)
    return pd.DataFrame(mean_list)