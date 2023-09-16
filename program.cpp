#include <iostream>
using namespace std;

// New push generated

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
    cout << "The program terminated successfully, new Push generated" << endl;
}