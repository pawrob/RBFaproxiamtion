import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import random
import datetime

from rbf import RBF


def plot_function(axes, points, color, marker='o', size=10):
    x_val = [point[0] for point in points]
    y_val = [point[1] for point in points]

    axes.plot(x_val, y_val, f'{color}{marker}', markersize=size)


def plot_error(axes, error, color, size, line='-', label=None):
    x_val = [i for i in range(len(error))]
    axes.plot(x_val, error, f'{color}{line}', label=label,
              linewidth=size, markersize=0)


def load_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            sample = [float(i) for i in line.split(' ')]
            data.append([np.array([sample[0]]), np.array([sample[1]])])
    return data


def training_session(data, test, axes, rbf, epochs):
    error_data = []
    error_test = []
    error_data.append(rbf.avg_error(data))
    error_test.append(rbf.avg_error(test))

    for _ in range(epochs):

        random.shuffle(data)
        for sample in data:
            rbf.back_propagation(sample[0], sample[1])

        error_data.append(rbf.avg_error(data))
        error_test.append(rbf.avg_error(test))

    computed = [[t[0], rbf.forward(t[0])] for t in test]
    plot_function(axes, data, 'r', 'o', 6)
    plot_function(axes, computed, 'b', 'o', 4)

    return error_data, error_test


def roll_centers(data, count):
    return random.sample(data, count)


def prepare_axes(axes, title):
    axes.clear()
    axes.grid(True)
    axes.set_title(title)


def train_on_data_set(data, test_data, directory, neurons, neighbours, epochs):
    fig, axes = plt.subplots()
    err_fig, err_axes = plt.subplots()

    for i in range(1, min(neurons, len(data)) + 1):
        print("Epoka: ", i)
        centers = roll_centers(data, i)
        centers_value = [sample[0] for sample in centers]
        rbf = RBF(centers_value, 1, 0.1)

        for j in range(1, neighbours + 1):

            if j >= i:
                break

            rbf.adjust_simgas(j)

            prepare_axes(axes, f'Centra {i} Sąsiedzi {j}')
            prepare_axes(err_axes, f'Centra {i} Sąsiedzi {j}')

            d_err, t_err = training_session(data, test_data, axes, rbf, epochs)
            plot_function(axes, centers, 'c', '^', 6)

            plot_error(err_axes, d_err, 'r', 4, label='data')
            plot_error(err_axes, t_err, 'b', 4, '--', label='test')

            err_axes.legend()
            err_axes.set_ylim(bottom=0.0, top=5.0)
            err_axes.set_yticks(np.arange(0, 5.2, 0.2))


            now = datetime.datetime.now()
            godzinka = now.strftime("%Y-%m-%d %H-%M-%S")

            fig.savefig(f'{directory}/approx/c{i}_n{j}_'+ godzinka +'.png')
            err_fig.savefig(f'{directory}/error/c{i}_n{j}.png')
            plt.close(fig)
            plt.close(err_fig)


def main():
    print("Zadanie 3 - 224460, 224270")
    matplotlib.use('Agg')
    dir = 'partA'
    neuron_max = 20
    neighbour_max = 10
    epochs = 20
    print("Ladowanie danych")
    data1 = load_data('approximation_train_1.txt')
    data2 = load_data('approximation_train_2.txt')
    test = load_data('approximation_test.txt')
    print("Rozpoczęcie nauki")
    train_on_data_set(data1, test, dir + '/t1',
                      neuron_max, neighbour_max, epochs)
    print("Zakończenie nauki na pierwszym zestawie danyhc\nRozpoczecie nauki na drugim zestawie danych")
    train_on_data_set(data2, test, dir + '/t2',
                      neuron_max, neighbour_max, epochs)
    print("Koniec programu, dane zostały zapisane ")


if __name__ == '__main__':
    main()
