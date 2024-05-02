#coding=utf-8

MSR = 1
MAR = 2
MDR = 3
RAM = 4
IR = 5
DST = 6
SRC = 7
AX = 8
BX = 9
CX = 10
DX = 11
DI = 12
SI = 13
SP = 14
BP = 15
CS = 16
DS = 17
SS = 18
ES = 19
VEC = 20
T1 = 21
T2 = 21

MSR_OUT=MSR
MAR_OUT=MAR
MDR_OUT=MDR
RAM_OUT=RAM
IR_OUT=IR
DST_OUT=DST
SRC_OUT=SRC
AX_OUT=AX
BX_OUT=BX
CX_OUT=CX
DX_OUT=DX
DI_OUT=DI
SI_OUT=SI
SP_OUT=SP
BP_OUT=BP
CS_OUT=CS
DS_OUT=DS
SS_OUT=SS
ES_OUT=ES
VEC_OUT=VEC
T1_OUT=T1
T2_OUT=T2

_DST_SHIFT = 5

MSR_IN=MSR << _DST_SHIFT
MAR_IN=MAR << _DST_SHIFT
MDR_IN=MDR << _DST_SHIFT
RAM_IN=RAM << _DST_SHIFT
IR_IN=IR << _DST_SHIFT
DST_IN=DST << _DST_SHIFT
SRC_IN=SRC << _DST_SHIFT
AX_IN=AX << _DST_SHIFT
BX_IN=BX << _DST_SHIFT
CX_IN=CX << _DST_SHIFT
DX_IN=DX << _DST_SHIFT
DI_IN=DI << _DST_SHIFT
SI_IN=SI << _DST_SHIFT
SP_IN=SP << _DST_SHIFT
BP_IN=BP << _DST_SHIFT
CS_IN=CS << _DST_SHIFT
DS_IN=DS << _DST_SHIFT
SS_IN=SS << _DST_SHIFT
ES_IN=ES << _DST_SHIFT
VEC_IN=VEC << _DST_SHIFT
T1_IN=T1 << _DST_SHIFT
T2_IN=T2 << _DST_SHIFT

SRC_R = 2 ** 10
SRC_W = 2 ** 11
DST_R = 2 ** 12
DST_W = 2 ** 13

PC_WE = 2 ** 14
PC_CS = 2 ** 15
PC_EN = 2 ** 16

PC_OUT = PC_CS
PC_IN = PC_CS | PC_WE
PC_INC = PC_CS | PC_WE | PC_EN

HLT = 2 ** 31