#graph using python
import matplotlib.pyplot as plt
x=['Maths','English', 'Science','Nepali','Social','Population']
y1=[90,87,69,64,34,12]
y2=[92,89,71,66,36,14]
y3=[93,87,59,64,38,12]
y4=[100,89,71,74,36,14]

plt.plot(x,y1,label="Rabin",color=g)
plt.plot(x,y2,label="Kabita")
plt.plot(x,y3,label="Arbin")
plt.plot(x,y4,label="Harsit")
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.title('Marks Graphs')
plt.legend()
plt.show()