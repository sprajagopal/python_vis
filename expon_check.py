import cmath
import math
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
import time

def expon_check(z, n):
    return (1 + z/n)**n

def plot_limits(z):
    reals = [1]
    imags = [0]
    plt.ion()
    fig = plt.figure()  # Create figure
    axes = fig.add_subplot(111) # Add subplot (dont worry only one plot appears)
    axes.set_autoscale_on(True) # enable autoscale
    axes.autoscale_view(True,True,True)
    p, = axes.plot(reals, imags, '-o')
    for i in range(1, 2000):
        ret = expon_check(z, i)
        reals.append(ret.real)
        imags.append(ret.imag)
        axes.annotate("{} + {}i".format(round(ret.real, 2), round(ret.imag, 2)), (ret.real, ret.imag))
        p.set_data(reals,imags)
        axes.relim()        # Recalculate limits
        axes.autoscale_view(True,True,True) #Autoscale
        plt.draw()
        fig.canvas.draw()
        fig.canvas.flush_events()
        time.sleep(0.002)
        
