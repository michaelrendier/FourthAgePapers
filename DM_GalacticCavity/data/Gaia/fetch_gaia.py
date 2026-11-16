#!/usr/bin/env python3
"""Fetch a random subsample of Gaia DR3 stars with radial velocities from the public ESA TAP service (async). One request, Mozilla UA.
Written 2026-11-16. Usage: python3 fetch_gaia.py   -> gaia_dr3_rvs_sample.csv  (re-fetch method for the vertical-wave test, 10_gaia_vertical_wave.py)"""
import requests, time, sys, os
UA = os.environ.get('CLAUDE_UA', 'Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/128.0')
URL = 'https://gea.esac.esa.int/tap-server/tap/async'
Q = ("SELECT source_id,ra,dec,parallax,parallax_error,pmra,pmdec,radial_velocity,radial_velocity_error,phot_g_mean_mag "
     "FROM gaiadr3.gaia_source WHERE random_index < 80000000 AND radial_velocity IS NOT NULL AND parallax_over_error > 10 "
     "AND radial_velocity_error < 10 AND ruwe < 1.4")
s = requests.Session(); s.headers['User-Agent'] = UA
r = s.post(URL, data=dict(REQUEST='doQuery', LANG='ADQL', FORMAT='csv', MAXREC='2000000', PHASE='RUN', QUERY=Q), allow_redirects=False)
job = r.headers['Location']; print('job', job, flush=True)
while True:
    ph = s.get(job + '/phase').text.strip(); print(ph, flush=True)
    if ph in ('COMPLETED', 'ERROR', 'ABORTED'): break
    time.sleep(15)
if ph != 'COMPLETED': print(s.get(job).text[:2000]); sys.exit(1)
with s.get(job + '/results/result', stream=True) as g, open('gaia_dr3_rvs_sample.csv', 'wb') as f:
    for ch in g.iter_content(1 << 20): f.write(ch)
print('done', os.path.getsize('gaia_dr3_rvs_sample.csv'))
