from Products.Archetypes.config import *
from Products.Archetypes import listTypes
from Products.Archetypes.Extensions.utils import installTypes
from StringIO import StringIO

def install(self):
    out=StringIO()

    if not hasattr(self, "_isPortalRoot"):
        print >> out, "Must be installed in a CMF Site (read Plone)"
        return
    
    if INCLUDE_DEMO_TYPES:
        print >> out, "Installing %s" % listTypes()
        
    installTypes(self, out, listTypes(PKG_NAME), PKG_NAME)
    if INCLUDE_DEMO_TYPES:
        print >> out, 'Successfully installed the demo types.'

        
    print >> out, 'Successfully installed %s' % PKG_NAME
        
    return out.getvalue()

