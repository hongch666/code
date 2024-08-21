## 使用dune构建项目
1. 创建一个目录
2. 创建一个src文件夹，里面放入源代码
3. 在src中创建一个dune文件（无后缀），内容如下（最后一项是导入的测试单元）
```
(executable
 (name test)
 (libraries ounit2))
```
4. 在外层目录下创建一个dune-project文件（无后缀），内容如下（版本和项目名字根据实际情况填写）
```
(lang dune 3.10)
(name OUnit)
```
5. 在终端对于目录下运行下面指令（最后一条的运行指令对应的可执行文件名是在dune文件中定义的）
```bash
dune build
dune exec ./src/test.exe
```