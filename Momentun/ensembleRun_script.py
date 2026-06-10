# ======================================================
# At first you need to make the case using using command below
# make COMPILER=gfortran
# This script will only work in the KiD directtory
# You will get your output inside KiD/output
# ======================================================

import xarray as xr
import subprocess
import os
import glob
import shutil

# =====================================================
# Read LHS ensemble
# =====================================================

ds = xr.open_dataset(
    "/home/ppaul/Drizzle_Dynamics_summer2026/Momentun/lhs_100_members.nc"
)

# =====================================================
# Directories
# =====================================================

template_nml = "/data1/pappu/KiD-A/namelists/warm1_template.nml"
run_nml      = "/data1/pappu/KiD-A/namelists/warm1.nml"

exe = "/data1/pappu/KiD-A/bin_gfortran_/KiD_1D.exe"

output_dir = "/data1/pappu/KiD-A/output"
ensemble_dir = "/data1/pappu/KiD-A/output/tau_case1_100"   ######### change here if you are making different sample test##############

os.makedirs(ensemble_dir, exist_ok=True)

# =====================================================
# Ensemble loop
# =====================================================

#for i in range(len(ds.member)):
for i in range(2):
    N     = float(ds["aero_N_init"][i])
    rd    = float(ds["aero_rd_init"][i])
    sigma = float(ds["aero_sig_init"][i])
    w     = float(ds["wctrl"][i])
    t     = int(ds["tctrl"][i])

    print(
        f"Running member {i:03d}: "
        f"N={N:.2e}, rd={rd:.2e}, "
        f"sigma={sigma:.2f}, w={w:.2f}, t={t}"
    )

    # -----------------------------------------
    # Read template
    # -----------------------------------------

    with open(template_nml, "r") as f:
        txt = f.read()

    txt = txt.replace("__N__", str(N))
    txt = txt.replace("__RD__", str(rd))
    txt = txt.replace("__SIGMA__", str(sigma))
    txt = txt.replace("__W__", str(w))
    txt = txt.replace("__T__", str(t))

    # -----------------------------------------
    # Write run namelist
    # -----------------------------------------

    with open(run_nml, "w") as f:
        f.write(txt)

    # -----------------------------------------
    # Run KiD
    # -----------------------------------------

    subprocess.run(
        [exe, run_nml],
        check=True
    )

    # -----------------------------------------
    # Move output files
    # -----------------------------------------

    nc_files = glob.glob(f"{output_dir}/*.nc")
    nml_files = glob.glob(f"{output_dir}/*.nml")

    for f in nc_files:

        shutil.move(
            f,
            f"{ensemble_dir}/member_{i:03d}.nc"
        )

    for f in nml_files:

        shutil.move(
            f,
            f"{ensemble_dir}/member_{i:03d}.nml"
        )

    print(f"Finished member {i:03d}")

print("All ensemble members completed.")
