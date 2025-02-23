# -*- coding: utf-8 -*-
#
#  SelfTest/Cipher/__init__.py: Self-test for cipher modules
#
# Written in 2008 by Dwayne C. Litzenberger <dlitz@dlitz.net>
#
# ===================================================================
# The contents of this file are dedicated to the public domain.  To
# the extent that dedication to the public domain is not available,
# everyone is granted a worldwide, perpetual, royalty-free,
# non-exclusive license to exercise all rights associated with the
# contents of this file for any purpose whatsoever.
# No rights are reserved.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ===================================================================

"""Self-test for cipher modules"""

__revision__ = "$Id$"

def get_tests(config={}):
    tests = []
    import test_AES;      tests += test_AES.get_tests(config=config)
    import test_ARC2;     tests += test_ARC2.get_tests(config=config)
    import test_ARC4;     tests += test_ARC4.get_tests(config=config)
    import test_Blowfish; tests += test_Blowfish.get_tests(config=config)
    import test_CAST;     tests += test_CAST.get_tests(config=config)
    import test_DES3;     tests += test_DES3.get_tests(config=config)
    import test_DES;      tests += test_DES.get_tests(config=config)
    import test_XOR;      tests += test_XOR.get_tests(config=config)
    import test_pkcs1_15; tests += test_pkcs1_15.get_tests(config=config)
    import test_pkcs1_oaep; tests += test_pkcs1_oaep.get_tests(config=config)
    return tests

if __name__ == '__main__':
    import unittest
    suite = lambda: unittest.TestSuite(get_tests())
    unittest.main(defaultTest='suite')

# vim:set ts=4 sw=4 sts=4 expandtab:
