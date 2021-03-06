"""Noise process tests."""
# flake8: noqa
import numpy as np
import pytest


# Floating point arithmetic comparison threshold
@pytest.fixture(params=[10**-10])
def threshold(request):
    return request.param

# Common
@pytest.fixture(params=[1])
def t(request):
    return request.param

@pytest.fixture(params=[16])
def n(request):
    return request.param

@pytest.fixture(params=[True, False])
def zero(request):
    return request.param

# Generate some random times for the sample_at() method
times_random = np.cumsum(np.abs(np.random.normal(size=16)))
times_random_zero = np.cumsum([0] + list(np.abs(np.random.normal(size=16))))

@pytest.fixture(params=[times_random, times_random_zero])
def times(request):
    return request.param

# FractionalGaussianNoise
@pytest.fixture(params=[0.2, 0.5, 0.7])
def hurst(request):
    return request.param

@pytest.fixture(params=[1, 1.1])
def hurst_fixture(request):
    return request.param

@pytest.fixture(params=['daviesharte', 'hosking'])
def algorithm(request):
    return request.param

@pytest.fixture(params=['badalgorithm'])
def algorithm_fixture(request):
    return request.param
