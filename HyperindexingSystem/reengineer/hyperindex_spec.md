# Hyperindex Specification

Status: draft, built up incrementally. Sections are added as they are settled.

## 1. File layers

Four JSON files, organised by calendar date:

| File | Level | Entries |
|---|---|---|
| `Ptolemy.json` | top | Core only. Never carries Navigation or Relations. |
| `Year.json` | year | Core + Navigation + Relations (roll-up of Month.json) |
| `Month.json` | month | Core + Navigation + Relations (roll-up of Day.json) |
| `Day.json` | day | Core + Navigation + Relations (leaf entries: ingested documents) |

Each file is a JSON array of entries. Each file holds at least one entry (a sample entry at creation).

Searching and navigation happen only in the files below `Ptolemy.json`.

## 2. Entry sections

An entry is an object with up to three sections: `core`, `navigation`, `relations`.

### 2.1 Core (all four files)

| Key | Type | Meaning |
|---|---|---|
| `index` | string | The hyperindex: 64 hex digits (placeholder `0` × 64; width to change later) |
| `len` | integer | Length of the encoded item |
| `perm` | string | Permutation / alphabet used to decode (`ascii`, `json`) |
| `seen` | integer | Ingest timestamp, Unix epoch seconds (UTC) |
| `title` | string | Short human-readable title |

### 2.2 Navigation (Year, Month, Day)

| Key | Type | Meaning |
|---|---|---|
| `kind` | string | Type of item (chat, paper, code, web, notes; `year`/`month` for roll-ups) |
| `category` | string | One value from a small controlled vocabulary (the browse/filter axis) |
| `source` | string | Who or what the item came from |
| `tags` | array of string | Free-form tags |
| `note` | string | One-line summary |

Not part of Navigation: collection, position/sequence, occurred date. The calendar position supplies the date.

### 2.3 Relations (Year, Month, Day): STUB

Reserved for later engineering. Present in the files as placeholders only.

| Key | Type | Meaning |
|---|---|---|
| `up` | string or null | `index` of the entry this continues / replies to / supersedes |
| `ref` | array of string | `index` values of entries it cites |

## 3. Roll-up

Navigation works like a file manager with one directory in focus. An entry in `Year.json` or `Month.json` stands for the level below it and is what navigation reads. Its Navigation values summarise that level. Exact roll-up fields are not yet specified.

## 4. Out of scope

- Retrieval statistics (play-count analogue): kept in the Monad's Paper's Hands Blockchain Long Path, not in these entries.
- Hashes / checksums: not used.

## 5. Open items

- Short vs readable keys (flat vs nested `core`/`navigation`/`relations` sections), pending the Horner stage.
- Controlled `category` vocabulary.
- Roll-up fields (date range, counts, tag union).
- Hyperindex width (currently 64 hex digits).
