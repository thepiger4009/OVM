/*
OVM - Owl Virtual Machine
Development Build: 72123r1

Copyright (c) 2022-2023
*/

package main

import (
	"fmt"
	"os"

	"github.com/eiannone/keyboard"
)

func ovm_init() {
	for i := 0; i < len(boot_rom); i++ { //Initialize memory
		memory[i] = boot_rom[i]
	}

	PR_LOAD()

	go func() { //Keyboard & Timer & Interrupt handler
		for {
			key, _, err := keyboard.GetSingleKey()
			if err != nil {
				panic(err)
			}
			memory[524287] = uint32(key)
			switch memory[524287] {
			case 92:
				os.Exit(4)
			case 95:
				switch display_state {
				case 1:
					display_state = 0
					fmt.Print("\033[H\033[2J")
				case 0:
					display_state = 1
				}
			}
			memory[524286] += 1
			if memory[524286] > 60 {
				memory[524286] = 0
			}
			if ovm_m.i == 1 {
				ovm_m.i = 0
				ovm_m.stack[ovm_m.sp] = ovm_m.pc
				ovm_m.pc = 524285
			}
			if display_state == 1 {
				fmt.Print("\033[H\033[2J")
				fmt.Println("x:", ovm_m.x, "y:", ovm_m.y, "t:", ovm_m.t, "p:", ovm_m.p, "u:", ovm_m.u, "op:", ovm_m.op)
				fmt.Println("pc:", ovm_m.pc, "sp:", ovm_m.sp, "e:", ovm_m.e, "o:", ovm_m.o, "i:", ovm_m.i)
			}
		}
	}()

	ovm_main()
}

func ovm_main() {
	for { //Main Execution Loop
		ovm_m.op = memory[ovm_m.pc]
		switch ovm_m.op {
		case 100:
			LD3() //LD #,x
		case 101:
			LD4() //LD $,x
		case 102:
			LD5p() //LD $p
		case 103:
			LD5u() //LD $u
		case 104:
			TRF() //TRF x
		case 105:
			ADD() //ADD x,y
		case 106:
			SUB() //SUB x,y
		case 107:
			CMP() //CMP x,#
		case 108:
			CPA() //CPA $,#
		case 109:
			INC() //INC x
		case 110:
			DEC() //DEC x
		case 111:
			ST4() //ST x,$
		case 112:
			ST5p() //ST $p
		case 113:
			ST5u() //ST $u
		case 114:
			JMP() //JMP $
		case 115:
			JOE() //JOE $
		case 116:
			JNE() //JNE $
		case 117:
			JSP() //JSP $
		case 118:
			RTP() //RTP
		case 119:
			DSP() //DSP M x
		case 120:
			PSH() //PSH x
		case 121:
			PUL() //PUL x
		}
	}
}

func main() {
	ovm_init()
}
