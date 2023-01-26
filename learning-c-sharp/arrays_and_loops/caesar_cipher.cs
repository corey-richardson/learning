using System;

namespace CaesarCipher
{
  class Program
  {
    static void Main(string[] args)
    {
      char[] alphabet = new char[] {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '};

      // set shift value here
      int shift = 3;

      // get input
      Console.WriteLine("Enter message to encode: ");
      string toEncode = Console.ReadLine();
      
      // to array
      char[] secretMessage = toEncode.ToCharArray();

      // empty array with same length
      char[] encodedArray = new char[secretMessage.Length];

      // for each letter in array
      int counter = 0;
      foreach (char letter in secretMessage)
      {
        // get index of the letter in alphabet
        int alphabetIdx = Array.IndexOf(alphabet, letter);
        // assign the corresponding value of 'encodedArray' to the shifted value
        // 27 not 26 as alphabet + space character
        // (alphabet + shift) % 27
        // z = 26, +3 = 29 --> out of range
        // therefore, mod 27, 29 --> 3 (in range)
        encodedArray[counter] = alphabet[(alphabetIdx + shift) % 27];
        counter++; // increment
      }

      // join array into single string
      string encodedString = String.Join("", encodedArray);

      // output to console
      Console.WriteLine(encodedString);

    }
  }
}

/*
$ dotnet run
Enter message to encode: 
hello world
khoorczruog
*/

/*
$ dotnet run
Enter message to encode: 
wxyz abc
z abcdef
*/

// limitation
/*
$ dotnet run
Enter message to encode: 
0123456789
cccccccccc
*/
// only lower case alpha chars and space char are listed in array
// if any other char is given it is assigned the index of -1
// -1 + 3 = 2 --> c
// c represents space char and unassigned chars