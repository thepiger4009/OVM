/*
OVM - Owl Virtual Machine
Development Build: 72023r1

Copyright (c) 2022-2023
*/

package main

import (
	"fmt"
)

func LD3() { //LD # - Load a value into a register
	switch memory[ovm_m.pc+1] {
	case 1:
		ovm_m.x = memory[ovm_m.pc+2]
	case 2:
		ovm_m.y = memory[ovm_m.pc+2]
	case 3:
		ovm_m.t = memory[ovm_m.pc+2]
	case 4:
		ovm_m.p = memory[ovm_m.pc+2]
	case 5:
		ovm_m.u = memory[ovm_m.pc+2]
	}
	ovm_m.pc += 3
}

func LD4() { //LD $ - Load a address into a register
	switch memory[ovm_m.pc+1] {
	case 1:
		ovm_m.x = memory[memory[ovm_m.pc+2]]
	case 2:
		ovm_m.y = memory[memory[ovm_m.pc+2]]
	case 3:
		ovm_m.t = memory[memory[ovm_m.pc+2]]
	case 4:
		ovm_m.p = memory[memory[ovm_m.pc+2]]
	case 5:
		ovm_m.u = memory[memory[ovm_m.pc+2]]
	}
	ovm_m.pc += 3

}

func LD5p() { //LD $%p - Load a address+p into a register
	switch memory[ovm_m.pc+1] {
	case 1:
		ovm_m.x = memory[memory[ovm_m.pc+2]+ovm_m.p]
	case 2:
		ovm_m.y = memory[memory[ovm_m.pc+2]+ovm_m.p]
	case 3:
		ovm_m.t = memory[memory[ovm_m.pc+2]+ovm_m.p]
	case 4:
		ovm_m.p = memory[memory[ovm_m.pc+2]+ovm_m.p]
	case 5:
		ovm_m.u = memory[memory[ovm_m.pc+2]+ovm_m.p]
	}
	ovm_m.pc += 3
}

func LD5u() { //LD $%u - Load a address+u into a register
	switch memory[ovm_m.pc+1] {
	case 1:
		ovm_m.x = memory[memory[ovm_m.pc+2]+ovm_m.u]
	case 2:
		ovm_m.y = memory[memory[ovm_m.pc+2]+ovm_m.u]
	case 3:
		ovm_m.t = memory[memory[ovm_m.pc+2]+ovm_m.u]
	case 4:
		ovm_m.p = memory[memory[ovm_m.pc+2]+ovm_m.u]
	case 5:
		ovm_m.u = memory[memory[ovm_m.pc+2]+ovm_m.u]
	}
	ovm_m.pc += 3
}

func TRF() { //TRF x,y - transfer a register to a register
	switch memory[ovm_m.pc+1] {
	case 1:
		switch memory[ovm_m.pc+2] {
		case 1:
			ovm_m.x = ovm_m.x
		case 2:
			ovm_m.x = ovm_m.y
		case 3:
			ovm_m.x = ovm_m.t
		case 4:
			ovm_m.x = ovm_m.p
		case 5:
			ovm_m.x = ovm_m.u
		}
	case 2:
		switch memory[ovm_m.pc+2] {
		case 1:
			ovm_m.y = ovm_m.x
		case 2:
			ovm_m.y = ovm_m.y
		case 3:
			ovm_m.y = ovm_m.t
		case 4:
			ovm_m.y = ovm_m.p
		case 5:
			ovm_m.y = ovm_m.u
		}
	case 3:
		switch memory[ovm_m.pc+2] {
		case 1:
			ovm_m.t = ovm_m.x
		case 2:
			ovm_m.t = ovm_m.y
		case 3:
			ovm_m.t = ovm_m.t
		case 4:
			ovm_m.t = ovm_m.p
		case 5:
			ovm_m.t = ovm_m.u
		}
	case 4:
		switch memory[ovm_m.pc+2] {
		case 1:
			ovm_m.p = ovm_m.x
		case 2:
			ovm_m.p = ovm_m.y
		case 3:
			ovm_m.p = ovm_m.t
		case 4:
			ovm_m.p = ovm_m.p
		case 5:
			ovm_m.p = ovm_m.u
		}
	case 5:
		switch memory[ovm_m.pc+2] {
		case 1:
			ovm_m.u = ovm_m.x
		case 2:
			ovm_m.u = ovm_m.y
		case 3:
			ovm_m.u = ovm_m.t
		case 4:
			ovm_m.u = ovm_m.p
		case 5:
			ovm_m.u = ovm_m.u
		}
	}
	ovm_m.pc += 3
}

func ADD() { //ADD x,y - add a register to a register
	switch memory[ovm_m.pc+1] {
	case 1:
		switch memory[ovm_m.pc+2] {
		case 1:
			ovm_m.x = ovm_m.x + ovm_m.x
		case 2:
			ovm_m.x = ovm_m.x + ovm_m.y
		case 3:
			ovm_m.x = ovm_m.x + ovm_m.t
		case 4:
			ovm_m.x = ovm_m.x + ovm_m.p
		case 5:
			ovm_m.x = ovm_m.x + ovm_m.u
		}
	case 2:
		switch memory[ovm_m.pc+2] {
		case 1:
			ovm_m.y = ovm_m.x + ovm_m.x
		case 2:
			ovm_m.y = ovm_m.x + ovm_m.y
		case 3:
			ovm_m.y = ovm_m.x + ovm_m.t
		case 4:
			ovm_m.y = ovm_m.x + ovm_m.p
		case 5:
			ovm_m.y = ovm_m.x + ovm_m.u
		}
	case 3:
		switch memory[ovm_m.pc+2] {
		case 1:
			ovm_m.t = ovm_m.x + ovm_m.x
		case 2:
			ovm_m.t = ovm_m.x + ovm_m.y
		case 3:
			ovm_m.t = ovm_m.x + ovm_m.t
		case 4:
			ovm_m.t = ovm_m.x + ovm_m.p
		case 5:
			ovm_m.t = ovm_m.x + ovm_m.u
		}
	case 4:
		switch memory[ovm_m.pc+2] {
		case 1:
			ovm_m.p = ovm_m.x + ovm_m.x
		case 2:
			ovm_m.p = ovm_m.x + ovm_m.y
		case 3:
			ovm_m.p = ovm_m.x + ovm_m.t
		case 4:
			ovm_m.p = ovm_m.x + ovm_m.p
		case 5:
			ovm_m.p = ovm_m.x + ovm_m.u
		}
	case 5:
		switch memory[ovm_m.pc+2] {
		case 1:
			ovm_m.u = ovm_m.x + ovm_m.x
		case 2:
			ovm_m.u = ovm_m.x + ovm_m.y
		case 3:
			ovm_m.u = ovm_m.x + ovm_m.t
		case 4:
			ovm_m.u = ovm_m.x + ovm_m.p
		case 5:
			ovm_m.u = ovm_m.x + ovm_m.u
		}
	}
	ovm_m.pc += 3
}

func SUB() { //SUB x,y - subtract a register from a register
	switch memory[ovm_m.pc+1] {
	case 1:
		switch memory[ovm_m.pc+2] {
		case 1:
			ovm_m.x = ovm_m.x - ovm_m.x
		case 2:
			ovm_m.x = ovm_m.x - ovm_m.y
		case 3:
			ovm_m.x = ovm_m.x - ovm_m.t
		case 4:
			ovm_m.x = ovm_m.x - ovm_m.p
		case 5:
			ovm_m.x = ovm_m.x - ovm_m.u
		}
	case 2:
		switch memory[ovm_m.pc+2] {
		case 1:
			ovm_m.y = ovm_m.x - ovm_m.x
		case 2:
			ovm_m.y = ovm_m.x - ovm_m.y
		case 3:
			ovm_m.y = ovm_m.x - ovm_m.t
		case 4:
			ovm_m.y = ovm_m.x - ovm_m.p
		case 5:
			ovm_m.y = ovm_m.x - ovm_m.u
		}
	case 3:
		switch memory[ovm_m.pc+2] {
		case 1:
			ovm_m.t = ovm_m.x - ovm_m.x
		case 2:
			ovm_m.t = ovm_m.x - ovm_m.y
		case 3:
			ovm_m.t = ovm_m.x - ovm_m.t
		case 4:
			ovm_m.t = ovm_m.x - ovm_m.p
		case 5:
			ovm_m.t = ovm_m.x - ovm_m.u
		}
	case 4:
		switch memory[ovm_m.pc+2] {
		case 1:
			ovm_m.p = ovm_m.x - ovm_m.x
		case 2:
			ovm_m.p = ovm_m.x - ovm_m.y
		case 3:
			ovm_m.p = ovm_m.x - ovm_m.t
		case 4:
			ovm_m.p = ovm_m.x - ovm_m.p
		case 5:
			ovm_m.p = ovm_m.x - ovm_m.u
		}
	case 5:
		switch memory[ovm_m.pc+2] {
		case 1:
			ovm_m.u = ovm_m.x - ovm_m.x
		case 2:
			ovm_m.u = ovm_m.x - ovm_m.y
		case 3:
			ovm_m.u = ovm_m.x - ovm_m.t
		case 4:
			ovm_m.u = ovm_m.x - ovm_m.p
		case 5:
			ovm_m.u = ovm_m.x - ovm_m.u
		}
	}
	ovm_m.pc += 3
}

func CMP() { //CMP x,# - Compare register with value, if true set equal to 1
	switch memory[ovm_m.pc+1] {
	case 1:
		if ovm_m.x == memory[ovm_m.pc+2] {
			ovm_m.e = 1
		}
	case 2:
		if ovm_m.y == memory[ovm_m.pc+2] {
			ovm_m.e = 1
		}
	case 3:
		if ovm_m.t == memory[ovm_m.pc+2] {
			ovm_m.e = 1
		}
	case 4:
		if ovm_m.p == memory[ovm_m.pc+2] {
			ovm_m.e = 1
		}
	case 5:
		if ovm_m.u == memory[ovm_m.pc+2] {
			ovm_m.e = 1
		}
	}
	ovm_m.pc += 3
}

func CPA() { //CPA $,# - Compare address with value, if true set equal to 1
	if memory[memory[ovm_m.pc+1]] == memory[ovm_m.pc+2] {
		ovm_m.e = 1
	}
	ovm_m.pc += 3
}

func INC() { //INC x - Plus 1 by register
	switch memory[ovm_m.pc+1] {
	case 1:
		ovm_m.x += 1
	case 2:
		ovm_m.y += 1
	case 3:
		ovm_m.t += 1
	case 4:
		ovm_m.p += 1
	case 5:
		ovm_m.u += 1
	}
	ovm_m.pc += 2
}

func DEC() { //DEC X - Minus 1 by register
	switch memory[ovm_m.pc+1] {
	case 1:
		ovm_m.x -= 1
	case 2:
		ovm_m.y -= 1
	case 3:
		ovm_m.t -= 1
	case 4:
		ovm_m.p -= 1
	case 5:
		ovm_m.u -= 1
	}
	ovm_m.pc += 2
}

func ST4() { //ST x,$ - Store register in address
	switch memory[ovm_m.pc+1] {
	case 1:
		memory[memory[ovm_m.pc+2]] = ovm_m.x
	case 2:
		memory[memory[ovm_m.pc+2]] = ovm_m.y
	case 3:
		memory[memory[ovm_m.pc+2]] = ovm_m.t
	case 4:
		memory[memory[ovm_m.pc+2]] = ovm_m.p
	case 5:
		memory[memory[ovm_m.pc+2]] = ovm_m.u
	}
	ovm_m.pc += 3
}

func ST5p() { //ST x,$p - Store register in address+p
	switch memory[ovm_m.pc+1] {
	case 1:
		memory[memory[ovm_m.pc+2+ovm_m.p]] = ovm_m.x
	case 2:
		memory[memory[ovm_m.pc+2+ovm_m.p]] = ovm_m.y
	case 3:
		memory[memory[ovm_m.pc+2+ovm_m.p]] = ovm_m.t
	case 4:
		memory[memory[ovm_m.pc+2+ovm_m.p]] = ovm_m.p
	case 5:
		memory[memory[ovm_m.pc+2+ovm_m.p]] = ovm_m.u
	}
	ovm_m.pc += 3
}

func ST5u() { //ST x,$u - Store register in address+u
	switch memory[ovm_m.pc+1] {
	case 1:
		memory[memory[ovm_m.pc+2+ovm_m.u]] = ovm_m.x
	case 2:
		memory[memory[ovm_m.pc+2+ovm_m.u]] = ovm_m.y
	case 3:
		memory[memory[ovm_m.pc+2+ovm_m.u]] = ovm_m.t
	case 4:
		memory[memory[ovm_m.pc+2+ovm_m.u]] = ovm_m.p
	case 5:
		memory[memory[ovm_m.pc+2+ovm_m.u]] = ovm_m.u
	}
	ovm_m.pc += 3
}

func JMP() { //JMP $ - Go to a new address
	ovm_m.pc = memory[ovm_m.pc+1]
}

func JOE() { //JOE $ - Go to a new address if equal is 1
	if ovm_m.e == 1 {
		ovm_m.pc = memory[ovm_m.pc+1]
		ovm_m.e = 0
	}
}

func JNE() { //JNE $ - Go to a new address if equal is not 1
	if ovm_m.e == 0 {
		ovm_m.pc = memory[ovm_m.pc+1]
	}
}

func JSP() { //JSP $ - Go to a new address while saving the past address
	ovm_m.stack[ovm_m.sp] = ovm_m.pc
	ovm_m.pc = memory[ovm_m.pc+1]
	ovm_m.sp += 1
}

func RTP() { //RTP - Return to a past address
	ovm_m.sp -= 1
	ovm_m.pc = ovm_m.stack[ovm_m.sp]
}

func DSP() { //DSP M x - Display something
	switch memory[ovm_m.pc+1] {
	case 1: //Value Mode, no new line
		switch memory[ovm_m.pc+2] {
		case 1:
			fmt.Print(ovm_m.x)
		case 2:
			fmt.Print(ovm_m.y)
		case 3:
			fmt.Print(ovm_m.t)
		case 4:
			fmt.Print(ovm_m.p)
		case 5:
			fmt.Print(ovm_m.u)
		}
		ovm_m.pc += 3 //Note Keep this, needed since this op includes differences
	case 2: //Ascii Mode, no new line
		switch memory[ovm_m.pc+2] {
		case 1:
			fmt.Print(string(ovm_m.x))
		case 2:
			fmt.Print(string(ovm_m.y))
		case 3:
			fmt.Print(string(ovm_m.t))
		case 4:
			fmt.Print(string(ovm_m.p))
		case 5:
			fmt.Print(string(ovm_m.u))
			ovm_m.pc += 3
		}
	case 3: //Display a new line
		fmt.Println("")
		ovm_m.pc += 2
	case 4: //Display a space
		fmt.Print(" ")
		ovm_m.pc += 2
	case 5: //Backspace
		fmt.Printf("\b \b")
		ovm_m.pc += 2
	}
}

func PSH() { //PSH x - Push a register onto the stack
	switch memory[ovm_m.pc+1] {
	case 1:
		ovm_m.stack[ovm_m.sp] = ovm_m.x
	case 2:
		ovm_m.stack[ovm_m.sp] = ovm_m.y
	case 3:
		ovm_m.stack[ovm_m.sp] = ovm_m.t
	case 4:
		ovm_m.stack[ovm_m.sp] = ovm_m.p
	case 5:
		ovm_m.stack[ovm_m.sp] = ovm_m.u
	}
	ovm_m.sp += 1
	ovm_m.pc += 2
}

func PUL() { //PUL x - Pull from the stack onto the register
	ovm_m.sp -= 1
	switch memory[ovm_m.pc+1] {
	case 1:
		ovm_m.x = ovm_m.stack[ovm_m.sp]
	case 2:
		ovm_m.y = ovm_m.stack[ovm_m.sp]
	case 3:
		ovm_m.t = ovm_m.stack[ovm_m.sp]
	case 4:
		ovm_m.p = ovm_m.stack[ovm_m.sp]
	case 5:
		ovm_m.u = ovm_m.stack[ovm_m.sp]
	}
	ovm_m.pc += 2
}
