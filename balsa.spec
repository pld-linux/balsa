Summary:	balsa - GNOME e-Mail program
Name:		balsa
Version:	0.8.0
Release:	1
License:	GPL
Group:		X11/GNOME
Group(pl):	X11/GNOME
Source0:	ftp://ftp.newton.cx/pub/balsa/%{name}-%{version}.tar.gz
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	libPropList-devel
URL:		http://www.newton.cx/balsa/main.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME
%define		_localstatedir	/var

%description
e-Mail program for the GNOME desktop, supporting local mailboxes, POP3
and IMAP. GNOME is the GNU Network Object Model Environment. That's a
fancy name but really GNOME is a nice GUI desktop environment. It
makes using your computer easy, powerful, and easy to configure.

%description -l pl
Balsa to klient e-mail dla ¶rodowiska GNOME. Obs³uguje POP3, IMAP oraz
lokalne skrzynki pocztowe. GNOME to Network Object Model Environment.
Mimo osobliwej nazwy jest to naparwdê estetyczne ¶rodowisko graficzne.
Dziêki niemu u¿ywanie komputera jest ³atwiejsze; system jest
potê¿niejszy i ³atwo go skonfigurowaæ.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
gettextize --copy --force 
%configure \
	--enable-system-install \
	--enable-all \
	--enable-info \
	--enable-threads
make

%install
rm -rf $RPM_BUILD_ROOT

make install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_applnkdir}/Networking/Mail

gzip -9nf AUTHORS ChangeLog NEWS README TODO \
	$RPM_BUILD_ROOT%{_mandir}/man1/*

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/CORBA/servers/*
%{_sysconfdir}/sound/events/*
%{_datadir}/sounds/balsa
%{_datadir}/pixmaps/balsa
%{_applnkdir}/Networking/Mail/*
%{_mandir}/man1/*
