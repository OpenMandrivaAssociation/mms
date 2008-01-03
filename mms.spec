
%define name	mms
%define version	1.1.0
%define prever	rc1
%define rel	2
%if %prever
%define release	%mkrel 0.%prever.%rel
%else
%define release	%mkrel %rel
%endif

Summary:	My Media System - PVR software
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		Video
URL:		http://mms.sunsite.dk/
%if %prever
Source:		http://mms.sunsite.dk/%name-%version-%prever.tar.bz2
%else
Source:		http://mms.sunsite.dk/%name-%version.tar.bz2
%endif
BuildRoot:	%_tmppath/%name-root
BuildRequires:	imlib2-devel
BuildRequires:	taglib-devel
BuildRequires:	sqlite-devel
BuildRequires:	libxine-devel
BuildRequires:	em8300-devel
BuildRequires:	lirc-devel
BuildRequires:	libcommoncpp2-devel
BuildRequires:	SDL-devel
BuildRequires:	mesagl-devel
BuildRequires:	mesaglu-devel
BuildRequires:	libsvgalib-devel
BuildRequires:	pcre-devel
BuildRequires:	libtool
BuildRequires:	libxscrnsaver-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	ncurses-devel
BuildRequires:	python-devel
BuildRequires:	libgstreamer0.10-devel
BuildRequires:	libalsaplayer-devel
BuildRequires:	inotify-tools-devel
BuildRequires:	boost-devel
BuildRequires:	sqlite3-devel
Suggests:	wget eject mplayer

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
%if %prever
%setup -q -n %{name}-%{version}-%{prever}
%else
%setup -q
%endif

%build

# custom configure script
./configure \
	--prefix=%{_prefix} \
	--enable-game \
	--enable-tv \
	--enable-picture-epg \
	--enable-lirc \
	--enable-evdev \
	--enable-dvb \
	--enable-opengl \
	--enable-dxr3 \
	--enable-mpeg \
	--enable-xine-audio \
	--enable-gst-audio \
	--enable-python

# (anssi 01/2008): vgagl disabled, due to
# dlopen failed with error: /usr/share/mms/plugins/lib_output_vgagl.so: undefined symbol: vga_getmodeinfo


%make EXTRA_FLAGS="%optflags"

%install
rm -rf %buildroot

%makeinstall_std

install -m755 tools/* %buildroot/%_bindir
# Shipped in mplayer
rm %buildroot/%_bindir/midentify

%find_lang %name --all-name

%clean
rm -rf %buildroot

%files -f %name.lang
%defattr(-,root,root)
%doc cfg doc/CHANGELOG doc/README
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/input
%dir %_sysconfdir/%name/input/keyboard
%dir %_sysconfdir/%name/input/lirc
%config(noreplace) %_sysconfdir/%name/*Config
%config(noreplace) %_sysconfdir/%name/input/*/*
%config(noreplace) %_sysconfdir/%name/genericplayer.ops
%config %_sysconfdir/%name/lircrc.example
%_bindir/%name
%_bindir/mms-audio-library
%_bindir/mms-movie-library
%_bindir/mms-pic-library
%_bindir/fetch_channels.py
%_bindir/fork-launcher.sh
%_bindir/gen_tvlisting.sh
%_bindir/nxtvepg-to-tv-xml.sh
%_mandir/man1/%name.1*
%_mandir/man1/mms-pic-library.1*
%_mandir/de
%_datadir/%name
#dir %_localstatedir/%name
#dir %_localstatedir/%name/playlists
#dir %_var/cache/%name
#config(noreplace) %_localstatedir/%name/options

