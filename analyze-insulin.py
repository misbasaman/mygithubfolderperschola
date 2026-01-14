import re

# Step 1: Read raw preproinsulin file
with open("preproinsulin-seq.txt", "r") as file:
    raw_data = file.read()

# Step 2: Clean the sequence
# Remove ORIGIN, //, numbers, spaces, and newlines
clean_sequence = re.sub(r"ORIGIN|\d+|//|\s+", "", raw_data).lower()

# Step 3: Verify total length
print("Total length:", len(clean_sequence))

if len(clean_sequence) != 110:
    raise ValueError("Sequence length is incorrect!")

# Step 4: Write cleaned full sequence
with open("preproinsulin-seq-clean.txt", "w") as file:
    file.write(clean_sequence)

# Step 5: Slice sequences
lsinsulin = clean_sequence[0:24]      # 1–24
binsulin  = clean_sequence[24:54]     # 25–54
cinsulin  = clean_sequence[54:89]     # 55–89
ainsulin  = clean_sequence[89:110]    # 90–110

# Step 6: Write output files
files = {
    "lsinsulin-seq-clean.txt": lsinsulin,
    "binsulin-seq-clean.txt": binsulin,
    "cinsulin-seq-clean.txt": cinsulin,
    "ainsulin-seq-clean.txt": ainsulin
}

for filename, sequence in files.items():
    with open(filename, "w") as file:
        file.write(sequence)
    print(f"{filename}: {len(sequence)} characters")

print("✅ Insulin sequence processing completed successfully.")
