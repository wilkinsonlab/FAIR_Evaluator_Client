#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for the FAIRtools module.
"""
import pytest

# from FAIRtools import Collections


def test_without_test_object():
    # TODO: implement tests properly
    pass


class TestCollections(object):
    @pytest.fixture
    def sample_collection(self):
        # return Collections(id)
        return None

    def test_FAIRtools(self, sample_collection):
        # TODO: implement tests properly
        pass

    def test_with_error(self, sample_collection):
        # TODO: implement tests properly
        with pytest.raises(ValueError):
            raise ValueError()
