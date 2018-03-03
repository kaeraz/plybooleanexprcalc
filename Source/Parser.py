import ply.yacc as yacc
import Source.Ast as Ast
import logging

#=============================================================================
# Logger configuration
#=============================================================================

_l = logging.getLogger("[Parser]")

# --------------------------------------------------------------------------
# PLY LEXER configuration
# --------------------------------------------------------------------------

class Parser:
    
    #------------------------------------------------------------- Constructor
    
    def __init__(self, tokens):
        self.tokens = tokens
    
    #--------------------------------------- Parser rules (grammar definition)
    
    def p_expr_or(self, p):
        """ expr : expr OR term
        """
        _l.debug("expr : expr OR term")
        p[0] = Ast.Or(p[1], p[3])
    
    def p_expr_and(self, p):
        """ expr : expr AND term
        """
        _l.debug("expr : expr AND term")
        p[0] = Ast.And(p[1], p[3])
    
    def p_expr(self, p):
        """ expr : term
        """
        _l.debug("expr : term")
        p[0] = p[1]
    
    def p_term_not(self, p):
        """ term : NOT term
        """
        _l.debug("term : NOT factor")
        p[0] = Ast.Not(p[2])
    
    def p_term_parens(self, p):
        """ term : LPAREN expr RPAREN
        """
        _l.debug("term : LPAREN expr RPAREN")
        p[0] = p[2]
    
    def p_term(self, p):
        """ term : INTEGER
        """
        _l.debug("term : INTEGER")
        p[0] = Ast.Bool(p[1])
    
    #-------------------------------------------------------------- Error rule
    
    def p_error(self, p):
        if p is None:
            raise SyntaxError("Unexpected EOF.")
        raise SyntaxError("Error while parsing the input tokens.")

    #--------------------------------------------------------- Class functions
    
    def build(self, *args, **kwargs):
        return yacc.yacc(module=self, *args, **kwargs)
