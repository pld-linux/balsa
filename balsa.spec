# TODO:
# - use webkit as html widget?
#
# Conditional build:
%bcond_without	ldap		# build without LDAP support
%bcond_with	gpgme		# build with GPG support (experimental)
%bcond_without	esmtp		# build without ESMTP support
%bcond_without	gtkhtml		# build without HTML support
%bcond_without	gtkhtml2	# build with libgtkhtml-2 (default gtkhtml-4)
%bcond_with	compface	# build with Compface
%bcond_with	gtksourceview	# build with GtkSourceView
%bcond_without	gtkspell	# build without GtkSpell
%bcond_with	sqlite		# build with SQLite for GPE address books

Summary:	Balsa Mail Client
Summary(es.UTF-8):	Balsa es un lector de e-mail
Summary(pl.UTF-8):	Balsa - klient poczty
Summary(pt_BR.UTF-8):	Balsa é um leitor de e-mail
Name:		balsa
Version:	2.4.10
Release:	2
License:	GPL v3+
Group:		X11/Applications
Source0:	http://pawsa.fedorapeople.org/balsa/%{name}-%{version}.tar.bz2
# Source0-md5:	fa2b7cb9d248912ac2e3dcc08cd6aa5b
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-gtkhtml4.patch
URL:		http://balsa.gnome.org/
BuildRequires:	ORBit2-devel >= 1:2.12.4
BuildRequires:	aspell-devel >= 2:0.50
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
%{?with_compface:BuildRequires:	compface-devel}
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 2.6.4-1
BuildRequires:	gmime-devel >= 2.4.0
BuildRequires:	gnome-doc-utils
BuildRequires:	gnome-icon-theme
%{?with_gpgme:BuildRequires:	gpgme-devel >= 1:0.9.0}
BuildRequires:	gtk+2-devel >= 2:2.10.0
%{?with_gtksourceview:BuildRequires:	gtksourceview-devel}
%{?with_gtkspell:BuildRequires:	gtkspell-devel}
BuildRequires:	heimdal-devel
BuildRequires:	intltool
%{?with_esmtp:BuildRequires:	libesmtp-devel >= 1.0.4}
%if %{with gtkhtml}
%{!?with_gtkhtml2:BuildRequires:	gtkhtml-devel >= 4.0}
%{?with_gtkhtml2:BuildRequires:	libgtkhtml-devel >= 2.0}
%endif
BuildRequires:	libgnomeui-devel >= 2.3.3.1-2
BuildRequires:	libltdl-devel
BuildRequires:	libnotify-devel
BuildRequires:	libtool
BuildRequires:	libunique-devel
%{?with_ldap:BuildRequires:	openldap-devel >= 2.4.6}
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pcre-devel >= 3.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper >= 0.1.4
# actually, it requires sqlite >= 2.8
%{?with_sqlite:BuildRequires:	sqlite3-devel}
%{?with_gpgme:Requires:	gpgme >= 1:0.9.0}
Requires(post,postun):	scrollkeeper
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Balsa is an e-mail reader. This client is part of the GNOME desktop
environment. It supports local mailboxes, POP3 and IMAP.

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
%{!?with_gtkhtml2:%patch1 -p1}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__autoconf}
%configure \
	--with-gss \
	--with-ssl \
	--with-unique \
	--disable-silent-rules \
	%{!?with_esmtp:--without-esmtp} \
%if %{with gtkhtml}
	--with-html-widget=%{?with_gtkhtml2:gtkhtml2}%{!?with_gtkhtml2:gtkhtml4} \
%else
	--disable-gtkhtml \
%endif
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

[ -d $RPM_BUILD_ROOT%{_datadir}/locale/sr@latin ] || \
	mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sr@{Latn,latin}
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
%attr(755,root,root) %{_bindir}/balsa
%attr(755,root,root) %{_bindir}/balsa-ab
%dir %{_sysconfdir}/sound/events
%{_sysconfdir}/sound/events/balsa.soundlist
%{_datadir}/%{name}
%{_datadir}/sounds/%{name}
%{_mandir}/man1/balsa.1*
%{_omf_dest_dir}/%{name}
%{_desktopdir}/balsa.desktop
%{_pixmapsdir}/gnome-balsa2.png
%{_iconsdir}/hicolor/48x48/mimetypes/*.png
