# Parallel

Welcome to Parallel!

Parallel is now on version 0.1. The very first one!

It was built because we (data scientists from CTS-FGV) were sick of
losing time filtering and comparing graphs to other researches. Parallel
came to save our time and to allow other researches to play with data.

But, why not to use other viz tools? Well, the easy ones are paid and
do not allow us to share in private. The other ones do not have all
plots variety that Plotly have. And, we already use Plotly as the main
tool of data vizualization.

Because of that, we developed Parallel to make as easy as possible to
insert a new plot. The dev just need to say what variables they want to
control, insert the Plotly plot and some key informations about the
data. More about that on **How to add a plot**


This tool was built using Dash from Plotly. It is an incredible tool
that allows python developers to use all Plotly plots power on the web
with dozens of interactions.

## Installing and running

It is all built on Docker. This means that it is super easy to make it
run.

-First, you have to install [Docker in the machine that you want to
run](https://www.docker.com/get-docker)

- Clone this repo and build the the Docker image. It can take a while.
`docker build -t dash-plotly .`

- Initialize the container:
`docker run -it  -v  $(pwd):/app -p 5000:5000 --name dash-server dash-plotly`

- Your viz good to go at `localhost:5000`

It is possible to edit the viz without reinitializing the server. Just
edit, save and refresh!

## How to add a plot

Parallel was thought to be the end of our internal data exploration
process. We get crunch, massage and take care of the data. A lot of
plots are made, but just a few contains relevant and complex
information that need to be look with more care. For those ones,
Parallel was built.

Thus, we assume that you **already have the data and a plot**.

Let's go through the steps.

- All plot codes are stored on the `plots` folder that contains:
    - __init.py__
    - config.yaml
    - get_raw_data.py
    - infos.py
    - plot.py

- You can just copy the template to the plots folder, but you have to
choose a *plot name* that have to be unique.
`copy plot_template plots/<plot-name>`

- Now, you have to edit the `config.yaml`. There you will set the
plot name and the variables that you want controlled. Currently,
you can use two components, dropdown and time range selector. You can
choose as many components you want, the sky is the limited.
Remember that each variable is associated with a data column. So, you
have to make sure that you inserted the right name.
The `config.yaml` is well commented and no problems should arise.

- Go to `get_raw_data.py` and get the raw data :) You can get the data
in the way you want, csv, json, sql, it does not matter. What matters is
that the data has to be a Pandas DataFrame in the end. There are some
examples in the template file.

- Now it is time to plot something! In `plot.py` you will have to put
your Plotly code. The function plot receives the filters data, the
already filtered data and the raw data. You just have to fit your
code there and pass a Plotly figure.

- Finally, if you want, you can set some extra information to go with
the graph. It can be done in `infos.py` and it works as `plot.py` but
you have to pass a list of dicts.

- Run it with
`docker run -it  -v  $(pwd):/app -p 5000:5000 --name dash-server dash-plotly`
If it does not work, check out the terminal.


## Authors
- João Carabetta
- Fernanda Scovino
- Alifer Sales
