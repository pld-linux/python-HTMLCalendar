
%include	/usr/lib/rpm/macros.python
%define 	module HTMLCalendar

Summary:	Python module for generating HTML calendars
Summary(pl):	Modu³ Pythona umo¿liwiaj±cy generowanie kalendarzy HTML
Name:		python-%{module}
Version:	0.1.0
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	http://freespace.virgin.net/hamish.sanderson/%{module}-%{version}.tar.gz
# Source0-md5:	21b603a946aa76a95686e009934a545e
URL:		http://freespace.virgin.net/hamish.sanderson/htmlcalendar.html
BuildRequires:	python-devel >= 2.3
Requires:	python >= 2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTMLCalendar generates one- and twelve-month calendars in HTML format
with optional links.


%description -l pl
HTMLCalendar generuje miesiêczne i roczne kalendarze w formacie HTML,
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
%doc README.txt
%{py_sitescriptdir}/HTMLCalendar.py[oc]
