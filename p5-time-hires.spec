### RPM external p5-time-hires 1.66
## INITENV +PATH PERL5LIB %i/lib/site_perl/%perlversion/%perlarch
%define perlversion %(perl -e 'printf "%%vd", $^V')
%define perlarch %(perl -MConfig -e 'print $Config{archname}')
%define downloadn Time-HiRes

Requires: perl-virtual
Source: http://search.cpan.org/CPAN/authors/id/J/JH/JHI/%{downloadn}-%{v}.tar.gz
%prep
%setup -n %downloadn-%v
%build
LC_ALL=C; export LC_ALL
perl Makefile.PL PREFIX=%i LIB=%i/lib/site_perl/%perlversion
make
