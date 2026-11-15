
from collections.abc import Callable

import numpy as np


class Function:
    """
    A mathematical function with an explicitly defined
    input dimension and output type.
    """

    def __init__(
        self,
        func: Callable,
        input_dim: int,
        output_dim: int | None = None,
        name: str | None = None,
    ):
        # Validate the underlying callable.
        if not callable(func):
            raise TypeError("func must be callable")

        # Validate the input dimension.
        if (
            isinstance(input_dim, bool)
            or not isinstance(input_dim, int)
            or input_dim <= 0
        ):
            raise ValueError(
                "input_dim must be a positive integer"
            )

        # Validate the output dimension.
        if output_dim is not None:
            if (
                isinstance(output_dim, bool)
                or not isinstance(output_dim, int)
                or output_dim <= 0
            ):
                raise ValueError(
                    "output_dim must be None or a positive integer"
                )

        self._func = func
        self.input_dim = input_dim
        self.output_dim = output_dim

        self.name = name or getattr(
            func, "__name__", "unnamed_function"
        )

    def evaluate(self, x: np.ndarray):
        """
        Evaluate the function at one input point.
        """

        x = np.asarray(x, dtype=float)

        # Validate input shape.
        expected_shape = (self.input_dim,)

        if x.shape != expected_shape:
            raise ValueError(
                f"{self.name} expects input shape "
                f"{expected_shape}, got {x.shape}"
            )

        # Execute the underlying mathematical function.
        result = np.asarray(self._func(x), dtype=float)

        # Scalar-valued function.
        if self.output_dim is None:
            if result.shape != ():
                raise ValueError(
                    f"{self.name} must return a scalar, "
                    f"got shape {result.shape}"
                )

            return float(result)

        # Vector-valued function.
        expected_output_shape = (self.output_dim,)

        if result.shape != expected_output_shape:
            raise ValueError(
                f"{self.name} must return shape "
                f"{expected_output_shape}, "
                f"got {result.shape}"
            )

        return result

    def evaluate_batch(self, X: np.ndarray):
        """
        Evaluate the function at multiple input points.

        Each row of X represents one input point.
        """

        X = np.asarray(X, dtype=float)

        if X.ndim != 2:
            raise ValueError(
                "Batch input must be a 2D array"
            )

        if X.shape[1] != self.input_dim:
            raise ValueError(
                f"Expected batch input shape (N, "
                f"{self.input_dim}), got {X.shape}"
            )

        outputs = [
            self.evaluate(point)
            for point in X
        ]

        # Scalar-valued function: shape (N,)
        if self.output_dim is None:
            return np.asarray(outputs, dtype=float)

        # Handle an empty batch explicitly.
        if len(outputs) == 0:
            return np.empty(
                (0, self.output_dim),
                dtype=float
            )

        # Vector-valued function: shape (N, m)
        return np.stack(outputs, axis=0)

    def __call__(self, x: np.ndarray):
        """
        Allow the Function object to be called like
        an ordinary Python function.
        """
        return self.evaluate(x)

    def __repr__(self):
        return (
            f"Function(name={self.name!r}, "
            f"input_dim={self.input_dim}, "
            f"output_dim={self.output_dim})"
        )

