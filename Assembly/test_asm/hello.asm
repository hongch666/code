; hello.asm
section .data
    hello db 'Hello, world!', 0x0A  ; 0x0A 是换行符
    hello_len equ $ - hello          ; 计算字符串长度

section .text
    global _start

_start:
    ; 写 "Hello, world!" 到 stdout
    mov rax, 1                      ; 系统调用号 (sys_write)
    mov rdi, 1                      ; 文件描述符 (stdout)
    mov rsi, hello                  ; 指向消息的指针
    mov rdx, hello_len              ; 消息长度
    syscall

    ; 退出程序
    mov rax, 60                     ; 系统调用号 (sys_exit)
    xor rdi, rdi                    ; 退出码 0
    syscall