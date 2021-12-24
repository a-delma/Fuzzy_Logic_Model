Ndl     1   DV_patterning
Gd      1   Ndl
Snk     1   Gd
Easter  1   Snk & Pipe
Pipe    -   input
DV_patterning   -   input
Spirit  1   Grass
SPE     1   Easter | Psh | Sphinx
| Spirit | Spd
Grass   1   ModSP
Fungi   -   input
GramP_Bact  -   input
Spd     1   Grass
Sphinx  1   Grass
ModSP   1   (PGRP-SA | PGRP- SD) & (GNBP1 | GNBP3)
GramN_Bact  -   input
Psh     1   Viru_Fact & !Nec
Viru_Fact   1   Fungi | GramP_Bact
PGRP-SA 1   GramP_Bact
GNBP1   1   GramP_Bact
PGRP-SD 1   DAP
DAP     1   GramN_Bact
GNBP3   1   Fungi
Nec     -   input
Spz     1   SPE