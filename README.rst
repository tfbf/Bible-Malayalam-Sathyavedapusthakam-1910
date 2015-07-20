Sathyavedapusthakam
===================

This is the content of The Holy Bible translation into Malayalam
language known as `Sathyavedapusthakam published by The British and Foreign Bible Society
in 1910 <https://archive.org/details/Sathyavedapusthakam_1910>`_.  The
source format used here is `USFM <http://paratext.org/about/usfm>`_.
The text can be converted to other formats using USFM converters.

* `Discussion Group <https://groups.google.com/forum/#!forum/tfbfgroup>`_

Proofreading
------------

The USFM source text may contain spelling mistakes.  You are welcome
to proofread the text and report the issues.  There are few `wiki
pages <https://github.com/tfbf/sathyavedapusthakam/wiki>`_ created to
explain the process.

Creating SWORD module
---------------------

1. Install SWORD utilities and xiphos (Assuming Debian/Ubuntu is used)

   ::

     sudo apt-get install libsword-utils xiphos

2. Convert USFM files to OSIS

   ::

     python scripts/usfm2osis.py mal usfm1910/*.usfm

3. Convert OSIS to SWORD module

   ::

     mkdir -p ~/.sword/modules/texts/ztext/mal/
     osis2mod ~/.sword/modules/texts/ztext/mal/ mal.osis.xml -v MAL -z z

   Note: In the old versions of `osis2mod` use `-z` option without `z` argument.

4. Copy configuration file

   ::

     mkdir -p ~/.sword/mods.d/
     cp conf/mal.conf ~/.sword/mods.d/

5. Open Xiphos and verify Malayalam Bible is appearing

   ::

     xiphos
