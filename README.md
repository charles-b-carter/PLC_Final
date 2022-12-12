# PLC_Final
        #Charles Carter
        # Hello All keywords in this programming language are written with a single character Boolean values can only
        # be stored in boolean type variables and the values can only be 1 or 0 All conditional statements are
        # resolved by boolean characters logic can be implemented inside of loops and statements to modify the
        # boolean values in order to change the conditions

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
        
        # START => {
        # ASN_OP => =
        # SPOS => #
        # FON => $
        # ASN_DES => @
        # END => }
        # NUM1 => ^1
        # NUM2 => ^2
        # NUM4 => ^4
        # NUM4 => ^8
        # REAL => ^r
        # NAT => ^n
        # BOL => ^b
        # STRING_VAR => ^s
        # CHAR => ^c
        # ADD => +
        # SUB => -
        # MUL => *
        # DIV => /
        # MOD => %
        # LT => <
        # GT => >
        # LTE => <<=
        # GTE => <<=
        # EQ => ===
        # NEQ => !!!
        # LPAR => (
        # RPAR => )
        # LBRK => [
        # RBRK => ]
        # COL => :
        # SEP => ;
        # LAND => &&
        # LOR => |
        # LNOT => |!
