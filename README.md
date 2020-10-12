# Description

The awesome project to work on something

# Run It

```
cd <prj_path>
make venv_install_requirements
source .venv3/bin/activate

git init
pre-commit install

git add .
git commit -am 'initial commit'
git branch -M main
git remote add origin git@github.com:tehtbl/grodt_prj.git
git push -u origin main
```

```
make start_devel
make logs

make clean_all

make restart_devel
make stop_devel
```
