assume cs:codesg,ds:data,ss:stack
data segment
        str db '00012345','$'
        res db '0000','$'
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
                mov sp,10
                mov si,4

                mov bx,0
                mov cx,8
                mov ax,0
        for:
                mov dx,ax
                shl ax,1
                shl ax,1
                shl ax,1
                shl dx,1
                add ax,dx

                add al,str[bx]
                adc ah,0
                sub ax,30H

                inc bx
        loop for

        mov cx,4
        l:
            mov dx,ax
            and dx,0FH
            add dx,30H
            cmp dx,3AH
            jb s1
            add dx,7H
            
        s1:
            dec si
            mov ds:res[si],dl
            shr ax,1
            shr ax,1
            shr ax,1
            shr ax,1
        loop l
                lea dx,res
                mov ah,9
                int 21H

                mov ah,4cH
                int 21H

codesg ends
end start