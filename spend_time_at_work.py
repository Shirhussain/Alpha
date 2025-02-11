import matplotlib.pyplot as plt

activities = ['Coding', 'Learning and Research', 'Team Collaboration', 'Planning']
percentages = [55, 20, 15, 10]



plt.pie(percentages, labels=activities)
plt.title('Shir\'s Work Time')

plt.show()