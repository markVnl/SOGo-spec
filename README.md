# Build Sogo RPMs

sogo doesn't have a stable repository for free, you need to go to the nightly repository. Here a way to build your own sogo rpm

First clone the sogo spec

  git clone https://github.com/markVnl/SOGo-spec.git
  
Then inside adjust which version of the rpm you want, for that you can look http://packages.inverse.ca/SOGo/nightly/3/rhel/7/x86_64/RPMS/ in the nightly repo or https://sogo.nu/download.html in the web page. This is an https://github.com/stephdl/SOGo-spec/commit/5fcf04b0f7e73a79e0567d533597d3da2640e021 example 

Now go to build sogo build dependencies 

  dist=ns7 mockcfg=epel-7-x86_64 make-rpms libwbxml.spec

  dist=ns7 mockcfg=epel-7-x86_64 make-rpms sope.spec

Once done we need to create a local repository because sogo needs some build dependencies you built  

  sope49-appserver-devel-4.9-20161202_324.ns7.x86_64
  sope49-core-devel-4.9-20161202_324.ns7.x86_64
  sope49-ldap-devel-4.9-20161202_324.ns7.x86_64
  sope49-mime-devel-4.9-20161202_324.ns7.x86_64
  sope49-xml-devel-4.9-20161202_324.ns7.x86_64
  sope49-gdl1-devel-4.9-20161202_324.ns7.x86_64
  sope49-sbjson-devel-2.3.1-20161202_324.ns7.x86_64
  libwbxml-devel-0.11.2-3.ns7.x86_64

Therefore you must create a local repository where your files are. For example

  sudo vim /etc/mock/nethserver-7-x86_64.cfg

modify accordingly where your files are and paste 

  [sogo]
  name=sogo
  baseurl=file:///home/lsd/dev/git_work/SOGo-spec

Obviously, this modification must be done on all mock architectures. For initiating your local repository (install first createrepo)

  createrepo /home/lsd/dev/git_work/SOGo-spec

Now you can build by

  dist=ns7 mockcfg=epel-7-x86_64 make-rpms sogo.spec

enjoy :)

