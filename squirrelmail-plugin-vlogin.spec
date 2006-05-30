%define		_plugin	vlogin
Summary:	Plugin that makes virtual hosting a possibility, automatically
Summary(pl):	Wtyczka pozwalaj±ca na u¿ywanie wirtualnych hostów
Name:		squirrelmail-plugin-%{_plugin}
Version:	3.5
Release:	3
License:	GPL
Group:		Applications/Mail
Source0:	http://www.squirrelmail.org/plugins/%{_plugin}-%{version}-1.2.7.tar.gz
# Source0-md5:	db20600be5d7a56fbadb220296dfef38
URL:		http://www.squirrelmail.org/
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

%description -l pl
Ta wtyczka pozwala u¿ywaæ jednej instalacji SquirrelMaila do
hostowania poczty na WWW dla wielu domen. Jest wysoko konfigurowalna i
pozwala na rzeczy takie jak:
- umo¿liwienie u¿ytkownikom logowania samym "jose" w przypadku kiedy
  pe³ny login dla IMAP-a to co¶ w rodzaju "jose@domena.com"
- pokazywanie innego obrazka na stronie tytu³owej dla ka¿dej z domen
- zmianê wiêkszo¶ci ustawieñ w konfiguracji SquirrelMaila w zale¿no¶ci
  od domeny (lub nawet u¿ytkownika!)
- dostêp do tabeli wirtualnych u¿ytkowników w stylu sendmaila
- zmianê serwerów IMAP (lub innych ustawieñ) w zale¿no¶ci od domeny
  (lub nawet u¿ytkownika)
- w³±czenie lub wy³±czenie ró¿nych wtyczek w zale¿no¶ci od domeny
- rozwijanie aliasów z domen aliasów Qmaila/Vpopmaila
- t³umaczenie nazw domen
- i inne...

Warto zauwa¿yæ, ¿e je¶li potrzebna jest tylko czê¶æ tych mo¿liwo¶ci,
pozosta³e mo¿na wy³±czyæ.

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
