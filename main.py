import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics 
import random
import pandas as pd
import csv

df = pd.read_csv("studentMarks.csv") 
data = df["Math_score"].tolist()

def random_set_of_means(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean
    
mean_list = []
for i in range(0, 1000):
    set_of_means = random_set_of_means(100)
    mean_list.append(set_of_means)
    
std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)

print("Mean is ", mean)
print("Standard Deviation is ", std_deviation)

fig = ff.create_distplot([data],["Maths Scores"],show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean], y = [0,0.20], mode = "lines", name="MEAN"))
fig.show()
