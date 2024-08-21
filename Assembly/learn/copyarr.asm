assume cs:codesg,ds:data,ss:stack
data segment
        arr db 1,2,3,4,10,20,30,40
        res db 8 dup(0)
data ends
stack segment
        db 100 dup (0)
stack ends

codesg segment
        start:
                mov ax,data
                mov ds,ax

                mov bx,0
                mov cx,8
        for:
                mov al,ds:arr[bx]
                mov ds:res[bx],al
                inc bx
        loop for
                
                mov ah,4cH
                int 21H

codesg ends
end start