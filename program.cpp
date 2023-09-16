#include <iostream>
using namespace std;

main()
{
    int rows;
    cout << "Enter the Number of rows: ";
    cin >> rows;

    for (int x = rows; x >= 0; x--)
    {
        for (int y = 0; y < x; y++)
        {
            cout << "*";
        }
        cout << endl;
    }
}