
# create instruction in a lazy way


regs = (
    '$zero','$at','$v0','$v1','$a0','$a1','$a2','$a3',
    '$t0','$t1','$t2','$t3','$t4','$t5','$t6','$t7',
    '$s0','$s1','$s2','$s3','$s4','$s5','$s6','$s7',
    '$t8','$t9','$k0','$k1','$gp','$sp','$fp','$ra'
)


def rid(name):
    return regs.index(name.lower())



#################### R-type

def r(rd, rs, rt, shamt, funct):
    op = 0
    return funct + (shamt<<6) + (rid(rd)<<11) + (rid(rt)<<16) + (rid(rs)<<21) + (op<<26)


def add(rd, rs, rt):
    shamt = 0
    funct = 0x100000
    return r(rd, rs, rt, shamt, funct)

def sub(rd, rs, rt):
    shamt = 0
    funct = 0x100011
    return r(rd, rs, rt, shamt, funct)

def and_(rd, rs, rt):
    shamt = 0
    funct = 0x100100
    return r(rd, rs, rt, shamt, funct)

def or_(rd, rs, rt):
    shamt = 0
    funct = 0x100101
    return r(rd, rs, rt, shamt, funct)


def slt(rd, rs, rt):
    shamt = 0
    funct = 0x101010
    return r(rd, rs, rt, shamt, funct)


################## I-type


def i(op, rs, rt, offset):
    return offset + (rid(rt)<<16) + (rid(rs)<<21) + (op<<26)


def addi(rt, rs, imm):
    op = 0x001000
    return i(op, rs, rt, imm)


def lw(rt, rs, offset):
    op = 0x100011
    return i(op, rs, rt, offset)
    

def sw(rt, rs, offset):
    op = 0x101011
    return i(op, rs, rt, offset)

def beq(rs, rt, offset):
    op = 0x000100
    return i(op, rs, rt, offset)


################## J-type


def j(target):
    op = 0x000010
    return target + (op<<26)


def syscall():
    op = 0x000000
    funct = 0x001100
    return funct + (op<<26)




