	.data
str_nl: .asciz "\n"
	.text
j main
max3:
	addi sp,sp,28
	sw ra,(sp)
L2:
	lw t1, -12(gp)
	add,t1,t1,t2
L3:
	lw t1,-28(sp)
	sw t1, -12(gp)
L4:
	lw t1,-12(sp)
	lw t2,-16(sp)
	bgt,t1,t2,L6
L5:
	b L10
L6:
	lw t1,-12(sp)
	lw t2,-20(sp)
	bgt,t1,t2,L8
L7:
	b L10
L8:
	lw t1,-12(sp)
	sw t1, -24(sp)
L9:
	b L17
L10:
	lw t1,-16(sp)
	lw t2,-12(sp)
	bgt,t1,t2,L12
L11:
	b L16
L12:
	lw t1,-16(sp)
	lw t2,-20(sp)
	bgt,t1,t2,L14
L13:
	b L16
L14:
	lw t1,-16(sp)
	sw t1, -24(sp)
L15:
	b L17
L16:
	lw t1,-20(sp)
	sw t1, -24(sp)
L17:
	lw t1,-24(sp)
	lw t0, -8(sp)
	sw t1, 0(t0)
L18:
	addi sp,sp,-32
	lw ra,(sp)
	jr ra
fib:
	addi sp,sp,24
	sw ra,(sp)
L20:
	lw t1, -12(gp)
	add,t1,t1,t2
L21:
	lw t1,-16(sp)
	sw t1, -12(gp)
L22:
	lw t1,-12(sp)
	blt,t1,t2,L24
L23:
	b L27
L24:
	sub,t1,t1,t2
L25:
	lw t0, -8(sp)
	sw t1, 0(t0)
L26:
	b L43
L27:
	lw t1,-12(sp)
	beq,t1,t2,L31
L28:
	b L29
L29:
	lw t1,-12(sp)
	beq,t1,t2,L31
L30:
	b L33
L31:
	lw t0, -8(sp)
	sw t1, 0(t0)
L32:
	b L43
L33:
	lw t1,-12(sp)
	sub,t1,t1,t2
L34:
	sw t0,-12(fp)
L35:
	addi t0,sp,-20
	sw t0,-8(fp)
L36:
	lw t0,-4(sp)
	sw t0,-4(fp)
	addi sp,sp,28
	jal fib
L37:
	lw t1,-12(sp)
	sub,t1,t1,t2
L38:
	sw t0,-16(fp)
L39:
	addi t0,sp,-24
	sw t0,-8(fp)
L40:
	lw t0,-4(sp)
	sw t0,-4(fp)
	addi sp,sp,28
	jal fib
L41:
	lw t1,-20(sp)
	lw t2,-24(sp)
	add,t1,t1,t2
L42:
	lw t0, -8(sp)
	sw t1, 0(t0)
L43:
	addi sp,sp,-28
	lw ra,(sp)
	jr ra
divides:
	addi sp,sp,20
	sw ra,(sp)
L46:
	lw t1, -12(gp)
	add,t1,t1,t2
L47:
	lw t1,-20(sp)
	sw t1, -12(gp)
L48:
	lw t1,-16(sp)
	lw t0,-4(sp)
	lw t2,0(t0)
	div,t1,t1,t2
L49:
	lw t0,-4(sp)
	lw t2,0(t0)
	mul,t1,t1,t2
L50:
	lw t1,-16(sp)
	beq,t1,t2,L52
L51:
	b L54
L52:
	lw t0, -8(sp)
	sw t1, 0(t0)
L53:
	b L55
L54:
	lw t0, -8(sp)
	sw t1, 0(t0)
L55:
	addi sp,sp,-24
	lw ra,(sp)
	jr ra
isPrime:
	addi sp,sp,28
	sw ra,(sp)
L56:
	lw t1, -12(gp)
	add,t1,t1,t2
L57:
	lw t1,-20(sp)
	sw t1, -12(gp)
L58:
	sw t1, -16(sp)
L59:
	lw t1,-16(sp)
	lw t2,-12(sp)
	blt,t1,t2,L61
L60:
	b L72
L61:
	lw t0,-16(sp)
	sw t0,-20(fp)
L62:
	lw t0,-12(sp)
	sw t0,-24(fp)
L63:
	addi t0,sp,-24
	sw t0,-8(fp)
L64:
	sw sp,-4(fp)
	addi sp,sp,24
	jal divides
L65:
	lw t1,-24(sp)
	beq,t1,t2,L67
L66:
	b L69
L67:
	lw t0, -8(sp)
	sw t1, 0(t0)
L68:
	b L73
L69:
	lw t1,-16(sp)
	add,t1,t1,t2
L70:
	lw t1,-28(sp)
	sw t1, -16(sp)
L71:
	b L59
L72:
	lw t0, -8(sp)
	sw t1, 0(t0)
L73:
	addi sp,sp,-32
	lw ra,(sp)
	jr ra
sqr:
	addi sp,sp,16
	sw ra,(sp)
L76:
	lw t1, -12(gp)
	add,t1,t1,t2
L77:
	lw t1,-16(sp)
	sw t1, -12(gp)
L78:
	lw t0,-4(sp)
	lw t1,0(t0)
	lw t0,-4(sp)
	lw t2,0(t0)
	mul,t1,t1,t2
L79:
	lw t0, -8(sp)
	sw t1, 0(t0)
L80:
	addi sp,sp,-20
	lw ra,(sp)
	jr ra
quad:
	addi sp,sp,32
	sw ra,(sp)
L81:
	lw t1, -12(gp)
	add,t1,t1,t2
L82:
	lw t1,-20(sp)
	sw t1, -12(gp)
L83:
	lw t0,-12(sp)
	sw t0,-28(fp)
L84:
	addi t0,sp,-24
	sw t0,-8(fp)
L85:
	sw sp,-4(fp)
	addi sp,sp,20
	jal sqr
L86:
	lw t0,-12(sp)
	sw t0,-32(fp)
L87:
	addi t0,sp,-28
	sw t0,-8(fp)
L88:
	sw sp,-4(fp)
	addi sp,sp,20
	jal sqr
L89:
	lw t1,-24(sp)
	lw t2,-28(sp)
	mul,t1,t1,t2
L90:
	lw t1,-32(sp)
	sw t1, -16(sp)
L91:
	lw t1,-16(sp)
	lw t0, -8(sp)
	sw t1, 0(t0)
L92:
	addi sp,sp,-36
	lw ra,(sp)
	jr ra
leap:
	addi sp,sp,16
	sw ra,(sp)
L94:
	lw t1, -12(gp)
	add,t1,t1,t2
L95:
	lw t1,-16(sp)
	sw t1, -12(gp)
L96:
L97:
	beq,t1,t2,L99
L98:
	b L102
L99:
L100:
	bne,t1,t2,L105
L101:
	b L102
L102:
L103:
	beq,t1,t2,L105
L104:
	b L107
L105:
	lw t0, -8(sp)
	sw t1, 0(t0)
L106:
	b L108
L107:
	lw t0, -8(sp)
	sw t1, 0(t0)
L108:
	addi sp,sp,-20
	lw ra,(sp)
	jr ra
main:
	addi sp,sp,48
	sw ra,(sp)
L110:
	sw t1, -12(gp)
L111:
	li a7,5
	ecall
L112:
	mv a0,t0
	li a7,1
	ecall
	la a0,str_nl
	li a7,4
	ecall
L113:
	sw t1, -16(gp)
L114:
	lw t1, -16(gp)
	ble,t1,t2,L116
L115:
	b L123
L116:
	lw t0, -16(gp)
	sw t0,-36(fp)
L117:
	addi t0,sp,-20
	sw t0,-8(fp)
L118:
	sw sp,-4(fp)
	addi sp,sp,20
	jal leap
L119:
	mv a0,t0
	li a7,1
	ecall
	la a0,str_nl
	li a7,4
	ecall
L120:
	lw t1, -16(gp)
	add,t1,t1,t2
L121:
	lw t1, -24(gp)
	sw t1, -16(gp)
L122:
	b L114
L123:
	sw t0,-40(fp)
L124:
	addi t0,sp,-28
	sw t0,-8(fp)
L125:
	sw sp,-4(fp)
	addi sp,sp,20
	jal leap
L126:
	mv a0,t0
	li a7,1
	ecall
	la a0,str_nl
	li a7,4
	ecall
L127:
	sw t0,-44(fp)
L128:
	addi t0,sp,-32
	sw t0,-8(fp)
L129:
	sw sp,-4(fp)
	addi sp,sp,20
	jal leap
L130:
	mv a0,t0
	li a7,1
	ecall
	la a0,str_nl
	li a7,4
	ecall
L131:
	sw t0,-48(fp)
L132:
	addi t0,sp,-36
	sw t0,-8(fp)
L133:
	sw sp,-4(fp)
	addi sp,sp,36
	jal quad
L134:
	mv a0,t0
	li a7,1
	ecall
	la a0,str_nl
	li a7,4
	ecall
L135:
	sw t0,-52(fp)
L136:
	addi t0,sp,-40
	sw t0,-8(fp)
L137:
	sw sp,-4(fp)
	addi sp,sp,28
	jal fib
L138:
	mv a0,t0
	li a7,1
	ecall
	la a0,str_nl
	li a7,4
	ecall
L139:
	sw t1, -16(gp)
L140:
	lw t1, -16(gp)
	ble,t1,t2,L142
L141:
	b L149
L142:
	lw t0, -16(gp)
	sw t0,-56(fp)
L143:
	addi t0,sp,-44
	sw t0,-8(fp)
L144:
	sw sp,-4(fp)
	addi sp,sp,32
	jal isPrime
L145:
	mv a0,t0
	li a7,1
	ecall
	la a0,str_nl
	li a7,4
	ecall
L146:
	lw t1, -16(gp)
	add,t1,t1,t2
L147:
	lw t1, -48(gp)
	sw t1, -16(gp)
L148:
	b L140
L149:
	mv a0,t0
	li a7,1
	ecall
	la a0,str_nl
	li a7,4
	ecall
L150:
L151:
exit:
	li a0,0
	li a7,93
	ecall
