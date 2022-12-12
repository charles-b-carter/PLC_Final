from Node import Tree


class Parser:
    def __init__(self, lexemes):
        self.prevToken = "null"
        self.index = -1
        self.nextToken = "null"
        self.eof = False
        self.parseTree = Tree()
        self.root = None

        self.lex = lexemes

        if len(self.lex) > 0:
            self.getNextToken()

        # Hello All keywords in this programming language are written with a single character Boolean values can only
        # be stored in boolean type variables and the values can only be 1 or 0 All conditional statements are
        # resolved by boolean characters logic can be implemented inside of loops and statements to modify the
        # boolean values in order to change the conditions
        #

        # START => '{'<statement>
        # <statement> => <SPOS> | <PRFM> | <ASN> | <BLOCK>| <END> | <DEC>
        # <DEC> => 'NUM1'|'NUM2'|'NUM4'|'NUM8'|'STRING'|'BOOL'|'CHAR'|'REAL'{'ASN_OP''IDENT'}'SEP'
        # <BLOCK> => '['{<statement}']'
        # <SPOS> => '#''('{<BOOL>')'<statement>}
        # <FON> => '$''('{<BOOL>')'<statement>}
        # <EXP> => <TRM>{{'MOD'|'ADD'|'SUB'}<TRM>}
        # <TRM> => <LOG>{{'MULT'|'DIV'}<LOG>}
        # <LOG> => <BOL>{{'LAND'|'LNOT'|'LOR'}<BOL>}
        # <BOOL> => <FCT>{'LT'|'GT'|'LTE'|'GTE'|'EQ'}<FCT>
        # <FCT> => IDENT | LIT | REAL_LIT | S_LIT <EXP>
        # <ASN> => 'IDENT'{'ASN_OP'<EXP>}'SEP'
        # <END> => '}'

        # print(self.lex)

        if not self.lex[-1] == 'END':
            print("\nEND ERROR")
            self.error()

        if not self.lex[0] == 'START':
            # if not S then error
            print("\nSTART ERROR")
            self.error()

        while not self.eof:
            print("index=" + str(self.index) + ", next token = " + self.nextToken)
            #
            if (self.nextToken == 'START') or (self.nextToken == 'END'):
                self.root = self.parseTree.insert(self.root, self.nextToken)
                print("skip = " + self.nextToken)
                self.getNextToken()
            # A (statement)
            elif (self.nextToken == 'SPOS') or (self.nextToken == 'FON') or (self.nextToken == 'PRFM') \
                    or (self.nextToken == 'LBRK') or (self.nextToken == 'ASN_DES'):
                self.statement()
            # B (declaration)
            elif (self.nextToken == 'NUM1') or (self.nextToken == 'NUM2') or (self.nextToken == 'NUM4') or (
                    self.nextToken == 'STRING_VAR') \
                    or (self.nextToken == 'REAL') or (self.nextToken == 'BOL'):
                self.dec()

            elif (self.nextToken == 'LIT') or (self.nextToken == 'IDENT') or (self.nextToken == 'LPAR') or \
                    (self.nextToken == 'REAL_LIT') or (
                    self.nextToken == 'ADD') or (
                    self.nextToken == 'SUB') or (self.nextToken == 'MULT') or (self.nextToken == 'DIV') or (
                    self.nextToken == 'IDENT'):
                self.exp()
            # elif (x == 'IDENT') or (x == "LIT"):
            #     self.exp()
            else:
                self.parseTree.insert(self.root, self.nextToken)
                # self.getNextToken()
                print("DRIVER ERROR")
                self.error()

        print(self.lex)

    def getNextToken(self):
        if self.index < (len(self.lex) - 1):
            self.prevToken = self.lex[self.index]
            self.index = self.index + 1
            self.nextToken = self.lex[self.index]
            print("--gnt--")
            print("next token = " + self.nextToken)
            print("-------")

            if self.nextToken == 'END':
                self.eof = True
                self.root = self.parseTree.insert(self.root, "END")

                print(self.nextToken)

            return self.nextToken
        else:
            self.eof = True
        # self.nextToken = self.lex[self.index]

    def fct(self):
        print("fact = " + self.nextToken)
        self.parseTree.insert(self.root, "FCT = " + self.nextToken)
        if (self.nextToken == 'IDENT') or (self.nextToken == 'LIT') or (self.nextToken == 'REAL_LIT') or (
                self.nextToken == 'S_LIT') or (self.nextToken == 'CHAR_LIT') or (
                self.nextToken == 'BLIT'):
            self.getNextToken()
            return True

            print("in index=" + str(self.index) + ", next token = " + self.nextToken)
            # print("in nxt nxttoken = " + self.nextToken)

        elif self.nextToken == 'LPAR':
            self.getNextToken()

            print("in in index=" + str(self.index) + ", next token = " + self.nextToken)
            # print("in inn nxt tokensoken = " + self.nextToken)

            self.exp()
            if self.nextToken == 'RPAR':
                print("rpar succes")
                self.getNextToken()
                return True
            else:
                print("PARENTHESES ERROR")
                self.error()
        else:
            print("FCT ERROR")

    def trm(self):
        self.parseTree.insert(self.root, "TRM = " + self.nextToken)
        print("trm = " + self.nextToken)
        self.log()
        while (self.nextToken == 'DIV') or (self.nextToken == 'MUL'):
            self.getNextToken()
            return self.log()

    def bol(self):
        self.parseTree.insert(self.root, "bol" + self.nextToken)
        print("bol = " + self.nextToken)
        self.fct()
        while (self.nextToken == 'EQ') or (self.nextToken == 'GT') or (self.nextToken == 'LT') \
                or (self.nextToken == 'GTE') or (self.nextToken == 'LTE'):
            self.getNextToken()
            return self.fct()

    def log(self):
        self.parseTree.insert(self.root, "bol" + self.nextToken)
        print("bol = " + self.nextToken)
        self.bol()
        while (self.nextToken == 'LAND') or (self.nextToken == 'LOR') or (self.nextToken == 'LNOT'):
            self.getNextToken()
            return self.bol()

    def exp(self):
        self.parseTree.insert(self.root, "EXP = " + self.nextToken)
        if not ((self.nextToken == 'SEP') or (self.nextToken == 'START') or (self.nextToken == 'END')):
            print("exp = " + self.nextToken)
            self.trm()
            while (self.nextToken == 'ADD') or (self.nextToken == 'SUB') or (self.nextToken == 'MOD'):
                self.getNextToken()
                return self.trm()
        else:
            print("exp skip = " + self.nextToken)
            self.getNextToken()

    def statement(self):
        self.parseTree.insert(self.root, self.nextToken)
        print("statement = " + self.lex[self.index])
        print(self.lex[self.index])
        if self.nextToken == 'SPOS':
            self.spos()
        elif self.nextToken == 'ASN_DES':
            self.asn()
        elif self.nextToken == 'FON':
            self.fon()
        elif self.nextToken == 'PRFM':
            self.prfm()
        elif self.nextToken == 'LBRK':
            self.block()
        pass

    def block(self):
        self.parseTree.insert(self.root, self.nextToken)
        print("block = " + self.lex[self.index])
        if self.nextToken == 'LBRK':
            self.getNextToken()
            while (self.nextToken == 'FON') or (self.nextToken == 'IDENT') or (
                    self.nextToken == 'SPOS') \
                    or (self.nextToken == 'ASN_DES'):
                self.statement()

        if self.lex[self.index] == 'RBRK':
            print("block success")
            self.getNextToken()
        else:
            print("BLOCK ERROR")
            self.error()

        pass

    def fon(self):
        # fon(if) statement must start with $ char and then have an exp or ident in the parentheses to evaluate
        print("fon = " + self.nextToken)
        if self.nextToken == 'FON':
            self.getNextToken()
            if self.nextToken == 'LPAR':
                self.exp()
                if self.nextToken == 'LBRK':
                    self.statement()
                    print("FON SUCCESS")

                # if self.nextToken == 'LBRK':
                #     self.statement()
                #     print("FON SUCCESS")
                #     return True
            else:
                print("FON PARENTHESES ERROR")
                self.error()
            self.getNextToken()
        pass

    def spos(self):
        # fon(if) statement must start with $ char and then have an exp or ident in the parentheses to evaluate
        print("spos = " + self.nextToken)
        if self.nextToken == 'SPOS':
            self.getNextToken()
            if self.nextToken == 'LPAR':
                self.exp()
                if self.nextToken == 'LBRK':
                    self.statement()
                    print("SPOS SUCCESS")

                # if self.nextToken == 'LBRK':
                #     self.statement()
                #     print("FON SUCCESS")
                #     return True
            else:
                print("SPOS PARENTHESES ERROR")
                self.error()
            self.getNextToken()
        pass

    def dec(self):
        self.parseTree.insert(self.root, "DEC = " + self.nextToken)
        print("dec = " + self.nextToken)
        self.getNextToken()
        if self.nextToken == 'IDENT':
            self.parseTree.insert(self.root, "DEC = " + self.nextToken)
            self.getNextToken()
            # print(self.nextToken)
            if self.nextToken == 'SEP':
                self.parseTree.insert(self.root, "DEC = " + self.nextToken)
                print("DEC SUCCESS")
                self.getNextToken()
                return True
                # self.exp()
            else:
                print("MUST HAVE SEPERATOR AFTER DECLARATION")
                self.error()
        else:
            print("DECLARATION ERROR")
            self.error()

        pass

    def asn(self):
        self.parseTree.insert(self.root, self.nextToken)
        print("ASN = " + self.nextToken)
        self.getNextToken()
        if self.nextToken == 'IDENT':
            self.getNextToken()
            if self.nextToken == 'ASN_OP':
                self.getNextToken()
                if (self.nextToken == 'IDENT') or (self.nextToken == 'LIT') or (self.nextToken == 'REAL') or (
                        self.nextToken == 'SLIT') or (
                        self.nextToken == 'NAT'):
                    self.getNextToken()
                    if self.nextToken == 'SEP':
                        print("ASN SUCCESS")
                        self.getNextToken()
                        return True
                    else:
                        print("MUST HAVE SEPERATOR AFTER ASSIGNMENT")
                        self.error()
        else:
            print("ASSIGNMENT")

        pass

    def error(self):
        print("\nSYNTAX ERROR")
        exit()
