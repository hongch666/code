assume cs:codesg,ds:data,ss:stack
data segment
        
data ends
stack segment
        db 10 dup (0)
stack ends

codesg segment
        arr db 12,34
        arr2 db 'hello world'
        start:
                mov ax,arr[0]

codesg ends
end start