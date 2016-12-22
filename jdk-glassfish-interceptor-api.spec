Name     : jdk-glassfish-interceptor-api
Version  : 1.2
Release  : 1
URL      : http://repo.maven.apache.org/maven2/javax/interceptor/javax.interceptor-api/1.2/javax.interceptor-api-1.2.jar
Source0  : http://repo.maven.apache.org/maven2/javax/interceptor/javax.interceptor-api/1.2/javax.interceptor-api-1.2.jar
Source1  : http://repo.maven.apache.org/maven2/javax/interceptor/javax.interceptor-api/1.2/javax.interceptor-api-1.2.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/glassfish-interceptor-api.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/glassfish-interceptor-api.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/glassfish-interceptor-api.xml \
%{buildroot}/usr/share/maven-poms/glassfish-interceptor-api.pom \
%{buildroot}/usr/share/java/glassfish-interceptor-api.jar \

%files
%defattr(-,root,root,-)
/usr/share/maven-metadata/glassfish-interceptor-api.xml
/usr/share/maven-poms/glassfish-interceptor-api.pom
/usr/share/java/glassfish-interceptor-api.jar
