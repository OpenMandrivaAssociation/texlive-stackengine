Name:		texlive-stackengine
Version:	60019
Release:	1
Summary:	Highly customised stacking of objects, insets, baseline changes, etc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/stackengine
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stackengine.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stackengine.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
