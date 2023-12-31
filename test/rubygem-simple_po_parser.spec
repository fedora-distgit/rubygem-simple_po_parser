# Generated from simple_po_parser-1.1.6.gem by gem2rpm -*- rpm-spec -*-
%global gem_name simple_po_parser

Name: rubygem-%{gem_name}
Version: 1.1.6
Release: 1%{?dist}
Summary: A simple PO file to ruby hash parser
License: MIT
URL: http://github.com/experteer/simple_po_parser
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildArch: noarch

%description
A simple PO file to ruby hash parser . PO files are translation files
generated by GNU/Gettext tool.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/



%check
pushd .%{gem_instdir}
# Run the test suite.
popd

%files
%dir %{gem_instdir}
%{gem_instdir}/.gitattributes
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/.rspec
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/simple_po_parser.gemspec
%{gem_instdir}/spec
%{gem_instdir}/test

%changelog
* Fri Jun 23 2023 Pavel Valena <pvalena@redhat.com> - 1.1.6-1
- Initial package
