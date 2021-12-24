Stat92E 1   Hop:1 & !Su_var & !Ptp61F& !Ken & !Brwd3 & !Socs44A
Stat92E 2   Hop:2 & !Su_var & !Ptp61F& !Ken & !Brwd3 & !Socs44
Dome    1   Upd2 | OS | Upd3
Socs36E 1   Stat92E:2
OS      -   input
Hop     1   Dome & !ET & [(Stam & Hrs & Socs36E) | !(Stam & Hrs) & !Socs36E)]
Hop     2   Dome & !ET & !Socs36E & Stam & Hrs
Upd2    -   input
Upd3    -   input
Su_var  -   input
Brwd3   -   input
Socs44A -   input
NStat92E    -   input
Targets -   Stat92E & !NStat92E
Ptp61F  -   input
Ken     -   input
ET      -   input
Stam    -   input
Hrs     -   input
