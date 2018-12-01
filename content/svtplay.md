Title: Ladda ned videor från SVT Play, TV4 Play och UR Play
Date: 2018-11-18
Category: Vetenskap
Authors: Peter M. Dahlgren
Slug: svt-play
Summary: Ladda ned videoklipp från SVT Play till mp4-format med hjälp av webbläsartilägg till Chrome, samt Python-tillägget svtplay-dl.

SVT Play låter inte användare ladda ned deras videoklipp, vilket gör det svårt för forskningsyften. Det finns dock några sätt runt problemet.

## Privatkopiera för Chrome och Firefox

[Privatkopiera](https://stefansundin.github.io/privatkopiera/) är ett tillägg för Chrome och Firefox som låter dig ladda ned videoklipp från en mängd webbplatser:

- svtplay.se (även direktsändningar)
- svt.se
- oppetarkiv.se
- sverigesradio.se
- urplay.se
- urskola.se
- tv4.se
- tv4play.se (ej premium/direktsändningar)
- tv.nrk.no
- radio.nrk.no

## Python-paketet `svtplay-dl`

Ett annat alternativ är att använda Python-paketet [svtplay-dl](https://svtplay-dl.se/install/)

Du installerar det enklast via Linux (Ubuntus pakethanterare `apt-get` i det här fallet):

```bash
$ sudo apt-get install svtplay-dl
```

Därefter är det bara att köra kommandot följt av webbadressen till videoklippet:

```bash
$ svtplay-dl https://www.svtplay.se/video/19051331/svenska-nyheter/svenska-nyheter-sasong-2-avsnitt-1
```

Det finns också ett Python-paket som heter `youtube-dl` som fungerar för YouTube-videor.