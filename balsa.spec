
%define		snap	20030103

Summary:	balsa - GNOME e-Mail program
Summary(pl):	Klient poczty dla GNOME z silnikiem mutt-a
Summary(es):	Balsa es un lector de e-mail. Usa el toolkit GTK
Summary(pt_BR):	Balsa é um leitor de e-mail. Usa o toolkit GTK
Name:		balsa
Version:	2.0.4
Release:	0.%{snap}.1
License:	GPL
Group:		X11/Applications
#Source0:	http://balsa.gnome.org/%{name}-%{version}.tar.bz2
Source0:	%{name}-%{version}-%{snap}.tar.bz2
Patch0:		%{name}-libtool_hack.patch
URL:		http://balsa.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libesmtp-devel
BuildRequires:	libgnomeprintui-devel >= 1.106.0
BuildRequires:	gtk+2-devel 
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Mimo osobliwej nazwy jest to naprawdê estetyczne ¶rodowisko graficzne.
Dziêki niemu u¿ywanie komputera jest ³atwiejsze; system jest
potê¿niejszy i ³atwo go skonfigurowaæ.

%description -l pt_BR
Balsa é um leitor de e-mail, parte do ambiente de desktop GNOME.
Suporta caixas de correio locais, POP3 a IMAP.

%prep
%setup -q
%patch0 -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure

# TODO find this gdp stylesheet
%{__make} 

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
%{_datadir}/applications/*
%{_datadir}/%{name}
%{_datadir}/sounds/%{name}
%{_mandir}/man1/*
%{_omf_dest_dir}/%{name}
%{_pixmapsdir}/*
