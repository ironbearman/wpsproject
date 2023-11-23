import unittest


class OutputCheck(unittest.TestCase):
    def assert_output(self, expr, actual):
        """
        断言返回体
        1.
        2.
        3.
        4.
        :param expr: 期望值，dict demo：
        :param actual:

        """

        # 首先，方法使用self.assertEqual(len(expr.keys()), len(actual.keys()), msg='actual keys error!')来检查expr和actual两个字典的键的数量是否相同。
        self.assertEqual(len(expr.keys()), len(actual.keys()), msg='key长度不一致')
        # 然后，它遍历expr字典的每个键值对，并检查键是否存在于actual字典中。如果不存在，测试失败并抛出错误消息"key error!"。
        for k, v in expr.items():
            self.assertIn(k, actual.keys())
            # 它首先检查值是否是类型
            if isinstance(v, type):
                self.assertEqual(v, type(actual[k]), msg=f'{k} Dynamic value type assert fail！')
                # 如果是，它将期望值与实际值进行比较，
            elif isinstance(v, dict):
                self.assert_output(v, actual[k])
            elif isinstance(v, list):
                for index in range(len(v)):
                    if isinstance(v[index], dict):
                        self.assert_output(v[index], actual[k][index])
                    else:
                        self.assertEqual(v[index], actual[k][index], msg=f'{k}(type:list) index: {index} assert error!')
            else:
                self.assertEqual(v, actual[k], msg=f'key: {k} 期望值不一致error!')

