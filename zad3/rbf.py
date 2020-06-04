import numpy as np
import random


class RBF:
    def __init__(self, centers, output_count, learning_rate):
        self.shape = (output_count, len(centers) + 1)  # +1 for bias
        self.centers = centers
        self.weights = np.random.rand(*self.shape)
        self.sigmas = np.random.rand(self.shape[1] - 1)

        self.learning_rate = learning_rate

    def radial_neurons_value(self, value):
        values_list = [RBF.gauss(value, self.centers[i], self.sigmas[i])
                       for i in range(self.shape[1] - 1)]
        # 1 for the bias at 0th index
        values_list.insert(0, 1)
        return np.array(values_list)

    def forward(self, value):
        radial_value = self.radial_neurons_value(value)
        return self.weights @ radial_value

    def back_propagation(self, value, expected):
        activations = self.radial_neurons_value(value)
        # cost - derivative of cost function
        cost = 2 * (self.weights @ activations - expected)
        weight_delta = np.asmatrix(cost).T @ np.asmatrix(activations)
        self.weights -= self.learning_rate * weight_delta

    def adjust_simgas(self, neighbour_count):
        # pick valid neighbours count
        count = min((self.shape[1] - 1, neighbour_count + 1)) - 1
        if count == 0:
            return

        for i in range(self.shape[1] - 1):
            center = self.centers[i]
            neighbours = self.centers[:]

            def custom_key(value):
                return RBF.distance(value, center)

            # Sort neighbours by distance and pick only 'count' first
            # except the 1st one, for which the distance is 0
            neighbours.sort(key=custom_key)
            picked = neighbours[1:count]

            if len(picked) == 0:
                return

            # Compute sigma based on picked neighbours
            self.sigmas[i] = RBF.sigma(center, picked)

    def avg_error(self, batch):
        err = 0
        for sample in batch:
            value = self.forward(sample[0])
            err += RBF.cost(value, sample[1])

        return err / len(batch)

    @staticmethod
    def cost(result, expected):
        d = result - expected
        return np.dot(d, d)

    @staticmethod
    def gauss(value, center, sigma):
        delta = np.array(value) - np.array(center)
        magnitude2 = np.dot(delta, delta)
        return np.exp(-magnitude2 / (2 * sigma * sigma))

    @staticmethod
    def distance2(a, b):
        delta = a - b
        return np.dot(delta, delta)

    @staticmethod
    def distance(a, b):
        return np.sqrt(RBF.distance2(a, b))

    @staticmethod
    def sigma(center, neighbours):
        sig = 0
        for neighbour in neighbours:
            sig += RBF.distance2(center, neighbour)

        return np.sqrt(sig / len(neighbours))


def main():
    pass


if __name__ == '__main__':
    main()
