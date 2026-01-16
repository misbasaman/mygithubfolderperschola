import jsonFileHandler

data = jsonFileHandler.readJsonFile("insulin.json")

if data != "":
    bInsulin = data["molecules"]["bInsulin"]
    aInsulin = data["molecules"]["aInsulin"]
    insulin = bInsulin + aInsulin

    molecularWeightInsulinActual = data["molecularWeightInsulinActual"]

    print("bInsulin:", bInsulin)
    print("aInsulin:", aInsulin)
    print("molecularWeightInsulinActual:", molecularWeightInsulinActual)

    # Amino acid weights
    aaWeights = data["weights"]

    # Count amino acids
    aaCountInsulin = {
        x: insulin.upper().count(x)
        for x in [
            "A","C","D","E","F","G","H","I","K","L",
            "M","N","P","Q","R","S","T","V","W","Y"
        ]
    }

    # Calculate molecular weight
    molecularWeightInsulin = sum(
        aaCountInsulin[x] * aaWeights[x]
        for x in aaCountInsulin
    )

    print("The rough molecular weight of insulin:", molecularWeightInsulin)

    percentError = (
        (molecularWeightInsulin - molecularWeightInsulinActual)
        / molecularWeightInsulinActual
    ) * 100

    print("Percent error:", percentError)

else:
    print("Error. Exiting program")
