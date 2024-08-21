assume cs:codesg,ds:data,ss:stack
data segment
        arr dw 1H,1H,100 dup(0)
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

                mov bx,4
                mov cx,10
        for:
                mov dx,0
                add dx,ds:arr[bx-2]
                add dx,ds:arr[bx-4]
                mov ds:arr[bx],dx
                add bx,2
        loop for
                
                mov ah,4cH
                int 21H

codesg ends
end start