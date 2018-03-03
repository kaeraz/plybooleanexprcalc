import os
from Source.Lexer import Lexer
from Source.Parser import Parser
from serial.tools.miniterm import raw_input
import logging
import subprocess

# --------------------------------------------------------------------------
# MAIN program part
# --------------------------------------------------------------------------
_thisDirPath = os.path.abspath(os.path.dirname(__name__))


def main_lexer():
    # Construct lexer
    lexer = Lexer().build()
    
    # Give LEXER some input]
    while True:
        try:
            data = raw_input("<BoolCalc> ")
        except EOFError:
            print("Program terminated on demand...")
            break;
        if data:
            try:
                lexer.input(data)
                while True:
                    tok = lexer.token()
                    if not tok:
                        break # No more input
                    print("   {}".format(tok))
            except SyntaxError:
                print("Syntax Error!")
        else:
            print("Program terminated on demand...")
            break

def main_parser():
    # Construct lexer
    lexer = Lexer().build()
    # Construct parser
    parser = Parser(Lexer().tokens).build()
    
    # Give LEXER some input]
    while True:
        try:
            data = raw_input("BoolCalc>>> ")
        except EOFError:
            print("Program terminated on demand...")
            break;
        if data:
            try:
                # Parse the input text
                ast = parser.parse(input=data, lexer=lexer, tracking=False)
                ast.organize()
                # Open a graphviz dot script file
                try:
                    # Create a file and append AST data to it
                    file_name = "ast.txt"
                    sf = open(file_name, "w")
                    sf.write("digraph ast {")
                    sf.write("node [shape = circle];")
                    sf.write(ast.to_str())
                    sf.write("}")
                except:
                    print("Something went wrong while generating graph diagram...")
                else:
                    sf.close()
                    try:
                        # Generate a PDF graph with graphviz dot
                        p1 = subprocess.Popen("dot -Tpdf -O " + file_name)
                        p1.wait()
                        # Open a graph with default application
                        returncode = os.system("start " + file_name + ".pdf")
                        if returncode != 0:
                            raise Exception
                    except:
                        print("Something went wrong while opening graph diagram...")
                    else:
                        p1.kill()
            except SyntaxError:
                print("Syntax Error!")
        else:
            print("Program terminated on demand...")
            break

if __name__ == '__main__':
    print('*** Start of [{0}]'.format(__file__))
    
    logging.basicConfig(level=logging.INFO)
    
    main_parser()
    
    print('*** End of   [{0}]'.format(__file__))


