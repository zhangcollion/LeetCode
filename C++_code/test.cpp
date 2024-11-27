#include <iostream>
#include <iomanip>
#include <string>
using namespace std;
// void PrintParaPoint(int a,  int& b){
//     cout << "a = " << a<<",b= " << b << endl;
//     cout << "addr b is " << &b <<endl;
//     b = 3; // b为num的引用，修改b 同样修改num
//     return;
// }

void PrintParaPoint(int a,  int* b){
    cout << "a = " << a<<",b= " << *b << endl;
    cout << "addr b is " << &b <<endl;
    *b = 333; // b为num的引用，修改b 同样修改num
    return;
}

int main()
{
    int num = 1;
    cout << "address of num: " << &num <<endl;
    int newNum = num;
    num = 2;
    cout << "address of num: "  << &num << endl;
    cout << "address of new num: "  << &newNum << endl;
    cout << "num = " << num << "\nnewNum = " << newNum << endl; 
    int& rNum  = num;  // int& 引用变量，rNum 为num的别名，对num 操作就是对rNum 操作
    int* pNum = &num; // pNum 指针，指向num的内存地址； & 取值地址运算符
    cout << "rNum: "  << rNum << endl;
    cout << "pNum: " << *pNum << endl; // * 间接寻址运算符，将pNum 内存地址中的数据取出
    *pNum = 1000;
    cout << "pNum: " << *pNum << endl; // * 间接寻址运算符，将pNum 内存地址中的数据取出
    cout << "num: " << num << endl; 
    PrintParaPoint(num, &num);
    cout << "num: "<<num << endl; 
    return 0;

}
