#include<iostream>
#include<time.h>
#include<iomanip>
using namespace std;

void Random(int a[], int n)
{
    cout << "指令如下：" << endl;
    int m, i = 0;
    a[0]= 10000;
    int num;
    srand((unsigned int)(time(NULL)));
    for (i = 1; i < n; i++)
    {
        num = rand() % 1024 + 1;
        if (num <= 512 && num >= 1)
        {
            a[i] = a[i - 1] + 1;
        }
        else if (num <= 768 && num >= 513)
        {
            a[i] = rand() % (a[i - 1]) + 1;
        }
        else if (num <= 1024 && num >= 769)
        {
            a[i] = rand() % (32768 - a[i-1]) + a[i-1];
        }
    }

    for (i = 0; i < n; i++)
    {
        cout << setw(10)<<a[i];
        if ((i + 1) % 10 == 0)
            cout << endl;
    }
    cout << endl;
}

int Translate(int a[], int Page[], int n, int p)
{
    cout << "页面调度序列如下：" << endl;
    int i, j = 0;
    int temp = -1, result;
    for (i = 0; i < n; i++)
    {
        result = a[i] / (p * 1024);
        if (result != temp)
            temp = Page[j++] = result;
    }
    for (i = 0; i < j; i++)
    {
        cout << setw(10)<<Page[i];
        if ((i + 1) % 10 == 0)
            cout << endl;
    }
    cout << endl;
    return j;
}

//输出函数
void Output1(int* p, int n)
{
    for (int i = 0; i < n; i++)
        cout << setw(8)<<p[i];
}


void OPT(int Page[], int n, int piece)
{
    int rate = 0;
    int* p = new int[piece];
    //标记页数在内存的情况，0：不在内存块，1：在内存块，2：以后会再次访问并且已经在内存块的
    for (int i = 0; i < piece; i++)
        p[i] = -1;//内存块数赋初值
    int i, j;
    int x,y;
    bool *flag=new bool[piece];
    int *max=new int[piece];
    for (int o = 0; o < piece; o++)
    {
        flag[o] = false;
        max[o] = n+1;
    }
    int k,l;
    for (i = 0; i < piece; i++)
    {
        cout << i + 1 << setw(3) << Page[i] << ":";
        for (j = 0; j < piece && p[j] != Page[i]; j++)//查找是否缺
            ;
        if (p[j] == Page[i])
        {
            Output1(p, piece);
            cout << "     不缺页" << endl;
        }
        else
        {
            rate++;
            for (j = 0; j < piece - 1; j++)//缺页处理
                p[j] = p[j + 1];
            p[j] = Page[i];
            Output1(p, piece);
            cout << "     缺页" << endl;
        }
    }
    for (i = piece; i < n; i++)
    {
        cout << i + 1 << setw(3) << Page[i] << ":";
        for (j = 0; j < piece && p[j] != Page[i]; j++)//查找是否缺
            ;
        if (p[j] == Page[i])
        {
            Output1(p, piece);
            cout << "     不缺页" << endl;
        }
        else
        {
            rate++;
            for (x = 0; x < piece; x++)
            {
                for (y = i; y < n; y++)
                {
                    if (p[x] == Page[y])
                    {
                        flag[x] = true;
                        if (max[x] > y)
                        {
                            max[x] = y;
                        }
                    }
                }
            }
            bool flag1 = false;
            for (k = 0; k < piece; k++)
            {
                
                if (flag[k] == false)
                {
                    flag1 = true;
                }
            }
            int Max_m = -1;
            int Max_num;
            for (l = 0; l < piece; l++)
            {
               
                if (max[l] > Max_m)
                {
                    Max_m = max[l];
                    Max_num = l;
                }
            }
            if (flag1 == true)
            {
                p[k] = Page[i];
            }
            else
            {
                p[Max_num] = Page[i];
            }
            Output1(p, piece);
            cout << "     缺页" << endl;
        }
    }
    cout << "缺页次数：" << rate << "" << "总数" << n << endl;
    cout << "最佳置换算法（OPT)缺页率为" << (double)rate / n * 100 << "%" << endl;
    delete[]p;
}

void FIFO(int Page[], int n, int piece)
{
    int i, number = 0, j, position = 0;
    int rate = 0;
    int* p = new int[piece];
    for (i = 0; i < piece; i++)
        p[i] = -1;//内存块数赋初值
    for (i = 0; i < n; i++)
    {
        cout << i + 1 <<setw(3)<<Page[i]<<":";
        for (j = 0; j < piece && p[j] != Page[i]; j++)//查找是否缺
            ;
        if (p[j] == Page[i])
        {
            Output1(p, piece);
            cout <<"     不缺页" << endl;
        }
        else
        {
            rate++;
            for (j = 0; j < piece - 1; j++)//缺页处理
                p[j] = p[j + 1];
            p[j] = Page[i];
            Output1(p, piece);
            cout << "     缺页" << endl;
        }
    }
    cout << "缺页次数：" << rate << "" << "总数" << n << endl;
    cout << "先进先出置换算法（FIFO）缺页率为" << (double)rate / n * 100 << "%" << endl;
    delete[]p;
}

void LRU(int Page[], int n, int piece, int total)
{
    int i, number = 0, j, position = 0;
    int rate = 0;
    int temp;
    int* p = new int[piece];
    for (i = 0; i < piece; i++)
        p[i] = -1;//内存块数赋初值
    for (i = 0; i < n; i++)
    {
        cout << i + 1 << " ";
        cout << Page[i] << ":" << setw(4);
        for (j = 0; j < piece && p[j] != Page[i]; j++)//查找是否缺页
            ;
        if (p[j] == Page[i])//不缺页处理
        {
            temp = p[j];
            while (j < piece - 1)
            {
                p[j] = p[j + 1];
                j++;
            }
            p[j] = temp;
            Output1(p, piece);
            cout << "不缺页" << endl;
        }
        else//缺页处理
        {
            rate++;
            for (j = 0; j < piece - 1; j++)
                p[j] = p[j + 1];
            p[j] = Page[i];
            Output1(p, piece);
            cout << "缺页" << endl;
        }
    }
    cout << "缺页次数：" << rate << "" << "总数" << n << endl;
    cout << "最近最少用置换算法（LRU）缺页率为" << (double)rate / n * 100 << "%" << endl;
    delete[]p;

}


int main()
{
    int a[256];//存放320条指令
    int i = 1;
    int p;//存放页大小
    int page[256];//存放合并后要使用的页号
    int PageNumber;//存放页号数量
    int piece;//存放块数
    bool flag = true;
    while (flag)
    {
        switch (i)
        {
        case 1:
            Random(a, 256);
        case 2:
            cout << "请输入页大小（1K、2K、4K、8K、16K）：";
            cin >> p;
            PageNumber = Translate(a, page, 256, p);
            cout << "将相邻相同的页号合并为一个后要使用到的页号数为" << PageNumber << "个" << endl;
        case 3:
            cout << "请输入块数（1~" << PageNumber << "）：";
            cin >> piece;
        case 4:
            cout << "请选择页面置换算法(1~3)" << endl;
            cout << "1.最佳置换算法（OPT)" << endl;
            cout << "2.先进先出置换算法（FIFO）" << endl;
            cout << "3.最近最少用置换算法（LRU）" << endl;
            cin >> i;
            switch (i)
            {
            case 1:OPT(page, PageNumber, piece); break;
            case 2:FIFO(page, PageNumber, piece); break;
            case 3:LRU(page, PageNumber, piece, 32 / p); break;
            default:cout << "输入有误" << endl; break;
            }
            cout << "*****************************" << endl;
            cout << "*****1.重新开始" << endl;
            cout << "*****2.返回重新输入页大小" << endl;
            cout << "*****3.返回重新输入块数" << endl;
            cout << "*****4.返回重新选择页面置换算法" << endl;
            cout << "*****5.结束程序" << endl;
            cin >> i; break;
        default:flag = false;
        }
    }
    return 0;
}