%define		_plugin	vlogin
Summary:	Makes virtual hosting a possibility, automatically
Summary(pl):	Pozwala na u¿ywanie wirtualnych hostów
Name:		squirrelmail-plugin-%{_plugin}
Version:	3.2
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://www.squirrelmail.org/plugins/%{_plugin}-%{version}.tar.gz
# Source0-md5:	69c212a64a1f643b4e468e1f4a2de114
URL:		http://www.squirrelmail.org/
Requires:	squirrelmail
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	/home/httpd/html/squirrel/plugin/%{_plugin}

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
%dir %{_plugindir}
%{_plugindir}/*.php
%{_plugindir}/data/index.php
%config(noreplace) %{_plugindir}/data/config.php
