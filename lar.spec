Summary:	LAR - Library Archiver for CP/M LU format libraries
Summary(pl.UTF-8):   LAR - narzędzie dla bibliotek w formacie LU z systemu CP/M
Name:		lar
%define	ver	5.1.2
Version:	%{ver}
Release:	1
License:	Public Domain
Group:		Development/Tools
Source0:	http://www.seasip.demon.co.uk/Unix/Lar/%{name}-%{version}.tar.gz
# Source0-md5:	66dc3bd61c4f3f633170129c129a624c
URL:		http://www.seasip.demon.co.uk/Unix/Lar/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lar is a Unix program to manipulate CP/M LU format libraries. The
original CP/M library program LU is the product of Gary P.
Novosielski. The primary use of lar is to combine several files
together for upload/download to a personal computer.

%description -l pl.UTF-8
lar to uniksowe narzędzie do manipulowania bibliotekami w formacie LU
z systemu CP/M. Oryginalny program LU do bibliotek CP/M został
stworzony przez Gary'ego P. Novosielskiego. Głównym zastosowaniem
programu lar jest łączenie kilku plików w jeden w celu przesłania lub
ściągnięcia na własny komputer.

%package lbr
Summary:	Shell script that allows the Midnight Commander to browse LBR files
Summary(pl.UTF-8):   Skrypt dla Midnight Commandera pozwalający na przeglądanie plików LBR
Group:		Applications/File
Version:	5.10
Requires:	%{name} = %{ver}
Requires:	mc

%description lbr
lbr is a shell script which, used in conjunction with lar, allows the
Midnight Commander (mc) to browse inside LBR files in the same way
that it can browse TAR files.

%description lbr -l pl.UTF-8
lbr to skrypt powłoki dla Midnight Commandera (mc), który, w
połączeniu z larem, pozwala na przeglądanie zawartości plików LBR w
ten sam sposób, co plików TAR.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -include /usr/include/errno.h"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/mc/extfs}

install lar $RPM_BUILD_ROOT%{_bindir}
install lar.1 $RPM_BUILD_ROOT%{_mandir}/man1
install lbr $RPM_BUILD_ROOT%{_datadir}/mc/extfs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/lar
%{_mandir}/man1/lar.1*

%files lbr
%defattr(644,root,root,755)
%doc lbr.doc
%attr(755,root,root) %{_datadir}/mc/extfs/lbr
