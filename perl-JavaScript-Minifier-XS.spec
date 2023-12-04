#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-JavaScript-Minifier-XS
Version  : 0.15
Release  : 29
URL      : https://cpan.metacpan.org/authors/id/G/GT/GTERMARS/JavaScript-Minifier-XS-0.15.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GT/GTERMARS/JavaScript-Minifier-XS-0.15.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libj/libjavascript-minifier-xs-perl/libjavascript-minifier-xs-perl_0.11-1.debian.tar.xz
Summary  : 'XS based JavaScript minifier'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-JavaScript-Minifier-XS-license = %{version}-%{release}
Requires: perl-JavaScript-Minifier-XS-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::DiagINC)

%description
NAME
JavaScript::Minifier::XS - XS based JavaScript minifier
SYNOPSIS
use JavaScript::Minifier::XS qw(minify);
my $js       = '...';
my $minified = minify($js);

%package dev
Summary: dev components for the perl-JavaScript-Minifier-XS package.
Group: Development
Provides: perl-JavaScript-Minifier-XS-devel = %{version}-%{release}
Requires: perl-JavaScript-Minifier-XS = %{version}-%{release}

%description dev
dev components for the perl-JavaScript-Minifier-XS package.


%package license
Summary: license components for the perl-JavaScript-Minifier-XS package.
Group: Default

%description license
license components for the perl-JavaScript-Minifier-XS package.


%package perl
Summary: perl components for the perl-JavaScript-Minifier-XS package.
Group: Default
Requires: perl-JavaScript-Minifier-XS = %{version}-%{release}

%description perl
perl components for the perl-JavaScript-Minifier-XS package.


%prep
%setup -q -n JavaScript-Minifier-XS-0.15
cd %{_builddir}
tar xf %{_sourcedir}/libjavascript-minifier-xs-perl_0.11-1.debian.tar.xz
cd %{_builddir}/JavaScript-Minifier-XS-0.15
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/JavaScript-Minifier-XS-0.15/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-JavaScript-Minifier-XS
cp %{_builddir}/JavaScript-Minifier-XS-0.15/LICENSE %{buildroot}/usr/share/package-licenses/perl-JavaScript-Minifier-XS/92e92d46bac9fa036a3d260671b6ce26398461d4
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-JavaScript-Minifier-XS/279997f6998e49b91f5313df30f01aa47e6691be
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/JavaScript::Minifier::XS.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-JavaScript-Minifier-XS/279997f6998e49b91f5313df30f01aa47e6691be
/usr/share/package-licenses/perl-JavaScript-Minifier-XS/92e92d46bac9fa036a3d260671b6ce26398461d4

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
