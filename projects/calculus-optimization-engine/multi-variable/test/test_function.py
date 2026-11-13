
import numpy as np
import pytest

from src.function import Function


def scalar_f(x):
    return x[0]**2 + x[1]**2


def vector_g(x):
    return np.array([
        x[0] + x[1],
        x[0] * x[1]
    ])


def test_scalar_function():
    f = Function(scalar_f, input_dim=2)

    result = f(np.array([3.0, 4.0]))

    assert result == 25.0
    assert isinstance(result, float)


def test_vector_function():
    g = Function(
        vector_g,
        input_dim=2,
        output_dim=2
    )

    result = g(np.array([2.0, 3.0]))

    np.testing.assert_allclose(
        result,
        np.array([5.0, 6.0])
    )

    assert result.shape == (2,)


def test_scalar_batch():
    f = Function(scalar_f, input_dim=2)

    X = np.array([
        [3.0, 4.0],
        [5.0, 12.0]
    ])

    result = f.evaluate_batch(X)

    np.testing.assert_allclose(
        result,
        np.array([25.0, 169.0])
    )

    assert result.shape == (2,)


def test_vector_batch():
    g = Function(
        vector_g,
        input_dim=2,
        output_dim=2
    )

    X = np.array([
        [1.0, 2.0],
        [3.0, 4.0]
    ])

    result = g.evaluate_batch(X)

    np.testing.assert_allclose(
        result,
        np.array([
            [3.0, 2.0],
            [7.0, 12.0]
        ])
    )

    assert result.shape == (2, 2)


def test_wrong_input_dimension():
    f = Function(scalar_f, input_dim=2)

    with pytest.raises(ValueError):
        f(np.array([1.0, 2.0, 3.0]))


def test_wrong_output_dimension():
    g = Function(
        vector_g,
        input_dim=2,
        output_dim=3
    )

    with pytest.raises(ValueError):
        g(np.array([2.0, 3.0]))


def test_empty_vector_batch():
    g = Function(
        vector_g,
        input_dim=2,
        output_dim=2
    )

    X = np.empty((0, 2))

    result = g.evaluate_batch(X)

    assert result.shape == (0, 2)
