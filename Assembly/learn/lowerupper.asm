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
        s:
                mov al,[bx]
                ; and al,1011111B
                or al,100000B
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