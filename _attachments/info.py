#!/usr/bin/env python
# (c) 2012 g33k @ libxenon.org 

import os
import struct
import sys

FIXMCRS = ["POI_VM", "PU_VM", "GPIO_Wakeup"]
VMVP = ["VoiceMacro", "VoicePrompt"]
ONOFF = ["on","off"]


def toInt(array):
	ret = 0
	for c in reversed(array):
		ret <<= 8
		ret += c
	return ret

def no_func(dat):
	return ""

SRATES = [4, 5.33, 6.4, 8, 12.8, 16, 32]

def cfg_reg0(dat):
	return "sample rate %.2f kHz" % (SRATES[dat>>5])
	
def cfg_reg1(dat):
	str = ""
	if (dat & 0x20) > 0:
		str += "LRMP "
	if (dat & 0x10) > 0:
		str += "CFG0_READ "
	if (dat & 0x04) > 0:
		str += "NRMP "
	if (dat & 0x02) > 0:
		str += "SRSIL "
	if (dat & 0x01) > 0:
		str += "SRCFG "
	return str
	
def cfg_reg2(dat):
	str = ""
	if (dat & 0x40) > 0:
		str += "DECODE "
	if (dat & 0x20) > 0:
		str += "SPI_IN "
	if (dat & 0x04) > 0:
		str += "PWM_OUT "
	if (dat & 0x01) > 0:
		str += "SPI_OUT "
	return str
	
def volc(dat):
	return "+%.2fdB" % (dat * 0.25)
	
PWMFRQ = [287, 420, 862, 1260, 84, 125, 166, 245]
	
def cfg_reg9(dat):
	return "PWM: %dkHz  Dither: %d" % (PWMFRQ[dat>>5], dat & 0x03)
	
REGS = [[0x00, "CFG_REG0", cfg_reg0],
				[0x01, "CFG_REG1", cfg_reg1],
				[0x02, "CFG_REG2", cfg_reg2],
				[0x03, "VOLC", volc],
				[0x04, "CFG_REG4", no_func],
				[0x09, "CFG_REG9", cfg_reg9],
				[0x19, "GPIO_DO", no_func],
				[0x1A, "GPIO_OE", no_func],
				[0x1B, "GPIO_PE", no_func],
				[0x1C, "GPIO_DIN", no_func],
				[0x1D, "GPIO_PS", no_func],
				[0x1E, "GPIO_AF1", no_func], [0x1F, "GPIO_AF0", no_func],
				[0x20, "R0[7:0]", no_func], [0x21, "R0[15:8]", no_func],
				[0x22, "R1[7:0]", no_func], [0x23, "R1[15:8]", no_func],
				[0x24, "R2[7:0]", no_func], [0x25, "R2[15:8]", no_func],
				[0x26, "R3[7:0]", no_func], [0x27, "R3[15:8]", no_func],
				[0x28, "R4[7:0]", no_func], [0x29, "R4[15:8]", no_func],
				[0x2A, "R5[7:0]", no_func], [0x2B, "R5[15:8]", no_func],
				[0x2C, "R6[7:0]", no_func], [0x2D, "R6[15:8]", no_func],
				[0x2E, "R7[7:0]", no_func], [0x2F, "R7[15:8]", no_func]]

def play_vp(dat):
	return "%8d" % ((dat[0]<<8) + dat[1])
	
def play_sil(dat):
	return "%dms" % (dat[0]*32)
		
def set_clk_cfg(dat):
	return "0x%02X" % (dat[0])
	
def wr_cfg_reg(dat):
	for i in REGS:
		if i[0] == dat[0]:
			return "%8s = 0x%02X  %s" % (i[1], dat[1], i[2](dat[1]))
	return "0x%02X = 0x%02X" % (dat[0], dat[1])
	
OPCODES = [ [0x10, 1, "PWR_UP", no_func],
						[0x12, 1, "PWR_DWN", no_func],
						[0xA6, 3, "PLAY_VP", play_vp],
						[0xA8, 2, "PLAY_SIL", play_sil],
						[0xB4, 2, "SET_CLK_CFG", set_clk_cfg],
						[0xB8, 3, "WR_CFG_REG", wr_cfg_reg],
						[0xFC, 3, "UKNOWN", no_func],
						[0xFF, 3, "?NOP?", no_func] ]
						 
def printMacro(macro):
	i = 0
	while i < len(macro):
		for cmd in OPCODES:
			if cmd[0] == macro[i]:
				print "  %10s  %s" % (cmd[2], cmd[3](macro[i+1:i+cmd[1]]))
				i += cmd[1]
				break
	
		
# main
if len(sys.argv) < 2:
	print "usage: %s FILE" % (sys.argv[0])
	sys.exit()

dump = bytearray(open(sys.argv[1], "rb").read())
print "%s  size: 0x%X (%d Bytes)" % (os.path.basename(sys.argv[1]), len(dump), len(dump))
print

if (dump[0] & 0xF0) <> 0XC0:
	print "invalid dump (must start with 0xCX)"
	sys.exit()

print "Header: 0x%02X" % (dump[0])
print "   RP: %s" % (ONOFF[(dump[0] & 0x04) > 0])
print "   WP: %s" % (ONOFF[(dump[0] & 0x02) > 0])
print "  CEP: %s" % (ONOFF[(dump[0] & 0x01) > 0])
print
print

print "PMP: 0x%04X" % (toInt(dump[3:5]))
print
print

vmstart = toInt(dump[5:8])

for i in range(0, len(FIXMCRS)):
	start = toInt(dump[(i*6+5):(i*6+8)])
	end = toInt(dump[(i*6+8):(i*6+11)])
	print "%s: 0x%05X to 0x%05X" % (FIXMCRS[i], start, end)
	print "  length: %d Bytes" % (end - start)
	print 
	printMacro(dump[start:end+1])
	print
	print

i = len(FIXMCRS)
while 1:
	start = toInt(dump[(i*6+5):(i*6+8)])
	end = toInt(dump[(i*6+8):(i*6+11)])
	if start >= 0xffff00:
		break
	voice = start < vmstart
	print "%s %d: 0x%05X to 0x%05X" % (VMVP[voice], i, start, end)
	print "  length: %d Bytes" % (end - start)
	print
	if not voice: 
		printMacro(dump[start:end+1])
		print
	i += 1
	print
