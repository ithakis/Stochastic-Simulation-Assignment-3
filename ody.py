from matplotlib import pyplot as plt


def plot():
    fig = plt.figure()
    fig.set_facecolor('w')
    fig.set_size_inches(10, 10, forward=True)
    fig.tight_layout()
    ax = fig.add_subplot()

    ax.grid(b=True, which='major', c='lightgray', lw=1, ls='-');
    ax.set_facecolor('whitesmoke')

    return ax


def show(ax):
    ax.legend(loc='upper right')
    plt.show()
