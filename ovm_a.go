/*
OVM - Owl Virtual Machine
Development Build: 72123r1

Copyright (c) 2022-2023
*/

package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
)

var memory [524288]uint32 //Memory
var io uint32             //Interface Output

var display_state = 0

type ovm_core struct {
	op            uint32      //Opcode Register
	x, y, t, p, u uint32      //Universal Registers
	pc            uint32      //Program Counter
	sp            uint8       //Stack Pointer
	stack         [256]uint32 //Stack
	e, m, o, i    byte        //Equal, math, overflow, and interrupt flags
}

var ovm_m ovm_core
var boot_rom []uint32 = []uint32{114, 400}

func PR_LOAD() {
	file := os.Args[1:]
	name := strings.Join(file, " ")
	var PR_LOAD_Count int = 0
	f, err := os.Open(name)
	if err != nil {
		log.Fatal(err)
	}
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		READ_LINE := scanner.Text()
		if READ_LINE == "ADDR" {
			scanner.Scan()
			READ_LINE := scanner.Text()
			PR_LOAD_Count, _ = strconv.Atoi(READ_LINE)
			PR_LOAD_Count = PR_LOAD_Count + 0 //RETARD FIX
		} else {
			READ_LINE, _ := strconv.Atoi(READ_LINE)
			memory[PR_LOAD_Count] = uint32(READ_LINE)
			PR_LOAD_Count += 1
		}
		f.Close()
	}

}
