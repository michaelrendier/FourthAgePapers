# SPARC data: where it is and how it was re-fetched (2026-11-14)

Source: https://astroweb.cwru.edu/SPARC/ (Lelli, McGaugh & Schombert 2016, AJ 152, 157). `http://` does not answer; use `https://`.

- In this repository (`data/SPARC/`, 13 MB): the 16 tables, the 175 rotation curves, mass models, surface-brightness profiles and bulge-disk files. Compared on 2026-11-14 with the files on the official site: all 16 tables and all 175 + 175 + 219 + 177 extracted files are **byte-identical**.
- Complete official set, 1.3 GB, on the Telescope Data drive: `/media/rendier/Telescope Data/SPARC/` (31 files: the above, the early-type galaxies, `RARsnapshots.zip`, `BayesLineFit.zip`, `MaximumDiskPhytonCode.zip`, `MCMCfits.tar.gz`, `PXL/{Compress_Fit,Fits,CornerPlot}.tar.gz`). Every zip and gzip tests clean (`unzip -tq`, `gzip -t`).
- Re-fetch: `SPARC_manifest.json` (this directory) with `~/.claude/skills/telescope-download/run_download.sh MANIFEST STATE "/media/rendier/Telescope Data" LOG`. Mozilla user agent; one file at a time; resumable.
- The `.pdf.zip` / `.png.zip` plot archives of the site were not fetched (figures only).
