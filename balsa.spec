#
# Conditional build:
# --without ldap

%define		snap	20030522

Summary:	balsa - GNOME e-Mail program
Summary(pl):	Klient poczty dla GNOME z silnikiem mutt-a
Summary(es):	Balsa es un lector de e-mail. Usa el toolkit GTK
Summary(pt_BR):	Balsa � um leitor de e-mail. Usa o toolkit GTK
Name:		balsa
Version:	2.0.11
Release:	1.%{snap}
#Release:	1
License:	GPL
Group:		X11/Applications
#Source0:	http://balsa.gnome.org/%{name}-%{version}.tar.bz2
Source0:	%{name}-%{version}-%{snap}.tar.bz2
# Source0-md5: 75d91e8c0b3fa10bc8b0d63eb7d29c2c
Patch0:		%{name}-libtool_hack.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-message-tree-patch-2003-05-22.gz
Patch3:		%{name}-gcc33.patch
URL:		http://balsa.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libesmtp-devel
BuildRequires:	libgnomeprintui-devel >= 1.106.0
BuildRequires:	gpgme-devel >= 0.3.14 
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:  libgtkhtml-devel
BuildRequires:  libgnome-devel
BuildRequires:  libgnomeui-devel
%{!?_without_ldap:BuildRequires:	openldap-devel}
BuildRequires:  aspell-devel >= 0.50
BuildRequires:	xft-devel
Requires:	gpgme >= 0.3.14
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
e-Mail program for the GNOME desktop, supporting local mailboxes, POP3
and IMAP. GNOME is the GNU Network Object Model Environment. That's a
fancy name but really GNOME is a nice GUI desktop environment. It
makes using your computer easy, powerful, and easy to configure.

%description -l es
Balsa es un lector de e-mail. Es parte del entorno GNOME. Soporta
cajas de correo electr�nico locales, POP3 y IMAP.

%description -l pl
Balsa to klient e-mail dla �rodowiska GNOME. Obs�uguje POP3, IMAP oraz
lokalne skrzynki pocztowe. GNOME to Network Object Model Environment.
Mimo osobliwej nazwy jest to naprawd� estetyczne �rodowisko graficzne.
Dzi�ki niemu u�ywanie komputera jest �atwiejsze; system jest
pot�niejszy i �atwo go skonfigurowa�.

%description -l pt_BR
Balsa � um leitor de e-mail, parte do ambiente de desktop GNOME.
Suporta caixas de correio locais, POP3 a IMAP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3	-p1

%build
#%glib-gettextize --copy --force
#%intltoolize --copy --force
#%%{__libtoolize}
#%%{__aclocal}
#%%{__autoheader}
#%%{__automake}
#%%{__autoconf}

#%cd libmutt
#%%{__libtoolize}
#%%{__aclocal}
#%%{__autoheader}
#%%{__automake}
#%%{__autoconf}
#%cd ..
./autogen.sh
%configure \
	--with-ssl \
	--with-gpgme \
	%{!?_without_ldap:--enable-ldap} \
	%{?_without_ldap:--disable-ldap}

%{__make} CFLAGS="%{rpmcflags} -fno-strict-aliasing"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT 

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /usr/bin/scrollkeeper-update 

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/sound/events/*
%{_datadir}/%{name}
%{_datadir}/sounds/%{name}
%{_mandir}/man1/*
%{_omf_dest_dir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*
