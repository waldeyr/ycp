######################################
# PDF PRINTER
######################################
p = DGPrinter()
# print molecule with all the hydrogenes attached
p.graphPrinter.collapseHydrogens = True
p.graphPrinter.withIndex = False
# color molecules with rings red, charged molecules blue
p.pushVertexColour(lambda g, dg: "red" if overallCharge(g) != 0 else "black" if countCycs(g) > 0 else "black")

postSection("YCP Sesquitepenes Biosynthesis from FPP and H2O")
dg.print(p)
