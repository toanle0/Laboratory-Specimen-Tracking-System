from specimen_tracker import add_specimen
from chain_of_custody import log_transfer

add_specimen("SP-200", "PT-300", "Glass Slide")

log_transfer("SP-200", "Accessioning", "TLE")
log_transfer("SP-200", "Pathology", "TLE")

print("Specimen workflow simulated.")