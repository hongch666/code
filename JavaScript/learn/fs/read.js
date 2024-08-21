const fs = require("fs");

fs.readFile(__dirname + "/files/1.txt", "utf-8", function (err, dataStr) {
  if (err) {
    return console.log("读取文件失败！" + err.message);
  }
  console.log("读取文件成功，内容是：", dataStr);
});
