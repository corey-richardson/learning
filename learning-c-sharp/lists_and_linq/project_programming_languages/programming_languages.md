# Programming Languages

Do you know when C# was invented? How about your other favorite programming languages, like JavaScript, Ruby, and R?

In this project you’ll be using lists and LINQ to search a database for answers!

The data is stored in a .tsv file, which stands for tab-separated values. It’s a common way to export data from a spreadsheet or database — you might see this file type when you try to download data from apps like Microsoft Excel and Google Sheets.

Here is what the data would look like as a table (just a few random rows included):

Year	|Name	|Chief Developer	|Predecessors
--------|-------|-------------------|------------------------------------
1990	|AMOS BASIC	|François Lionet, Constantin Sotiropoulos	|STOS BASIC
1991	|Visual Basic	|Alan Cooper (sold to Microsoft)	|QuickBASIC
1995	|Ruby	|Yukihiro Matsumoto	|Smalltalk;Perl
2009	|Go	|Google	|C;Oberon;Limbo;Smalltalk

In Program.cs, the data importing is already taken care of, so you can focus on the queries! The data is stored in languages which is a list of type `List<Language>`. You can find the definition for the Language class in Language.cs. Here are the class’s important members:

- int Year — When the language was invented
- string Name — The name of the language
- string ChiefDeveloper — The head developer and/or company responsible for making the language
- string Predecessors — The other programming languages that this language is based on
- string Prettify() — Returns a nicely formatted string version of the object