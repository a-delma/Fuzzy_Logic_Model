Wg      1   Dally:1 & Dlp:1
Fz      1   Wg:1 & Boca
Arr     1   Wg:1
Dsh     1   (Arr:1 | Fz:1) & !Nkd
Axin    1   !Dsh:1
Sgg     1   !Dsh:1
APC     1   !Dsh:1
Arm     1   !Sgg:1 & !APC:1 & ! Axin:1 & !(Proteasome & Slmb) & Hipk & CK1alpha
Proteasome -    input
Slmb    -   input
Hipk    -   input
Pan     1   Arm:1 & !Nemo:1
Nemo    1   Pan:1
Pygo    -   input
Nej     -   input
Lgs     -   input
Hyx     -   input
Gro     -   input
Wf      -   input
Nkd     -   input
Boca    -   input
CK1alpha    -   input
Dlp     1   Ttv & !Wf
Ttv     -   input
Dally   1   Ttb & !Wf
Targets 1   Pygo:1 & Lgs:1 & CBP:1 & PAN:1 & Hyx:1 & !Gro
