import os, sys
if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

from common import *
from utils import *

from Products.Archetypes.public import *
from Products.Archetypes.config import PKG_NAME
from Products.Archetypes.Schema import Schemata, getNames
from Products.Archetypes import listTypes

from DateTime import DateTime
import unittest


class SchemataManipulationTest( ArchetypesTestCase ):

    def setUp(self):
        self.schema = Schema(
               (StringField('a', schemata='waldi'),
                StringField('d', schemata='nasbaer'),
                StringField('x', schemata='edgar'),
                StringField('b', schemata='waldi'),
                StringField('e', schemata='nasbaer'),
                StringField('y', schemata='edgar'),
                StringField('c', schemata='waldi'),
                StringField('f', schemata='nasbaer'),
                StringField('z', schemata='edgar')
            ))

    def fields2names(self, fields):
        return [f.getName() for f in fields]

    def testBasic(self):
        self.assertEqual(self.fields2names(self.schema.fields()), 
                        ['a','d','x', 'b','e','y','c','f','z'])
        self.assertEqual(self.schema.getSchemataNames(), ['waldi', 'nasbaer', 'edgar'])

    def testSchemataFields(self):
        self.assertEqual(self.fields2names(self.schema.getSchemataFields('waldi')),
                        ['a', 'b', 'c'])
        self.assertEqual(self.fields2names(self.schema.getSchemataFields('nasbaer')),
                        ['d', 'e', 'f'])
        self.assertEqual(self.fields2names(self.schema.getSchemataFields('edgar')),
                        ['x', 'y', 'z'])

    def testDelField(self):
        self.schema.delField('x')
        self.schema.delField('b')
        self.schema.delField('z')
        self.assertEqual(self.fields2names(self.schema.fields()), 
                        ['a','d','e','y','c','f'])
        self.schema.addField(StringField('z'))
        self.schema.addField(StringField('b'))
        self.schema.addField(StringField('x'))
        self.assertEqual(self.fields2names(self.schema.fields()), 
                        ['a','d','e','y','c','f','z','b','x'])
        self.schema.delField('b')
        self.schema.delField('z')
        self.schema.delField('x')
        self.assertEqual(self.fields2names(self.schema.fields()), 
                        ['a','d','e','y','c','f'])

if __name__ == '__main__':
    framework()
else:
    # While framework.py provides its own test_suite()
    # method the testrunner utility does not.
    import unittest
    def test_suite():
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(SchemataManipulationTest))
        return suite
