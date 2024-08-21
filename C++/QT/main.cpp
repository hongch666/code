// main.cpp
#include <QApplication>
#include <QPushButton>
#include <QVBoxLayout>
#include <QWidget>
#include <QDebug>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    QWidget window;
    window.setWindowTitle("Hello, Qt!");

    QPushButton *button = new QPushButton("Click me", &window);
    QObject::connect(button, &QPushButton::clicked, []() {
        qDebug() << "Button clicked!";
    });

    QVBoxLayout *layout = new QVBoxLayout;
    layout->addWidget(button);
    window.setLayout(layout);

    window.resize(320, 240);
    window.show();

    return app.exec();
}
/*
QT使用手册
创建main.cpp
创建my_qt_project.pro,写入与该项目相同的内容
然后终端在项目目录下使用指令qmake
再使用make
最后./对应可执行文件
*/