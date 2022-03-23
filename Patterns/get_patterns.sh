# !/bin/sh
mkdir results

python get_text_spmf.py codisum
java -jar spmf.jar run MaxSP  codisum_spmf.text results/codisum_maximal 2%
python analyze_results.py results/codisum_maximal test  0
rm codisum_spmf.text results/codisum_maximal


python get_text_spmf.py coregen
java -jar spmf.jar run MaxSP  coregen_spmf.text results/coregen_maximal 2%
python analyze_results.py results/coregen_maximal test 0
rm coregen_spmf.text results/coregen_maximal

python get_text_spmf.py nmt
java -jar spmf.jar run MaxSP  nmt_spmf.text results/nmt_maximal 2%
python analyze_results.py results/nmt_maximal test 0
rm nmt_spmf.text results/nmt_maximal

python get_text_spmf.py ptrgn
java -jar spmf.jar run MaxSP  ptrgn_spmf.text results/ptrgn_maximal 2%
python analyze_results.py results/ptrgn_maximal test 0
rm ptrgn_spmf.text results/ptrgn_maximal