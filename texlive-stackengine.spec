# revision 32593
# category Package
# catalog-ctan /macros/latex/contrib/stackengine
# catalog-date 2014-01-06 14:33:54 +0100
# catalog-license lppl1.3
# catalog-version 3.24
Name:		texlive-stackengine
Version:	3.24
Release:	1
Summary:	Highly customised stacking of objects, insets, baseline changes, etc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/stackengine
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stackengine.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stackengine.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a versatile way to stack objects
vertically in a variety of customizable ways. A number of
useful macros are provided, all of which make use of the
stackengine core.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/stackengine/stackengine.sty
%doc %{_texmfdistdir}/doc/latex/stackengine/README
%doc %{_texmfdistdir}/doc/latex/stackengine/stackengine.pdf
%doc %{_texmfdistdir}/doc/latex/stackengine/stackengine.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
