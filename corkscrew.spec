%define patchSet0 20060404

Name: corkscrew
Summary: Tool for tunneling SSH through HTTP proxies
Version: 2.0
Release: 8
License: GPL
Url: http://www.agroman.net/%{name}
Group: Networking/Other
Source0: http://www.agroman.net/%{name}/%{name}-%{version}.tar.bz2
Patch0: %{name}-%{version}.%{patchSet0}-manpage.patch.bz2
Patch1: %{name}-%{version}.%{patchSet0}-firstpacket.patch.bz2

%description
Corkscrew is a tool for tunneling SSH through HTTP proxies.

%prep
%setup
%patch0 -p1 -b .manpage
%patch1 -p1 -b .firstpacket

# Fix some bad references in the man pages
perl -pi -e 's|/usr/local/bin|%{_bindir}|g;' corkscrew.1 README

%build
rm -f install-sh missing mkinstalldirs
sed -i -e 's:AM_C_PROTOTYPES:dnl &:' configure.in
autoreconf -fi

%configure
%make

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
cp corkscrew.1 %{buildroot}%{_mandir}/man1/corkscrew.1

%makeinstall

%files
%doc README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
