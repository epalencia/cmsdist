### RPM external meschach 1.2.pCMS1
Source: http://www.math.uiowa.edu/~dstewart/meschach/mesch12b.tar.gz
Patch: meschach-1.2-slc4
Patch1: meschach-1.2b-fPIC

%prep
%setup -c -n meschach-1.2 -a 0
%patch -p0
%patch1 -p0

%build
# Just fix this by hand for MacOSX (the configure probably needs to be updated)
%ifos darwin
perl -p -i -e "s|define HAVE_MALLOC_H 1|undef MALLOCDECL|g" machine.h
%endif
make
%install
mkdir -p %i/include
mkdir -p %i/lib
cp *.h %i/include
cp meschach.a %i/lib/libmeschach.a
# SCRAM ToolBox toolfile
mkdir -p %i/etc/scram.d
cat << \EOF_TOOLFILE >%i/etc/scram.d/%n
<doc type=BuildSystem::ToolDoc version=1.0>
<Tool name=Meschach version=%v>
<info url=http://www.meschach.com></info>
<lib name=meschach>
<Client>
<Environment name=MESCHACH_BASE default="%i"></Environment>
<Environment name=LIBDIR default="$MESCHACH_BASE/lib"></Environment>
<Environment name=INCLUDE default="$MESCHACH_BASE/include"></Environment>
</Client>
</Tool>
EOF_TOOLFILE

%post
%{relocateConfig}etc/scram.d/%n

