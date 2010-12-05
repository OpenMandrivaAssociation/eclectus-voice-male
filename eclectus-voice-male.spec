Summary:	Han character dictionary
Name:		eclectus-voice-male
Version:	0.2
Release:	%mkrel 2
Group:		Development/Python
License:	GPLv3+
URL:		http://code.google.com/p/eclectus/
Source0:	http://eclectus.googlecode.com/files/chi-balm-hsk1-%{version}beta.tar.gz
BuildArch:	noarch
Requires:	eclectus
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot

%description
Eclectus is a small Han character dictionary especially designed for
learners of Chinese character based languages like Mandarin Chinese
or Japanese.

%prep
%setup -qn chi-balm-hsk1-%{version}beta

%install
rm -rf %{buildroot}
make install installpath=%{buildroot}%{_datadir}/eclectus/chi-balm-hsk1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/eclectus/chi-balm-hsk1
