import os
import sys

sys.path.insert(0, os.path.abspath(".."))


def test_overflow():
    from pycaret.datasets import get_data

    data = get_data("boston")
    from pycaret.regression import create_model, setup, tune_model

    s = setup(
        data,
        target="medv",
        html=False,
        session_id=123,
        n_jobs=1,
    )
    gbr = create_model("gbr")
    tuned_gbr = tune_model(gbr)
    xgboost = create_model("xgboost")
    tuned_xgboost = tune_model(xgboost)
    lightgbm = create_model("lightgbm")
    tuned_lightgbm = tune_model(lightgbm)
    assert 1 == 1
