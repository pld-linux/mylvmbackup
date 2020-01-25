Summary:	Utility for creating MySQL backups via LVM snapshots
Summary(pl.UTF-8):	Narzędzie do tworzenia kopii zapasowych MySQL przy użyciu migawek LVM
Name:		mylvmbackup
Version:	0.15
Release:	1
License:	GPL
Group:		Applications/Databases
Source0:	http://www.lenzg.net/mylvmbackup/%{name}-%{version}.tar.gz
# Source0-md5:	57bfdc44bb34919386e68f0bfd95e5e6
URL:		http://www.lenzg.org/mylvmbackup/
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	gzip
Requires:	lvm2
Requires:	perl-DBD-mysql >= 4.019
Requires:	tar
Suggests:	rsync
Suggests:	zbackup
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

%description -l pl.UTF-8
mylvmbackup to narzędzie do szybkiego tworzenia kopii zapasowych baz
MySQL. W celu wykonania kopii, mylvmbackup zakłada blokadę na
wszystkich tabelach i zapisuje cache serwera, a następnie tworzy
migawkę LVM woluminu zawierającego katalog data MySQL, po czym
odblokowuje tabele. Proces tworzenia migawki trwa stosunkowo krótko.
Gdy zostanie to wykonane, serwer może wznowić normalną pracę.

%prep
%setup -q

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
