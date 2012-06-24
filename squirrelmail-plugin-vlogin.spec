%define		_plugin	vlogin
Summary:	Plugin that makes virtual hosting a possibility, automatically
Summary(pl):	Wtyczka pozwalaj�ca na u�ywanie wirtualnych host�w
Name:		squirrelmail-plugin-%{_plugin}
Version:	3.3
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://www.squirrelmail.org/plugins/%{_plugin}-%{version}.tar.gz
# Source0-md5:	b7461594d6a78626599ec7e8969f07f1
URL:		http://www.squirrelmail.org/
Requires:	squirrelmail
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	/home/httpd/html/squirrel/plugins/%{_plugin}

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
Ta wtyczka pozwala u�ywa� jednej instalacji SquirrelMaila do
hostowania poczty na WWW dla wielu domen. Jest wysoko konfigurowalna i
pozwala na rzeczy takie jak:

 - umo�liwienie u�ytkownikom logowania samym "jose" w przypadku kiedy
   pe�ny login dla IMAP-a to co� w rodzaju "jose@domena.com"
 - pokazywanie innego obrazka na stronie tytu�owej dla ka�dej z domen
 - zmian� wi�kszo�ci ustawie� w konfiguracji SquirrelMaila w
   zale�no�ci od domeny (lub nawet u�ytkownika!)
 - dost�p do tabeli wirtualnych u�ytkownik�w w stylu sendmaila
 - zmien� serwer�w IMAP (lub innych ustawie�) w zale�no�ci od domeny
   (lub nawet u�ytkownika)
 - w��czenie lub wy��czenie r�nych wtyczek w zale�no�ci od domeny
 - rozwijanie alias�w z domen alias�w Qmaila/Vpopmaila
 - t�umaczenie nazw domen
 - i inne...

Warto zauwa�y�, �e je�li potrzebna jest tylko cz�� tych mo�liwo�ci,
pozosta�e mo�na wy��czy�.

%prep
%setup -q -n %{_plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir}/data

install *.php $RPM_BUILD_ROOT%{_plugindir}
install data/*.php $RPM_BUILD_ROOT%{_plugindir}/data
install data/config.php.sample $RPM_BUILD_ROOT%{_plugindir}/data/config.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL README data/*.sample data/*.typical
%config(noreplace) %verify(not size mtime md5) %{_plugindir}/data/config.php
%dir %{_plugindir}
%{_plugindir}/*.php
%dir %{_plugindir}/data
%{_plugindir}/data/index.php
