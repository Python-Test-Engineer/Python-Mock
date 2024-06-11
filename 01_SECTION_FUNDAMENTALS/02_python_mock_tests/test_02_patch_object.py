# This test suite is intended to demonstrate sample usage of the python mock library.
# Much of this is already covered in the mock documentation, but this hopefully
# adds a few useful examples, calls out some subtleties, and addresses
# some common misunderstandings.

# It is intended to be read in-order, as a primer.
# Almost like a technical blog post written as a test suite.

# Run these tests with `python tests.py`


import unittest
from unittest import TestCase
from unittest.mock import MagicMock, patch

import mypackage.a
import mypackage.b
import mypackage.c


################################################################################################
# PART 2: The patch() helpers
# The mock library has two major components that are separate, but work powerfully in tandem.
# The first is the Mock class (and subclasses). The second are the 'patch' helpers.
# Next, we will demonstrate how to use the patch helpers
################################################################################################


DEFAULT_VALUE = 1
PATCHED_VALUE = 42
QUERY_DATABASE_DEFAULT_VALUE = 1000000


class PatchObjectExamples(TestCase):
    #    The purpose of patching is always to replace some ATTRIBUTE on some TARGET OBJECT.
    #     That target object might be a user-defined object instance, a class object, or a module object.
    #     The main patch() callable takes a string descriptor of this target object that is a source of confusion and
    #     will be described later. It's easier to get started by describing the helper patch.object(), which
    #     takes the target object as a direct parameter

    def test_patch_object_as_func_decorator(self):
        # There are several ways to invoke the patch helpers (including patch.object). One is as a function decorator.
        # my_instance._val is changed to PATCHED_VALUE when _test() is invoked, then set back to its old value afterwards
        # patch is literally going to call getattr(target, attr_name) to get the existing value & replace it by calling
        # setattr(target, attr_name, new) (later restoring it)

        my_instance = mypackage.c.MyClass(DEFAULT_VALUE)

        @patch.object(my_instance, "_val", new=PATCHED_VALUE)
        def _test():
            self.assertEqual(PATCHED_VALUE, my_instance.foo())

        _test()

    def test_patch_object_as_context_processor(self):
        # Patching can also be invoked as a context processor, using the "with" statement
        my_instance = mypackage.c.MyClass(DEFAULT_VALUE)
        with patch.object(my_instance, "_val", new=PATCHED_VALUE):
            self.assertEqual(PATCHED_VALUE, my_instance.foo())

    def test_patch_object_as_class_decorator(self):
        # As a special case, patching can be invoked as a class decorator. This is always for subclasses of
        # unittest.TestCase, and only methods prefixed with mock.path.TEST_PREFIX are patched ("test_" by default)

        my_instance = mypackage.c.MyClass(DEFAULT_VALUE)

        @patch.object(my_instance, "_val", new=PATCHED_VALUE)
        class MyNewTestClass(unittest.TestCase):

            def test_one(self):
                self.assertEqual(PATCHED_VALUE, my_instance.foo())

            def test_two(self):
                self.assertEqual(PATCHED_VALUE, my_instance.foo())

            def other_method(self):
                self.assertNotEqual(PATCHED_VALUE, my_instance.foo())
                self.assertEqual(DEFAULT_VALUE, my_instance.foo())

            def runTest(self):
                # just need this due to declaration inside function
                pass

        test_class = MyNewTestClass()

        # test_xxx methods have been patched
        test_class.test_one()
        test_class.test_two()

        # this one was not
        test_class.other_method()

    def test_patch_object_on_instances(self):
        # patch.object can patch individual class instances
        my_instance = mypackage.c.MyClass(DEFAULT_VALUE)
        another_instance = mypackage.c.MyClass(DEFAULT_VALUE)

        with patch.object(my_instance, "foo", new=MagicMock(return_value=666)):
            self.assertEqual(666, my_instance.foo())
            self.assertEqual(DEFAULT_VALUE, another_instance.foo())

        with patch.object(my_instance, "_val", new=777):
            self.assertEqual(777, my_instance.foo())
            self.assertEqual(DEFAULT_VALUE, another_instance.foo())

    def test_patch_object_on_classes(self):
        # patch.object can also patch a class object itself
        my_instance = mypackage.c.MyClass(DEFAULT_VALUE)
        another_instance = mypackage.c.MyClass(DEFAULT_VALUE)

        with patch.object(mypackage.c.MyClass, "foo", new=MagicMock(return_value=666)):
            self.assertEqual(666, my_instance.foo())
            self.assertEqual(666, another_instance.foo())

        @patch.object(mypackage.c.MyClass, "_val", new=777)
        def test_patching_instance_var_on_class():
            pass

        # mypackage.c.MyClass does not have the attribute '_val', so this can't be done
        self.assertRaises(AttributeError, test_patching_instance_var_on_class)

    def test_patch_dict(self):
        # patch.dict is a convenience for patching dict-like objects
        d = {"a": 111, "b": 222}
        with patch.dict(d, values={"a": 333}):
            self.assertEqual(d["a"], 333)
            self.assertEqual(d["b"], 222)


class PatchTargetingExamples(TestCase):
    # A lot of the confusion in patching comes when patching using the string targeting syntax.

    @patch("mypackage.a.A_MODULE_VAR", new=777)
    def test_patch_module_variable(self):
        """Patching module level variables works - keep in mind it will
        only be in effect at patch time, so other dependent variables are unaffected"""
        self.assertEqual(777, mypackage.a.A_MODULE_VAR)
        self.assertEqual(777, mypackage.a.fn_referencing_module_var())
        self.assertEqual(42 * 2, mypackage.a.A_DERIVED_MODULE_VAR)


class PropertyExample(TestCase):
    # Properties (Python descriptors in general) require some special effort to correctly patch

    def test_patching_writable_property(self):
        """If the property is writable, patching does work. need to patch the value, not the property definition function"""
        my_instance = mypackage.c.MyClass(DEFAULT_VALUE)
        self.assertEqual(my_instance.writeable_prop, DEFAULT_VALUE)

        @patch.object(my_instance, "writeable_prop", new="xyz")
        def test_patching_writable_property():
            self.assertEqual("xyz", my_instance.writeable_prop)

        # patching the writable property works
        test_patching_writable_property()


if __name__ == "__main__":
    unittest.main()
