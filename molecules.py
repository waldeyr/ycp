# MOLECULES DEFNITIONS
######################################
#  PIVOT MOLECULES
######################################
fpp = graphDFS("CC(=CCCC(=CCCC(=CCO[P](=O)(O)O[P](=O)(O)O)C)C)C", "FPP")
npp = graphDFS("CC(C)=CCCC(C)=CCCC(C)(OP(O)(OP(O)(O)=O)=O)C=C", "NPP")
H = graphDFS("[H+]", "H+")
H2O = smiles("[OH2]", "H2O")
######################################
# ANIONS
######################################
opp = graphDFS("OP(O)(OP(O)([O-])=O)=O", "OPP-")
######################################
# CATIONS
######################################
cationC1 = smiles("CC(C)=CCCC(C)=CCCC(C)=C[CH2+]", "FPP cation C1+")
cationC3 = smiles("C[C+](CCC=C(C)CCC=C(C)C)C=C", "FPP/NPP C3+")
germacrenylC11 = smiles("C[C+](C)C1CCC(C)=CCCC(C)=CC1", "germacrenyl cation c11")
humulylC10 = smiles("CC1CC[CH+]C(C)(C)CC=C(C)CCC=1", "humulyl C10+")

######################################
# TARGET MOLECULES
######################################
target01 = smiles("C[C](C)C1CCC(C)C23CC=C(C)C2[CH2]13", "alpha-cubebene")
target02 = smiles("C[C](C)C1CCC2(C)C3CC=C(C)C2[CH2]13", "alpha-copaene")
target03 = smiles("[CH2][C](C)[CH]1C(C)(CCC([CH2]=1)=C(C)C)C=C", "alpha-elemene")
target04 = smiles("CC1CCC2C(CC2(C)C)C(CCC=1)=C", "beta-caryophyllene")
target05 = smiles("CC1=CCC(C=CCC(=CCC1)C)(C)C", "alpha-humulene")
target06 = smiles("C[C](C)C1CCC(C)=CCCC(C=[CH2]1)=C", "germacrene D")
target07 = smiles("C[C](C)C1CC=C(C)C2CCC(C)=C[CH2]12", "alpha-muurolene")
target08 = smiles("C[C](C)C1CCC(C)=C2CCC(C)=C[CH2]12", "delta-cadinene")
target09 = smiles("CC1(O)CCC2C1[CH2]3C(CCC2=C)C3(C)C", "spathulenol")
target10 = smiles("C[C]1CCC2C(C)CCC(CC1=2)C(C)(C)O", "Guaiol")
target11 = smiles("CC1C2CC(CCC2(C)[CH]CC=1)C(C)(C)O", "alpha-eudesmol")
target12 = smiles("C[C]1CC[CH]2C3(C)CCC(CC1=2)C3(C)C", "beta-patchoulene")
target13 = smiles("CC(C)=CCCC1(C)C2CCC(C)=C1C2", "alpha-bergamotene")

######################################
# OTHER MOLECULES
######################################
germacreneB = smiles("CC(C)=C1CCC(C)=CCCC(C)=CC1", "germacrene B")
hedycaryol = smiles("CC1CCC=C(C)CCC(CC=1)C(C)(C)O", "Hedycaryol")
