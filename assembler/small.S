# A smallest program written in MIPS Assembly language
# Author: onesuper
# Email: onesuperclark@gmail.com


        .data   
var1:       .word       3
var2:       .word       2   


        .text
main:
        lw  $t0, var1
        lw  $t1, var2
        add $t2, $t1, $t0
        done
        