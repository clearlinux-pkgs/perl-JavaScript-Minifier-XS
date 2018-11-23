#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-JavaScript-Minifier-XS
Version  : 0.11
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/G/GT/GTERMARS/JavaScript-Minifier-XS-0.11.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GT/GTERMARS/JavaScript-Minifier-XS-0.11.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libj/libjavascript-minifier-xs-perl/libjavascript-minifier-xs-perl_0.11-1.debian.tar.xz
Summary  : 'XS based JavaScript minifier'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-JavaScript-Minifier-XS-lib = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
JavaScript::Minifier::XS minifies JavaScript documents by removing un-necessary whitespace

%package dev
Summary: dev components for the perl-JavaScript-Minifier-XS package.
Group: Development
Requires: perl-JavaScript-Minifier-XS-lib = %{version}-%{release}
Provides: perl-JavaScript-Minifier-XS-devel = %{version}-%{release}

%description dev
dev components for the perl-JavaScript-Minifier-XS package.


%package lib
Summary: lib components for the perl-JavaScript-Minifier-XS package.
Group: Libraries

%description lib
lib components for the perl-JavaScript-Minifier-XS package.


%prep
%setup -q -n JavaScript-Minifier-XS-0.11
cd ..
%setup -q -T -D -n JavaScript-Minifier-XS-0.11 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/JavaScript-Minifier-XS-0.11/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
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
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/JavaScript/Minifier/XS.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/JavaScript::Minifier::XS.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/auto/JavaScript/Minifier/XS/XS.so
