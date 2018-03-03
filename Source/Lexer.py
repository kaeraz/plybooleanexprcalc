from ply import lex

# --------------------------------------------------------------------------
# PLY LEXER configuration
# --------------------------------------------------------------------------

class Lexer:
    
    #------------------------------------------------------------- Constructor
    
    def __init__(self):
        pass
    
    #------------------------------------------------------------------ Tokens
    
    # List of tokens
    tokens = [
            "INTEGER",
            "OR",
            "AND",
            "NOT",
            "LPAREN",
            "RPAREN"
        ]
    
    # Ignored comment pattern
    t_ignore_COMMENT = r'(/\*(.|\n)*?\*/)|(//.*)|(\#.*)'
    
    # Regular expression rules for simple tokens
    t_OR = r"\|"
    t_AND = r"&"
    t_NOT= r"!"
    t_LPAREN = r"\("
    t_RPAREN = r"\)"
    
    t_ignore = ' \t'
    
    # Regular expression rules for complex tokens
    def t_INTEGER(self, t):
        r"\d+\b"
        t.value = int(t.value)
        return t
    
    def t_newline(self, t):
        r"(\r\n)+|(\n)+|(\r)+"
        t.lexer.lineno += len(t.value)

    def t_eof(self, t):
        return None

    def t_error(self, t):
        raise SyntaxError

    #--------------------------------------------------------- Class functions
    
    def build(self, *args, **kwargs):
        return lex.lex(module=self, *args, **kwargs)

