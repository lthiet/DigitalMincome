import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import mpld3
import seaborn as sns
sns.set()
matplotlib.use('Agg')

def plot(params):

    # Data for plotting
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + params['transaction_fee'] * np.sin(2 * np.pi * t)

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
        title='About as simple as it gets, folks')
    ax.grid()

    mpld3.save_html(fig,"app/templates/plot.html")
    return "plot.html"
