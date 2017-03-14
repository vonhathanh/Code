public class Problem
{
	public static boolean isUniqueChars(String s)
	{
		if (s.length() > 128) {
			return false;
		}
		boolean[] charSet = new boolean[128];
		for (int i = 0; i < s.length(); i++)
		{
			if (charSet[s.charAt(i)] == true) {
				return false;
			}
			charSet[s.charAt(i)] = true;
		}
		return true;
	}

	public static void main(String[] args)
	{
		String[] words = {"abcd","12312312123","045454a","012345"};
		for (String word:words) {
			System.out.println(word + ": " + isUniqueChars(word));
		}
	}
}