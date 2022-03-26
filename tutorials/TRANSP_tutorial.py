'''
Tutorial to run TRANSP
'''

from portals.misc_tools 	import IOtools
from portals.transp_tools 	import TRANSPtools

# ---------------------------------------------------------------------------------
# Data Selection
# ---------------------------------------------------------------------------------

# Select the folder that contains namelist and UFILES
folder = IOtools.expandPath('$PORTALS_PATH/regressions/data/FolderTRANSP/')

# Select the mpisettings (this must coincide to whether the namelist is running any of the modules in parallel)
mpisettings = {'trmpi':1,'toricmpi':32,'ptrmpi':1}

# Select shotnumber (this is for historical reason, it doesn't need to match an experimental shot) and run name
# then, the TRANSP simulation will have the complete name "shotnumber+runname"
shotnumber = '12345'
runname    = 'A01'

# Select machine name
tokamak = 'CMOD'

# ---------------------------------------------------------------------------------
# Workflow Preparation
# ---------------------------------------------------------------------------------

# Initialize class
t = TRANSPtools.TRANSP(folder,tokamak)

# Define user and run parameters
t.defineRunParameters(shotnumber+runname,shotnumber,mpisettings=mpisettings)

# ---------------------------------------------------------------------------------
# Run TRANSP
# ---------------------------------------------------------------------------------

# Submit run
t.run()

# Check every 5min if the run has finished, and grab final results when they are ready
c = t.checkUntilFinished(label=runname,checkMin=5)

# ---------------------------------------------------------------------------------
# Plot results
# ---------------------------------------------------------------------------------

# Plot
t.plot(label=runname) 

'''
Read results that already exist
-------------------------------
If TRANSP has already been run and the .CDF results file already exists (cdf_file), this workflow is not needed
and one can simply read and plot the results:

	from portals.transp_tools import CDFtools
	c = CDFtools.CDFreactor(cdf_file)
	c.plotRun()

'''