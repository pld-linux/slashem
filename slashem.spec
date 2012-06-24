%define		_ver	%(echo %{version} | tr -d . | tr EF ef)
Summary:	Variant of the roguelike game, NetHack
Summary(pl):	Wariant Nethacka
Name:		slashem
Version:	0.0.6E4F8
Release:	2
License:	Nethack GPL
Group:		Applications/Games
Source0:	http://avrc.city.ac.uk/nethack/slashem/se%{_ver}.tar.gz
# Source0-md5:	2abd847d4f5fc426d6c7ed5a97b0de99
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	%{name}rc.gz
# Source3-md5:	8161a6a7b9633be446dd07e19eeb243b
Patch0:		%{name}-config.patch
Patch1:		%{name}-makefile.patch
Patch2:		%{name}-qt3.patch
URL:		http://avrc.city.ac.uk/nethack/slashem.html
Requires:	/bin/gzip
BuildRequires:	XFree86-devel
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gtk+-devel
BuildRequires:	ncurses-devel
BuildRequires:	qt-devel
Requires:	applnk >= 1.5.13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_nhdir	/usr/lib/slashem
%define		_dyndir	/var/games/slashem

%description
Slash'EM (SuperLotsaAddedStuffHack - Extended Magic) is an extension
of SLASH which is an extension of NetHack, a hugely popular roguelike
game. It adds more monsters, more objects, more dungeon levels, more
roles and more races. It adds shopkeeper services, role- and race-
specific techniques and invisible objects.

Warning! Don't even try to play Slash'EM if you never seen Nethack.

%description -l pl
Slash'EM (SuperLotsaAddedStuffHack - Extended Magic) jest
rozszerzeniem SLASHa, kt�ry jest rozszerzeniem Nethacka, ogromnie
popularnej gry roguelike. Dodaje wi�cej potwor�w, wi�cej przedmiot�w,
wi�cej poziom�w lochu, wi�cej profesji i wi�cej ras. Dodaje us�ugi
sklepikarzy, techniki specyficzne dla profesji i klasy, oraz
niewidzialne przedmioty.

Uwaga! Nawet nie pr�buj gra� w t� torturowni�, je�eli nie widzia�e�
wcze�niej Nethacka.

%package bigtiles
Summary:	Big tiles
Summary(pl):	Du�e kafelki
Group:		Applications/Games
Requires:	%{name} = %{version}

%description bigtiles
32x32 tiles for Slash'EM.

%description bigtiles -l pl
Kafelki 32x32 dla Slash'EM.

%package 3dtiles
Summary:	3D tiles
Summary(pl):	Kafelki tr�jwymiarowe
Group:		Applications/Games
Requires:	%{name} = %{version}

%description 3dtiles
3D tiles for Slash'EM. They are ugly and have nothing to do with
roguelike spirit.

%description 3dtiles -l pl
Kafelki tr�jwymiarowe dla Slash'EM. S� obciachowe i nie maj� nic
wsp�lnego z duchem gier roguelike.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
install %{SOURCE3} .

%build
./sys/unix/setup.sh links

%{__make} all \
	CFLAGS="%{rpmcflags} -I../include -I%{_includedir}/ncurses" \
	LFLAGS="%{rpmldflags}" \
	CC="%{__cc}" \
	CXX="%{__cxx}"

%{__make} -C util recover \
	CFLAGS="%{rpmcflags} -I../include" \
	LFLAGS="%{rpmldflags}" \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Games/RPG,%{_mandir}/man6}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install doc/slashem.6	$RPM_BUILD_ROOT%{_mandir}/man6
install util/recover	$RPM_BUILD_ROOT%{_nhdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/RPG
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{Guidebook,strategy.txt} README.gtk history.txt license
%doc readme.s6 readme.txt slamfaq.txt
%attr(2755,root,games) %{_prefix}/games/slashem
%attr(2755,root,games) %{_nhdir}/slashem
%attr(2755,root,games) %{_nhdir}/recover
%dir %{_nhdir}
%dir %{_datadir}/slashem
%{_nhdir}/nhushare
%{_datadir}/slashem/*.xpm
%{_datadir}/slashem/gtkrc
%{_datadir}/slashem/nhshare
%{_datadir}/slashem/x11tiles
%attr(2775,root,games) %dir %{_dyndir}
%attr(2775,root,games) %dir %{_dyndir}/save
%attr(664,root,games) %{_dyndir}/perm
%attr(664,root,games) %config(noreplace) %verify(not,md5,size,mtime) %{_dyndir}/record
%attr(664,root,games) %config(noreplace) %verify(not,md5,size,mtime) %{_dyndir}/logfile
%{_mandir}/man6/*
%{_applnkdir}/Games/RPG/*
%{_pixmapsdir}/*

%files bigtiles
%defattr(644,root,root,755)
%{_datadir}/slashem/x11bigtiles

%files 3dtiles
%defattr(644,root,root,755)
%{_datadir}/slashem/x11big3dtiles
