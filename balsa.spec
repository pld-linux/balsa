Summary:	balsa - GNOME e-Mail program
Summary(pl):	Klient poczty dla GNOME z silnikiem mutt-a
Name:		balsa
Version:	1.1.7
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://www.theochem.kth.se/~pawsa/balsa/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	docbook-style-dsssl
BuildRequires:	gnome-doc-tools
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel >= 1.2.0
BuildRequires:	gnome-print-devel
BuildRequires:	gtkhtml-devel >= 0.9.2
BuildRequires:	flex
BuildRequires:	libesmtp-devel
BuildRequires:	libltdl-devel
BuildRequires:	libPropList-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	openjade
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel
BuildRequires:	pspell-devel >= 12.1
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
Balsa to klient e-mail dla �rodowiska GNOME. Obs�uguje POP3, IMAP oraz
lokalne skrzynki pocztowe. GNOME to Network Object Model Environment.
Mimo osobliwej nazwy jest to naparwd� estetyczne �rodowisko graficzne.
Dzi�ki niemu u�ywanie komputera jest �atwiejsze; system jest
pot�niejszy i �atwo go skonfigurowa�.

%prep
%setup -q

%build
libtoolize --copy --force
gettextize --copy --force 
aclocal -I macros
autoconf
rm -f missing
automake -a -c
(cd libmutt
aclocal
autoconf
automake -a -c)
%configure \
	--enable-system-install \
	--enable-all \
	--enable-info \
	--enable-threads \
	--disable-more-warnings \
	--with-mailpath=/var/mail \
	--with-ssl \
	--enable-ldap \
	--enable-gtkhtml

# TODO find this gdp stylesheet
%{__make} \
	GDP_STYLESHEET=/usr/share/sgml/docbook/gnome-customization-1.0/gdp-both.dsl

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_applnkdir}/Network/Mail

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/sound/events/*
%{_datadir}/sounds/balsa
%{_pixmapsdir}/*
%{_applnkdir}/Network/Mail/*
%{_mandir}/man1/*
