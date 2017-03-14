package com.company;

/**
 * Created by hanhvn on 3/11/2017.
 */
public class RemoveDuplicateChar {

    public static void removeDuplicateChar(char[] str)
    {
        if (str == null)
            return;
        if (str.length < 2)
            return;
        int tail = 1;

        for (int i = 1; i < str.length; i++)
        {
            int j;
            for (j = 0; j < tail; j++)
            {
                if (str[i] == str[j]) break;
            }
            if (j == tail)
            {
                str[tail] = str[i];
                ++tail;
            }
        }
        str[tail] = 0;
    }

    public static void removeDuplicateChar2(char[] str)
    {
        if (str == null)
            return;
        if (str.length < 2)
            return;
        int tail = 1;
        boolean[] hits = new boolean[256];
        hits[str[0]] = true;
        for (int i = 1; i < str.length; i++)
        {
            if (!hits[str[i]])
            {
                hits[str[i]] = true;
                str[tail] = str[i];
                ++tail;
            }
        }
        str[tail] = '\0';
    }
}
