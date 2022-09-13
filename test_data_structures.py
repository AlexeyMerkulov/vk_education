import pytest


class TestFloatStructure:
    @pytest.mark.parametrize('float_num, int_num, expected', [(5.0, 50, 55.0), (5.0, -50, -45.0), (5.0, 0, 5.0),
                                                              (-5.0, 50, 45.0), (-5.0, -50, -55.0), (-5.0, 0, -5.0),
                                                              (0.0, 50, 50.0), (0.0, -50, -50.0), (0.0, 0, 0.0)
                                                              ])
    def test_result_of_sum_operation_of_float_and_any_int_nums_is_also_float(self, float_num, int_num, expected):
        assert float_num + int_num == expected

    def test_float_has_no_tostring_method(self):
        float_num = 5.0
        expected = '5.0'
        try:
            assert expected == float_num.tostring()
        except AttributeError:
            print('Float has no tostring() method')
        else:
            print('Float has tostring() method')


class TestSetStructure:
    @pytest.mark.parametrize('list_of_nums, expected', [([1, 2, 3, 4, 5], {1, 2, 3, 4, 5}),
                                                        ([1, 1, 1, 2, 3, 4], {1, 2, 3, 4}),
                                                        ([1, 1, 1, 1, 1], {1})
                                                        ])
    def test_set_has_no_duplicates(self, list_of_nums, expected):
        assert set(list_of_nums) == expected

    def test_set_has_no_append_method(self):
        expected = {1, 2, 3, 4}
        simple_set = {1, 2, 3}
        try:
            assert expected == simple_set.append(4)
        except AttributeError:
            print('Set has no append() method')
        else:
            print('Set has append() method')


class TestStringStructure:
    @pytest.mark.parametrize('input_string, expected', [('abcde', True), ('abc1e', False), ('11111', False)])
    def test_string_isalpha_method(self, input_string, expected):
        assert input_string.isalpha() is expected

    def test_string_has_no_concat_method(self):
        expected = 'abcde'
        simple_string = 'abc'
        another_simple_string = 'de'
        try:
            assert expected == simple_string.concat(another_simple_string)
        except AttributeError:
            print('String has no concat() method')
        else:
            print('String has concat() method')


