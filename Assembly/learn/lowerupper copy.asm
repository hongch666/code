assume cs:codesg,ds:data,ss:stack
data segment
        str db 'aaaaabbbbbccccc ','aaaaabbbbbccccc ','aaaaabbbbbccccc ','aaaaabbbbbccccc ','$'
data ends
stack segment
        db 10 dup (0)
stack ends

codesg segment
        start:
                mov ax,data
                mov ds,ax

                mov bx,0
                mov cx,4
        for:
                mov dx,cx
                mov si,0
                mov cx,5
                for1:
                        mov al,ds:str[bx+si]
                        and al,1011111B
                        mov ds:str[bx+si],al
                        inc si
                loop for1
                mov cx,dx
                add bx,16
        loop for

                ; mov dx,offset str
                lea dx,str
                mov ah,9
                int 21H
                
                mov ah,4cH
                int 21H

codesg ends
end start