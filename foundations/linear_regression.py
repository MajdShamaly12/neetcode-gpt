import numpy as np
from numpy.typing import NDArray


class Solution:

    def binary_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
        # y_true: true labels (0 or 1)
        # y_pred: predicted probabilities
        # Hint: add a small epsilon (1e-7) to y_pred to avoid log(0)
        eps = 1e-7
        y_pred = np.clip(y_pred, eps, 1 - eps)
        sum=0
        for i in range(len(y_pred)):
            if y_true[i] == 1:
                sum+=np.log(y_pred[i])
            else:
                sum+=np.log(1-y_pred[i])
        return round(-1/len(y_pred)*sum,4)
        # return round(your_answer, 4)
        pass

    def categorical_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
        # y_true: one-hot encoded true labels (shape: n_samples x n_classes)
        # y_pred: predicted probabilities (shape: n_samples x n_classes)
        # Hint: add a small epsilon (1e-7) to y_pred to avoid log(0)
        eps = 1e-7
        y_pred = np.clip(y_pred, eps, 1 - eps)
        loss=0
        for i in range(len(y_pred)):
            loss+=np.sum(y_true[i]*np.log(y_pred[i]))
        # return round(your_answer, 4)
        return round(-loss/len(y_pred),4)
        pass
