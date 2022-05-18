import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_sorting(array, generator):
    """Animate a sorting function by inputting an array and
    a generator function. This function displays an animated bar chart."""
    fig, ax = plt.subplots()
    rects = ax.bar(range(len(array)), array, align="edge")

    def animate(array, rects):
        for rect, val in zip(rects, array):
            rect.set_height(val)

    anim = FuncAnimation(fig, func=animate,
                        fargs=(rects,), frames=generator, interval=1,
                        repeat=False)
    
    plt.show()