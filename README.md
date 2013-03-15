


* single-cycle: a simplest datapath implementation.An implementation in 
which an instruction is executed in one clock cycle. It provides a smallest subsets of MIPS, including lw, sw, beq, j, add, sub, and, or, slt.


## Registers

$at, $k0, $k1: reserved for OS and assembler

$a0-$a3:  used to pass first 4 arguments to routine (rest passed on stack)

$v0, $v1: used for return values from functions

$t0-$t9:  caller-saved registers, used to hold temporaries, 
          not perserved across calls

$s0-$s7: callee-saved registers, hold long lived data
         should be preserved across calls

$gp:  global pointer points to middle of 64K block in static data segment

        addresses in .data are given relative to it:

        lw  $v0, 0x20($gp)

$sp: the stack pointer, points to last location on the stack

$fp: frame pointer 

$ra: the return address from procedure call
