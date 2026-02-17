----Smart transport weight management system-----
Personalization Details

L value (Length of Name): L = len(name)

PLI value: PLI = L % 3

Applied Rule:

PLI Value	Rule Applied
0	All overload entries are moved to invalid_entries.
1	All very_light entries are removed.
2	All overload, very_light, and invalid_entries are removed.
