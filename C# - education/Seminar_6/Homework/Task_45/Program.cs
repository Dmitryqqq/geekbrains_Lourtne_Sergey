using System;

public class Example
{
	public static void Main()
	{
		int[] arr = { 5, 4, 7, 2, 9 };
		int start = 1;
		int length = 3;

		int[] copy = new int[length];
		Array.Copy(arr, start, copy, 0, length);

		Console.WriteLine(String.Join(", ", copy));
	}
}