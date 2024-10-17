Name:		texlive-coolstr
Version:	67015
Release:	1
Summary:	String manipulation in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/coolstr
License:	LGPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coolstr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coolstr.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coolstr.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Coolstr is a subpackage of the cool bundle that deals with the
manipulation of strings. A string is defined as a sequence of
characters (not tokens). The package provides the ability to
access a specific character of a string, as well as determine
if the string contains numeric or integer data.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/coolstr/coolstr.sty
%doc %{_texmfdistdir}/doc/latex/coolstr/README
%doc %{_texmfdistdir}/doc/latex/coolstr/coolstr.pdf
#- source
%doc %{_texmfdistdir}/source/latex/coolstr/coolstr.dtx
%doc %{_texmfdistdir}/source/latex/coolstr/coolstr.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
