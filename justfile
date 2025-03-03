#!/usr/bin/env just --justfile

default: show_receipts

set shell := ["bash", "-uc"]
set dotenv-load := true

show_receipts:
    just --list

show_system_info:
    @echo "=================================="
    @echo "os : {{ os() }}"
    @echo "arch: {{ arch() }}"
    @echo "justfile dir: {{ justfile_directory() }}"
    @echo "invocation dir: {{ invocation_directory() }}"
    @echo "running dir: `pwd -P`"
    @echo "=================================="

setup:
    asdf install

create_venv:
    @echo "creating venv"
    python3 -m pip install --upgrade pip setuptools wheel
    python3 -m venv venv

install_deps:
    @echo "installing dependencies"
    python3 -m hatch dep show requirements --project-only > /tmp/requirements.txt
    pip3 install -r /tmp/requirements.txt

install_deps_dev:
    @echo "installing dev dependencies"
    python3 -m hatch dep show requirements --project-only > /tmp/requirements.txt
    python3 -m hatch dep show requirements --env-only >> /tmp/requirements.txt
    pip3 install -r /tmp/requirements.txt

create_reqs:
    @echo "creating requirements"
    pipreqs --force --savepath requirements.txt src/octodns_netbox_dns

lint:
    just show_system_info
    hatch run lint:style
    hatch run lint:typing

format *args:
    just show_system_info
    hatch run lint:fmt {{ args }}

check:
    just lint
    just format

build:
    hatch build --clean

test:
    hatch run default:test

up:
    docker compose -f dev/compose.yml build
    docker compose -f dev/compose.yml up

down:
    docker compose -f dev/compose.yml down

clean:
    rm -rf dev/db-data/*
    rm -rf dev/redis-data/*
    rm -rf dev/netbox-data/*

sync *args:
    hatch -v run default:sync {{ args }}

sync2 *args:
    hatch -v run default:sync {{ args }}

dump *args:
    hatch -v run default:dump {{ args }}

dump2 *args:
    hatch -v run default:dump2 {{ args }}

validate *args:
    hatch -v run default:validate {{ args }}

validate2 *args:
    hatch -v run default:validate {{ args }}
