Sathyavedapusthakam
===================

This reposirory contains source of The Holy Bible translation into
Malayalam language known as `Sathyavedapusthakam published by The
British and Foreign Bible Society in 1910
<https://archive.org/details/Sathyavedapusthakam_1910>`_.  The source
format used here is `USFM <http://paratext.org/about/usfm>`_.  The
text can be converted to other formats using USFM converters.

If you are interested to help this project, you can join our
`discussion group
<https://groups.google.com/forum/#!forum/tfbfgroup>`_

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

5. Open Xiphos and verify Malayalam Bible is appearing properly

   ::

     xiphos
