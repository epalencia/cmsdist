### RPM external py2-sqlalchemy 0.3.1
%define pythonv %(echo $PYTHON_VERSION | cut -f1,2 -d.)
## INITENV +PATH PYTHONPATH %i/lib/python$(echo $PYTHON_VERSION | cut -f1,2 -d.)/site-packages

Source: http://superb-east.dl.sourceforge.net/sourceforge/sqlalchemy/SQLAlchemy-%v.tar.gz
Requires: python

%prep
%setup -n SQLAlchemy-%v
%build
%install
mkdir -p %i/lib/python%{pythonv}/site-packages
python setup.py build
mv build/lib/* %i/lib/python%{pythonv}/site-packages

