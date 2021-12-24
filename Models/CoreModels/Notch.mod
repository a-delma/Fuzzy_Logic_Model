Hh       -   input
Notch   1   Delta:1
Delta   -   input
E_Spl   1   !(Nicd & Mam) | !(Su_H_CSL | Hh) | !(Gro | CtBP) & Hh
E_Spl   2   Su_H & Nicd & Mam & !Hh & !Gro & !CtBP
CtBP    -   input
Nicd    -   Notch:1
Gro     -   input
Mam     -   input
Da      -   1
Su_H    -   input
Emc     1   Nicd:1
Twi     1   Da & !Emc & !E_Spl:2
Bx42    -   input
P300    -   input
