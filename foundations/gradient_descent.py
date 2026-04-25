class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        x=init
        cycles=iterations
        derovative= 2*x
        for cycle in range(cycles):
            derovative = 2*x
            x=x-learning_rate * derovative
        return round(x,5)


        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        pass
