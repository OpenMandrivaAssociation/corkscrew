%define name corkscrew
%define version 2.0
%define rel     8
%define patchSet0 20060404

Name: %{name}
Summary: Tool for tunneling SSH through HTTP proxies
Version: %{version}
Release: %mkrel %{rel}
License: GPL
Url: http://www.agroman.net/%{name}
Group: Networking/Other
Source0: http://www.agroman.net/%{name}/%{name}-%{version}.tar.bz2
Patch0: %{name}-%{version}.%{patchSet0}-manpage.patch.bz2
Patch1: %{name}-%{version}.%{patchSet0}-firstpacket.patch.bz2

BuildRoot: %{_tmppath}/%{name}-buildroot



%description
Corkscrew is a tool for tunneling SSH through HTTP proxies.

%prep
%setup
%patch0 -p1 -b .manpage
%patch1 -p1 -b .firstpacket

# Fix some bad references in the man pages
perl -pi -e 's|/usr/local/bin|%{_bindir}|g;' corkscrew.1 README

%build
rm configure # to prevent aclocal's ac-wrapper from using the old autoconf 
aclocal --force
autoheader
automake -a --add-missing --force-missing --gnu
autoconf

%configure
%make

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
cp corkscrew.1 $RPM_BUILD_ROOT%{_mandir}/man1/corkscrew.1

%makeinstall


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
