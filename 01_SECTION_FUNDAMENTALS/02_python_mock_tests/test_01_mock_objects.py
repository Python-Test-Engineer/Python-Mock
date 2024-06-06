"""
This test suite is intended to demonstrate sample usage of the python mock library.
Much of this is already covered in the mock documentation, but this hopefully
adds a few useful examples, calls out some subtleties, and addresses
some common misunderstandings.

It is intended to be read in-order, as a primer.
Almost like a technical blog post written as a test suite.

Run these tests with `python tests.py`
"""

from unittest import TestCase
from unittest.mock import Mock, MagicMock


################################################################################################
# PART 1: The Mock class
# The mock library has two major components that are separate, but work powerfully in tandem.
# The first is the Mock class (and subclasses). The second are the 'patch' helpers.
# First, we will demonstrate usage of the Mock class.
################################################################################################


class MockObjectBasics(TestCase):
    """Demonstates the basics of the 'Mock' class."""

    def test_mock(self):
        # A Mock object is callable, and you can configure
        # this callable's return value. By default it returns
        # another Mock instance, created on first access.
        # Any arbitrary attribute access also creates & returns another
        # mock instance. This 'spreads' to form a tree of Mock objects

        m = Mock()
        self.assertIsInstance(m, Mock)

        # a mock is always callable, and returns its return_value (by default, another Mock instance)
        self.assertIsInstance(m(), Mock)

        # any arbitrary attribute access or invocation will return another mock
        self.assertIsInstance(m.xyz, Mock)
        self.assertIsInstance(m.foo(), Mock)
        self.assertIsInstance(m.just.keep.on().trucking, Mock)

        # different attributes will all have different mock objects returned
        self.assertNotEqual(m.abcd, m.efgh)

        # but once referenced, the same mock is always returned
        self.assertEqual(m.abcd, m.abcd)

    def test_return_value(self):
        # The Mock constructor takes some optional arguments to control the Mock's behavior.
        # return_value allows you to control what is returned when the Mock is called like a function.
        # You can change it at after construction as well.
        m = MagicMock(return_value=123)
        self.assertEqual(123, m())
        m.return_value = 345
        self.assertEqual(345, m())

    def test_mock_kwargs_constructor(self):
        #    In addition to the 6 supported arguments to the Mock constructor ("return_value", "side_effect", "spec", "spec_set", "wraps", and "name"),
        #     arbitrary keyword arguments can be passed in, and these will be used to set attributes on child mocks after they are created.
        #     One can even set attributes on child mock elements arbitrarily deep
        m = Mock(
            **{
                "first_name": "owned",
                "calculate_minimum.return_value": 456,
                "company.xyz.get_url.side_effect": Exception,
            }
        )
        self.assertEqual("owned", m.first_name)
        self.assertEqual(456, m.calculate_minimum())
        self.assertRaises(Exception, m.company.xyz.get_url)

    def test_mock_magic_methods(self):
        # The Mock class supports replacing Python magic methods.
        # The MagicMock class (covered later) supplies useful default implementations for most of them.

        def my_str(self):
            return "owned"

        m = Mock()
        m.__str__ = my_str
        self.assertEqual("owned", str(m))

    def test_mock_called(self):
        # You can use the special "called" attribute to check that a Mock object was called
        m = Mock()
        self.assertFalse(m.called)
        m()
        self.assertTrue(m.called)


class MockObjectSideEffects(TestCase):
    # Another optional argument to the Mock constructor is side_effect. It has several different use cases.
    # It can be used for dynamic return values, for making other things happen whenever
    # a mock is called, or for raising exceptions. If you give it an iterable, it will iterate over the elements in
    # that iterable as successive return values.

    def test_side_effect_with_iterable(self):
        # Here is an example of giving an iterable as side_effect

        m = Mock(side_effect=range(4))
        self.assertEqual(0, m())
        self.assertEqual(1, m())
        self.assertEqual(2, m())
        self.assertEqual(3, m())

        # will raise StopIteration when iterator is exhausted
        self.assertRaises(StopIteration, m)

    def test_side_effect_with_exception(self):
        # You can give an Exception class or instance as a side_effect and that exception will be raised on every call

        class MyException(Exception):
            def __init__(self, detail):
                self.detail = detail

        # exception instance
        m = Mock(side_effect=MyException("xyz"))
        self.assertRaises(MyException, m)

        # passing an exception class only works as expected if the exception has a no-arg constructor
        m = Mock(side_effect=MyException)
        self.assertRaises(
            TypeError, m
        )  # TypeError: __init__() takes exactly 2 arguments (1 given)

        m = Mock(side_effect=KeyError)
        self.assertRaises(KeyError, m)

    def test_side_effect_with_callable(self):
        # If you pass a callable as side_effect, it will be called with the same arguments
        # as the mock, and its return value will be used as the mock object's return value.

        def my_side_effect(mock_arg):
            if mock_arg % 2 == 0:
                return "even"
            else:
                return "odd"

        m = Mock(side_effect=my_side_effect)
        self.assertEqual("even", m(2))
        self.assertEqual("odd", m(3))
