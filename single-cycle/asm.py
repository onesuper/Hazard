

from obj import Obj
from exception import AsmException 



class Assembler(object):

    regs = (
	'$zero','$at','$v0','$v1','$a0','$a1','$a2','$a3',
	'$t0','$t1','$t2','$t3','$t4','$t5','$t6','$t7',
	'$s0','$s1','$s2','$s3','$s4','$s5','$s6','$s7',
	'$t8','$t9','$k0','$k1','$gp','$sp','$fp','$ra'
        )

    def _reg_id(self, name):
        try:
            return regs.index(name)
        except ValueError:
           raise AsmException('Unknown register: {0}'.format(name))


    def _mk_i_type(self, op, rs, rt, imm):
        return imm + (rt<<16) + (rs<<21) + (op<<26)

    def _mk_r_type(self, op, rs, rt, rd, shamt, funct):
        return funct + (shamt<<6) + (rd<<11) + (rt<<16) + (rs<<21) + (op<<26)

    def _mk_j_type(self, op, addr):
        return addr + (op<<26)


    def _put_text(self, obj, inst):
        obj.text_section.append(inst & 0xff)
        obj.text_section.append((inst & 0xff00)>>8)
        obj.text_section.append((inst & 0xff0000)>>16)
        obj.text_section.append((inst & 0xff000000)>>24)
        return len(obj.text_section)-4


    # put data according to its datatype(a string)
    def _put_data(self, obj, datatype, valuestr):
        if datatype == '.word':
            # little endian assumed!
            obj.data_section.append(eval(valuestr) & 0xff)
            obj.data_section.append((eval(valuestr) & 0xff00)>>8)
            obj.data_section.append((eval(valuestr) & 0xff000)>>16)
            obj.data_section.append((eval(valuestr) & 0xff000000)>>24)
            return len(obj.data_section)-4
        else:
            raise AsmException('Unknown data type: {0}'.format(datatype))


    def assemble(self, asm):

        obj = Obj()
        symbol_table = {}


        # tokenize the asm code
        import re
        scanner=re.Scanner([
                (r'\.[a-z]+', lambda scanner, token : ('keyword', token)),
                (r'[a-z_]?[a-zA-Z0-9_]+:', lambda scanner, token : ('label', token)),
                (r'[a-zA-Z0-9_]+\(\$[a-z0-9]+\)', lambda scanner, token : ('offset+reg', token)),
                (r'[a-zA-Z]+', lambda scanner, token : ('op', token)),
                (r'[a-z_][a-zA-Z0-9_]+', lambda scanner, token : ('ref', token)),
                (r'0x[0-9]+', lambda scanner, token : ('hex', token)),
                (r'-?[0-9]+', lambda scanner, token : ('dec', token)),
                (r'\$[a-z0-9]+', lambda scanner, token : ('reg', token)),
                (r'#.*|\s+|,', None),  # skip comments/whitespace/comma
                ])
        tokens, remainder=scanner.scan(asm)
        
        literals = [a[1] for a in tokens]
        if not '.text' in literals:     # assure there is .text
            raise '.text is missing'
        
        # if .data exists, split the tokens into two parts
        if '.data' in literals:      
            data_start = literals.index('.data')
            text_start = literals.index('.text')
            if data_start < text_start:  # data section as the first part
                data_tokens = tokens[1:text_start]                
                text_tokens = tokens[text_start+1:len(tokens)]
            else:  # text section as the first part
                text_tokens = tokens[1:data_start]
                data_tokens = tokens[data_start+1:len(tokens)]
            # build the data_labels while layouting the data
            for i in range(0, len(data_tokens), 3):
                if data_tokens[i][0] == 'label':
                    symbol_table = [data_tokens[i][1]] = self._put_data(obj, data_tokens[i+1][1], data_tokens[i+2][1])
                else:
                    raise AsmException('there must be a label first')
            print symbol_table
            print text_tokens
            print obj

            # loop through the text tokens
            i = 0
            while i<len(text_tokens):
                (token_type, token_name) = text_tokens[i]
                if token_type == 'label':
                    print 'label'
                    
                elif token_type == 'op':
                    if token_name.lower() == 'lw':
                        instr = self._mk_i_type(0x100011, text_tokens[i+1][1], text_tokens[i+2][1])
                    elif token_name.lower() == 'sw':
                        pass
                    else:
                        raise AsmException('opcode:{0} not supported'.format(token_name))
                    
                

code = '''
# small program
                .data
value1:		.word	12
value2:         .word   0x1
result:         .word  -1                   
		
		.text
main:	        lw      $t1, value1($)   # haha
                lw      $t2, value2($gp)   # hehe
                add     $t3, $t1, $t2      # xixi
                sw      $t3, result($)

'''

Assembler().assemble(code)
