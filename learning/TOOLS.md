<!-- verified-at: <short-sha> · <YYYY-MM-DD> -->
# Tool & Dependency Catalog

> **SEED FILE.** Consult before adding a dependency; append the tool and its score after you adopt it. The two entries below are the kit's own baseline.

## Vetted Tools

### python-standard-library
- **Purpose**: Zero-dependency, cross-platform execution for the sensitive-data scanner and git hooks.
- **Version / install**: built-in, Python 3.8+ (checked <YYYY-MM-DD>)
- **Score**: 38/40 (Fit 5 · License 5 · Integration 5 · Perf 5 · Maint 5 · Docs 5 · Security 5 · Alts 3) · unverified: none
- **Gotchas**: `python3` must be on PATH; Windows users may need `python` rather than `python3`.

## Rejected Tools

- **`pre-commit` (pip package)**: adds a third-party runtime and virtualenv overhead for what native `core.hooksPath` plus a standalone script already does (<YYYY-MM-DD>).
