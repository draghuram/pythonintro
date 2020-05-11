==============
 Music Player
==============

Raspberry Pi has a program called "omxplayer" that can play MP3 files
(in addition to other formats). Without any options, the program
starts playing the track at the beginning. Here is an example.

.. code-block:: bash

  $ omxplayer track1.mp3

The command has an option called ``--pos`` that can be used to start
playing at any arbitrary position in the track. For example, the
following command will start playing from 30 minute mark.

.. code-block:: bash

  $ omxplayer --pos 00:30:00 track1.mp3

Now, if you kill the command and re-run it, it will not remember where
it stopped but instead, it will start playing either at beginning
(or at the time passed using ``--pos`` option).

Your task is to implement a program called ``musicplayer.py`` that takes
a MP3 file as input and plays it. 

.. code-block:: bash

  $ musicplayer.py track1.mp3

If you kill the program and run it again, it should resume playing
the track where it left off (a few seconds rewind is ok). So you need
to come up with a mechanism of "remembering" the play location. 

Once you have this program working, extend it so that it can play
multiple tracks. The input is a file which contains multiple tracks,
with one track per line. Here is a sample input file:

.. code-block:: bash

    $ cat playlist.txt

    track1.mp3
    track2.mp3
    track3.mp3

    $ musicplayer2.py playlist.txt

In the second form, the program will play all the tracks in the play
list file, in order. But again, it should remember the location so
that when it is killed and rerun, the player should start at the right
track and at the right position in that track.

With a program such as ``musicplayer2.py``, we can use Raspberry Pi as
sort of an iPod where it can start playing a playlist every time it is
turned on.


    



  


