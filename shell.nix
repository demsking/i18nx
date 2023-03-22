{ pkgs ? import <nixpkgs> {} }:

let
  envDir = "$(pwd)/env";
in

pkgs.mkShell {
  nativeBuildInputs = [
    pkgs.pylint
    pkgs.python39
    pkgs.python39Packages.setuptools
    pkgs.python39Packages.wheel
    pkgs.python39Packages.build
    pkgs.python39Packages.twine
    pkgs.python39Packages.pytest
    pkgs.python39Packages.pytest-cov
  ];
  shellHook = ''
    virtualenv `basename ${envDir}` --app-data ${envDir}

    export PIP_PREFIX=${envDir}
    export PYTHONUSERBASE=${envDir}
    export PYTHONPATH="$PIP_PREFIX/${pkgs.python3.sitePackages}:$PYTHONPATH"
    export PATH="$PIP_PREFIX/bin:$PATH"
    export LD_LIBRARY_PATH=${envDir}/lib
  '';
}
