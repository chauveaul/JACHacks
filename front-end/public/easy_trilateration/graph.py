import math

import matplotlib.pyplot as plt
from random import randint

import pandas as pd
from matplotlib.animation import FuncAnimation
from easy_trilateration import model
import matplotlib

from easy_trilateration.model import Point, Trilateration


def static(history: [model.Trilateration], actual: [Point] = [], ax=plt.axes()):
    x_values = []
    y_values = []

    sniffers = set()
    to_draw = []

    conNumber = []
    radius = []

    for i in range(len(history)):
        tri: Trilateration = history[i]
        for sniffer in tri.sniffers:
            sniffers.add(sniffer.center)
        x_values.append(tri.result.center.x)
        y_values.append(tri.result.center.y)

        if i % 10 == 0:
            to_draw.append(create_circle(tri.result))
            conNumber.append(tri.meta)
            radius.append(tri.result.radius)
            print("---")
            print(tri.result.center.x, tri.result.center.y, tri.result.radius)
            print(tri.meta)
            print("---")
        if i == 0:
            for sniff in sniffers:
                to_draw.append(create_point(sniff, color="red"))


    actual_x = []
    actual_y = []

    data = {'Condition': conNumber,
            'Radius': radius}

    df = pd.DataFrame(data, columns=['Condition', 'Radius'])

    df.to_csv('export_dataframe.csv', index=False, header=True)

    # plt.plot(x_values, y_values, color="blue", linewidth=1)

    for act in actual:
        actual_x.append(act.x)
        actual_y.append(act.y)
    plt.plot(actual_x, actual_y, color="green", linewidth=3)
    draw(to_draw)


# def animate(history: [model.Trilateration], ax=plt.axes()):
#    new = FuncAnimation(plt.gcf(), anim, len(history), fargs=(history, ax,), repeat=False)
# plt.show()
#    return new


# def anim(i, history: [model.Trilateration], ax):
#    x_values = []
#    y_values = []
#    for i in range(i + 1):
#        if i % 100 == 0:
#            item = history[i]
#            x_values.append(item.result.center.x)
#            y_values.append(item.result.center.y)
# for item in history[i].sniffers:
# create_point(item.center)
#    create_circle(history[i].result, target=True)
#    ax.plot(x_values, y_values, 'blue', linestyle='--')


def create_circle(circle: model.Circle, color=None, target=False):
    if target:
        color = matplotlib.cm.jet(1000)
    elif color is None:
        color = matplotlib.cm.jet(randint(50, 100))
    add_shape(plt.Circle((circle.center.x, circle.center.y), color=color, fill=False, zorder=1, radius=circle.radius,
                         alpha=0.8))
    plt.scatter(circle.center.x, circle.center.y, color=color, s=100, zorder=2)


def create_point(point: model.Point, color=matplotlib.cm.jet(randint(0, 00))):
    plt.scatter(int(point.x), int(point.y), color=color, s=100, zorder=2)


def add_shape(patch):
    ax = plt.gca()
    ax.add_patch(patch)
    plt.axis('scaled')


def draw(draw_list):
    for item in draw_list:
        if isinstance(item, model.Circle):
            create_circle(item)
        if isinstance(item, model.Point):
            create_point(item)
    plt.savefig("front-end/public/yippee.png")
