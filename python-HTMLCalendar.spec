
%define 	module	HTMLCalendar

Summary:	Python module for generating HTML calendars
Summary(pl.UTF-8):	Moduł Pythona umożliwiający generowanie kalendarzy HTML
Name:		python-%{module}
Version:	1.0.0
Release:	3
License:	LGPL
Group:		Libraries/Python
Source0:	http://freespace.virgin.net/hamish.sanderson/%{module}-%{version}.tar.gz
# Source0-md5:	842d130402c1db8f97a812c243e9007c
URL:		http://freespace.virgin.net/hamish.sanderson/htmlcalendar.html
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
Requires:	python >= 2.3
Requires:	python-HTMLTemplate >= 1.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTMLCalendar generates one- and twelve-month calendars in HTML format
with optional links.

%description -l pl.UTF-8
HTMLCalendar generuje miesięczne i roczne kalendarze w formacie HTML,
wraz z opcjonalnymi, konfigurowalnymi linkami.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-lib=%{py_sitescriptdir} \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt Manual.txt
%{py_sitescriptdir}/HTMLCalendar.py[oc]
