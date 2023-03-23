{ pkgs ? import <nixpkgs> {} }:

let
  envDir = "$(pwd)/venv";
in

pkgs.mkShell {
  nativeBuildInputs = [
    pkgs.gnumake
    pkgs.pylint
    pkgs.python39
    pkgs.python39Packages.pip
    pkgs.python39Packages.wheel
    pkgs.python39Packages.build
    pkgs.python39Packages.twine
    pkgs.python39Packages.pytest
    pkgs.python39Packages.pytest-cov
    pkgs.python39Packages.setuptools
  ];
  shellHook = ''
    ${pkgs.python39}/bin/python -m venv ${envDir}

    export PIP_PREFIX=${envDir}
    export PYTHONUSERBASE=${envDir}
    export PYTHONPATH="$PIP_PREFIX/${pkgs.python3.sitePackages}:$PYTHONPATH"
    export PATH="$PIP_PREFIX/bin:$PATH"
    export LD_LIBRARY_PATH=${envDir}/lib

    source ${envDir}/bin/activate
  '';
}
