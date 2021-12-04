#ifndef __GLOBALS_H__
#define __GLOBALS_H__

#include <string>
#include <iostream>
#include <vector>
#include <typeinfo>

namespace glb
{
    int arr_find(auto array[], int size, auto find)
    {
        for(int i = 0; i < size; i++)
        {
            if(array[i] == find)
                return i;
        }
        return -1;
    }

    void arr_indexes(auto array[], int size, std::vector<int> &indexes, decltype(+array[0]) find)
    {
        for(int i = 0; i < size; i++)
        {
            if(array[i] == find)
            {
                indexes.push_back(i);
            }
        }
    }

    template <typename T>
    void vec_indexes(std::vector<T> vec, std::vector<int> &indexes, T find)
    {
        for(int i = 0; i < vec.size(); i++)
        {
            if(vec.at(i) == find)
            {
                indexes.push_back(i);
            }
        }
    }

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

    std::string replace_str(std::string str, std::string replace, std::string replace_with)
    {
        std::string new_str = "";
        if(str.length() < replace.length())
            return str;
        else if(str.length() == replace.length())
            if(str == replace) return replace;
            else return str;

        for(int i = 0; i < str.length()-replace.length()+1; i++)
        {
            std::string last_non_repl = tempstr;
            std::string tempstr = str.substr(i, replace.length());
            if(tempstr == replace)
            {
                new_str += replace_with;
                i += replace.length()-1;
            }
            else
            {
                new_str += str[i];
            }
        }

        for(int i = str.length()-replace.length(); i < str.length(); i++)
        {
            new_str += str[i];
        }

        return new_str;
    }
}

#endif