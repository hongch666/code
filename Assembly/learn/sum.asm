assume cs:codesg,ds:data,ss:stack
data segment
        arr db 1,2,3,4,10,20,30,40
        str db 'Hello World','$'
data ends
stack segment
        db 100 dup (0)
stack ends

codesg segment
        start:
                mov ax,data
                mov ds,ax

                mov ax,0
                mov bx,0
                mov cx,8
        for:
                add al,ds:arr[bx]
                adc ah,0
                inc bx
        loop for
                
                mov ah,4cH
                int 21H

codesg ends
end start