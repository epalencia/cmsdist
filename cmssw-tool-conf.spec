### RPM cms cmssw-tool-conf 18.8
# with cmsBuild, change the above version only when a new
# tool is added

Provides: libboost_regex-gcc-mt.so 
Provides: libboost_signals-gcc-mt.so 
Provides: libboost_thread-gcc-mt.so

Requires: fakesystem
Requires: gcc-toolfile
Requires: gmake
Requires: pcre
Requires: zlib
Requires: bz2lib
Requires: uuid
Requires: python
Requires: expat
Requires: openssl-toolfile
Requires: db4
Requires: gdbm
Requires: gccxml
Requires: boost
Requires: gsl-toolfile
Requires: clhep-toolfile
Requires: root
Requires: roofit
Requires: xrootd
Requires: qt
Requires: castor-toolfile
Requires: libpng
Requires: libjpg
Requires: dcap-toofile 
Requires: oracle
Requires: oracle-env
Requires: libungif
Requires: libtiff
Requires: cppunit
Requires: frontier_client
Requires: sqlite
Requires: graphviz
Requires: xerces-c
Requires: systemtools
Requires: coral
Requires: xdaq
Requires: geant4-toolfile
Requires: hepmc
Requires: heppdt
Requires: elementtree
Requires: sigcpp
Requires: mimetic
Requires: rulechecker
Requires: soqt
Requires: coin
Requires: curl
Requires: simage
Requires: tkonlinesw
Requires: meschach
Requires: glimpse
Requires: valgrind
Requires: google-perftools
Requires: fastjet-toolfile
Requires: ktjet
Requires: lhapdf-toolfile
Requires: pythia6-toolfile
Requires: pythia8-toolfile
Requires: jimmy
Requires: hector
Requires: alpgen
Requires: tauola
Requires: toprex
Requires: charybdis
Requires: photos
Requires: cmsswdata
Requires: dpm-toolfile
Requires: evtgenlhc
Requires: mcdb
Requires: dbs-client
Requires: herwigpp
Requires: thepeg-toolfile
Requires: libhepml
Requires: python-ldap
Requires: millepede
Requires: gdb
Requires: pyqt
Requires: igprof-toolfile
Requires: py2-matplotlib-toolfile
Requires: py2-numpy-toolfile
Requires: classlib-toolfile
Requires: herwig-toolfile
Requires: sherpa-toolfile
Requires: cascade-toolfile
Requires: fftw3-toolfile
Requires: fftjet-toolfile
Requires: rivet-toolfile

%define skipreqtools jcompiler lhapdfwrapfull lhapdffull

## IMPORT scramv1-tool-conf
