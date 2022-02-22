#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： fushaoshan
# datetime： 2022/2/22 10:55 上午
import pytest

class Test_wrongLogin:

    @pytest.mark.run(ordering=1)
    def test_C001001(self):
        print('\n用例C001001')
        assert 1 == 1

    @pytest.mark.run(ordering=1)
    def test_C001002(self):
        print('\n用例C001002')
        assert 2 == 2

    @pytest.mark.run(ordering=1)
    def test_C001003(self):
        print('\n用例C001003')
        assert 3 == 3
