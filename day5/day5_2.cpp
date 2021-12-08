#include "..\lib.hpp"
#include <fstream>
using namespace glb;
using namespace std;

int main(void)
{
    ifstream f;
    f.open("input");

    vector<int> x1;
    vector<int> x2;
    vector<int> y1;
    vector<int> y2;

    string line = "";
    while(getline(f, line))
    {
        x1.push_back(stoi(line.substr(0, line.find(","))));
        y1.push_back(stoi(line.substr(line.find(",")+1, line.find(" ")-line.find(",")-1)));
        x2.push_back(stoi(line.substr(line.rfind(" ")+1, line.rfind(",")-line.rfind(" ")-1)));
        y2.push_back(stoi(line.substr(line.rfind(",")+1, line.length()-line.rfind(","))));
    }

    int max_x = 0;
    int max_y = 0;
    for(int i = 0; i < x1.size(); i++)
    {
        max_x = max(max(x1.at(i), max_x), x2.at(i));
        max_y = max(max(y1.at(i), max_y), y2.at(i));
    }
    max_x++;
    max_y++;

    short int coords[max_y][max_x];
    for(int i = 0; i < max_y; i++)
    {
        for(int u = 0; u < max_x; u++)
        {
            coords[i][u] = 0;
        }
    }

    for(int i = 0; i < x1.size(); i++)
    {
        if(y1.at(i) == y2.at(i))
        {
            for(int u = min(x1.at(i), x2.at(i)); u <= max(x1.at(i), x2.at(i)); u++)
                coords[y1.at(i)][u]++;
        }
        else if(x1.at(i) == x2.at(i))
        {
            for(int u = min(y1.at(i), y2.at(i)); u <= max(y1.at(i), y2.at(i)); u++)
                coords[u][x1.at(i)]++;
        }
        else
        {
            int x_val = (y1.at(i) > y2.at(i)) ? x2.at(i) : x1.at(i);
            bool add = (x1.at(i) < x2.at(i)) ? true : false;
            add = (x_val == x2.at(i)) ? !add : add;
            for(int u = min(y1.at(i), y2.at(i)); u <= max(y1.at(i), y2.at(i)); u++)
            {
                coords[u][x_val]++;
                if(add) x_val++;
                else x_val--;
            }
        }
    }

    int i = 0;
    int num2s = 0;
    for(i = 0; i < max_y; i++)
    {
        for(int u = 0; u < max_x; u++)
        {
            if(coords[i][u] > 1)
                num2s += 1;
        }
    }
    cout << i << ": NUM2s - " << num2s << endl;
}