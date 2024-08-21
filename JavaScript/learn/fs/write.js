const fs = require('fs');

fs.writeFile('./files/1.txt','abcd',function(err){
    if(err){
        return console.log('写入文件失败！'+err.message)
    }
    console.log('写入文件成功！')
})