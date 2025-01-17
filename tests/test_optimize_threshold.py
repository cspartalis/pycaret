import os
import sys

sys.path.insert(0, os.path.abspath(".."))

import numpy as np
import pandas as pd
import pytest

import pycaret.classification
import pycaret.datasets
from pycaret.internal.meta_estimators import CustomProbabilityThresholdClassifier


def test_optimize_threshold():

    # loading dataset
    data = pycaret.datasets.get_data("blood")

    # initialize setup
    clf1 = pycaret.classification.setup(
        data,
        target="Class",
        html=False,
        n_jobs=1,
    )

    # train model
    lr = pycaret.classification.create_model("lr")

    # optimize threshold
    optimized_data, optimized_model = pycaret.classification.optimize_threshold(
        lr, return_data=True
    )
    assert isinstance(optimized_data, pd.core.frame.DataFrame)
    assert isinstance(optimized_model, CustomProbabilityThresholdClassifier)


if __name__ == "__main__":
    test_optimize_threshold()
