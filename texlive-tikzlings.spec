Name:		texlive-tikzlings
Version:	63628
Release:	1
Summary:	A collection of cute little animals and similar creatures
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tikzlings
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzlings.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzlings.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A collection of LaTeX packages for drawing cute little animals
and similar creatures using TikZ. Currently, the following
TikZlings are included: anteater bat bear bee bug cat chicken
coati elephant hippo koala marmot mole mouse owl panda penguin
pig rhino sheep sloth snowman squirrel wolf These little
drawings can be customized in many ways.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tikzlings
%doc %{_texmfdistdir}/doc/latex/tikzlings

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
