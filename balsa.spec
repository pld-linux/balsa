Summary:	balsa - GNOME e-Mail program
Summary(pl):	Klient poczty dla GNOME z silnikiem mutt-a
Summary(es):	Balsa es un lector de e-mail. Usa el toolkit GTK
Summary(pt_BR):	Balsa é um leitor de e-mail. Usa o toolkit GTK
Name:		balsa
Version:	1.4.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.theochem.kth.se/~pawsa/balsa/%{name}-%{version}.tar.bz2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	cyrus-sasl-devel
BuildRequires:	docbook-style-dsssl
BuildRequires:	flex
BuildRequires:	freetype-devel >= 2.0.0
BuildRequires:	gal-devel >= 0.19
BuildRequires:	gdk-pixbuf-gnome-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-tools
BuildRequires:	gnome-libs-devel >= 1.2.1
BuildRequires:	gnome-print-devel >= 0.25.0
BuildRequires:	gtkhtml-devel >= 0.12.0
BuildRequires:	libPropList-devel
BuildRequires:	libesmtp-devel >= 1.0
BuildRequires:	libltdl-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	openjade
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel >= 0.9.6j
BuildRequires:	pam-devel
BuildRequires:	pcre-devel
BuildRequires:	pspell-devel >= 12.1
URL:		http://balsa.gnome.org/
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

%description -l es
Balsa es un lector de e-mail. Es parte del entorno GNOME. Soporta
cajas de correo electrónico locales, POP3 y IMAP.

%description -l pl
Balsa to klient e-mail dla ¶rodowiska GNOME. Obs³uguje POP3, IMAP oraz
lokalne skrzynki pocztowe. GNOME to Network Object Model Environment.
Mimo osobliwej nazwy jest to naparwdê estetyczne ¶rodowisko graficzne.
Dziêki niemu u¿ywanie komputera jest ³atwiejsze; system jest
potê¿niejszy i ³atwo go skonfigurowaæ.

%description -l pt_BR
Balsa é um leitor de e-mail, parte do ambiente de desktop GNOME.
Suporta caixas de correio locais, POP3 a IMAP.

%prep
%setup -q

%build
rm -f missing
cd libmutt
	aclocal
	%{__autoconf}
	automake -a -c
cd ..
libtoolize --copy --force
gettextize --copy --force
aclocal -I macros
%{__autoconf}
%{__automake}
%configure \
	--enable-system-install \
	--enable-all \
	--enable-info \
	--disable-threads \
	--disable-more-warnings \
	--with-mailpath=/var/mail \
	--with-ssl \
	--with-esmtp \
	--enable-pcre \
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

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/sound/events/*
%{_datadir}/sounds/balsa
%{_pixmapsdir}/*
%{_applnkdir}/Network/Mail/*
%{_mandir}/man1/*
