"""
This script moves a shark across a terminal screen. A toy example is shown below, with the same mechanism.
ABCDE
FGHIJ
KLMNO
PQRST
Only show a bit mask consisting of 3x2 chars like 
MMM
.M.
across the middle row. The output of this would be:
   .....
   .....***
   ..... *
   .....
   .....
   ....J**
   .....*
   .....
   .....
   ...IJ*
   ....O
   .....
   .....
   ..HIJ
   ...N.
   .....
   .....
   .GHI.
   ..M..
   .....
   .....
   FGH..
   .L...
   .....
   .....
  *FG...
   K....
   .....
   .....
 **F....
  *.....
   .....
   .....
***.....
 * .....
   .....
"""
import time
import os
import random

def get_mask_lines(lines_above, lines_below):
    mask_str = ""
    for i in range(lines_above):
      mask_str += "0"*35 + '\n'
    mask_str += """\
00000000000000000000000000111111111
00000000000000000000011111111111110
00000000000000000111111111111111100
00000000000000111111111111111111000
00000000000011111111111111111110000
00000000001111111111111111111110000
00000000111111111111111111111100000
00000001111111111111111111111100000
00000011111111111111111111111100000
00000111111111111111111111111100000
00001111111111111111111111111100000
00011111111111111111111111111100000
00111111111111111111111111111100000
01111111111111111111111111111100000
01111111111111111111111111111110000
11111111111111111111111111111110000
11111111111111111111111111111111000
11111111111111111111111111111111100
"""
    for i in range(lines_below):
      mask_str += "0"*35 + '\n'
    mask = list(filter(None, mask_str.split('\n')))
    return mask

def get_rand_hex(required_chars):
    ret_str = ""
    while required_chars > len(ret_str):
        ret_str += hex(random.randint(0, 2**64))[2:];
    return ret_str[:required_chars]

def create_grid(width, height, mask_line_len):
    lines = []
    for i in range(height):
        line = '.'*mask_line_len + get_rand_hex(width) + '.'*mask_line_len
        lines.append(line)
    return '\n'.join(lines)

def walking_fin(lines_above, lines_below, framerate, screen_width):
  min_height = 18
  total_height = lines_above+lines_below+min_height
  mask = get_mask_lines(lines_above, lines_below)
  mask_line_len = len(mask[0])
  background = create_grid(screen_width, total_height, mask_line_len)

  num_frames = mask_line_len*2 + (screen_width - mask_line_len - 1) + 2
  for i in range(num_frames):
      frame_text = ""
      preceding_spaces = screen_width + mask_line_len-i
      trailing_spaces = i
      mask_str = '0'.join(["0"*preceding_spaces + line + "0"*trailing_spaces for line in mask]) # Extra joining 0 is to match newline
      for i in range(len(background)):
          if background[i] == '\n':
              frame_text += '\n'
          elif background[i] == '.': # Means that background is out of frame
              continue
          elif mask_str[i] == '1':
              frame_text += background[i]
          else:
              frame_text += '*'
      frame_text += '\n\n'
      time.sleep(1/framerate)
      print(frame_text)

while True:
  walking_fin(4, 6, 12, 120)
@pocc
 
