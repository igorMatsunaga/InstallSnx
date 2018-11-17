# InstallSnx
Script automatizado para instalação SNX, para acesso VPN Check Point em ambiente Linux.
 
 Manual baseado na distribuição Linux “Ubuntu”16.04, porém ele pode ser adaptado para outras versões ou distribuições.
Inicialmente baixe os pré-requisitos para funcionamento do cliente SNX (execute como root):

apt-get install libpam0g:i386 libstdc++5 libx11-6:i386 libstdc++6:i386 libstdc++5:i386

Instale a versão mais atualizada do Java JRE da Oracle (neste manual iremos contemplar a JRE8 – caso já possua o JRE instalado, desconsidere este passo):
Add-apt-repository ppa:webupd8team/java
Apt-get update
Apt-get install oracle-java8-installer
Apt-get install oracle-java8-set-default

Em seguida acesse o site da Checkpoint e baixe o instalador no link https://supportcenter.checkpoint.com/supportcenter/portal/user/anon/page/default.psml/media-type/html?action=portlets.DCFileAction&eventSubmit_doGetdcdetails=&fileid=22824.

Por fim, execute o arquivo baixado:

./snx_install_linux30.sh
Installation Successful.
Uma vez instalado com sucesso o SNX, execute a linha de comando para efetuar a conexão no servidor:

snx –s servidor –u loginderede
