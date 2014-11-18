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
to proofread the text and report the issues.

SWORD module
------------

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

Malayalam Bible in Android
--------------------------

(Credits for this instruction: Jeesmon Jacob)

1. Install `AndBible <https://play.google.com/store/apps/details?id=net.bible.android.activity>`_ from Google Play Store
2. Install `ES File Explorer <https://play.google.com/store/apps/details?id=com.estrongs.android.pop>`_ from Google Play Store. This App is for unzipping the module to a folder.
3. Download `Malayalam SWORD module <http://www.tfbf.in/downloads/mal-0.1.zip>`_ to your device
4. Open ES File Explorer and navigate to /sdcard folder. It might be the default folder when you open ES File Explorer.
5. Click device menu -> New -> Folder. Name new folder as jsword (all lowercase)
6. Navigate to Download folder. That's where the module is downloaded in Step 3.
7. Long press (not just tap) on mal-0.1.zip file. It will pop up a menu with many options. Select "Extract to" menu option.
8. Select "Choose path" option
9. Type /sdcard/jsword as the path. Click Ok.
10. Open AndBible and you will see Malayalam content (Change language to Malayalam from Menu).
