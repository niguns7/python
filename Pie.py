import matplotlib.pyplot as plt 
Subjects=['Art','Science','Commerce','Others']
perc=[25,45,15,15]
ex=(0.1,0,0,0)
c=["r","g","b","g"]
plt.pie(perc,explode=ex,labels=Subjects,colors=c,autopct='%1.2f%%',shadow=True)
plt.axis('equal')
plt.title('Kabita Parajuli')
plt.show()