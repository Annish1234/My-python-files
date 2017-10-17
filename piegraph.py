import matplotlib.pyplot as plt
 
# defining labels
activities = ['Mechanical', 'Information Technology', 'Eletronics', 'Biotechnology']
 
# portion covered by each label
slices = [5, 2, 8, 6]
 
# color for each label
colors = ['g', 'r', 'b', 'm']
 
# plotting the pie chart
plt.pie(slices, labels = activities, colors=colors, 
        startangle=90, shadow = True, explode = (0, 0, 0.1, 0),
        radius = 1.33, autopct = '%1.1f%%')
 
# plotting legend
plt.legend()
 
# showing the plot
plt.show()