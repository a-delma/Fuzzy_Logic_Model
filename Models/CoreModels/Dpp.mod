Dpp     -   input
Scw     -   input
Gbb     -   input
Punt    -   input
Tkv     1   Punt & (Dpp:1 | Scw | Gbb) & !(Sog | Tsg) & !Dpp:2
Tkv     2   Punt & Dpp:2 & !(Sog | Tsg)
Sax     1   Punt & (Gbb:1 | Scw:1 | Dpp) & !Sog
Tsg     -   input
Sog     1   !Tld
Tld     -   input
MadMed  1   [(Tkv:1 | Sax:1) & !Dad:1 & !Tkv:2] | (Tkv:2 & Dad:1)
MadMed  2   Tkv:2 & !Dad:1
Brk     1   !MadMed:1 & !Shn:1
Shn     -   input
Dad     -   input
Nej     -   input
Targets 1   MadMed & Nej:1 & !Brk:1