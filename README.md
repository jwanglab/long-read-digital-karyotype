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

Nano\_Leuk\_0244
  * G-band karyotype: 46,XY
  * Blast %: <span style="color:green">high (presumed >80%)</span>
  ![0244 sequencing depth](20241108_PBA33418_Nano_Leuk_244_DNA_dorado-0.6.0.duplex_sup_5mCG_5hmCG_T2T.karyo.png)

Nano\_Leuk\_0149
  * G-band karyotype: 54,XX,+X,<span style="color:lightgray">t(2;14)(p11.2;q11.2),</span>+4,+6,<span style="color:lightgray">inv(9)(p11q13)c,</span>+10,+14,+17,+21,+21<span style="color:lightgray">[14]/46,XX,inv(9)(p11q13)c[9]</span>
  * Blast %: <span style="color:green">99%</span>
  ![0149 sequencing depth](20240327_PAU75219_Nano_Leuk_0149_DNA_dorado-0.5.3.duplex_sup_5mCG_5hmCG.T2T.sorted.karyo.png)

Nano\_Leuk\_0129
  * G-band karyotype: 59,XX,+X,+4,+4,+6,+7,<span style="color:lightgray">i(7)(q10),</span>+8,+9,+10,+14,+17,+18,<span style="color:lightgray">der(19)t(1;19)(q?21;p13.3),</span>+21,+21<span style="color:lightgray">[7]/46,XX[15]</span>
  * Blast %: <span style="color:red">61%</span>
  ![0129 sequencing depth](20240327_PAU75219_Nano_Leuk_0129_DNA_dorado-0.5.3.duplex_sup_5mCG_5hmCG.T2T.sorted.karyo.png)

Nano\_Leuk\_0223
  * G-band karyotype: 39,XX,-3,-4,<span style="color:lightgray">der(5)t(5;11)(q35;q12).ish der(5)t(5;11)(q35;q12)(wcp11+),</span>-7,-9,<span style="color:lightgray">add(12)(p11.2),</span>-15,-16,-17,-18,-22,<span style="color:lightgray">+2mar [6/30%]; 68-71,idemx2,-3,i(3)(p11)x2,-7,-11\[cp5] [5/25%]; 39,X,add(X)(q24),add(1)(q24),-3,i(3)(p11),-4,inv(5)(p15.3q13),-7,add(9)(p22),-10,der(12)t(7;12)(q11.2;q24.1),-15,-16,add(17)(q25),-18,add(21)(q22).ish der(21)t(3;21)(p24;q22)(wcp3+),-22,+mar [3/15%]; 46,XX [6/30%]</span>
  * Blast %: <span style="color:green">high (presumed >80%)</span>
  ![0223 sequencing depth](20231221_PAS57389_Nano_Leuk_0223_DNA_dorado-0.5.1.duplex_sup_5mCG_5hmCG.T2T.sorted.karyo.png)


Raw read depth data are in the ./data/ folder, in 1Mbp bins, matching these sample names.
