# TODO: what is "other"???
%define		_pver	_x86_linux
Summary:	Uptime-Project client
Summary(pl.UTF-8):	Program klienta Uptime-Project
Name:		yasuc
Version:	0.4.1
Release:	1
License:	other
Group:		Applications
Source0:	http://www.i-glyphix.net/files/%{name}-%{version}%{_pver}.tar.bz2
# Source0-md5:	0e183a0867c741c326883d7d493a29c0
URL:		http://www.uptime-project.net/
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yasuc is a client of Uptime-Project which gets uptime from computer
and sends to main server where this data is beeing analized and
presented via http. It's "Fun-Project" - non profit.

%description -l pl.UTF-8
Yasuc jest klientem internetowego projektu Uptime-Project, który
zbiera, analizuje i prezentuje informacje na temat czasów uptime
komputerów uczestniczących w projekcie. Czysta rozrywka, żadnych
profitów.

%prep
%setup -q -n dist

%install
rm -rf $RPM_BUILD_ROOT

cd %{name}-%{version}

install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}}
install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo "		NOTICE"
echo "	Don't forget to edit /etc/yasuc.conf"
echo "	and add a cronjob (e.g. \"crontab -e\")"

%files
%defattr(644,root,root,755)
%doc %{name}-%{version}/{INSTALL,README}
%attr(755,root,root) %{_bindir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
