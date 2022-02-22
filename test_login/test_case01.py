#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： fushaoshan
# datetime： 2022/2/22 10:55 上午
import pytest
import allure

@allure.feature('test_module_01')
class Test_wrongLogin:

    @allure.story("1==1")
    def test_C001001(self):
        print('\n用例C001001')
        assert 1 == 1

    @allure.story("2==2")
    def test_C001002(self):
        print('\n用例C001002')
        assert 2 == 2

    @allure.story("3==3")
    def test_C001003(self):
        print('\n用例C001003')
        assert 3 == 2
