assume cs:codesg,ds:data,ss:stack
data segment
        arr db 32H,34H,47H,31H,1H,21H,3H,55H,87H
data ends
stack segment
        db 10 dup (0)
stack ends

codesg segment
        start:
                mov ax,data
                mov ds,ax

                mov bx,0
                mov cx,8
        for:
                mov dx,cx
                mov si,8
                mov cx,8
                sub cx,bx
                for1:
                        mov ah,ds:arr[si]
                        mov al,ds:arr[si-1]
                        cmp ah,al
                        jnb all
                        
                        xchg ah,al
                        mov ds:arr[si],ah
                        mov ds:arr[si-1],al
                        all:
                        dec si
                loop for1
                mov cx,dx
                add bx,1
        loop for
                
                mov ah,4cH
                int 21H

codesg ends
end start