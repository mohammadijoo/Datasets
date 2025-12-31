# Datasets

A curated collection of **CSV datasets** intended for **machine learning tutorials** and quick experimentation.

> Repository description (GitHub): “CSV datasets useful for Machine Learning Applications”.  
> Primary organization is by task type: **Bioinformatics**, **Classification**, **Clustering**, **NLP**, and **Regression**.  
> (See folder structure below.)

## Repository structure

Top-level folders:

- `Bioinformatics/Genes information`  
- `Classification`
- `Clustering`
- `NLP`
- `Regression`

Each folder is expected to contain one or more datasets relevant to that category (typically as `.csv`) and—ideally—accompanying metadata (see **Dataset metadata standard**).

## Quick start

### Clone the repo

```bash
git clone https://github.com/mohammadijoo/Datasets.git
cd Datasets
```

### Use a dataset in Python (local)

```python
import pandas as pd

df = pd.read_csv("NLP/<dataset>.csv")  # replace path as needed
df.head()
```

### Use a dataset in tutorials via a GitHub URL (recommended patterns)

If your tutorials link directly to datasets hosted here, prefer **stable references**:

1. **Pinned commit SHA** (most reproducible)
2. **Tag / release** (friendly + reproducible)
3. Branch (`main`) (least stable; can change over time)

**Raw GitHub pattern** (replace placeholders):

```
https://raw.githubusercontent.com/<owner>/<repo>/<ref>/<path>
```

Example (template):

```python
import pandas as pd

url = "https://raw.githubusercontent.com/mohammadijoo/Datasets/<ref>/NLP/<dataset>.csv"
df = pd.read_csv(url)
```

Notes:
- Using a commit SHA for `<ref>` ensures your tutorial always downloads identical content.
- If you plan to support external users, consider publishing **tags/releases** for “tutorial seasons” or course versions.

## Dataset catalog

This repository is organized by ML task category. For a browsable index, each folder should include a short `README.md` listing:
- dataset file name
- task type
- target column (if applicable)
- row/column counts (optional but helpful)
- source/provenance link
- license/terms of use
- any preprocessing performed

If you want, you can also add a machine-readable catalog file (e.g., `catalog.yml`) at the repo root.

## Dataset metadata standard (recommended)

For every dataset added or modified, include metadata in one of these forms:

- a sidecar file: `<dataset>.meta.yml` (preferred), or
- a folder-level table in `README.md`.

Minimal recommended fields:

```yaml
name: "<dataset>"
path: "NLP/<dataset>.csv"
task: "classification | regression | clustering | nlp | bioinformatics | other"
target: "<target_column_or_null>"
source:
  name: "<upstream_source_name>"
  url: "<upstream_url>"
license: "<license_name_or_terms>"
added_by: "<github_handle>"
notes: "<optional preprocessing / caveats>"
```

## Data provenance and licensing

This repository may contain datasets collected from external sources. Contributors and maintainers must ensure:

- **Provenance is documented** (link to upstream source).
- **Redistribution is allowed** under the upstream license/terms.
- Any **attribution requirements** are preserved.
- Sensitive or personal data is not included unless explicitly permitted and appropriately anonymized.

If a dataset’s redistribution rights are unclear, do not add it; instead add a script or instructions to fetch it from the original source.

## Maintainers and governance

### Maintainers

- **Lead maintainer / repository owner:** `@mohammadijoo`

Maintainers are responsible for:
- reviewing and merging pull requests
- ensuring dataset provenance and licensing compliance
- keeping folder-level indexes/catalogs accurate
- defining and enforcing repository conventions (naming, metadata, formatting)

### Decision-making

- Routine changes (small additions/fixes): single maintainer approval.
- Material changes (renames, deletions, dataset replacements, or major reorganizations): require explicit approval by the lead maintainer, plus clear migration notes.

### Versioning and stability guarantees

This repo is intended to support external tutorial links, so stability matters.

Recommended policy:
- **Do not rename or move existing dataset files** without providing a compatibility path.
- If a dataset must move:
  - keep a copy in the old location for at least one release cycle, or
  - document a redirect/migration mapping in `MIGRATIONS.md`.

Because GitHub currently shows **no releases**, consider adding:
- semantic tags (e.g., `v1.0.0`) for course cohorts
- a `CHANGELOG.md` with dataset-level changes

### Deprecation policy

A dataset may be deprecated if:
- licensing/provenance becomes unclear
- data quality issues are discovered
- a better canonical source becomes available

Deprecations should be recorded in `CHANGELOG.md` (or `MIGRATIONS.md`) with:
- reason for deprecation
- replacement dataset (if any)
- effective date/version

## Contributing

Contributions are welcome via pull request.

### Adding a dataset

1. Choose the correct top-level folder (e.g., `Regression/`).
2. Add the `.csv` file.
3. Add metadata (see **Dataset metadata standard**).
4. Update the folder’s `README.md` index (or root catalog).
5. Keep files reasonably sized (consider Git LFS for very large files).

### Formatting conventions

- Prefer `.csv` with a header row.
- Use UTF-8 encoding.
- Use consistent missing value markers (e.g., empty, `NA`, or `NaN`) and document it in metadata.

## Issue reporting

Please open a GitHub Issue for:
- broken tutorial links / moved files
- data quality problems (duplicate rows, corrupted columns, encoding issues)
- licensing/provenance questions

## Security and responsible data use

If you believe a dataset includes sensitive information that should not be distributed, open an issue describing:
- the dataset path
- the concern (PII, re-identification risk, license violation)
- suggested remediation

## License

No repository-wide license is currently indicated on the GitHub landing page.  
To clarify reuse conditions, consider adding a `LICENSE` file and ensuring each dataset’s upstream license/terms are documented in metadata.
