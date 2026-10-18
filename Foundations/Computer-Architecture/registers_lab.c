/*
 * Day 1 Lab Target: C Program for Assembly & GDB Register Disassembly
 * Cybersecurity Master Roadmap - Phase 1: Foundations
 * Author: dvsh03 (Cybersecurity Portfolio)
 *
 * Objective:
 * Demonstrates the x86_64 System V AMD64 Calling Convention:
 * - 1st argument (x = 15 = 0x0F) passed into RDI register
 * - 2nd argument (y = 25 = 0x19) passed into RSI register
 * - Function return value (total = 40 = 0x28) returned in RAX register
 * - Function Prologue (push rbp; mov rbp, rsp; sub rsp, N)
 * - Function Epilogue (leave; ret)
 */

#include <stdio.h>

int calculate(int x, int y) {
    int sum = x + y;
    return sum;
}

int main() {
    int a = 15;
    int b = 25;
    int total = calculate(a, b);
    printf("[+] Calculated Sum: %d\n", total);
    return 0;
}
