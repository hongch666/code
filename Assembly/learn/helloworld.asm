assume cs:codesg,ds:data,ss:stack
data segment
        str db 'hello world',10,'123','$'
data ends
stack segment
        db 10 dup (0)
stack ends

codesg segment
        start:
                mov ax,data
                mov ds,ax
                mov dx,offset str
                mov ah,9
                int 21H

                mov ah,4cH
                int 21H

codesg ends
end start