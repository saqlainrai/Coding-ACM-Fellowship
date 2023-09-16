#include <iostream>
using namespace std;

int main()
{
    int rows, columns;
    cin >> rows;
    for (int x = rows; x > 0; x--)
    {
        for (int y = 0; y < x; y++)
        {
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}