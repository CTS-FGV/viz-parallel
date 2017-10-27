# Vizualização das Tramitações

A viz é montada no Docker. Para desenvolver na sua máquina local faça:

- Baixe o [Docker na sua máquina local](https://www.docker.com/get-docker)

- Clone esse repositório e monte a imagem com
`docker build -t dash-plotly .

- Inicie o container com
`docker run -it  -v  $(pwd):/app -p 5000:5000 --name dash-server dash-plotly`

- Abra a viz em `localhost:5000`

Agora é possível editar a viz em qualquer editor de texto. Não se esqueça de commitar
suas modificações.