assume cs:codesg,ds:data,ss:stack
data segment
        arr dw 1111H,2222H,3333H,4444H,5555H,6666H,7777H,8888H
        res db 8 dup(0)
data ends
stack segment
        db 100 dup (0)
stack ends

codesg segment
        start:
                mov ax,data
                mov ds,ax
                mov ax,stack
                mov ss,ax

                mov bx,0
                mov cx,8
        for:
                push ds:arr[bx]
                add bx,2
        loop for

                mov bx,0
                mov cx,8
        for1:
                pop ds:arr[bx]
                add bx,2
        loop for1
                
                mov ah,4cH
                int 21H

codesg ends
end start