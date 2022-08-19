
# sql
SELECT * FROM "scence" where ac_time between '2021-1-1' and '2021-2-1'

# pack env

conda install -c conda-forge -c main --file requirement\base.txt
conda pack -n env_name -o env_name.tar.gz --ignore-editable-packages