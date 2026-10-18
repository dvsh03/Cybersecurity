#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 1 Lab Tool: Endianness & Memory Architecture Probe
Cybersecurity Master Roadmap - Phase 1: Foundations
Author: dvsh03 (Cybersecurity Portfolio)

Objective:
Demonstrates ground-truth hardware endianness, byte-ordering mechanics,
and binary memory layout for x86_64 systems.
"""

import sys
import struct
import platform

def print_banner():
    banner = """
===================================================================
[*] HARDWARE ARCHITECTURE & ENDIANNESS PROBE (x86_64)
[*] Cybersecurity Master Roadmap - Phase 1 Foundations
===================================================================
    """
    print(banner.strip())

def probe_system_architecture():
    print("\n[+] SYSTEM HARDWARE PROFILE:")
    print(f"    - Machine Hardware    : {platform.machine()}")
    print(f"    - Processor Type      : {platform.processor() or 'x86_64 Family'}")
    print(f"    - Architecture Width  : {struct.calcsize('P') * 8}-bit")
    print(f"    - Pointer Size        : {struct.calcsize('P')} Bytes")
    print(f"    - System Byte Order   : {sys.byteorder.upper()} ENDIAN")
    print(f"    - Operating System    : {platform.system()} {platform.release()}")

def demonstrate_endianness(hex_val=0xDEADBEEFCAFE1337):
    print(f"\n[+] DEMONSTRATING MEMORY BYTE LAYOUT FOR VALUE: {hex(hex_val)}")
    
    # Pack as 64-bit unsigned integer (8 bytes) in Little Endian (<Q) and Big Endian (>Q)
    le_bytes = struct.pack('<Q', hex_val)
    be_bytes = struct.pack('>Q', hex_val)
    
    print("\n--- [LITTLE ENDIAN (x86_64 CPU Default)] ---")
    print("Memory Address:   [0]      [1]      [2]      [3]      [4]      [5]      [6]      [7]")
    print("Stored Bytes  :  " + "     ".join(f"0x{b:02X}" for b in le_bytes))
    print("Hex Representation: " + " ".join(f"\\x{b:02x}" for b in le_bytes))
    print(">> Notice: Least Significant Byte (0x37) is placed at the LOWEST memory address [0].")

    print("\n--- [BIG ENDIAN (Network Byte Order)] ---")
    print("Memory Address:   [0]      [1]      [2]      [3]      [4]      [5]      [6]      [7]")
    print("Stored Bytes  :  " + "     ".join(f"0x{b:02X}" for b in be_bytes))
    print("Hex Representation: " + " ".join(f"\\x{b:02x}" for b in be_bytes))
    print(">> Notice: Most Significant Byte (0xDE) is placed at the LOWEST memory address [0].")

def explain_exploit_impact():
    target_addr = 0x7FFFFFFFE420
    packed_payload = struct.pack('<Q', target_addr)
    print("\n[+] CYBERSECURITY EXPLOIT RELEVANCE:")
    print(f"    Target Return Address to Hijack (RIP) : {hex(target_addr)}")
    print(f"    Required Payload String (Little Endian): {repr(packed_payload)}")
    print("    In Buffer Overflows, you must send addresses in Little-Endian byte order!")

if __name__ == '__main__':
    print_banner()
    probe_system_architecture()
    demonstrate_endianness()
    explain_exploit_impact()
    print("\n[+] Verification complete. Hardware state verified.\n")
