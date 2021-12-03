#ifndef __GLOBALS_H__
#define __GLOBALS_H__

#include <string>
#include <iostream>
#include <vector>

namespace glb
{
    std::string replace_char(std::string str, char replace, std::string replace_with)
    {
        std::string new_str = "";
        for(int i = 0; i < str.length(); i++)
        {
            if(str[i] == replace) new_str += replace_with;
            else new_str += str[i];
        }
        return new_str;
    }
}

#endif