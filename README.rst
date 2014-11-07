Digital Sathyavedapusthakam
===========================

This is the content of The Holy Bible translation into Malayalam
language known as `Sathyavedapusthakam published by The British and Foreign Bible Society
in 1910 <https://archive.org/details/Sathyavedapusthakam_1910>`_.  The
source format used here is `USFM <http://paratext.org/about/usfm>`_.
The text can be converted to other formats using USFM converters.

* `Discussion Group <https://groups.google.com/forum/#!forum/tfbfgroup>`_

Installation
------------

To run the *svpm* program, you need Python 3.4 and few other third
party dependencies.  This is only tested in Debian GNU/Linux -
*Jessie* version and Fedora 20.  It may work in other GNU/Linux
distributions also.  These are the steps to install *svpm* program in
Debian GNU/Linux and Fedora 20.

1. Install `development libraries
   <https://docs.python.org/devguide/setup.html>`_ and other
   dependencies as root user

   a. Debian

      ::

        # apt-get -y build-dep python3
        # apt-get -y install wget git

   b. Fedora

      ::

        # yum install -y yum-utils wget git
        # yum-builddep python3

2. Install Python 3.4

   a. Download `Python 3.4 XZ compressed source tarball
      <https://www.python.org/ftp/python/3.4.0/Python-3.4.0.tar.xz>`_

      ::

      
        $ wget -c https://www.python.org/ftp/python/3.4.0/Python-3.4.0.tar.xz

   b. Extract Python source tarball, build and install

      ::

        $ tar Jxvf Python-3.4.0.tar.xz
        $ cd Python-3.4.0
        $ ./configure --prefix=$HOME/usr
        $ make
        $ make install

3. Create a `virtual environment
   <https://docs.python.org/3.4/library/venv.html>`_ and activate it

   ::

     $ $HOME/usr/bin/pyvenv $HOME/ve
     $ source $HOME/ve/bin/activate

4. Clone the `parsely <http://parsley.readthedocs.org>`_ code from the
   Git repository and install it

   ::

     $ cd $HOME
     $ git clone git@github.com:vsajip/parsley.git
     $ cd parsley
     $ python setup.py install

5. Clone the *svpm* code from the Git repository and install it

   ::

     $ cd $HOME
     $ git clone git@bitbucket.org:sathyavedapusthakam/svpm.git
     $ cd svpm
     $ python setup.py develop

6. Now you can run the *svpm* program with various arguments
   For example, to convert the USFM files to HTML::

     $ svpm -c conf/html.cfg --html


Proofreading
------------

The USFM source text may contain spelling mistakes.  You are welcome
to proofread the text and report the issues.
