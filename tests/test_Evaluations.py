#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for the FAIRtools module.
"""
import pytest

# from FAIRtools import Evaluations


def test_without_test_object():
    # TODO: implement tests properly
    pass


class TestCollections(object):
    @pytest.fixture
    def sample_evaluation(self):
        # return Evaluations(id)
        return None

    def test_FAIRtools(self, sample_evaluation):
        # TODO: implement tests properly
        pass

    def test_with_error(self, sample_evaluation):
        # TODO: implement tests properly
        with pytest.raises(ValueError):
            raise ValueError()
