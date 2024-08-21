assume cs:codesg,ds:data,ss:stack
data segment
        str db 'Hello World','$'
data ends
stack segment
        db 10 dup (0)
stack ends

codesg segment
        start:
                mov ax,data
                mov ds,ax

                mov bx,0
                mov cx,11
                ; mov ah,0
                mov ah,0FFH
        s:
                mov al,[bx]
                cmp ah,al
                ; jnb s1
                jna s1
                mov ah,al
        s1:
                mov [bx],al
                inc bx
                loop s

                ; mov dx,offset str
                lea dx,str
                mov ah,9
                int 21H
                
                mov ah,4cH
                int 21H

codesg ends
end start