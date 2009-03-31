%include	/usr/lib/rpm/macros.perl
Summary:	Utility for creating MySQL backups via LVM snapshots
Name:		mylvmbackup
Version:	0.11
Release:	1
License:	GPL
Group:		Applications/Databases
Source0:	http://www.lenzg.net/mylvmbackup/%{name}-%{version}.tar.gz
# Source0-md5:	ea3013320ea2f1718f19bc524eeff8a9
URL:		http://www.lenzg.org/mylvmbackup/
BuildRequires:	rpm-perlprov >= 4.1-13
Patch0:		%{name}.patch
Requires:	perl-DBD-mysql
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mylvmbackup is a script for quickly creating backups of MySQL server's
data files. To perform a backup, mylvmbackup obtains a read lock on
all tables and flushes all server caches to disk, makes an LVM
snapshot of the volume containing the MySQL data directory, and
unlocks the tables again. The snapshot process takes only a small
amount of time. When it is done, the server can continue normal
operations, while the actual file backup proceeds.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	mandir=%{_mandir} \
	install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog CREDITS INSTALL README TODO
%config(noreplace,missingok) %attr(600, root, root) %{_sysconfdir}/mylvmbackup.conf
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
# for HOOKS (see manual)
%{_datadir}/%{name}
