# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/coolstr
# catalog-date 2009-09-09 20:34:25 +0200
# catalog-license lgpl
# catalog-version 2.2
Name:		texlive-coolstr
Version:	2.2
Release:	1
Summary:	String manipulation in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/coolstr
License:	LGPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coolstr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coolstr.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coolstr.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
