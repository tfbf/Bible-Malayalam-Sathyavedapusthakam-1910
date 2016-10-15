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

Modern Script
-------------
There is a separate branch https://github.com/tfbf/sathyavedapusthakam/tree/modernScript where we maintain the text in the modern orthography (Currently ൎ > ർ).



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
     osis2mod ~/.sword/modules/texts/ztext/mal/ mal.osis.xml -v NRSV -z z

   Note 1: In the old versions of `osis2mod` use `-z` option without `z` argument.
   Note 2: The versification is selected as NRSV instead of KJV to include 3 John 1:15
           Three more verses are still merged to previous verse:
           Deuteronomy 13:19 - Deuteronomy 28:69 - Song of Solomon 7:14

4. Copy configuration file

   ::

     mkdir -p ~/.sword/mods.d/
     cp conf/mal.conf ~/.sword/mods.d/

5. Open Xiphos and verify Malayalam Bible is appearing properly

   ::

     xiphos
