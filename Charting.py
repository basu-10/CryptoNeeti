import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
from DBase import Stats
from datetime import datetime
from matplotlib import style

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
style.use('fivethirtyeight')

xs = []
ys = []

def fill_values(coinname):
    global xs,ys
    
    
    dbobj = Stats()
    tb_name=str(datetime.now().strftime("tb_y%Y_m%m_d%d_%p"))
    
    searchtup=dbobj.search_in_tables(tb_name, 'market', coinname.upper())
    ts=(searchtup[0])[-1]
    dt_obj = datetime.fromtimestamp(ts)
    
    dt_= dt_obj.strftime('%a, %d-%h-%Y %-I%p %Mmins %Ssecs')
    print(f'\t: {searchtup[0]} \nfor remote server time: {dt_}')
    
       
    rows=searchtup
    
    for x in range(20): 
        buy_val=(rows[x])[-3]
        dt_val=(rows[x])[-1]
        
        dt_= datetime.fromtimestamp(dt_val).strftime('%a, %d-%h-%Y %-I%p %Mm %Ss')
        
        ys.append(buy_val)
        xs.append(dt_)
    '''
    print('value generated:')
    print(f'xs={xs}')
    print(f'ys={ys}')'''









# This function is called periodically from FuncAnimation
def animate(i):
    print()
    global xs,ys   
    
    coinanme='DOGEINR'
    
    fill_values(coinanme)
    
    
    print('creating chart with values:')
    print(xs)
    print(ys)
    
    xs.reverse()

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)
    
   
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title(f'value of {coinanme}')
    plt.ylabel('Bids')
    
    xs,ys=[],[]
    
    print('Deleting old values')
    print(xs)
    print(ys)

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, interval=10000)
plt.show()

available = ['default'] + plt.style.available
#print(f'available  styles: {available}')
