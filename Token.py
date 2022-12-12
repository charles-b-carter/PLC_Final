class Token:
    def __init__(self, lex, code):
        self.lexeme = lex
        self.tokenCode = code

        self.matchLex = {
            # START => {
            '{': 'START',
            # ASN_OP => =
            '=': 'ASN_OP',
            # SPOS => #
            '#': 'SPOS',
            # FON => $
            '$': 'FON',
            # ASN_DES => @
            '@': 'ASN_DES',
            # END => }
            '}': 'END',
            # NUM1 => ^1
            '^1': 'NUM1',
            # NUM2 => ^2
            '^2': 'NUM2',
            # NUM4 => ^4
            '^4': 'NUM4',
            # NUM4 => ^8
            '^8': 'NUM8',
            # REAL => ^r
            '^r': 'REAL',
            # NAT => ^n
            '^n': 'NAT',
            # BOL => ^b
            '^b': 'BOL',
            # STRING_VAR => ^s
            '^s': 'STRING_VAR',
            # CHAR => ^c
            '^c': 'CHAR',
            # ADD => +
            '+': 'ADD',
            # SUB => -
            '-': 'SUB',
            # MUL => *
            '*': 'MUL',
            # DIV => /
            '/': 'DIV',
            # MOD => %
            '%': 'MOD',
            # LT => <
            '<': 'LT',  # less than
            # GT => >
            '>': 'GT',  # greater than
            # LTE => <<=
            '<<=': 'LTE',  # less than equal to
            # GTE => <<=
            '>>=': 'GTE',  # greater than equal to
            # EQ => ===
            '===': 'EQ',  # equals
            # NEQ => !!!
            '!!!': 'NEQ',  # not equals
            # LPAR => (
            '(': 'LPAR',  # (
            # RPAR => )
            ')': 'RPAR',  # )
            # LBRK => [
            '[': 'LBRK',  # [
            # RBRK => ]
            ']': 'RBRK',  # ]
            # COL => :
            ':': 'COL',  # :
            # SEP => ;
            ';': 'SEP',  # ;
            # LAND => &&
            '&&': 'LAND',
            # LAND => &&
            '|': 'LOR',
            # LAND => &&
            '&&': 'LAND',
            # LNOT => |!
            '|!': 'LNOT'
        }
        self.tcode = {
            'START': '1',
            'ASN_OP': '2',
            'SPOS': '3',
            'FON': '4',
            'ASN_DES': '5',
            'END': '6',
            'NUM1': '7',
            'NUM2': '8',
            'NUM4': '9',
            'NUM8': '10',
            'REAL': '11',
            'NAT': '12',
            'BOL': '13',
            'STRING': '14',
            'ADD': '16',
            'SUB': '17',
            'MULT': '18',
            'DIV': '19',
            'MOD': '20',
            'LT': '21',  # less than
            'GT': '22',  # greater than
            'LTE': '23',  # less than equal to
            'GTE': '24',  # greater than equal to
            'EQ': '25',  # equals
            'NEQ': '26',  # not equals
            'LPAR': '27',  # (
            'RPAR': '28',  # )
            'LBRK': '29',  # [
            'RBRK': '30',  # ]
            'SEMI': '31',  # :
            'SEP': '15',  # ;
            'IDENT': '35',
            'S_LIT': '36',
            'REAL_LIT': '37',
            'CHAR_LIT': '38',
            'B_LIT': '39',
            'LAND': '40',
            'LOR': '41',
            'LNOT': '42'

        }

    # def mapTok(self, lexList):
    #         for x in lexList:







