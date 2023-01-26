using System;

namespace ExquisiteCorpse
{
  class Program
  {
    static void Main(string[] args)
    {
      //BuildACreature("ghost","monster","bug");
      RandomMode();
    }

    static void BuildACreature(string head, string body, string feet)
    {
      switch(head)
      {
        case "ghost":
          GhostHead();
          break;
        case "bug":
          BugHead();
          break;
        case "monster":
          MonsterHead();
          break;
        default:
          break;
      }
      switch(body)
      {
        case "ghost":
          GhostBody();
          break;
        case "bug":
          BugBody();
          break;
        case "monster":
          MonsterBody();
          break;
        default:
          break;
      }
      switch(feet)
      {
        case "ghost":
          GhostFeet();
          break;
        case "bug":
          BugFeet();
          break;
        case "monster":
          MonsterFeet();
          break;
        default:
          break;
      }
    }

    static void RandomMode()
    {
      Random rnd = new Random();
      int head = rnd.Next(1,4);
      int body = rnd.Next(1,4);
      int feet = rnd.Next(1,4);

      switch(head)
      {
        case 1:
          GhostHead();
          break;
        case 2:
          BugHead();
          break;
        case 3:
          MonsterHead();
          break;
        default:
          break;
      }
      switch(body)
      {
        case 1:
          GhostBody();
          break;
        case 2:
          BugBody();
          break;
        case 3:
          MonsterBody();
          break;
        default:
          break;
      }
      switch(feet)
      {
        case 1:
          GhostFeet();
          break;
        case 2:
          BugFeet();
          break;
        case 3:
          MonsterFeet();
          break;
        default:
          break;
      }
    }
    static void GhostHead()
    {
      Console.WriteLine("     ..-..");
      Console.WriteLine("    ( o o )");
      Console.WriteLine("    |  O  |");
    }

    static void GhostBody()
    {
      Console.WriteLine("    |     |");
      Console.WriteLine("    |     |");
      Console.WriteLine("    |     |");
    }

    static void GhostFeet()
    {
      Console.WriteLine("    |     |");
      Console.WriteLine("    |     |");
      Console.WriteLine("    '~~~~~'");
    }

    static void BugHead()
    {
      Console.WriteLine("     /   \\");
      Console.WriteLine("     \\. ./");
      Console.WriteLine("    (o + o)");
    }

    static void BugBody()
    {
      Console.WriteLine("  --|  |  |--");
      Console.WriteLine("  --|  |  |--");
      Console.WriteLine("  --|  |  |--");
    }

    static void BugFeet()
    {
      Console.WriteLine("     v   v");
      Console.WriteLine("     *****");
    }

    static void MonsterHead()
    {
      Console.WriteLine("     _____");
      Console.WriteLine(" .-,;='';_),-.");
      Console.WriteLine("  \\_\\(),()/_/");
      Console.WriteLine("　  (,___,)");
    }

    static void MonsterBody()
    {
      Console.WriteLine("   ,-/`~`\\-,___");
      Console.WriteLine("  / /).:.('--._)");
      Console.WriteLine(" {_[ (_,_)");
    }

    static void MonsterFeet()
    {
      Console.WriteLine("    |  Y  |");
      Console.WriteLine("   /   |   \\");
      Console.WriteLine("   \"\"\"\" \"\"\"\"");
    }
  }
}
