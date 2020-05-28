FROM ubuntu:20.04

RUN apt-get update && env DEBIAN_FRONTEND=noninteractive apt-get install -y \
        postgis gdal-bin biber latexmk texlive-bibtex-extra python3-geopandas \
        python3-pygments

RUN apt-get install -y make git
