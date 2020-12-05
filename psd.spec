Name:           profile-sync-daemon 
Version:        6.42
Release:        1%{?dist}
Summary:        Offload browser profiles to RAM for speed and wear reduction
License:        MIT
URL:            https://github.com/graysky2/profile-sync-daemon 
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  systemd rsync
Requires:       rsync
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
Symlinks and syncs browser profiles to RAM via tmpfs which will reduce HDD/SDD
calls and speed-up browsers.

%prep
%setup -q

%build
%make_build

%install
make install DESTDIR=%{buildroot}

%post
if [ $1 -eq 1 ]; then
 setsebool -P rsync_full_access 1 >/dev/null 2>&1 || :
fi
%systemd_post psd.service

%preun
if [ $1 -eq 0 ]; then
 setsebool -P rsync_full_access 0 >/dev/null 2>&1 || :
fi
%systemd_preun psd.service

%postun
%systemd_postun_with_restart psd.service

%files
%doc README*
%license MIT
%{_bindir}/*
%dir %{_datadir}/zsh/site-functions/
%{_datadir}/zsh/site-functions/_psd
%{_mandir}/man1/*.1*
%{_userunitdir}/psd*.*
%{_datadir}/psd/*

%changelog
* Sat Dec 05 2020 Johannes Ballmann <copr@jball.de>
- Update to 6.42

* Sat May 09 2020 Johannes Ballmann <copr@jball.de>
- Update to 6.40

* Sat May 02 2020 Johannes Ballmann <copr@jball.de>
- Update to 6.38

* Tue Sep 17 2019 Szasza
- Update to 6.35

* Thu Sep 20 2018 Szasza
- Update to 6.33

* Sun Jan 29 2017 Eduardo Garcia Cebollero <me@egarcia.info>
- Update to 6.31

* Fri Nov 18 2016 Eduardo Garcia Cebollero <me@egarcia.info>
- Update to 6.28

* Tue Sep 8 2015 Eduardo Garcia Cebollero <me@egarcia.info>
- Update to 6.03
- New Version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.68-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 17 2015 Christopher Meng <rpm@cicku.me> - 5.68-1
- Update to 5.68

* Wed Sep 17 2014 Christopher Meng <rpm@cicku.me> - 5.51-1
- Update to 5.51

* Wed Sep 10 2014 Christopher Meng <rpm@cicku.me> - 5.50-1
- Update to 5.50

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.45.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 20 2014 Christopher Meng <rpm@cicku.me> - 5.45.1-1
- Update to 5.45.1

* Sat Nov 09 2013 Christopher Meng <rpm@cicku.me> - 5.44-1
- Update to 5.44

* Sun Nov 03 2013 Christopher Meng <rpm@cicku.me> - 5.43-1
- Update to 5.43

* Mon Sep 16 2013 Christopher Meng <rpm@cicku.me> - 5.40.1-1
- Update to 5.40.1

* Mon Sep 02 2013 Christopher Meng <rpm@cicku.me> - 5.39-1
- Update to 5.39

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.38.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 25 2013 Christopher Meng <rpm@cicku.me> - 5.38.2-1
- Update to 5.38.2

* Sun Jun 16 2013 Christopher Meng <rpm@cicku.me> - 5.36.2-1
- Update to 5.36.2

* Wed May 29 2013 Christopher Meng <rpm@cicku.me> - 5.35-1
- Initial Package.
