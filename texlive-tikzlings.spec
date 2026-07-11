%global tl_name tikzlings
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.5
Release:	%{tl_revision}.1
Summary:	A collection of cute little animals and similar creatures
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikzlings
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzlings.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzlings.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(epstopdf-pkg)
Requires:	texlive(iftex)
Requires:	texlive(pgf)
Requires:	texlive(pgf-blur)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A collection of LaTeX packages for drawing cute little animals and
similar creatures using TikZ. Currently, the following TikZlings are
included: anteater ape bat bear bee bug cat chicken coati dog elephant
hippo koala marmot meerkat mole mouse owl panda penguin pig rhino sheep
sloth snowman squirrel turkey wolf These little drawings can be
customized in many ways.

