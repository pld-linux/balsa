Summary:	balsa - GNOME e-Mail program
Name:		balsa
Version:	0.6.0
Release:	1
License:	GPL
Group:		X11/GNOME
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch:		%{name}-locale.patch
BuildRoot:	/tmp/%{name}-%{version}-root
URL:		http://www.balsa.net/

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME
%define		_localstatedir	/var
%define		_applnkdir	%{_datadir}/applnk

%description
e-Mail program for the GNOME desktop, supporting local mailboxes, POP3 and
IMAP.  GNOME is the GNU Network Object Model Environment.  That's a fancy
name but really GNOME is a nice GUI desktop environment.  It makes using
your computer easy, powerful, and easy to configure.

%prep
%setup -q
%patch -p1
%build
LDFLAGS="-s"; export LDFLAGS
autoconf
%configure \
	--enable-system-install \
	--enable-all \
	--enable-info \
	--enable-threads
make

%install
rm -rf $RPM_BUILD_ROOT

install -d 		$RPM_BUILD_ROOT%{_applnkdir}/Networking/Mail

make install		DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1}	$RPM_BUILD_ROOT%{_applnkdir}/Networking/Mail

gzip -9nf AUTHORS COPYING ChangeLog INSTALL NEWS README TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,COPYING,ChangeLog,INSTALL,NEWS,README,TODO}.gz
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/sounds/balsa
%dir %{_datadir}/pixmaps/balsa
%dir %{_datadir}/gnome/help/balsa
%{_sysconfdir}/CORBA/servers/*
%{_sysconfdir}/sound/events/*
%{_datadir}/sounds/balsa/*
%{_datadir}/pixmaps/balsa/*
%{_datadir}/idl/*
%{_datadir}/gnome/help/balsa/*
%{_applnkdir}/Networking/Mail/*
