%include	/usr/lib/rpm/macros.python
Summary:	A conversation server built using Twisted
Summary(pl):	Serwer konwersacyjny tworzony przy u�yciu �rodowiska Twisted
Name:		Quotient
Version:	0.8.8
Release:	1
License:	LGPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/divmod/%{name}-%{version}.tar.gz
# Source0-md5:	650cdb4ae2b59a0f432e49804f2923a9
URL:		http://www.divmod.org/Home/
BuildRequires:	python-devel >= 2.3
%pyrequires_eq	python-modules
Requires:	python >= 2.3
Requires:	python-Imaging
Requires:	python-Lupy >= 0.1.5.5
Requires:	python-Twisted >= 1.1.1
Requires:	python-nevow = %{version}-%{release}
Requires:	spambayes >= 1.0a7-0.2
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
Obecnie g��wn� funkcj� Quotient jest bycie w pe�ni wyposa�on�
platform� email, spe�niaj�c� zadania klient�w oraz serwer�w protoko��w
IMAP4, POP3 i SMTP. Quotient posiada te� zintegrowany interfejs
odbioru poczty poprzez www oraz filtr niechcianej poczty u�ywaj�cy
bayesowskich technik wykrywania niechcianych wiadomo�ci, kt�ry mo�e
by� rozszerzany poprzez interfejs www lub IMAP.

W przysz�o�ci Quotient rozwinie si� do nakierowanego na osob� serwera
aplikacji. Quotient b�dzie �ledzi� i utrzymywa� informacje o
kontaktach oraz umo�liwia� �atwe zarz�dzanie stopniem zaanga�owania.

%package -n python-nevow
Summary:	Web application templating system
Summary(pl):	System szablon�w do tworzenia stron www
Group:		Libraries/Python
Requires:	python-atop = %{version}-%{release}
Requires:	python-Twisted >= 1.1.1

%description -n python-nevow
Nevow is a next-generation web application templating system, based on
the ideas developed in the Twisted Woven package. Its main focus is on
separating the HTML template from both the business logic and the
display logic, while allowing the programmer to write pure Python code
as much as possible. It separates your code into 'data' and 'render'
functions, a simplified implementation of traditional MVC. It has
various parts which can be used individually or as a whole, integrated
web solution:

* XHTML templates: contain no programming logic, only nodes tagged
  with nevow attributes,
* data/render methods: simplified MVC,
* stan: An s-expression-like syntax for expressing xml in pure python,
* formless: For describing the types of objects which may be passed to
  methods of your classes, validating and coercing string input from
  either web or command-line sources, and calling your methods
  automatically once validation passes,
* freeform: For rendering web forms based on formless type
  descriptions, accepting form posts and passing them to formless
  validators, and rendering error forms in the event validation fails,
* livepage: Cross-browser JavaScript glue for sending client side
  events to the server and server side events to the client after the
  page has loaded, without causing the entire page to refresh.

%description -n python-nevow -l pl
Nevow jest systemem szblon�w wspomagaj�cym tworzenie aplikacji
webowych, bazuj�cym na pomys�ach zawartych w rozwijanym w ramach
projektu Twisted pakiecie Woven. G��wnym zadaniem Nevow jest
umo�liwienie deweloperowi odseparowanie kodu szablonu HTML od logiki
biznesowej i logiki prezentacyjnej tworzonego systemu. Nevow rozdziela
Tw�j kod na funkcje zarz�dzania danymi oraz ich wy�wietlania, co jest
uproszczon� wersj� wzroca projektowego MVC. Na Nevow sk�ada si� zbi�r
r�nych funkcjonalno�ci, kt�re mog� by� u�ywane osobno albo jako
ca�o�ciwe rozwi�zanie wspomagaj�ce tworzenie aplikacji webowych:

* szablony XHTML: nie zawieraj� logiki programistycznej, jedynie
  wierzcho�ki tagowane atrybutami przestrzeni nazw nevow,
* funkcje zarz�dzania danymi i wy�wietlaniem: uproszczenie wzorca
  projektowego Model-Widok-Kontroler (MVC),
* stan: sk�adnia wyra�ania element�w j�zyka xml w czystym pythonie w
  oparciu o s-wyra�enia,
* formless: opisywanie typ�w obiekt�w mog�cych by� argumentami
  tworzonych przez Ciebie metod klas, weryfikacji i poprawiania
  znakowych danych wej�ciowych od klient�w www lub innych �r�de� oraz
  automatyczne wywo�ywanie Twoich metod po poprawnej weryfikacji,
* freeform: renderowanie formularzy HTML oparte o opisy typ�w
  formless, akceptacja formularzy dostarczonych przez klienta, analiza
  ich zawarto�ci w oparciu o mechanizm weryfikator�w formless oraz
  tworzenie komunikat�w o b��dach podczas nieudanej weryfikacji
  formularza,
* livepage: mi�dzyplatformowy "klej" JavaScript umo�liwiaj�cy
  przesy�anie efekt�w ubocznych pracy klienta do serwera i odwrotnie
  po za�adowaniu strony bez konieczno�ci jej od�wie�ania.

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
ATOP (Atomic Transactional Object Persistor) jest obiektow� baz�
danych implementuj�c� interfejsy Berkeley DB i bsddb, z
funkcjonalno�ci� podobn� do innych pakiet�w pythona takich jak ZODB i
COG.

Atop zosta� rozwini�ty jako cz�� serwera komunikacyjnego Quotient.
				  
%prep
%setup -q

%build
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

python setup.py install \
        --root=$RPM_BUILD_ROOT \
	--install-lib=%{py_sitedir} \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README doc
%{py_sitedir}/quotient

%files -n python-nevow
%defattr(644,root,root,755)
%{py_sitedir}/nevow

%files -n python-atop
%defattr(644,root,root,755)
%{py_sitedir}/atop
