Summary:	A conversation server built using Twisted
Summary(pl.UTF-8):   Serwer konwersacyjny tworzony przy użyciu środowiska Twisted
Name:		Quotient
Version:	0.9.1
Release:	4
License:	LGPL
Group:		Applications/Communications
Source0:	http://www.divmod.org/users/release/divmod/%{name}-%{version}.tar.gz
# Source0-md5:	406fdd2160843bc3be43486b8e30273f
URL:		http://www.divmod.org/Home/
BuildRequires:	python-devel >= 1:2.3
%pyrequires_eq	python-modules
Requires:	python >= 2.3
Requires:	python-Imaging >= 1.1.4
Requires:	python-Lupy >= 0.2.1
Requires:	python-Twisted >= 1.3.0
Requires:	python-atop = %{version}-%{release}
Requires:	python-nevow >= 0.2.0
Requires:	python-pyOpenSSL
Requires:	spambayes >= 1.0a7-0.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quotient's primary function is a full-featured email platform, which
can act as an IMAP4, POP3, SMTP, server and client. It also has a
seamlessly integrated web-mail interface and spam filtering using
Spambayes, which is trainable either through the web UI or through
IMAP.

In future Quotient will be a person-centric application server, and a
simulation of your personal reality. It keeps track of your
communications and enables you to effortlessly prioritize your
commitments.

%description -l pl.UTF-8
Obecnie główną funkcją Quotient jest bycie w pełni wyposażoną
platformą email, spełniającą zadania klientów oraz serwerów protokołów
IMAP4, POP3 i SMTP. Quotient posiada też zintegrowany interfejs
odbioru poczty poprzez WWW oraz filtr niechcianej poczty używający
bayesowskich technik wykrywania niechcianych wiadomości, który może
być rozszerzany poprzez interfejs WWW lub IMAP.

W przyszłości Quotient rozwinie się do nakierowanego na osobę serwera
aplikacji. Quotient będzie śledził i utrzymywał informacje o
kontaktach oraz umożliwiał łatwe zarządzanie stopniem zaangażowania.

%package -n python-atop
Summary:	A simple transactional object database built on Berkeley DB
Summary(pl.UTF-8):   Prosta transakcyjna obiektowa baza danych oparta o Berkeley DB
Group:		Libraries/Python
Requires:	python-Twisted >= 1.3.0
Requires:	python-bsddb

%description -n python-atop
ATOP, the Atomic Transactional Object Persistor, is a Python object
database implemented atop the Berkeley DB and bsddb python module,
with functional similarities to other python packages such as ZODB and
COG.

Atop was designed in support of the Quotient messaging server. The
primary requirement was for a low-latency data store that was still
reliable and transactional, and still amenable to on-the-fly upgrading
and rapid code iterations.

%description -n python-atop -l pl.UTF-8
ATOP (Atomic Transactional Object Persistor) jest obiektową bazą
danych implementującą interfejsy Berkeley DB i bsddb, z
funkcjonalnością podobną do innych pakietów pythona takich jak ZODB i
COG.

Atop został rozwinięty jako część serwera komunikacyjnego Quotient.

%package doc
Summary:	Documentation for Quotient conversation server
Summary(pl.UTF-8):   Dokumentacja dla serwera komunikacyjnego Quotient
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains documentation files for Quotient conversation
server.

%description doc -l pl.UTF-8
Pakiet zawierający dokumentację dla serwera komunikacyjnego Quotient.

%package utils
Summary:	Tools for Quotient conversation server
Summary(pl.UTF-8):   Programy narzędziowe dla serwera komunikacyjnego Quotient
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description utils
This package contains tools for Quotient conversation server.

%description utils -l pl.UTF-8
Pakiet zawierający programy narzędziowe dla serwera komunikacyjnego
Quotient.

%prep
%setup -q

%build
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitescriptdir},%{_datadir}/quotient}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-lib=%{py_sitescriptdir} \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm {} \;

cp -a tools/* admin $RPM_BUILD_ROOT%{_datadir}/quotient

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/quotient

%files -n python-atop
%defattr(644,root,root,755)
%{py_sitescriptdir}/atop

%files doc
%defattr(644,root,root,755)
%doc doc/*

%files utils
%defattr(644,root,root,755)
%{_datadir}/quotient
