# Example input and output file structure to make  PLINK `.ped` and `.map` files with map_ped.py

This project converts genotype data (Excel) into PLINK `.ped` and `.map` formats.  
Below is an example (3 individuals × 3 SNPs).

---

## Genotype data (input for `.ped`)

| Participant ID | SNP1 | SNP2 | SNP3 |
|---|---|---|---|
| X | A G | T T |    |
| Y | C G | T G |    |
| Z | G G | T T |    |

> Genotypes may be written as A G, AG, A/G, A|G, or a single allele (A → interpreted as A A).
> Leave the cell empty if data is missing.

---

## SNP info (input for `.map`)

| #CHROM | ID        | POS      |
|---|---|---:|
| 1 | rs61776719 | 37995647 |
| 4 | rs781663   | 56915588 |
| 22| rs71313931 | 19972661 |

> Column names must be **#CHROM**, **ID**, **POS** (as required by the script, modify scirpt for different columns names).  
> Chromosome values should be numbers only (e.g., `1`, `4`, `22`).

---

## How this maps to PLINK files

- **`.ped` file**  
  Each row represents one participant.  
  The first 6 columns are fixed PLINK fields:

  Family ID | Individual ID | Paternal ID | Maternal ID | Sex | Phenotype

After these, all genotype columns follow (two alleles per SNP).  
Missing data is encoded as `0 0`.

- **`.map` file**  
Each row represents one SNP with 4 required fields:  


 Chromosome | SNP ID | Genetic distance (set to 0) | Base-pair position


---

## Example output

### `.ped`
```
X X 0 0 0 -9 A G T T 0 0
Y Y 0 0 0 -9 C G T G 0 0
Z Z 0 0 0 -9 G G T T 0 0
```


### `.map` 
```
1 rs61776719 0 37995647
4 rs781663 0 56915588
22 rs71313931 0 19972661
```



---

