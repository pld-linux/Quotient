%include	/usr/lib/rpm/macros.python
Summary:	A conversation server built using Twisted
Summary(pl):	Serwer konwersacyjny tworzony przy u¿yciu ¶rodowiska Twisted
Name:		Quotient
Version:	0.9.1
Release:	2
License:	LGPL
Group:		Applications/Communications
Source0:	http://www.divmod.org/users/release/divmod/%{name}-%{version}.tar.gz
# Source0-md5:	406fdd2160843bc3be43486b8e30273f
URL:		http://www.divmod.org/Home/
BuildRequires:	python-devel >= 2.3
%pyrequires_eq	python-modules
Requires:	python >= 2.3
Requires:	python-Imaging
Requires:	python-Lupy >= 0.1.5.5
Requires:	python-Twisted >= 1.3.0
Requires:	python-nevow >= 0.2.0
Requires:	python-atop = %{version}-%{release}
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

%description -l pl
Obecnie g³ówn± funkcj± Quotient jest bycie w pe³ni wyposa¿on±
platform± email, spe³niaj±c± zadania klientów oraz serwerów protoko³ów
IMAP4, POP3 i SMTP. Quotient posiada te¿ zintegrowany interfejs
odbioru poczty poprzez www oraz filtr niechcianej poczty u¿ywaj±cy
bayesowskich technik wykrywania niechcianych wiadomo¶ci, który mo¿e
byæ rozszerzany poprzez interfejs www lub IMAP.

W przysz³o¶ci Quotient rozwinie siê do nakierowanego na osobê serwera
aplikacji. Quotient bêdzie ¶ledzi³ i utrzymywa³ informacje o
kontaktach oraz umo¿liwia³ ³atwe zarz±dzanie stopniem zaanga¿owania.

%package -n python-atop
Summary:	A simple transactional object database built on Berkeley DB
Summary(pl):	Prosta transakcyjna obiektowa baza danych oparta o Berkeley DB
Group:		Libraries/Python
Requires:	python-Twisted >= 1.1.1
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

%description -n python-atop -l pl
ATOP (Atomic Transactional Object Persistor) jest obiektow± baz±
danych implementuj±c± interfejsy Berkeley DB i bsddb, z
funkcjonalno¶ci± podobn± do innych pakietów pythona takich jak ZODB i
COG.

Atop zosta³ rozwiniêty jako czê¶æ serwera komunikacyjnego Quotient.

%package doc
Summary:	Documentation for Quotient conversation server
Summary(pl):	Dokumentacja dla serwera komunikacyjnego Quotient
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains documentation files for Quotient conversation
server.

%description doc -l pl
Pakiet zawieraj±cy dokumentacjê dla serwera komunikacyjnego Quotient.

%package utils
Summary:	Tools for Quotient conversation server
Summary(pl):	Programy narzêdziowe dla serwera komunikacyjnego Quotient
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description utils
This package contains tools for Quotient conversation server.

%description utils -l pl
Pakiet zawieraj±cy programy narzêdziowe dla serwera komunikacyjnego
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

cp -ar tools/* $RPM_BUILD_ROOT%{_datadir}/quotient

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
