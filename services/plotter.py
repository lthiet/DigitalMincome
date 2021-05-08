import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import mpld3
import seaborn as sns
import os
import uuid
sns.set()
matplotlib.use('Agg')

import os, re

def purge(dir, pattern):
    for f in os.listdir(dir):
        if re.search(pattern, f):
            os.remove(os.path.join(dir, f))

def plot(params):
    purge("app/templates",r"plot.*\.html")
    # Data for plotting
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + params['transaction_fee'] * np.sin(2 * np.pi * t)

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
        title='About as simple as it gets, folks')
    ax.grid()

    plot_name = f"plot{uuid.uuid4()}.html"

    mpld3.save_html(fig,f"app/templates/{plot_name}")
    return plot_name
