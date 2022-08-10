import matplotlib.pyplot as plt
import numpy as np


file=open("datafisgal.txt","r")
data=file.readlines()
rad = np.pi/180
RA=[]
dec=[]
p=[]
d=[]
b=[]
l=[]
x=[]
y=[]
z=[]


for i in range(len(data)):
        RA.append(float(data[i].split()[3]))
        dec.append(float(data[i].split()[4]))
        p.append(float(data[i].split()[5]))

      
for i in range(len(data)):       
    d.append(1000/p[i])
    b.append(np.arcsin(-np.cos(dec[i]*rad)*np.sin(62.6*rad)*np.sin((RA[i]-282.25)*rad)+np.sin(dec[i]*rad)*np.cos(62.6*rad))/rad)
    l.append((np.arccos(np.cos(dec[i]*rad)*np.cos((RA[i]-282.25)*rad)/np.cos(b[i]*rad)))/rad+33.0)

for i in range(len(l)):
    x.append(d[i]*np.cos(b[i]*rad)*np.cos(l[i]*rad)-8.122)
    y.append(d[i]*np.cos(b[i]*rad)*np.sin(l[i]*rad))
    z.append(d[i]*np.sin(b[i]*rad))


fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.set_xlabel("X (pc)")
ax.set_ylabel("Y (pc)")
ax.set_zlabel("Z (pc)")
ax.set_title("Plot 3D Bintang Pada Bidang Galaksi")
ax.set_xlim(-200,200)
ax.set_ylim(-200,200)
ax.set_zlim(-200,200)
ax.scatter(x,y,z,s=0.00001)
plt.show()