
%define name	mms
%define version	1.0.8.3
%define rel	2

Summary:	My Media System - PVR software
Name:		%name
Version:	%version
Release:	%mkrel %rel
License:	GPL
Group:		Video
Source:		http://mms.sunsite.dk/%name-%version.tar.bz2
BuildRoot:	%_tmppath/%name-root
BuildRequires:	imlib2-devel
BuildRequires:	taglib-devel
BuildRequires:	sqlite-devel
BuildRequires:	libxine-devel
BuildRequires:	em8300-devel
BuildRequires:	lirc-devel
BuildRequires:	libcommoncpp2-devel
BuildRequires:	SDL-devel
BuildRequires:	libsvgalib-devel
BuildRequires:	pcre-devel
BuildRequires:	libtool
BuildRequires:	libxscrnsaver-devel
# MMS can control lots of external programs, so we only list the
# non-obvious ones here:
Requires:	wget eject

%description
My Media System is an application that manages, displays and plays
media content such as videos, music, pictures, and more. MMS runs
perfectly on anything from a Set-Top-Box connected to your TV-Set,
to your specially tailored multimedia PC and HD display.

As the name implies, MMS is a media system with you in control. It
lets other applications such as MPlayer, VDR, or Xine take care of
what they respectively do best, and integrates them into one system,
that is easy to understand and operate. By combining their
individual strength, you get the best of all worlds, in one media
application.

%prep
%setup -q

%build

# custom configure script
./configure \
	--prefix=%{_prefix} \
	--enable-game \
	--enable-tv \
	--enable-bttv-radio \
	--enable-picture-epg \
	--enable-eject-tray \
	--enable-lirc \
	--enable-evdev \
	--enable-dvb \
	--enable-vga \
	--enable-vgagl \
	--enable-fbdev \
	--enable-dxr3 \
	--enable-mpeg \
	--enable-xine-audio

%make EXTRA_FLAGS="%optflags"

%install
rm -rf %buildroot

%makeinstall_std

install -m755 tools/* %buildroot/%_bindir

%find_lang %name

%clean
rm -rf %buildroot

%files -f %name.lang
%defattr(-,root,root)
%doc cfg doc/CHANGELOG doc/README
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/config
%config(noreplace) %_sysconfdir/%name/input-keyboard
%config(noreplace) %_sysconfdir/%name/input-lirc
%config(noreplace) %_sysconfdir/%name/lirc.conf
%_bindir/%name
%_bindir/fetch_channels.py
%_bindir/fork-launcher.sh
%_bindir/gen_tvlisting.sh
%_bindir/nxtvepg-to-tv-xml.sh
%_mandir/man1/%name.1*
%_mandir/de
%_datadir/%name
%dir %_localstatedir/%name
%dir %_localstatedir/%name/playlists
%dir %_var/cache/%name
%config(noreplace) %_localstatedir/%name/options

