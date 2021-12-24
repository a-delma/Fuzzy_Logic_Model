Pvf1    -   input
Pvf2    -   input
Pvf3    -   input
Pvr     1   Pvf1:1 | Pvf2:1 | Pvf3:1
Sty     -   input
Drk     1   Pvr:1
Aop     1   !Rl:1
Rl      1   Dsor1:1 & Msk
Sos     1   Drk:1
Raf     1   Ras & Src42 & Cnk & Ksr
Dsor1   1   Raf:1
Targets 1   Pnt:1 & !Aop:1
Ras     1   Sos:1 & !Sty:1
Pnt     1   Rl:1
Ksr     -   input
Src42   -   input
Msk     -   input
Cnk     -   input
