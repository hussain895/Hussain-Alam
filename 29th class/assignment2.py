moma = {"Starry Night", "The Persistence of Memory", "The Scream", "Girl with a Pearl Earring"}
louvre = {"Mona Lisa", "The Scream", "Liberty Leading the People", "Girl with a Pearl Earring"}
rijksmuseum = {"The Night Watch", "Girl with a Pearl Earring", "The Milkmaid", "Starry Night"}

moma.add("Composition with Red, Blue, and Yellow")

shared = moma & louvre & rijksmuseum
print("Shared Masterpieces:", shared)

louvre.update({"Raft of the Medusa", "Liberty Leading the People"})
rijksmuseum.update({"The Jewish Bride", "The Milkmaid"})

master = moma | louvre | rijksmuseum
print("Total unique artworks:", len(master))

rijksmuseum.discard("The Milkmaid")

exclusive = moma - louvre - rijksmuseum
print("Exclusive MoMA pieces:", exclusive)
