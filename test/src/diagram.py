import matplotlib.pyplot as plt


def diagram(list_: list, file: str = None) -> None:
    """
    Function for create plot with diagram and save to file.
    :param file: str - path to file with diagram
    :param list_: list - list for creating diagram
    :return None
    """
    labels = [val for val in range(1, len(list_) + 1)]
    width = 0.35

    fig, ax = plt.subplots()

    ax.bar(labels, list_, width)

    ax.set_ylabel('Value')
    ax.set_title('Test diagram')
    ax.legend()

    plt.savefig(file)
