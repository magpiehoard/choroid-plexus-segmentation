import subprocess

# Define the path to your FreeSurfer installation
freesurfer_path = "/home/abigail/MSc/Apps/neurocommand/local/containers/freesurfer_7.4.1_20231214/freesurfer"

# The command to run, e.g., checking the version of `mri_binarize`
cmd = "mri_binarize --version"

# Build the full command, sourcing FreeSurfer setup first
full_cmd = f'''
bash -c "source {freesurfer_path}/SetUpFreeSurfer.sh && {cmd}"
'''

# Run it
result = subprocess.run(full_cmd, shell=True, capture_output=True, text=True)

# Print the results
print("STDOUT:")
print(result.stdout)
print("STDERR:")
print(result.stderr)
