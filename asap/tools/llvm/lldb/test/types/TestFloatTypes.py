"""
Test that variables of floating point types are displayed correctly.
"""

import AbstractBase
import unittest2
import lldb
import sys
from lldbtest import *

class FloatTypesTestCase(AbstractBase.GenericTester):

    mydir = AbstractBase.GenericTester.compute_mydir(__file__)

    def setUp(self):
        # Call super's setUp().
        AbstractBase.GenericTester.setUp(self)
        # disable "There is a running process, kill it and restart?" prompt
        self.runCmd("settings set auto-confirm true")
        self.addTearDownHook(lambda: self.runCmd("settings clear auto-confirm"))

    @skipUnlessDarwin
    @dsym_test
    def test_float_type_with_dsym(self):
        """Test that float-type variables are displayed correctly."""
        self.build_and_run('float.cpp', set(['float']))

    @skipUnlessDarwin
    @dsym_test
    def test_float_type_from_block_with_dsym(self):
        """Test that float-type variables are displayed correctly from a block."""
        self.build_and_run('float.cpp', set(['float']), bc=True)

    @dwarf_test
    def test_float_type_with_dwarf(self):
        """Test that float-type variables are displayed correctly."""
        self.build_and_run('float.cpp', set(['float']), dsym=False)

    @skipUnlessDarwin
    @dsym_test
    @expectedFlakeyDarwin # failed 1/140 runs 'frame variable --show-types a_union_nonzero_ref.u.a' matches the output (from compiled code): 11001110
    def test_double_type_with_dsym(self):
        """Test that double-type variables are displayed correctly."""
        self.build_and_run('double.cpp', set(['double']))

    @skipUnlessDarwin
    @dsym_test
    def test_double_type_from_block_with_dsym(self):
        """Test that double-type variables are displayed correctly from a block."""
        self.build_and_run('double.cpp', set(['double']), bc=True)

    @dwarf_test
    def test_double_type_with_dwarf(self):
        """Test that double-type variables are displayed correctly."""
        self.build_and_run('double.cpp', set(['double']), dsym=False)


if __name__ == '__main__':
    import atexit
    lldb.SBDebugger.Initialize()
    atexit.register(lambda: lldb.SBDebugger.Terminate())
    unittest2.main()
