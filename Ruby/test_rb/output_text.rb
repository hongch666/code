# puts 打印输出
puts "Please enter your name!"
=begin
gets和gets.chomp()都表示读入用户的输入并用于输出，但两者还是有所不同，
其中gets是得到的内容后，在输出时后面接着换行；
而gets.chmop()得到的内容输出时后面不带空格和换行
=end
name = gets.chomp
# "#{name}"  插值
puts "Hello，#{name}，welcome to Ruby！"
puts "sb"
# frozen_string_literal: true