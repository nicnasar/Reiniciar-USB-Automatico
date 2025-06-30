# Reiniciar-USB-Usiminas
Esse repositório foi criado com o intuito de facilitar a instalação e aplicação de um método para verificar se há internet no computador. Para que, em seguida reinicie a porta USB contendo o receptor de internet.

<br>

# Segue o passo a passo após clonar o repositório

> Mais informações em: https://learn.microsoft.com/en-us/windows-hardware/drivers/download-the-wdk 

## 1 - Instalar os pacotes necessários:

### 1.1 - Baixe o VisualStudio: 

É necessário instalar o VisualStudio para ter os drivers que possibilitarão o uso dos programas restantes.
Ele -- assim como os outros arquivos -- está na pasta `docs`, com o nome `VisualStudioSetup.exe`.

### 1.2 - Instale o SDK do Windows: 

Após ter instalado o `VisualStudio`, é necessário instalar o SDK do Windows. Ele é o arquivo de nome: `winsdksetup.exe`.

### 1.3 - Instale o WDK:

Em seguida, deve-se instalar o WDK, que permite o comando `devcon` de ser utilizado no Windows.
Ele é o arquio de nome `wdksetup.exe`.

## 2 - Encontrar o devcon.exe:

### 2.1 - Após instalar o WDK, navegue até:

`C:\Program Files (x86)\Windows Kits\10\Tools\<versão>\x64\`

Exemplo de arquivo:

`C:\Program Files (x86)\Windows Kits\10\Tools\10.0.26100.0\x64\`

Dentro dessa pasta, você encontrará o `devcon.exe`.

## 3 - Adicionando o devcon ao PATH:

### 3.1 - Copie o caminho da pasta onde está o devcon.exe.

Exemplo:

`C:\Program Files (x86)\Windows Kits\10\Tools\10.0.26100.0\x64\devcon.exe`

### 3.2 - Pressione Win + S e digite:

"variáveis de ambiente" → Clique em "Editar variáveis de ambiente do sistema"

### 3.3 - Na janela:

* Clique em "Variáveis de Ambiente..."
* Na seção "Variáveis do sistema", selecione a variável Path
* Clique em "Editar" → "Novo" → cole o caminho
* Clique em OK em todas as janelas

### 3.4 - Feche e reabra o PowerShell ou CMD para que o novo PATH seja reconhecido.

## 4 - Encontrando o Hardware ID do dispositivo USB:

1. Abra o Gerenciador de Dispositivos
2. Localize o dispositivo (ex: mouse, Arduino, etc.)
3. Clique com o botão direito → Propriedades
4. Vá em "Detalhes"
5. Em "Propriedade", selecione "IDs de Hardware"
6. Copie o valor principal, ex:
`HID\VID_17EF&PID_6019`

## 5 - Confirmando o dispositivo via DevCon:

Agora que o devcon está no PATH, abra o PowerShell como administrador e digite:

`devcon find *VID_17EF*`

Se tudo estiver certo, você verá algo como:

`HID\VID_17EF&PID_6019\7&123456&0&0000 : Lenovo Optical Mouse`

## 6 - Troque o nome da porta USB no script python.

## 7 - Execute o script:

### 7.1 - Abra o PowerShell como administrador.

### 7.2 - Execute o script:
`python C:\Users\SeuUsuario\Desktop\reiniciar_usb.py`

Você verá:

`✅ Dispositivo USB reiniciado com sucesso.`




