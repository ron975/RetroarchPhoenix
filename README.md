# RetroarchPhoenix


##The Rebirth of a Desktop U.I.

This is a "rebirth" of the RetroArch Phoenix project that was deprecated. I will probably change the name when I can think of one.
This is to provide RetroArch with an all-in-one graphical interface that focuses on desktop use. 
RGUI is a great interface for your console and t.v. however, I believe that it lacks speed when traversing the menus.
This project is so far a clone of the [OpenEmu](http://openemu.org/) frontend. Please show support for their hard work. 
This project will provide a lot of the functionality that they have provided, and more. 
Furthermore, this project is unofficial and so please directy ask questions about the frontend to me, since the
RetroArch developers will not know what you are talking about.
The official version of RetroArch is located at this [site](http://www.libretro.com/), this is the preferred. 

This frontend is free as in freedom and beer. I will not accept donations for building upon the hard work of others. I could however, use some help with the frontend, so please feel free to contact me at Druage@gmx.com.

###How it works:
  The frontend was built with [Qt 5.2](http://qt-project.org/downloads) Qml and so, utilizes Javascript and C++. I use [pyotherside](http://thp.io/2011/pyotherside/) as an alternative to PyQt5 in order to provide scripting capabilities that are written in [Python 3.3](http://www.python.org/download/releases/3.3.3/). The project also uses XML files to store user game data, I may switch this over to JSON once I have finished with the UI development. The frontend will work on Linux, OSX, and Windows; however these builds are tested alomst exclusively on Linux, though I will periodically test them on Windows, OSX is currently unknown. No binary packages currently exist because I haven't create any yet.

###Things that still need to be completed:

1. Have game artwork scrubber work.
2. Add controller mapping from within the frontend.
3. Make Rating system work.
