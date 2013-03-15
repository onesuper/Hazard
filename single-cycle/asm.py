





text_section_start = 0x00400000
data_section_start = 0x10000000




code = '''
# small program
                .data
value1:		.word	12
value2:         .word   0x1
result:         .word  -1                   
		
		.text
main:	        lw      $t1, value1($zero)   # haha
                lw      $t2, value2($zero)   # hehe
                add     $t3, $t1, $t2        # xixi
                sw      $t3, result($zero)

'''

class Assembler(object):

    regs = (
	'$zero','$at','$v0','$v1','$a0','$a1','$a2','$a3',
	'$t0','$t1','$t2','$t3','$t4','$t5','$t6','$t7',
	'$s0','$s1','$s2','$s3','$s4','$s5','$s6','$s7',
	'$t8','$t9','$k0','$k1','$gp','$sp','$fp','$ra'
        )
    i_type = ('lw', 'sw')
    r_type = ('add')
    j_type = ()
    s_type = ()

    def _reg_id(name):
        try:
            return regs.index(name)
        except ValueError:
           raise 'register unknown' 

    def assemble(self, asm):
        import re

        # tokenize the asm code
        scanner=re.Scanner([
                (r'\.[a-z]+',                       lambda scanner, token : ('keyword', token)),
                (r'[a-z_]?[a-zA-Z0-9_]+:',          lambda scanner, token : ('label', token)),
                (r'[a-zA-Z0-9_]+\(\$[a-z0-9]+\)',   lambda scanner, token : ('offset+reg', token)),
                (r'[a-zA-Z]+',                      lambda scanner, token : ('op', token)),
                (r'[a-z_][a-zA-Z0-9_]+',            lambda scanner, token : ('ref', token)),
                (r'0x[0-9]+',                       lambda scanner, token : ('hex', token)),
                (r'-?[0-9]+',                       lambda scanner, token : ('dec', token)),
                (r'\$[a-z0-9]+',                    lambda scanner, token : ('reg', token)),
                (r'#.*|\s+|,',                      None),  # skip comments/whitespace/comma
                ])
        results, remainder=scanner.scan(asm)
        for r in results:
            print r




Assembler().assemble(code)
