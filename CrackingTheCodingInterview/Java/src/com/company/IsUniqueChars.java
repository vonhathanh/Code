package com.company;

public class IsUniqueChars
{
	public static boolean isUniqueChars(String s)
	{
		if (s.length() > 128)
		{
			return false;
		}
		boolean[] charSet = new boolean[128];
		for (int i = 0; i < s.length(); i++)
		{
			if (charSet[s.charAt(i)] == true)
			{
				return false;
			}
			charSet[s.charAt(i)] = true;
		}
		return true;
	}

	public static boolean isUniqueChars2(String s)
	{
		if (s.length() > 128)
		{
			return false;
		}
		int checker = 0;
		for (int i = 0; i < s.length(); i++)
		{
			int val = s.charAt(i) - 'a';
			if ((checker & (1 << val)) > 0) return false;
			checker |= (1 << val);
		}
		return true;
	}
}