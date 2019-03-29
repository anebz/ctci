#include <iostream>

/*
 * Helper routine to return an frequency Table index
 */

int getCharIndex(char c) {
    int idx = -1;
    if (c >= 'a' && c <= 'z') {
        idx = c - 'a';
    }
    else if (c >= 'A' && c <= 'Z') {
        idx = c - 'A';
    }
    return idx;
}

/*
 * Function : countFrequency
 * Args     : input string, an array of int 
 * Return   : Void, array of int will populate each letter's frequency in string.
 */

void countFrequency(const std::string &str, int *frequency) {
    int idx;
    for (const char &c : str) {
        idx = getCharIndex(c);
        if (idx != -1) {
            ++frequency[idx];
        }
    }
}

int toggle(int bitVector, int index) {
    if (index < 0)
        return bitVector;

    int mask = 1 << index;
    //if bit is not set
    if ((bitVector & mask) == 0){
        bitVector |= mask;
    } else {  //if bit is set
        bitVector &= ~mask;
    }
    return bitVector;
}

/*
 * Helper functiont to find if a single bit is set
 * i.e. if bitVector is a multiple of power of 2
 */

bool isExactlyOneBitSet(int bitVector) {
    return ((bitVector & (bitVector - 1)) == 0);
}

/*
 * Third approach solution
 * toggle bit represent the respective char 
 * for each appearance in the string.
 */

bool isPermutationOfPallindrome(const std::string & str) {
    int bitVector = 0;
    int id = 0;
    for (const char & c : str)
    {
        id = getCharIndex(c);
        bitVector = toggle(bitVector, id);
    }
    return (bitVector == 0 || isExactlyOneBitSet(bitVector));
}