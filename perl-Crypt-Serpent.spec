#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Serpent
Summary:	Crypt::Serpent Perl module - Serpent block cipher implementation
Summary(pl):	Modu³ Perla Crypt::Serpent - implementacja szyfru blokowego Serpent
Name:		perl-Crypt-Serpent
Version:	1.01
Release:	1
# it's basically BSD, but contains code with clause:
# > This code is freely distributed for AES selection process.
# > No other use is allowed.
# (but AES selection is over - Rijndael has won...)
License:	non-distributable, unusable(?)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
NoSource:	0
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Term-ReadKey
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::Serpent is Crypt::CBC compliant Serpent block cipher encryption
module. Serpent was designed by Ross Anderson, Eli Biham and Lars
Knudsen as a candidate for the Advanced Encryption Standard. It has
been selected as one of the five finalists in the AES competition.
Serpent is faster than DES and more secure than Triple DES. Serpent is
a 128-bit block cipher. The key length can vary, but for the purposes
of the AES it is defined to be either 128, 192, or 256 bits. The
Serpent algorithm uses 32 rounds, or iterations of the main algorithm.

%description -l pl
Crypt::Serpent to zgodny z Crypt::CBC modu³ szyfru blokowego Serpent.
Serpent zosta³ zaprojektowany przez Rossa Andersona, Eli Bihama i
Larsa Knudsena jako kandydat na AES (Advanced Encryption Standard -
standard zaawansowanego szyfrowania). Zosta³ wybrany jako jeden z
piêciu finalistów konkursu na AES. Serpent jest szybszy ni¿ DES i
bezpieczniejszy ni¿ Triple DES. Jest 128-bitowym szyfrem blokowym
D³ugo¶æ klucza mo¿e byæ ró¿na, na potrzeby AES zosta³a zdefiniowana
jako 128, 192 lub 256 bitów. Algorytm u¿ywa 32 iteracji podstawowego
algorytmu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorarch}/Crypt/Serpent.pm
%dir %{perl_vendorarch}/auto/Crypt/Serpent
%{perl_vendorarch}/auto/Crypt/Serpent/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/Serpent/*.so
%{_mandir}/man3/*
