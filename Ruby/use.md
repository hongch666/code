在使用 Bundler 管理依赖的 Ruby 项目中编写代码以输出文字，你只需遵循一些简单的步骤。以下是如何在 Bundler 项目中创建一个 Ruby 文件，然后使用该文件输出一段文字：

### 1. 初始化项目并安装 Bundler

确保你已经在项目目录中创建了一个 `Gemfile`，并使用 Bundler 来管理你的 gem 依赖。如果还没有，你可以使用以下命令来初始化：

```bash
mkdir my_project
cd my_project
bundle init
```

这将创建一个空的 `Gemfile`。

### 2. 添加依赖

在 `Gemfile` 中添加你项目需要的 gem 依赖。即使你的项目目前只需要输出文字，你可能还是需要添加 `bundler` 本身作为依赖。编辑 `Gemfile` 并添加以下内容：

```ruby
source 'https://rubygems.org'

gem 'bundler', platform: :ruby
```

然后运行 `bundle install` 来安装这些依赖：

```bash
bundle install
```

### 3. 创建 Ruby 文件

在你的项目目录中创建一个新的 Ruby 文件，例如 `output_text.rb`。你可以在终端中使用 `touch` 命令来快速创建文件：

```bash
touch output_text.rb
```

或者使用文本编辑器创建：

```bash
nano output_text.rb
```

### 4. 编写 Ruby 代码

在 `output_text.rb` 文件中，编写你的 Ruby 代码来输出文字。例如：

```ruby
puts "Hello from a Bundler-managed project!"
```

### 5. 运行 Ruby 文件

为了确保你的 Ruby 文件在 Bundler 的环境下运行，你可以使用 `bundle exec` 命令来运行你的 Ruby 文件。这会确保你的 Ruby 文件在 Bundler 创建的 gem 环境中执行，使用了 `Gemfile` 中指定的依赖：

```bash
bundle exec ruby output_text.rb
```

你将看到终端中输出 "Hello from a Bundler-managed project!"。

### 总结

使用 Bundler 管理你的 Ruby 项目依赖是一个好习惯，即使对于简单的项目也是如此。这确保了你的项目在任何地方都能一致地运行，不受系统级 gem 安装的影响。通过使用 `bundle exec` 命令，你可以确保你的 Ruby 文件在正确的 gem 环境中运行。