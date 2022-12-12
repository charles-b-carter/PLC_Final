import Lexer
import Parser


class Compiler:
    def __init__(self, f):
        # read in file
        self.code = Lexer.Lexer(f)
        # get lexemes
        self.code.tokenize()
        self.code.format()
        self.code.match(self.code.lexeme)
        # match their codes
        for x in range(0, len(self.code.nTokens)):
            print("LEXEME: " + self.code.nTokens[x].lexeme + ",  CODE: " + str(self.code.nTokens[x].tokenCode))
        self.synta = Parser.Parser(self.code.frmtlexeme)
        # self.synta.parseTree.traverseInorder(self.synta.root)

