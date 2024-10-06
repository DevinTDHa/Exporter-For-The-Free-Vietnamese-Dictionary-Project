import json


def parse_entry(entry_lines):
    out_entries: list[dict] = list()
    current_word = ""
    current_sense: dict = {}
    current_section = None

    for line in entry_lines:
        if not line:
            continue

        line = line.strip()
        line_content = line[1:].strip()

        if line.startswith("@"):  # Word
            current_word = line_content

        elif line.startswith("*"):  # Part of speech
            current_section = "pos"

            if current_sense:  # Append the current sense to the out list
                out_entries.append(current_sense)

            current_sense = {
                "word": current_word,
                "pos": line_content,
                "senses": [],
            }

        elif line.startswith("-"):  # Translation or synonym
            # Only store information about synonyms or POS. Otherwise it seems like a reference to another word.
            if current_section == "syn":
                current_sense.setdefault("synonyms", []).append({"word": line_content})
            elif current_section == "pos":
                current_sense["senses"].append({"glosses": [line_content]})

        elif line.startswith("="):  # Example
            current_section = "ex"
            if "+" in line_content:  # Line contains both example and translation
                example, translation = line_content.split("+", 1)
            else:
                example = line_content
                translation = ""

            current_sense.setdefault("examples", []).append(
                {
                    "example": example,
                    "translation": translation,
                    "type": "example",
                }
            )

        elif line.startswith("#"):  # Synonyms
            current_section = "syn"

        elif line.startswith("!"):  # Idioms
            current_section = "id"
            current_sense.setdefault("examples", []).append(
                {
                    "example": line_content,
                    "translation": "",
                    "type": "idiom",
                }
            )

    # Handle the last sense
    if current_sense:  # Append the current sense to the entry, last one is done
        out_entries.append(current_sense)

    return out_entries


def parse_dictionary(input_data: str):
    entries = []
    current_entry_lines = []

    for line in input_data.splitlines():
        if line.startswith("@") and current_entry_lines:
            entries.extend(parse_entry(current_entry_lines))
            current_entry_lines = [line]
        else:
            current_entry_lines.append(line)

    if current_entry_lines:
        entries.extend(parse_entry(current_entry_lines))

    return entries


# Convert the parsed dictionary to JSONL format
def write_to_jsonl(entries, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for entry in entries:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def extract_gzipped_dict(gzipped_file: str, output_file: str):
    import gzip

    # Read from a folder in gzipped format
    with gzip.open(gzipped_file, "rt", encoding="utf-8") as f:
        data = f.read()

    entries = parse_dictionary(data)
    write_to_jsonl(entries, output_file)


if __name__ == "__main__":
    # Iterate over data/ and find all files with .dz extension
    import os

    for file in os.listdir("data"):
        if file.endswith(".dz"):
            print("Processing file:", file)
            extract_gzipped_dict(
                f"data/{file}", f"data/{file.replace('.dz', '.jsonl')}"
            )
