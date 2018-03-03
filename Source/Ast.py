
#=============================================================================
# Printable Base Class
#=============================================================================

class Printable:
    
    def __str__(self):
        return "[<Class {0}: {1}]".format(self.__class__.__name__, vars(self))
    
    def __repr__(self):
        return self.__str__()

#=============================================================================
# Abstract Syntax Tree
#=============================================================================

#-------------------------------------------------------------- Ast Base class

class Ast_Base(Printable):
    
    def __init__(self):
        self.idx = 0
        self.parent = None
    
    def organize(self, parent=None, idx=0):
        raise Exception
    
    def to_str(self):
        raise Exception

#-------------------------------------------------------- Ast concrete classes

class Or(Ast_Base):
    
    def __init__(self, l, r):
        assert (isinstance(l, Ast_Base))
        assert (isinstance(r, Ast_Base))
        Ast_Base.__init__(self)
        self.l = l
        self.r = r
    
    def organize(self, parent=None, idx=0):
        self.parent = parent
        self.idx = idx
        idx = self.l.organize(self, idx + 1)
        idx = self.r.organize(self, idx + 1)
        return idx
    
    def to_str(self):
        text = '"{0}" [label="{1}"];\n'.format(self.idx, "OR")
        text += '"{0}" -> "{1}" [label="{2}"];\n'.format(self.idx, self.l.idx, "l")
        text += self.l.to_str()
        text += '"{0}" -> "{1}" [label="{2}"];\n'.format(self.idx, self.r.idx, "r")
        text += self.r.to_str()
        return text
        
class And(Ast_Base):
    
    def __init__(self, l, r):
        assert (isinstance(l, Ast_Base))
        assert (isinstance(r, Ast_Base))
        Ast_Base.__init__(self)
        self.l = l
        self.r = r
    
    def organize(self, parent=None, idx=0):
        self.parent = parent
        self.idx = idx
        idx = self.l.organize(self, idx + 1)
        idx = self.r.organize(self, idx + 1)
        return idx
    
    def to_str(self):
        text = '"{0}" [label="{1}"];\n'.format(self.idx, "AND")
        text += '"{0}" -> "{1}" [label="{2}"];\n'.format(self.idx, self.l.idx, "l")
        text += self.l.to_str()
        text += '"{0}" -> "{1}" [label="{2}"];\n'.format(self.idx, self.r.idx, "r")
        text += self.r.to_str()
        return text

class Not(Ast_Base):
    
    def __init__(self, r):
        assert (isinstance(r, Ast_Base))
        Ast_Base.__init__(self)
        self.r = r
    
    def organize(self, parent=None, idx=0):
        self.parent = parent
        self.idx = idx
        idx = self.r.organize(self, idx + 1)
        return idx
    
    def to_str(self):
        text = '"{0}" [label="{1}"];\n'.format(self.idx, "NOT")
        text += '"{0}" -> "{1}" [label="{2}"];\n'.format(self.idx, self.r.idx, "r")
        text += self.r.to_str()
        return text

class Bool(Ast_Base):
    
    def __init__(self, v):
        assert (isinstance(v, int))
        Ast_Base.__init__(self)
        self.vv = v
        self.v = True if v != 0 else False
    
    def organize(self, parent=None, idx=0):
        self.parent = parent
        self.idx = idx
        return idx
    
    def to_str(self):
        text = '"{0}" [label="{1}"];\n'.format(self.idx, self.vv)
        return text


