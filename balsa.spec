# TODO:
#       - not packaged /usr/share/locale/ar/LC_MESSAGES/balsa.mo
#       - problems with id locale
#
# Conditional build:
%bcond_without	ldap		# build without LDAP support
%bcond_with	gpgme		# build with GPG support (experimental)
%bcond_without	esmtp		# build without ESMTP support
%bcond_without	gtkhtml		# build without HTML support
%bcond_with	gtkhtml2	# build with libgtkhtml-2 (default gtkhtml-3)
%bcond_with	compface	# build with Compface
%bcond_with	gtksourceview	# build with GtkSourceView
%bcond_without	gtkspell	# build without GtkSpell
%bcond_with	sqlite		# build with SQLite for GPE address books
#
Summary:	Balsa Mail Client
Summary(es.UTF-8):	Balsa es un lector de e-mail
Summary(pl.UTF-8):	Balsa - klient poczty
Summary(pt_BR.UTF-8):	Balsa é um leitor de e-mail
Name:		balsa
Version:	2.3.20
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://balsa.gnome.org/%{name}-%{version}.tar.bz2
# Source0-md5:	64763beb79731649da7e327b1140843a
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-includes.patch
Patch2:		%{name}-without_id_lang.patch
URL:		http://balsa.gnome.org/
BuildRequires:	ORBit2-devel >= 1:2.12.4
BuildRequires:	aspell-devel >= 2:0.50
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
%{?with_compface:BuildRequires:	compface-devel}
BuildRequires:	glib2-devel >= 2.6.4-1
BuildRequires:	gmime-devel >= 2.1.9
%{?with_gpgme:BuildRequires:	gpgme-devel >= 1:0.9.0}
BuildRequires:	gtk+2-devel >= 2:2.10.0
%{?with_gtksourceview:BuildRequires:	gtksourceview-devel}
%{?with_gtkspell:BuildRequires:	gtkspell-devel}
BuildRequires:	intltool
BuildRequires:	krb5-devel
%{?with_esmtp:BuildRequires:	libesmtp-devel >= 1.0.4}
%if %{with gtkhtml}
%{?with_gtkhtml2:BuildRequires:	libgtkhtml-devel >= 2.0}
%{!?with_gtkhtml2:BuildRequires:	gtkhtml-devel >= 3.0}
%endif
BuildRequires:	libgnomeui-devel >= 2.3.3.1-2
BuildRequires:	libltdl-devel
BuildRequires:	libnotify-devel
BuildRequires:	libtool
%{?with_ldap:BuildRequires:	openldap-devel >= 2.4.6}
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pcre-devel >= 3.0
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper >= 0.1.4
# actually, it requires sqlite >= 2.8
%{?with_sqlite:BuildRequires:	sqlite3-devel}
%{?with_gpgme:Requires:	gpgme >= 1:0.9.0}
Requires(post,postun):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Balsa is an e-mail reader.  This client is part of the GNOME
desktop environment.  It supports local mailboxes, POP3 and
IMAP.

%description -l es.UTF-8
Balsa es un lector de e-mail. Es parte del entorno GNOME. Soporta
cajas de correo electrónico locales, POP3 y IMAP.

%description -l pl.UTF-8
Balsa to klient e-mail. Jest częścią środowiska GNOME. Obsługuje POP3,
IMAP oraz lokalne skrzynki pocztowe. 

%description -l pt_BR.UTF-8
Balsa é um leitor de e-mail, parte do ambiente de desktop GNOME.
Suporta caixas de correio locais, POP3 a IMAP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__intltoolize}
%{__glib_gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__autoconf}
%configure \
	--with-gss \
	--with-ssl \
	%{!?with_esmtp:--without-esmtp} \
	%{!?with_gtkhtml:--disable-gtkhtml}\
	%{?with_gtkhtml2:--with-gtkhtml=2}\
	%{?with_gpgme:--with-gpgme} \
	%{?with_compface:--with-compface} \
	%{?with_gtksourceview:--with-gtksourceview} \
	%{?with_gtkspell:--with-gtkspell} \
	%{?with_sqlite:--with-sqlite} \
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
%scrollkeeper_update_post

%postun
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
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_iconsdir}/hicolor/48x48/mimetypes/*.png
