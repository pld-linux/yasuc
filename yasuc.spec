%define         _pver   _x86_linux
Summary:	Uptime-Project client
Summary(pl):	Program klienta Uptime-Project
Name:		yasuc
Version:	0.4.1
Release:	0.1
Group:          Applications
License:	other
Source0:	http://www.i-glyphix.net/files/%{name}-%{version}%{_pver}.tar.bz2
# Source0-md5:	0e183a0867c741c326883d7d493a29c0
URL:		http://www.uptime-project.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yasuc is a client of Uptime-Project which gets uptime from
computer and sends to main server where this data is beeing
analized and presented via http.
It's "Fun-Project" - non profit.

%description -l pl
Yasuc jest klientem internetowego projektu Uptime-Project,
który zbiera, analizuje i prezentuje informacje na temat
czasów uptime komputerów uczestnicz±cych w projekcie.
Czysta rozrywka, ¿adnych profitów.

%prep
%setup -q -n dist/%{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},/etc}
install yasuc $RPM_BUILD_ROOT%{_bindir}
install yasuc.conf $RPM_BUILD_ROOT/etc

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo "		NOTICE"
echo "	Don't forget to edit /etc/yasuc.conf"
echo "	and add a cronjob (e.g. \"crontab -e\")"

%files
%defattr(644,root,root,755)
%doc INSTALL README
%{_bindir}/yasuc
/etc/yasuc.conf
