#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for the FAIRtools module.
"""
import pytest

# from FAIRtools import Metrics


def test_without_test_object():
    # TODO: implement tests properly
    pass


class TestCollections(object):
    @pytest.fixture
    def sample_metric(self):
        # return Metrics(id)
        return None

    def test_FAIRtools(self, sample_metric):
        # TODO: implement tests properly
        pass

    def test_with_error(self, sample_metric):
        # TODO: implement tests properly
        with pytest.raises(ValueError):
            raise ValueError()
