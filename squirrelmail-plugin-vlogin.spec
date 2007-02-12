%define		_plugin	vlogin
Summary:	Plugin that makes virtual hosting a possibility, automatically
Summary(pl.UTF-8):   Wtyczka pozwalająca na używanie wirtualnych hostów
Name:		squirrelmail-plugin-%{_plugin}
Version:	3.5
Release:	3
License:	GPL
Group:		Applications/Mail
Source0:	http://www.squirrelmail.org/plugins/%{_plugin}-%{version}-1.2.7.tar.gz
# Source0-md5:	db20600be5d7a56fbadb220296dfef38
URL:		http://www.squirrelmail.org/plugin_view.php?id=47
Requires:	squirrelmail >= 1.4.3a-8
Requires:	squirrelmail-compatibility-2.0.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir %{_datadir}/squirrelmail/plugins/%{_plugin}

%description
This plugin allows you to use just one SquirrelMail installation to
host web mail for multiple domains. It is highly configurable, and
allows such things as:
- allow users to log in with just "jose" when in fact their IMAP login
  might be something like "jose@domain.com"
- show a different image on the login page for each of your domains
- change most any SquirrelMail configuration setting on a per-domain
  basis (or even per-user!)
- access a sendmail-style virtual users table
- change IMAP servers (or any other settings) on a per-domain (or even
  on a per-user) basis
- enable or disable certain plugins on a per-domain basis
- dealiasing of Qmail/Vpopmail aliased domains
- domain name translation
- much more...

Note that if you only need some of these features, the others may be
turned off.

%description -l pl.UTF-8
Ta wtyczka pozwala używać jednej instalacji SquirrelMaila do
hostowania poczty na WWW dla wielu domen. Jest wysoko konfigurowalna i
pozwala na rzeczy takie jak:
- umożliwienie użytkownikom logowania samym "jose" w przypadku kiedy
  pełny login dla IMAP-a to coś w rodzaju "jose@domena.com"
- pokazywanie innego obrazka na stronie tytułowej dla każdej z domen
- zmianę większości ustawień w konfiguracji SquirrelMaila w zależności
  od domeny (lub nawet użytkownika!)
- dostęp do tabeli wirtualnych użytkowników w stylu sendmaila
- zmianę serwerów IMAP (lub innych ustawień) w zależności od domeny
  (lub nawet użytkownika)
- włączenie lub wyłączenie różnych wtyczek w zależności od domeny
- rozwijanie aliasów z domen aliasów Qmaila/Vpopmaila
- tłumaczenie nazw domen
- i inne...

Warto zauważyć, że jeśli potrzebna jest tylko część tych możliwości,
pozostałe można wyłączyć.

%prep
%setup -q -n %{_plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_plugindir}/data,%{_sysconfdir}/squirrelmail}

install *.php $RPM_BUILD_ROOT%{_plugindir}
install data/*.php $RPM_BUILD_ROOT%{_plugindir}/data
install data/config.php.sample $RPM_BUILD_ROOT%{_sysconfdir}/squirrelmail/%{name}-config.php

ln -sf %{_sysconfdir}/squirrelmail/%{name}-config.php $RPM_BUILD_ROOT%{_plugindir}/data/config.php

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -- squirrelmail-plugin-%{_plugin} < 3.5-3
if [ -f /home/services/httpd/html/squirrel/plugins/vlogin/data/config.php.rpmsave ]; then
	echo "Moving old config file to %{_sysconfdir}/squirrelmail/%{name}-config.php"
	mv -f %{_sysconfdir}/squirrelmail/%{name}-config.php %{_sysconfdir}/squirrelmail/%{name}-config.php.rpmnew
	mv -f /home/services/httpd/html/squirrel/plugins/vlogin/data/config.php.rpmsave \
		%{_sysconfdir}/squirrelmail/%{name}-config.php
fi

%files
%defattr(644,root,root,755)
%doc INSTALL README data/*.sample data/*.typical
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/squirrelmail/%{name}-config.php
%dir %{_plugindir}
%{_plugindir}/*.php
%dir %{_plugindir}/data
%{_plugindir}/data/index.php
%{_plugindir}/data/config.php
