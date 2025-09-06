# MapTool
Tool for a GM to share player facing maps on video conferencing software.


Trying an approach where there are 2 windows:
1. A GM facing window that allows editing (fog of war, tokens, map/background, saving, loading)
2. A Player facing window that can be shared on video conferencing software, that renders only player-facing parts of the map


Current idea is to use an SVG like file that is edited on the GM side, and rendered on the Player side.

This could be donw with a wxPython GUI and using drawsvg for the backend.

A map would be stored as a json file, in a separate folder for maps.

I'm thinking there should be a shared library of map bitmaps and tokens.

To-do:
- Loading maps (which would be bitmaps, e.g. png).
- Set grid size and offset.
- Option to load and place a large (unlimited?) amount of tokens.
- Option to add fog-of-war shapes (rectangles, ellipses, free polygons).

- Option to hide grid on the GM and/or Player side.
- Option to hide tokens on the Player side (on the GM side... why?).
- Option for status rings on tokens? If tokens are circles they could just have colored strokes? (at first)

