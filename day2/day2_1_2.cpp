#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include "../globals.hpp"
using namespace std;
using namespace glb;

int main(void)
{
    ifstream f;
    f.open("input");
    
    string line;
    vector<string> lines;
    while(getline(f, line))
    {
        lines.push_back(replace_char(line, '\n', ""));
    }

    int hor_pos = 0;
    int ver_pos = 0;
    int aim = 0;

    for(string line : lines)
    {
        if(line.at(0) == 'f')
        {
            hor_pos += (int) line[line.length()-1]-'0';
            ver_pos += (((int) line[line.length()-1]-'0') * aim);
        }
        else if(line.at(0) == 'd')
        {
            aim += (int) line[line.length()-1]-'0';
        }
        else if(line.at(0) == 'u')
        {
            aim -= (int) line[line.length()-1]-'0';
        }
    }

    cout << "h: " << hor_pos << " : v: " <<  ver_pos << endl;
    cout << hor_pos * ver_pos << endl;
}