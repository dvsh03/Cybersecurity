# 🏛️ Computer Architecture for Cybersecurity: Master Syllabus & Roadmap
> **Track:** Tier 1 — Systems & Foundations  
> **Target Audience:** Cybersecurity Engineers, Exploit Developers, Reverse Engineers, Systems Researchers  
> **Architecture Focus:** x86_64 (Primary / Standard) & ARM64 (Secondary / Comparative)  
> **Reference Standard:** System V AMD64 ABI & Linux / Windows NT Internals  

---

## 🎯 Syllabus Purpose & Tracking
Yeh master syllabus Computer Architecture ka complete, zero-omission blueprint hai. Har module ko aise design kiya gaya hai ki aapko hardware ke microscopic level se lekar binary exploitation aur defensive hardening tak ka deep correlation pata rahe. 

Aap is syllabus ko apne **Notion Database** aur **Local Folder** mein ek master checklist ki tarah use kar sakte hain. Koi bhi topic kabhi nahi chutega!

---

## 🗺️ Master Curriculum Overview (7 Modules)

```text
[ MODULE 1: Silicon Foundations & Instruction Execution Pipeline ]
                              │
[ MODULE 2: Registers, Instruction Sets & Calling Conventions ]
                              │
[ MODULE 3: Process Memory Layout, Endianness & Stack Frames ]
                              │
[ MODULE 4: Memory Hierarchy, Cache Coherence & Hardware Exploits ]
                              │
[ MODULE 5: MMU, Virtual Memory, Multi-Level Paging & Page Tables ]
                              │
[ MODULE 6: Hardware Rings, System Calls & Kernel Transitions ]
                              │
[ MODULE 7: Hardware-Enforced Mitigations (NX, SMEP, SMAP, CET) ]
```

---

## 📚 MODULE 1: Silicon Foundations & The Instruction Pipeline
*Objective: Samjhein ki CPU silicon physically data aur instructions ko kaise process karta hai.*

### Theoretical Core:
- [ ] **Von Neumann vs Harvard Architecture:**
  - Stored-program concept (Data aur Code same memory share karte hain vs separate physical memory).
  - Cybersecurity relevance: Code injection attacks (Shellcode execution on data memory) Von Neumann architecture ki isi shared-memory reality par depend karte hain.
- [ ] **CPU Internal Subsystems:**
  - Arithmetic Logic Unit (ALU): Integer math (`ADD`, `SUB`) aur bitwise logical operations (`AND`, `OR`, `XOR`, `NOT`, `SHL`, `SHR`).
  - Control Unit (CU): Microcode execution, instruction decoder, clock timing synchronizer.
  - Internal SRAM Registers: Sub-nanosecond latency vs DRAM.
- [ ] **System Buses & Interconnects:**
  - Control Bus (Read/Write signals, IRQ interrupts).
  - Address Bus (Physical address width: 32-bit vs 48-bit/64-bit canonical addresses).
  - Data Bus (Word width, bandwidth, cache lines).
- [ ] **The 5-Stage Microscopic Instruction Cycle:**
  - Stage 1: Instruction Fetch (IF) — `RIP` address querying.
  - Stage 2: Instruction Decode (ID) — Opcode breakdown and operand sizing.
  - Stage 3: Execute (EX) — ALU execution and effective address computation (`[RBP - 0x10]`).
  - Stage 4: Memory Access (MEM) — Cache/RAM read-write operations.
  - Stage 5: Write-Back (WB) — Register updates and `RIP` incrementation.
- [ ] **Pipelining Hazards & Branch Prediction:**
  - Structural, Data, and Control Hazards.
  - Branch Target Buffer (BTB) & Branch Predictor (Spectre vulnerability ka hardware root).

### Hands-on Labs & Tools:
- [x] **Lab 1.1:** Hardware profiling via Python (`platform`, `struct`) to inspect byte order, pointer size, and architecture width.
- [ ] **Lab 1.2:** CPU instruction timing inspection using `rdtsc` (Read Time-Stamp Counter) assembly instruction to measure execution cycles.

---

## 📚 MODULE 2: CPU Registers, Instruction Sets & Calling Conventions
*Objective: Master all 16 x86_64 registers, sub-register slicing, and function argument passing protocols.*

### Theoretical Core:
- [ ] **The 16 General Purpose Registers (GPRs):**
  - `RAX`, `RBX`, `RCX`, `RDX`, `RSI`, `RDI`, `RBP`, `RSP`, `R8`, `R9`, `R10`, `R11`, `R12`, `R13`, `R14`, `R15`.
- [ ] **Sub-Register Slicing & Backwards Compatibility:**
  - 64-bit (`RAX`) ➔ 32-bit (`EAX`) ➔ 16-bit (`AX`) ➔ 8-bit Low (`AL`) & 8-bit High (`AH`).
  - High-byte slicing limitation: `AH`, `BH`, `CH`, `DH` sirf pehle 4 registers ke liye exist karte hain (`R8`–`R15` ke liye `R8B` etc. hote hain, high-byte sub-registers nahi hote).
- [ ] **Special-Purpose & Pointer Registers:**
  - `RIP` (Instruction Pointer): CPU ka target execution pointer.
  - `RSP` (Stack Pointer): Current stack top ko point karta hai.
  - `RBP` (Base/Frame Pointer): Current function frame ko anchor karta hai.
- [ ] **Flags Register (`RFLAGS` / `EFLAGS`):**
  - Status flags: `ZF` (Zero Flag), `CF` (Carry Flag), `SF` (Sign Flag), `OF` (Overflow Flag).
  - Control flags: `DF` (Direction Flag), `TF` (Trap Flag for debuggers/single-stepping).
- [ ] **System V AMD64 ABI Calling Convention (Linux/BSD/macOS):**
  - Argument passing order: `RDI` (1st), `RSI` (2nd), `RDX` (3rd), `RCX` (4th), `R8` (5th), `R9` (6th).
  - Return value: `RAX` (and `RDX` if 128-bit return).
  - Callee-saved registers (`RBX`, `RSP`, `RBP`, `R12`–`R15`) vs Caller-saved registers (`RAX`, `RCX`, `RDX`, `RSI`, `RDI`, `R8`–`R11`).
- [ ] **Microsoft x64 Calling Convention (Windows Fastcall):**
  - Argument passing order: `RCX` (1st), `RDX` (2nd), `R8` (3rd), `R9` (4th).
  - Shadow Space (32 bytes home space allocated on stack before calling).
- [ ] **ARM64 Architecture Comparative Analysis:**
  - RISC (Reduced Instruction Set Computer) vs CISC (Complex Instruction Set Computer).
  - Fixed 32-bit instruction size vs variable-length x86 opcodes.
  - 31 General Purpose Registers (`X0`–`X30`), `W` sub-registers (32-bit).
  - Link Register (`LR` / `X30`): Function return address stack par push hone ki jagah hardware register `LR` mein save hota hai.
- [ ] **Exploit Engineering Practical Insight:**
  - Null-Byte Elimination: `xor eax, eax` vs `mov rax, 0`.
  - Sub-register manipulation for compact shellcode payloads.

### Hands-on Labs & Tools:
- [x] **Lab 2.1:** Compile C test binary with `-g -O0` and trace argument registers (`RDI`, `RSI`) and return register (`RAX`) in GDB.
- [ ] **Lab 2.2:** Craft raw assembly function passing 6 arguments on Linux and verify register assignment using GDB `info registers`.

---

## 📚 MODULE 3: Process Memory Layout, Endianness & Stack Frames
*Objective: Understand how OS and CPU lay out program memory in RAM and how the stack operates at the byte level.*

### Theoretical Core:
- [ ] **Process Virtual Memory Layout (ELF / PE):**
  - `.text` Segment: Executable machine code (Read + Execute).
  - `.rodata` Segment: Read-only constants, string literals.
  - `.data` Segment: Initialized global and static variables (Read + Write).
  - `.bss` Segment: Uninitialized global variables (Block Started by Symbol, zero-filled).
  - **Heap:** Dynamic runtime memory allocation (`malloc`, `free`), grows **UPWARDS** towards high memory.
  - **Memory Mapping Segment:** Shared libraries (`libc.so`, `ntdll.dll`), memory-mapped files (`mmap`).
  - **Stack:** Local variables, function parameters, stack frames, grows **DOWNWARDS** towards low memory.
- [ ] **Endianness & Physical Byte Ordering:**
  - Little Endian (x86_64, ARM default): Least Significant Byte (LSB) lowest address par.
  - Big Endian (Network Byte Order RFC 791, SPARC, IBM z/Architecture): Most Significant Byte (MSB) lowest address par.
  - Cybersecurity impact: Return addresses, ROP gadgets, and memory addresses must be reversed in exploit strings (`\x20\xe4\xff\xff...`).
- [ ] **The Stack Frame Lifecycle & Calling Protocol:**
  - Stack alignment rules (x86_64 requires 16-byte stack alignment before `call`).
  - The `call` instruction: Pushes `Saved RIP` (address of next instruction) onto stack and jumps to callee.
  - Function Prologue:
    ```nasm
    push rbp        ; Caller's frame pointer stack par save karo
    mov rbp, rsp    ; RBP ko current stack top par anchor karo
    sub rsp, 0x20   ; Local variables ke liye 32 bytes reserve karo
    ```
  - Function Epilogue:
    ```nasm
    mov rsp, rbp    ; Local variables ko discard karo
    pop rbp         ; Caller's RBP restore karo
    ret             ; Stack top se Saved RIP pop karke RIP register mein daalo
    ```
- [ ] **Buffer Overflow Anatomy:**
  - Local array bounds exceed hone par memory overwrites linearly UPWARDS:
    `Local Buffer` ➔ `Saved RBP` ➔ `Saved RIP` (Hijacking Execution Flow).

### Hands-on Labs & Tools:
- [x] **Lab 3.1:** Memory endianness simulation probe script in Python (`struct.pack('<Q', val)` vs `struct.pack('>Q', val)`).
- [ ] **Lab 3.2:** GDB memory examination (`x/20gx $rsp`) during a nested function call to view exact stack frame boundaries.

---

## 📚 MODULE 4: Memory Hierarchy, Caches & Hardware Side-Channels
*Objective: Master the hardware speed pyramid and hardware-level microarchitectural vulnerabilities.*

### Theoretical Core:
- [ ] **The Hardware Storage Hierarchy:**
  - Registers (1 cycle, ~0.5 ns).
  - L1 Data & Instruction Caches (3–5 cycles, ~1 ns, core-private).
  - L2 Cache (12–14 cycles, ~3–4 ns, core-private).
  - L3 Cache / Last-Level Cache (LLC) (40–60 cycles, ~15–20 ns, shared across cores).
  - Main Memory (DRAM) (150–250 cycles, ~60–100 ns).
  - Disk / SSD / Swap (Millions of cycles, milliseconds/microseconds).
- [ ] **Cache Line Mechanics & Memory Access:**
  - 64-byte Cache Lines.
  - Cache Hits vs Cache Misses (Cache timing attacks: measuring access latency via `rdtsc`).
  - Temporal Locality vs Spatial Locality.
- [ ] **Out-of-Order Execution (OoOE) & Speculative Execution:**
  - Speculative execution branch predictor (CPU assumes branch outcome ahead of time to keep pipeline busy).
  - Microarchitectural state changes (Cache remains primed even if speculative execution is discarded!).
- [ ] **Hardware Side-Channel Vulnerabilities:**
  - **Meltdown (CVE-2017-5754):** CPU reads kernel memory during out-of-order execution before privilege check finishes, leaving a cache footprint readable by user space.
  - **Spectre (CVE-2017-5753, CVE-2017-5715):** Tricking branch prediction into speculatively reading secret memory and exfiltrating via cache timing (Flush+Reload).
  - **Rowhammer:** Repeatedly reading specific DRAM memory rows ("hammering") generates electromagnetic coupling that flips bits in adjacent rows without write permissions.

### Hands-on Labs & Tools:
- [ ] **Lab 4.1:** Write a C program using `__rdtscp()` to measure the exact nanosecond difference between a Cache Hit and a Cache Miss.
- [ ] **Lab 4.2:** Flush+Reload proof-of-concept timing demonstration in C.

---

## 📚 MODULE 5: MMU, Virtual Memory, Paging & Page Tables
*Objective: Uncover how the CPU hardware and OS isolate processes and translate virtual addresses to physical RAM.*

### Theoretical Core:
- [ ] **The Memory Management Unit (MMU):**
  - Hardware chip translating Virtual Addresses to Physical Addresses.
  - Process isolation (Process A cannot read Process B's memory because their virtual addresses map to completely different physical page frames).
- [ ] **x86_64 Multi-Level Paging (4-Level Page Tables):**
  - 4KB standard page size.
  - 48-bit Virtual Address breakdown:
    - Bits 47–39 (9 bits): Index into **PML4** (Page Map Level 4).
    - Bits 38–30 (9 bits): Index into **PDPT** (Page Directory Pointer Table).
    - Bits 29–21 (9 bits): Index into **PD** (Page Directory).
    - Bits 20–12 (9 bits): Index into **PT** (Page Table).
    - Bits 11–0 (12 bits): Physical Page Offset ($2^{12} = 4096$ bytes = 4KB).
  - `CR3` Control Register: Holds the physical base address of the current process's PML4 table.
- [ ] **Page Table Entry (PTE) Flags & Hardware Permissions:**
  - Bit 0 (`P`): Present flag (1 = in RAM, 0 = on disk/swap).
  - Bit 1 (`R/W`): Read/Write (0 = Read-only, 1 = Read/Write).
  - Bit 2 (`U/S`): User/Supervisor (0 = Ring 0 Kernel only, 1 = Ring 3 User accessible).
  - Bit 63 (`NX` / `XD`): No-Execute bit (1 = Hardware execution blocked -> DEP/W^X protection).
- [ ] **The Translation Lookaside Buffer (TLB):**
  - High-speed cache for page table translations.
  - TLB Miss penalty and TLB Invalidation (`invlpg`).
- [ ] **Page Fault Mechanics:**
  - Hardware interrupt (Interrupt 14) raised by MMU when an address cannot be translated.
  - Soft Page Fault (Allocating zero-filled RAM on first write).
  - Hard Page Fault (Reading missing page from disk swap).
  - Segmentation Fault (`SIGSEGV` / `0xC0000005` Access Violation): Accessing unmapped memory or violating permissions (e.g. writing to Read-Only page).

### Hands-on Labs & Tools:
- [ ] **Lab 5.1:** Inspect Linux virtual memory mapping via `/proc/[pid]/maps` and `/proc/[pid]/smaps`.
- [ ] **Lab 5.2:** Write a C program using `mmap()` and `mprotect()` to dynamically allocate memory, change PTE permissions, and trigger a hardware `SIGSEGV` on execution.

---

## 📚 MODULE 6: Hardware Privilege Rings, Transitions & System Calls
*Objective: Understand how the CPU enforces privilege boundaries between user apps and the OS kernel.*

### Theoretical Core:
- [ ] **Hardware Protection Rings:**
  - Ring 0: Kernel Mode / Supervisor (Full access to all hardware, I/O ports, control registers `CR0`–`CR4`, MSRs).
  - Ring 1 & 2: Device Drivers (rarely used in modern OS).
  - Ring 3: User Mode / Applications (Restricted execution, memory access limited by page tables).
  - Ring -1: Hypervisor / Virtualization (VT-x, AMD-V, root mode).
- [ ] **Privilege Ring Switching Mechanics:**
  - User mode cannot directly call kernel functions! Must trigger a controlled hardware transition.
  - **Legacy Transition:** Software Interrupts (`int 0x80` in Linux 32-bit, `int 0x2e` in Windows) via Interrupt Descriptor Table (IDT).
  - **Modern Transition:** Fast System Calls (`syscall` / `sysret` in x86_64, `sysenter` / `sysexit`).
- [ ] **The `IA32_LSTAR` MSR (Model-Specific Register):**
  - Holds the 64-bit kernel entry point address (`entry_SYSCALL_64` on Linux).
  - Jab user space `syscall` instruction execute karta hai, CPU automatically:
    1. Saves user `RIP` into `RCX`.
    2. Saves user `RFLAGS` into `R11`.
    3. Loads `IA32_LSTAR` into `RIP`.
    4. Switches CPU CPL (Current Privilege Level) from Ring 3 to Ring 0.
- [ ] **Context Switching & Register Preservation:**
  - Kernel stack setup (`swapgs` instruction to switch GS base to kernel data structure).
  - Saving user registers to `pt_regs` structure on the kernel stack.
  - System call dispatch table (`sys_call_table`).
  - Returning to user space via `sysretq`.

### Hands-on Labs & Tools:
- [ ] **Lab 6.1:** Trace every system call of a binary using `strace -c` and `strace -e trace=memory,process`.
- [ ] **Lab 6.2:** Write a raw x86_64 assembly program that calls Linux `sys_write` (syscall 1) and `sys_exit` (syscall 60) without using the C library (`libc`).

---

## 📚 MODULE 7: Hardware-Enforced Security Mitigations
*Objective: Understand the modern silicon and OS defense layers designed to neutralize binary attacks.*

### Theoretical Core:
- [ ] **Hardware-Enforced NX/DEP (No-Execute / Data Execution Prevention):**
  - AMD's No-Execute (NX) & Intel's Execute-Disable (XD) bit (Bit 63 of Page Table Entry).
  - W^X Policy (Write XOR Execute: A memory page can be writable OR executable, NEVER both).
  - Bypassing NX: Return-Oriented Programming (ROP) — reusing existing `.text` code gadgets.
- [ ] **ASLR & PIE (Address Space Layout Randomization & Position-Independent Executable):**
  - Randomizing stack, heap, shared libraries (`libc`), and binary base addresses on every execution.
  - 64-bit entropy vs 32-bit brute-forceability.
  - Defeating ASLR: Memory leaks (format string vulnerabilities, uninitialized read leaks).
- [ ] **Stack Smashing Protection (Stack Canaries):**
  - GCC `-fstack-protector`: Injects a random 8-byte canary value between local variables and Saved RBP.
  - Canary lookup from Thread Local Storage (`FS:0x28` on Linux, `GS:0x14` on Windows).
  - Terminator Canary: Contains `0x00`, `\n`, `0xFF` to terminate string copy functions (`strcpy`).
- [ ] **Kernel Privilege Isolation Mitigations:**
  - **SMEP (Supervisor Mode Execution Prevention - CR4 Bit 20):** Prevents kernel (Ring 0) from executing code located in user-space pages. Neutralizes user-space shellcode execution from kernel exploits.
  - **SMAP (Supervisor Mode Access Prevention - CR4 Bit 21):** Prevents kernel from directly reading/writing user-space memory without explicit `stac` (Set AC flag) instruction.
  - **KPTI (Kernel Page Table Isolation):** Separates kernel and user-space page tables completely to remediate Meltdown.
- [ ] **Intel CET (Control-Flow Enforcement Technology):**
  - **Shadow Stack:** Hardware-managed secondary stack storing only return addresses. If `ret` address on data stack doesn't match Shadow Stack, hardware triggers `#CP` (Control Protection exception).
  - **Indirect Branch Tracking (IBT):** Requires indirect jumps to land on an `ENDBR64` instruction.

### Hands-on Labs & Tools:
- [ ] **Lab 7.1:** Inspect binary protections using `checksec` (NX, Canary, PIE, RELRO).
- [ ] **Lab 7.2:** Compile a vulnerable C program with stack canaries disabled (`-fno-stack-protector`) vs enabled, and inspect assembly difference in GDB.

---

## 🏁 Exit Test & Competency Benchmarks
Aap is Computer Architecture phase ko complete aur mastered tabhi consider karenge jab aap in 5 practical benchmarks ko autonomously deliver kar sakein:

1. [ ] **GDB Autonomy:** Kisi bhi compiled x86_64 binary ko GDB mein load karke uske registers (`info registers`), stack frame (`x/16gx $rsp`), aur function prologue/epilogue ko 100% articulate karna.
2. [ ] **Calling Convention Flow:** 6 arguments pass karne waale function ki assembly ko trace karke batana ki konsa argument kis register (`RDI`, `RSI`, `RDX`...) mein baitha hai aur return value kahan aayi.
3. [ ] **Endianness Precision:** Kisi bhi hex memory address ko bina kisi software tool ke instantly Little-Endian payload string (`\xNN\xNN...`) mein manually convert karna.
4. [ ] **Page Table Translation:** Virtual address se physical address tak ke 4-level translation steps (`PML4` ➔ `PDPT` ➔ `PD` ➔ `PT` ➔ Offset) aur `CR3` register ke role ko diagram ke saath explain karna.
5. [ ] **Syscall Cycle Trace:** User mode `syscall` execution se lekar `IA32_LSTAR` register, Ring 0 transition, aur `sysretq` tak ke microscopic hardware steps ko trace karna.

---
*Created as part of the Cybersecurity Master Engineering Portfolio | Author: dvsh03*
