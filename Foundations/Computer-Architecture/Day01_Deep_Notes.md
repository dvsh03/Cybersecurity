# 🔬 Day 1: CPU Silicon Architecture, x86_64 Registers & Memory Mechanics

> **Phase 1: Computer Architecture & Operating Systems Internals**  
> *Author: dvsh03 | Cybersecurity Engineering Portfolio*  
> *Track: Tier 1 — Foundation | Standard: x86_64 System V AMD64 ABI*

---

## 🏛️ 1. Silicon Foundations: The Von Neumann Architecture

Modern computation relies on the **Von Neumann Architecture**, which unifies program instructions and application data inside the same physical memory space.

### Core Physical Components:
1. **Central Processing Unit (CPU):**
   - **Arithmetic Logic Unit (ALU):** Performs integer arithmetic (`ADD`, `SUB`, `IMUL`) and bitwise logical operations (`AND`, `OR`, `XOR`, `NOT`, `SHL`, `SHR`).
   - **Control Unit (CU):** Manages the microcode execution, clock timing pulses, and directs the flow of data between CPU registers and system memory.
   - **Internal Registers:** Ultra-fast Static RAM (SRAM) cells embedded directly inside the processor core operating at CPU core clock speeds (gigahertz frequencies with sub-nanosecond latency).
2. **System Buses (Hardware Interconnects):**
   - **Control Bus:** Transmits read/write strobes, interrupt requests (`IRQ`), and clock synchronizations between CPU and system chipset.
   - **Address Bus:** Unidirectional bus specifying the physical or virtual memory address being targeted. A 64-bit architecture supports up to $2^{64}$ addressable bytes (16 Exabytes theoretical limit).
   - **Data Bus:** Bidirectional transmission highway transferring raw data words between memory and CPU cache lines.

---

## ⚡ 2. The 5-Stage Microscopic Instruction Execution Cycle

Every assembly instruction executed by the CPU goes through five hardware stages:

```text
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  1. FETCH   │ ──> │  2. DECODE  │ ──> │ 3. EXECUTE  │ ──> │  4. MEMORY  │ ──> │ 5. WRITEBACK│
│  (Read RIP) │     │ (Opcode ID) │     │  (ALU Math) │     │  (RAM Read) │     │  (Save Reg) │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
```

1. **Instruction Fetch (IF):** The Control Unit queries the address stored in the **`RIP`** register, pulling the instruction bytes across the memory bus into the internal Instruction Register (`IR`).
2. **Instruction Decode (ID):** The decoder deconstructs opcode bytes (e.g., `0x48 0x89 0xE5` -> `mov rbp, rsp`), determines required operands, and sets internal execution flags.
3. **Execute (EX):** The ALU executes the operation or calculates effective memory addresses (e.g., `[rbp - 0x10]`).
4. **Memory Access (MEM):** If operands involve memory operands (such as dereferencing pointers), data is fetched from or written to L1/L2 cache or RAM.
5. **Write-Back (WB):** Output results are committed back to the designated destination register, and `RIP` is incremented to point to the immediate subsequent instruction.

---

## 🧩 3. x86_64 Register Hierarchy & Sub-Register Slicing

64-bit x86_64 processors provide 16 primary General Purpose Registers (`RAX` through `R15`), each 64 bits (8 bytes) wide. For backwards compatibility with 32-bit (x86) and 16-bit (8086) architectures, these registers are sub-divided into nested addressable registers.

### Sub-Register Anatomy Diagram:

```text
Bit: 63                                31              15       7      0
    ┌──────────────────────────────────┬───────────────┬────────┬───────┐
    │                                  │               │   AH   │  AL   │  -> AX (16-bit)
    │                                  ├───────────────┴────────┴───────┤
    │                                  │              EAX (32-bit)      │
    ├──────────────────────────────────┴────────────────────────────────┤
    │                            RAX (64-bit)                           │
    └───────────────────────────────────────────────────────────────────┘
```

### Complete x86_64 Register Map:

| 64-Bit Register | 32-Bit Sub | 16-Bit Sub | 8-Bit Low | 8-Bit High | System V AMD64 Calling Convention Role |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`RAX`** | `EAX` | `AX` | `AL` | `AH` | **Function Return Value** & System Call Number |
| **`RBX`** | `EBX` | `BX` | `BL` | `BH` | Callee-saved general base register |
| **`RCX`** | `ECX` | `CX` | `CL` | `CH` | **4th Function Argument** & Loop/String counter |
| **`RDX`** | `EDX` | `DX` | `DL` | `DH` | **3rd Function Argument** & Arithmetic/IO data |
| **`RSI`** | `ESI` | `SI` | `SIL` | - | **2nd Function Argument** & Source index pointer |
| **`RDI`** | `EDI` | `DI` | `DIL` | - | **1st Function Argument** & Destination index pointer |
| **`RBP`** | `EBP` | `BP` | `BPL` | - | Base/Frame Pointer (Anchors base of current stack frame) |
| **`RSP`** | `ESP` | `SP` | `SPL` | - | Stack Pointer (Points to the current top of the stack) |
| **`RIP`** | `EIP` | `IP` | - | - | Instruction Pointer (Holds address of next instruction) |
| **`R8`** | `R8D` | `R8W` | `R8B` | - | **5th Function Argument** |
| **`R9`** | `R9D` | `R9W` | `R9B` | - | **6th Function Argument** |
| **`R10`–`R11`**| `R10D`–`R11D` | `R10W`–`R11W` | `R10B`–`R11B` | - | Temporary scratch registers (Caller-saved) |
| **`R12`–`R15`**| `R12D`–`R15D` | `R12W`–`R15W` | `R12B`–`R15B` | - | Callee-saved general purpose registers |
| **`RFLAGS`** | `EFLAGS` | `FLAGS` | - | - | Processor Status: `ZF` (Zero), `CF` (Carry), `SF` (Sign), `OF` (Overflow) |

### 🔥 Exploit Engineering Insight: Null-Byte Elimination
In binary exploitation, strings are terminated by null bytes (`\x00`). If a shellcode payload contains a null byte, functions like `strcpy()` terminate early, breaking the exploit.
* Moving zero into a 64-bit register generates null bytes:  
  `mov rax, 0` -> Machine code: `\x48\xc7\xc0\x00\x00\x00\x00` (4 Null bytes!)
* Expert shellcode authors leverage sub-registers or XOR:  
  `xor eax, eax` -> Machine code: `\x31\xc0` (Zero null bytes)  
  `mov al, 59`   -> Machine code: `\xb0\x3b` (Sets syscall 59 `sys_execve` with zero null bytes!)

---

## 🔄 4. Endianness: Physical Byte Ordering in Memory

Memory is addressable at the single-byte level. When data larger than 1 byte (such as a 64-bit quadword) is stored, the CPU must follow a standardized byte order.

### Comparing Endianness for Value `0xDEADBEEFCAFE1337`:

```text
Byte Position:      [Byte 7] [Byte 6] [Byte 5] [Byte 4] [Byte 3] [Byte 2] [Byte 1] [Byte 0]
Hex Value:             DE       AD       BE       EF       CA       FE       13       37

Memory Address:       0x00     0x01     0x02     0x03     0x04     0x05     0x06     0x07
LITTLE ENDIAN (x86):  0x37     0x13     0xFE     0xCA     0xEF     0xBE     0xAD     0xDE
BIG ENDIAN (Network): 0xDE     0xAD     0xBE     0xEF     0xCA     0xFE     0x13     0x37
```

* **Little Endian (x86_64 CPU Default):** The Least Significant Byte (`0x37`) is stored at the lowest physical memory address.
* **Big Endian (Network Byte Order):** The Most Significant Byte (`0xDE`) is stored at the lowest memory address.

*Security Implication:* When crafting return addresses for buffer overflows, addresses must be supplied in reversed Little-Endian byte order. Address `0x00007FFFFFFFE420` must be injected as:
`\x20\xe4\xff\xff\xff\x7f\x00\x00`

---

## 📦 5. The Function Call Protocol & Stack Frame Mechanics

The stack grows **downward** from higher memory addresses to lower memory addresses.

```text
High Address
┌──────────────────────────────────────────────┐
│  Caller Frame Local Variables & Arguments    │
├──────────────────────────────────────────────┤
│  SAVED RIP (Return Address)                  │  <-- Target of Buffer Overflow Overwrites!
├──────────────────────────────────────────────┤
│  SAVED RBP (Base Pointer of Caller)          │  <-- Frame Anchor
├──────────────────────────────────────────────┤
│  Local Function Variables (e.g., char buf[64])│  <-- Buffer vulnerability point
└──────────────────────────────────────────────┘
Low Address (Pointed to by RSP)
```

1. **Call Instruction (`call <target>`):**
   - Pushes the address of the next instruction (`Saved RIP`) onto the stack.
   - Sets `RIP` to the starting address of `<target>`.
2. **Function Prologue:**
   ```assembly
   push rbp          ; Save the caller's base pointer
   mov rbp, rsp      ; Anchor the new frame base to current stack top
   sub rsp, 0x20     ; Move RSP down by 32 bytes to reserve local variable space
   ```
3. **Function Epilogue:**
   ```assembly
   mov rsp, rbp      ; Collapse local variables by pointing RSP back to RBP
   pop rbp           ; Restore the caller's base pointer
   ret               ; Pops Saved RIP from stack top into RIP register
   ```

---

## 🛠️ 6. Laboratory Verification Commands (GDB & Python)

```bash
# 1. Run the custom Endianness & Memory Architecture probe:
python3 endianness_probe.py

# 2. Compile the register lab binary:
gcc -g -O0 registers_lab.c -o registers_lab

# 3. Disassemble inside GDB:
gdb -q ./registers_lab
(gdb) set disassembly-flavor intel
(gdb) disassemble main
(gdb) break main
(gdb) run
(gdb) info registers
(gdb) x/8gx $rsp
(gdb) quit
```
