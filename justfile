#!/usr/bin/env just --justfile

default: show-receipts

set shell := ["bash", "-uc"]
set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]
set dotenv-load := true

show-receipts:
    just show-system-info
    just --list

show-system-info:
    @echo "=================================="
    @echo "os : {{ os() }}"
    @echo "arch: {{ arch() }}"
    @echo "justfile dir: {{ justfile_directory() }}"
    @echo "invocation dir: {{ invocation_directory() }}"
    @echo "running dir: `pwd -P`"
    @echo "=================================="

setup:
    asdf install

create-venv:
    @echo "creating venvs"
    hatch env create
    hatch env show

create-reqs:
    @echo "creating requirements files"
    hatch dep show requirements --project-only > requirements.txt
    hatch dep show requirements --env-only > requirements-dev.txt

create-pipreqs:
    @echo "creating requirements (pipreqs)"
    pipreqs --force --savepath requirements.txt src/

install-deps:
    @echo "installing dependencies locally"
    hatch dep show requirements --project-only > requirements.tmp
    pip install -r requirements.tmp

install-deps-dev:
    @echo "installing dev dependencies locally"
    hatch dep show requirements --env-only > requirements-dev.tmp
    pip install -r requirements-dev.tmp

lint *args:
    @echo "linting project"
    shfmt -d -i 4 -bn -ci -sr .
    hatch run lint:all {{ args }}

format *args:
    @echo "formatting project"
    shfmt -w -i 4 -bn -ci -sr .
    hatch run lint:fmt {{ args }}

check:
    just format
    just lint

test *args:
    @echo "running tests"
    hatch run test:test {{ args }}

build *args:
    @echo "building project"
    hatch build --clean {{ args }}

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
    hatch -v run test:sync {{ args }}

sync2 *args:
    hatch -v run test:sync2 {{ args }}

dump *args:
    hatch -v run test:dump {{ args }}

dump2 *args:
    hatch -v run test:dump2 {{ args }}

validate *args:
    hatch -v run test:validate {{ args }}

validate2 *args:
    hatch -v run test:validate2 {{ args }}
