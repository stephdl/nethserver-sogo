Summary: NethServer SOGo configuration
Name: nethserver-sogo
Version: 1.4.1
Release: 1%{dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

# nethserver-base requires postfix MTA:
Requires: nethserver-mail-server >= 1.1.0-2
Requires: nethserver-mysql >= 1.0.0
Requires: nethserver-memcached >= 1.0.0
Requires: nethserver-httpd >= 1.0.1-2
Requires: sogo >= 2.2.8
Requires: sogo-tool
Requires: sope49-gdl1-mysql

BuildRequires: perl
BuildRequires: nethserver-devtools 

%description
NethServer SOGo configuration

%prep
%setup

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
%{genfilelist} $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING" >> %{name}-%{version}-filelist

%post

%preun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

%changelog
* Thu Jun 12 2014 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.4.0-1.ns6
- Preserve request host name in SOGo - Enhancement #2759
- AD group mail delivery type switch - Feature #2751
- SOGo: shared folders not working for AD accounts - Bug #2730
- Use DNS A record to locate AD controllers - Enhancement #2729
- Configurable AD accounts LDAP subtree - Enhancement #2727
- SOGo: add dashboard widget - Enhancement #2710

* Wed Feb 05 2014 Davide Principi <davide.principi@nethesis.it> - 1.3.0-1.ns6
- Upgrade SOGo to release 2.1.1b - Enhancement #2457 [NethServer]
- Directory: backup service accounts passwords  - Enhancement #2063 [NethServer]

* Mon Dec 16 2013 Davide Principi <davide.principi@nethesis.it> - 1.2.2-1.ns6
- Redirect to internal DNS name - Bug #2371 [NethServer]
- Support iOS7 carddav client - Enhancement #2221 [NethServer]
- Remove apache "already loaded" warnings - Enhancement #2074 [NethServer]

* Tue Jun 11 2013 Davide Principi <davide.principi@nethesis.it> - 1.2.1-1.ns6
- Active Directory integration (experimental) #2000

* Mon Jun 10 2013 Davide Principi <davide.principi@nethesis.it> - 1.1.1-1.ns6
- Sogo mysql password unescaped: connection fails #2002

* Tue Apr 30 2013 Davide Principi <davide.principi@nethesis.it> - 1.1.0-1.ns6
- Full automatic package install/upgrade/uninstall support #1870 #1872 #1874
- Protect dovecot master user password #1825
- Expand /etc/cron.d/sogo template #1637
- Backup SOGo user folders #1800
- Added group LDAP source #1842
- Use submission port 587 to send messages #1817
- Fixed #1843 #1823

* Tue Mar 19 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.2-1.ns6
- createlinks: fixed wrong function name event_{actions => services}()  call. Refs #1637
- Moved httpd.conf template fragment to new location. Refs #1637
- Add migration code #1717
- Update URL spec tag #1654
- Set minimum version requirements  #1653

* Fri Feb  1 2013 Davide Principi <davide.principi@nethesis.it> - 1.0.1-1.ns6
- Fix #1643

* Thu Jan 31 2013 Davide Principi <davide.principi@nethesis.it> - 1.0.0-1.ns6
- Initial release


