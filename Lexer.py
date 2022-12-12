import Token


class Lexer:
    def __init__(self, file):
        self.stringHolder = None
        f = open(file, "r")

        self.spf = []
        self.tokens = []
        self.nTokens = []
        self.lexeme = []
        self.frmtlexeme = []
        self.nextChar = 0
        self.varLength = 8
        self.count = 0
        self.assgnhold = ''
        self.bogdolist = []
        self.numbolist = []
        self.charClass = {
            'LETTER': 1,
            'DIGIT': 2,
            'UKNWN': 3,

        }
        self.bogrules = {'(', ')', '+', '*', '%', '-'}

        self.matchLex = {
            '{': 'START',
            '=': 'ASN_OP',
            '#': 'SPOS',
            '$': 'FON',
            '@': 'ASN_DES',
            '}': 'END',
            '^1': 'NUM1',
            '^2': 'NUM2',
            '^4': 'NUM4',
            '^8': 'NUM8',
            '^r': 'REAL',
            '^n': 'NAT',
            '^b': 'BOL',
            '^s': 'STRING_VAR',
            '^c': 'CHAR',
            '+': 'ADD',
            '-': 'SUB',
            '*': 'MUL',
            '/': 'DIV',
            '%': 'MOD',
            '<': 'LT',  # less than
            '>': 'GT',  # greater than
            '<<=': 'LTE',  # less than equal to
            '>>=': 'GTE',  # greater than equal to
            '===': 'EQ',  # equals
            '!!!': 'NEQ',  # not equals
            '(': 'LPAR',  # (
            ')': 'RPAR',  # )
            '[': 'LBRK',  # [
            ']': 'RBRK',  # ]
            ':': 'COL',  # :
            ';': 'SEP',  # ;
            # ' ': 'SPACE',  # white space
            ',': 'SEP',  # comma
            # '.': 'DOT',

        }
        #
        # self.rules = {
        #     "ASSIGN": 9,
        #     'ADD': 10,  # addition
        #     'SUB': 11,  # subtraction
        #     'MULT': 12,  # multiplication
        #     'DIVI': 13,  # division
        #     'MODU': 14,  # modulo
        #     'LT': 15,  # less than
        #     'GT': 16,  # greater than
        #     'LTE': 17,  # less than equal to
        #     'GTE': 18,  # greater than equal to
        #     'EQ': 19,  # equals
        #     'NEQ': 20,  # not equals
        #     'LEFT_PAR': 21,  # (
        #     'RIGHT_PAR': 22,  # )
        #     'LEFT_BRA': 23,  # [
        #     'RIGHT_BRA': 24,  # ]
        #     'COL': 25,  # :
        #     'SEMICOL': 26,  # ;
        #     'WS': 27,  # white space
        #     '1IF': 28,  # if
        #     '1WHILE': 29,  # while loop
        #     'SINT_LIT': 30,  # small int literal
        #     'MINT_LIT': 31,  # med int literal
        #     'LINT_LIT': 32,  # large int literal
        #     'COMMA': 33,  # comma
        #
        # }
        self.tcode = {
            '{': '1',
            '=': '2',
            '#': '3',
            '$': '4',
            '@': '5',
            '}': '6',
            '^1': '7',
            '^2': '8',
            '^4': '9',
            '^8': '10',
            '^r': '11',
            '^n': '12',
            '^b': '13',
            '^s': '14',
            '\n': '15',
            '+': '16',
            '-': '17',
            '*': '18',
            '/': '19',
            '%': '20',
            '<': '21',  # less than
            '>': '22',  # greater than
            '<=': '23',  # less than equal to
            '>=': '24',  # greater than equal to
            '==': '25',  # equals
            '!': '26',  # not equals
            '(': '27',  # (
            ')': '28',  # )
            '[': '29',  # [
            ']': '30',  # ]
            ':': '31',  # :
            ';': '15',  # ;
            # ' ': 'SPACE',  # white space
            ',': '32',  # comma
            '.': '33',
        }

        for x in f:
            self.spf.append(list(x))

    def tokenize(self):
        for x in self.spf:
            for i in x:
                self.tokens.append(i)
                # if i.isalnum():
                #     if i.isdigit():
                #         self.tokens.append(
                #             i)  ## mapping characters to char types based on if they are letters or numbers
                #     if i.isalpha():
                #         self.tokens.append(i)
                # else:
                #     if len(self.match(i)) > 0:
                #        # self.tokens.append(self.match(i))
                #         self.tokens.append(i)

    def match(self, x):
        for x in self.lexeme:
            # if the token is in the library then match it and add the lexeme
            if self.matchLex.get(x):
                self.frmtlexeme.append(self.matchLex.get(x))
                self.nTokens.append(Token.Token(self.matchLex.get(x), self.tcode.get(x)))
            if x[0] == '"':
                if x[-1] == '"':
                    self.frmtlexeme.append("SLIT")
                else:
                    print("CLOSE QOUTES ERROR")
                    self.error()
            if x.isalnum():
                # if x in self.keywords:
                #     self.frmtlexeme.append(x)
                if len(x) > 8:
                    self.error()
                # identifier => {a-zA-Z_}
                if x[0].isalpha():
                    if (len(str(x)) >= 6) & (len(str(x)) <= 8):
                        self.frmtlexeme.append("IDENT")
                        self.nTokens.append(Token.Token("IDENT", 99))
                    # else:
                    #     self.error()

            if str(x).isdecimal():
                self.frmtlexeme.append("LIT")
                self.nTokens.append(Token.Token("LIT", 97))

            elif x.isdigit():
                self.frmtlexeme.append("LIT")
                self.nTokens.append(Token.Token("LIT", 98))

                # if abs(int(x)) < 127:
                #     self.frmtlexeme.append("SMINT")
                # if (abs(int(x)) > 127) & (abs(int(x)) < 32767):
                #     self.frmtlexeme.append("1SHORT")
                #     print(x)
                # if (abs(int(x)) > 32768) & (abs(int(x)) < 2147483647):
                #     self.frmtlexeme.append("1MINT")
                #     print(x)
                # if (abs(int(x)) > 2147483647) & (abs(int(x)) < 9223372036854775807):
                #     self.frmtlexeme.append("1LUNG")

        # return list(map(,self.frmtlexeme))  ## mapping non alphanumeric char to lex

    def add_char(self, x):
        self.lexeme.append(x)

    def format(self):
        while self.count < (len(self.tokens)):
            if self.tokens[self.count] == ' ':
                self.count = self.count + 1
            ## if the token is not a letter or number

            if not str((self.tokens[self.count])).isalnum():
                # check for EQ or ASN
                # asn_op => =
                if self.tokens[self.count] == '=':
                    # EQ => =
                    if self.tokens[self.count + 1] == '=':
                        self.lexeme.append(self.tokens[self.count] + self.tokens[self.count])
                        self.count = self.count + 1
                    else:
                        self.lexeme.append(self.tokens[self.count])
                        self.count = self.count + 1
                    # neq => !!!
                if self.tokens[self.count] == '!':
                    if self.tokens[self.count + 1] == '!':
                        self.count = self.count + 1
                        if self.tokens[self.count + 1] == '!':
                            self.lexeme.append('!!!')

                elif self.tokens[self.count] == '^':
                    # check the size of the int variable being made
                    # num1 => ^1
                    if self.tokens[self.count + 1] == '1':
                        self.lexeme.append('^1')
                        self.count = self.count + 1
                    # num1 => ^2
                    if self.tokens[self.count + 1] == '2':
                        self.lexeme.append('^2')
                        self.count = self.count + 1
                    # num1 => ^4

                    if self.tokens[self.count + 1] == '4':
                        self.lexeme.append('^4')
                        self.count = self.count + 1
                    # num1 => ^8

                    if self.tokens[self.count + 1] == '8':
                        self.lexeme.append('^8')
                        self.count = self.count + 1
                    # check for non int data types

                    # real => ^r
                    if self.tokens[self.count + 1] == 'r':
                        self.lexeme.append('^r')
                        self.count = self.count + 1
                    # string => ^s
                    if self.tokens[self.count + 1] == 's':
                        self.lexeme.append('^s')
                        self.count = self.count + 1
                    # bool => ^b
                    if self.tokens[self.count + 1] == 'b':
                        self.lexeme.append('^b')
                        self.count = self.count + 1
                # check for gte and lte
                # lte (less than or equal too) => <<=
                elif self.tokens[self.count] == '<':
                    if self.tokens[self.count + 1] == '<':
                        self.count = self.count + 1
                        if self.tokens[self.count + 1] == '=':
                            self.lexeme.append('<<=')
                # gte (less than or equal too) => >>=
                elif self.tokens[self.count] == '>':
                    if self.tokens[self.count + 1] == '>':
                        self.count = self.count + 1
                        if self.tokens[self.count + 1] == '=':
                            self.lexeme.append('>>=')
                # check for string lit
                # string_lit =>  "{a-zA-Z,.\'\";:\\!@#%^&*()_-=+`~<>?/\t\n\f\b}\*"
                elif self.tokens[self.count] == '"':
                    self.stringHolder = self.tokens[self.count]
                    if self.tokens[self.count + 1].isalnum():
                        while self.tokens[self.count + 1].isalnum():
                            self.count = self.count + 1
                            self.stringHolder = self.tokens[self.count]

                        if self.tokens[self.count + 1] == '"':
                            self.stringHolder = self.tokens[self.count + 1]
                            self.lexeme.append(self.stringHolder)
                        else:
                            print("string error")
                            self.error()


                #   real => {0-9}\*.{0-9}\*
                elif str(self.tokens[self.count]).isdigit():
                    try:
                        if self.tokens[self.count + 1] == '.':
                            self.count = self.count + 1
                            if str(self.tokens[self.count + 1]).isdigit():
                                self.count = self.count + 1
                                self.lexeme.append(
                                    str(self.tokens[self.count - 2]) + str(self.tokens[self.count - 1]) + str(
                                        self.tokens[self.count]))
                    finally:
                        print("DECIMAL ERROR")
                        self.error()




                else:
                    self.lexeme.append(self.tokens[self.count])
                self.count = self.count + 1

                if self.count > (len(self.tokens) - 1):
                    break  # keep in bounds
            #
            while (str((self.tokens[self.count])).isalpha()) | (str((self.tokens[self.count])).isdigit()):

                self.assgnhold = self.assgnhold + self.tokens[self.count]
                self.count = self.count + 1

                if self.count > (len(self.tokens) - 1):
                    break  # keep in bounds

            if len(self.assgnhold) > 0:
                self.lexeme.append(self.assgnhold)
                # self.error()

            self.assgnhold = ''

        self.count = 0

    def error(self):
        print("LEXICAL ERROR")
        exit(code=1)
