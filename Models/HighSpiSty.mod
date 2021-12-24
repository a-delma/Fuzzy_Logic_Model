Aos     -   input
Cbl     -   input
Cnk     -   input
Der     1   [(Spi:1 | Vein) & !Aos:1 & !Kek:1 & !Cbl & !Spi:2 & Shc] | [Spi:2 & Shc & (Kek:1 | Aos:1 | Cbl)]
Der     2   Spi:2 & !Kek:1 & !Aos:1 & !Cbl & Shc
Drk     1   Der:1 & !Der:2
Drk     2   Der:2
Dsor1   1   Raf:1 & !Raf:2
Dsor1   2   Raf:2
Gap1    1   PLCg:1 | PLCg:2 
Kek     -   input
Ksr     -   input
Msk     -   input
PLCg    1   Der:1
Pnt     1   Rl:1
Pnt     2   Rl:2
Raf     1   Ras:1 & !Ras:2 & Cnk & Src42 & Ksr
Raf     2   Ras:2 & Cnk & Src42 & Ksr
Ras     1   Sos:1 & !(Sty:1 & Gap1) | Gap1:1 & Sty:1 & Sos:2
Ras     2   Sos:2 & !(Sty:1 & Gap1)
Rl      1   Dsor1:1 & !Dsor1:2 & Msk
Rl      2   Dsor1:2 & Msk
Shc     -   input
Sos     1   Drk:1 & !Drk:2
Sos     2   Drk:2
Spi     -   input
Sty     -   input
Src42   -   input
Vein    1   Spi & Der
Aop     1   !Rl
Gro     1   !Rl
Cic     1   !Rl
Targets 1   (Pnt:1 | Pnt:2) & !Aop & !(Cic & Gro) 