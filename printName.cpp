#include <iostream>
#include <ctime>
using namespace std;

// Bubble sort Algorithm

main()
{
    clock_t start = clock();
    int length = 10;
    int array[10] = {2, 6, 1, 8, 3, 5, 7, 4, 10, 9};
    bool flag = false;
    for (int x = 0; x < length; x++)
    {
        for (int y = 0; y < length - x; y++)
        {
            if (array[y] > array[y + 1])
            {
                int temp;
                temp = array[y];
                array[y] = array[y + 1];
                array[y + 1] = temp;
                flag = true;
            }
        }
        if (flag == false)
        {
            cout << "Already Sorted" << endl;
            break;
        }
    }

    clock_t end = clock();

    double duration = (double)(end - start) / CLOCKS_PER_SEC;

    cout << "The Time taken is: " << duration << endl;

    for (int z = 0; z < length; z++)
    {
        cout << array[z] << " ";
    }



}