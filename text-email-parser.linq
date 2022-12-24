<Query Kind="Program">
  <Output>DataGrids</Output>
</Query>

void Main()
{
	string fname = "C:/dev/py-outlook/outlook-insight-2022-nov.CSV";
	string contents = File.ReadAllText(fname);

	const string Pattern =
		 @"(([\w-]+\.)+[\w-]+|([a-zA-Z]{1}|[\w-]{2,}))@"
		 + @"((([0-1]?[0-9]{1,2}|25[0-5]|2[0-4][0-9])\.([0-1]?[0-9]{1,2}|25[0-5]|2[0-4][0-9])\."
		   + @"([0-1]?[0-9]{1,2}|25[0-5]|2[0-4][0-9])\.([0-1]?[0-9]{1,2}|25[0-5]|2[0-4][0-9])){1}|"
		 + @"([a-zA-Z]+[\w-]+\.)+[a-zA-Z]{2,4})";

	// set up regex instance with options
	Regex emailPattern = new Regex(Pattern, RegexOptions.Compiled | RegexOptions.IgnoreCase);

	// perform match
	MatchCollection emailMatches = emailPattern.Matches(contents);

	// set up our string builder
	StringBuilder sb = new StringBuilder();

	// build the list
	Console.WriteLine("---EXTRACTED EMAIL ADDRESSES---");
	emailMatches
	.Select(x => x.Value.ToLower())
	.Distinct()
	.OrderBy(x=>x)
	.Dump("emails");

}

// You can define other methods, fields, classes and namespaces here