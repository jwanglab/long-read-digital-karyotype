Long read digital karyotyping (LRDK)
====================================

Aim: Taking long read (nanopore) whole-genome sequencing data - with our without adaptive sampling - build a "digital karyotype" defining large-scale aneuploidy (whole-chromosome or arm-level gains and losses)

Relevant factors:
  * Aneuploid/malignant fraction
    - In acute leukemia, this is the blast %. Ideally, we can both approximate the aneuploid fraction **and** the karyotype. An easier and still useful goal is to perform digital karyotyping with a minimum required aneuploid fraction (say, 80%)
  * Sequencing depth
    - What is the limit of detection, how low can we go?
  * Is depth alone sufficient, or do we need to use minor allele frequency?


Test data
---------

G-band karyotypes represent the dominant malignant karyotype and are simplified to whole-chromosome gains and losses

Nano\_Leuk\_0244
  * G-band karyotype: 46,XY
  * Blast %: <span style="color:green">high (presumed >80%)</span>
  * ![0244 sequencing depth](https://github.com/jwanglab/long-read-digital-karyotype/blob/main/img/20241108_PBA33418_Nano_Leuk_244_DNA_dorado-0.6.0.duplex_sup_5mCG_5hmCG_T2T.karyo.png?raw=true)

Nano\_Leuk\_0149
  * G-band karyotype: 54,XX,+X,+4,+6,+10,+14,+17,+21,+21
  * Blast %: <span style="color:green">99%</span>
  * ![0149 sequencing depth](https://github.com/jwanglab/long-read-digital-karyotype/blob/main/img/20240327_PAU75219_Nano_Leuk_0149_DNA_dorado-0.5.3.duplex_sup_5mCG_5hmCG.T2T.sorted.karyo.png?raw=true)

Nano\_Leuk\_0129
  * G-band karyotype: 59,XX,+X,+4,+4,+6,+7,+8,+9,+10,+14,+17,+18,+21,+21
  * Blast %: <span style="color:red">61%</span>
  * ![0129 sequencing depth](https://github.com/jwanglab/long-read-digital-karyotype/blob/main/img/20240327_PAU75219_Nano_Leuk_0129_DNA_dorado-0.5.3.duplex_sup_5mCG_5hmCG.T2T.sorted.karyo.png?raw=true)

Nano\_Leuk\_0223
  * G-band karyotype: 39,XX,-3,-4,-7,-9,-15,-16,-17,-18,-22
  * Blast %: <span style="color:green">high (presumed >80%)</span>
  * ![0223 sequencing depth](https://github.com/jwanglab/long-read-digital-karyotype/blob/main/img/20231221_PAS57389_Nano_Leuk_0223_DNA_dorado-0.5.1.duplex_sup_5mCG_5hmCG.T2T.sorted.karyo.png?raw=true)


Raw read depth data are in the ./data/ folder, in 1Mbp bins, matching these sample names.
