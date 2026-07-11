%global tl_name stackengine
%global tl_revision 75878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.11
Release:	%{tl_revision}.1
Summary:	Highly customised stacking of objects, insets, baseline changes, etc.
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/stackengine
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stackengine.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stackengine.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(listofitems)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a versatile way to stack objects vertically in a
variety of customizable ways. A number of useful macros are provided,
all of which make use of the stackengine core.

