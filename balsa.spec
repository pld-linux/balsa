#
# Conditional build:
%bcond_without	ldap		# build without LDAP support
%bcond_with	gpgme		# build with GPG support (experimental)
%bcond_without	esmtp		# build without ESMTP support
%bcond_without	gtkhtml		# build without HTML support
#
Summary:	Balsa Mail Client
Summary(es):	Balsa es un lector de e-mail
Summary(pl):	Balsa - klient poczty
Summary(pt_BR):	Balsa é um leitor de e-mail
Name:		balsa
Version:	2.3.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://balsa.gnome.org/%{name}-%{version}.tar.bz2
# Source0-md5:	ab4d6febaca56d72d13acef819da193b
Patch0:		%{name}-locale-names.patch
#Patch1:		%{name}-desktop.patch
Patch2:		%{name}-includes.patch
URL:		http://balsa.gnome.org/
BuildRequires:	aspell-devel >= 2:0.50
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
%{?with_esmtp:BuildRequires:	libesmtp-devel}
BuildRequires:	libgnomeprintui-devel >= 1.106.0
BuildRequires:	glib2-devel >= 2.6.4-1
BuildRequires:	gmime-devel >= 2.1.9
%{?with_gpgme:BuildRequires:	gpgme-devel >= 1:0.9.0}
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	intltool
%{?with_gtkhtml:BuildRequires:	libgtkhtml-devel >= 2.0}
BuildRequires:	libltdl-devel
BuildRequires:	libgnomeprintui-devel >= 2.1.4
BuildRequires:	libgnomeui-devel >= 2.3.3.1-2
BuildRequires:	libtool
%{?with_ldap:BuildRequires:	openldap-devel}
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pcre-devel >= 3.0
BuildRequires:	scrollkeeper >= 0.1.4
%{?with_gpgme:Requires:	gpgme >= 1:0.9.0}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Balsa is an e-mail reader.  This client is part of the GNOME
desktop environment.  It supports local mailboxes, POP3 and
IMAP.

%description -l es
Balsa es un lector de e-mail. Es parte del entorno GNOME. Soporta
cajas de correo electrónico locales, POP3 y IMAP.

%description -l pl
Balsa to klient e-mail. Jest czê¶ci± ¶rodowiska GNOME. Obs³uguje POP3,
IMAP oraz lokalne skrzynki pocztowe. 

%description -l pt_BR
Balsa é um leitor de e-mail, parte do ambiente de desktop GNOME.
Suporta caixas de correio locais, POP3 a IMAP.

%prep
%setup -q
%patch0 -p1
#%%patch1 -p1
%patch2 -p1

rm -f po/no.{po,gmo}

%build
%{__intltoolize}
%{__glib_gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__autoconf}
%configure \
	--with-ssl \
	%{!?with_esmtp:--without-esmtp} \
	%{!?with_gtkhtml:--disable-gtkhtml}\
	%{?with_gpgme:--with-gpgme} \
	%{?with_ldap:--with-ldap}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%scrollkeeper_update_post

%postun
%update_desktop_database_postun
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/sound/events/*
%{_datadir}/%{name}
%{_datadir}/sounds/%{name}
%{_libdir}/bonobo/servers/*.server
%{_datadir}/idl/*.idl
%{_mandir}/man1/*
%{_omf_dest_dir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*
