import matplotlib.pyplot as plt

sea =  df[df["Country"].isin(["Philippines","Thailand","Indonesia","Myanmar","Laos","Vietnam","Brunei","Singapore","Malaysia","Cambodia", "Timor-Leste"])]

country = sea["Country"]
population = sea["Population (2020)"]

fig, ax = plt.figure(figsize=(16,9))

ax.barh(country, population)

ax.set_title("2020 Population by COunty (SEA)", loc="center")

#removes axes splines
for s in['top', 'buttom', 'left', 'right']:
    ax.spinse[s].set_visible(Fales)
    
    #add annotations to bar
for i in ax.patches:
    plt.text(i.get_width() + 0.2, i.get_y() + 0.5, str(round((i,get_width()),2)), fontsize=10, fontweight="bold", color="grey")
    
    #removes x, y thicks
ax,xasis.set_ticks_position("none")
ax,yasis.set_ticks_position("none")

# plt.barh(country, population)
#Add paading and spaces between axes and labels
ax.xaxis.set_tick_params(pad=5)
ax.yaxis.set_tick_params(pad=10)

#add x and y gridlines
ax.grid(b=True, color="grey", linestyle="-.", linewidth=0.5, alpha=0.2)

ax.invert_yaxis
