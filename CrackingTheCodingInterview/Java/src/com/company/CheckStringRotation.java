package com.company;

/**
 * Created by hanhvn on 3/11/2017.
 */
public class CheckStringRotation {
    public static boolean Check(String s1, String s2)
    {
        if (s1.length() > 0 && s1.length() == s2.length())
        {
            String s1s1 = s1 + s1;
            if (s1s1.contains(s2))
                return true;
        }
        return false;
    }
}
