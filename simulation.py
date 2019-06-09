######################################
# RULES
######################################
pushFilePrefix("rules/")

ruleGML("1-10CycFromFPP.gml")
ruleGML("1-11CycFromFPP.gml")
ruleGML("1-6CycFromNPP.gml")

ruleGML("1-2Hshift.gml")
ruleGML("1-3Hshift.gml")
ruleGML('allylshift.gml')

ruleGML("1-6Cyc.gml")
ruleGML("1-11Cyc.gml")
ruleGML("2-6Cyc.gml")
ruleGML("2-7Cyc.gml")
ruleGML("2-10Cyc.gml")
ruleGML("7-11Cyc.gml")

ruleGML("Cope02.gml")
ruleGML("BicycloGermacrenesC3Oxidation.gml")
ruleGML("C2protonation.gml")
ruleGML("6-2cycForGermacrenoids.gml")

ruleGML("H2Ogain.gml")
ruleGML("Hloss.gml")

popFilePrefix()
######################################
# DEFINE LIST OF INITIAL INPUTS
######################################
eductMols = [fpp,npp,H2O]

######################################
# ITERATIONS
######################################


strat = (addSubset(eductMols) >> repeat[6](inputRules))


######################################
# NETWORK GENERATION
######################################
ls = LabelSettings(LabelType.Term, LabelRelation.Unification)
def overallCharge(a): return sum(int(v.charge) for v in a.vertices)
def countCycs(a): return a.numEdges - a.numVertices + 1
dg = dgRuleComp(inputGraphs, strat, ls)
dg.calc()