pidgin-qq-rpm
=============
This is repo for specs and submodules to build pidgin-lwqq plugin for Fedora x86_64

How to build
------------
run *./create-sources.sh version_number* to create archives of submodules in current dir
then copy archives to ~/rpmbuild/SOURCES and specs to ~/rpmbuild/SPECS and run rpmbuild on spec files

Notes
-----
Currently builds for x86_64
