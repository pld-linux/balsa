# Note that this is NOT a relocatable package
%define ver      0.4.9
%define rel      bero1
%define prefix   /usr/gnome

Summary: balsa - GNOME e-Mail program
Name: balsa
Version: %ver
Release: %rel
Copyright: GPL
Group: X11/GNOME
Source: ftp://ftp.gnome.org/pub/GNOME/sources/balsa-%{ver}.tar.bz2
BuildRoot: /var/tmp/balsa-root
URL: http://www.balsa.net/
Docdir: %{prefix}/doc
Requires: gnome-libs >= 0.99.1

%description
e-Mail program for the GNOME desktop, supporting local mailboxes, POP3 and
IMAP.

GNOME is the GNU Network Object Model Environment.  That's a fancy
name but really GNOME is a nice GUI desktop environment.  It makes
using your computer easy, powerful, and easy to configure.

%changelog
* Wed Jan 27 1999 Bernhard Rosenkraenzer <bero@microsoft.sucks.eu.org>
- initial version

%prep
%setup

%build
# balsa doesn't like new ORBits...
cd idl
orbit-idl balsa.idl
cd ..

# Needed for snapshot releases.
if [ ! -f configure ]; then
  CFLAGS="$RPM_OPT_FLAGS" ./autogen.sh --prefix=%prefix --with-gnome=%prefix \
	--with-gtk-prefix=/usr
else
  CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%prefix --with-gnome=%prefix \
	--with-gtk-prefix=/usr
fi

if [ "$SMP" != "" ]; then
  (make "MAKE=make -k -j $SMP"; exit 0)
  make
else
  make
fi

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%{prefix}/bin/*
%{prefix}/lib/*
%{prefix}/etc/CORBA/servers/*
%{prefix}/etc/sound/events/*
%{prefix}/share/locale/*/*/*
%{prefix}/share/sounds/*
%{prefix}/share/pixmaps/*
