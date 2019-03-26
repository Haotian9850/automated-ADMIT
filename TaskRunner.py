#!/usr/bin/env casarun
import admit 


def assemble(i, numsigma, minchan, maxchan, fileName):
        """
        Args:
                i: task ID (used to associate parameter set with its task)
                numsigma: param numsigma
                minchan: param minchan
                maxchan: param maxchan
                fileName: input .fits file (String)
        Returns:
                assembed ADMIT task
        """
        p = admit.Project('molecular-line.admit' + '_' + str(i), dataserver=True)      #dataserver suppress browser session
        t0  = p.addtask(admit.Ingest_AT(file=fileName))
        t1  = p.addtask(admit.CubeStats_AT(ppp=True), [t0])
        t2  = p.addtask(admit.Moment_AT(mom0clip=2.0, numsigma=[numsigma]), [t0, t1])
        t3  = p.addtask(admit.CubeSpectrum_AT(), [t0, t2])
        t4 = p.addtask(admit.LineID_AT(
            vlsr = 8.0, #fixed value
            numsigma = numsigma,
            minchan = minchan,
            maxgap = maxchan, #default value
            identifylines = True,
            allowexotics = True,
            recomblevel = 'deep',
        ), [t1, t3])
        return p

def runAllProjects(allParams, fileName):
        """
        Calls assmble(), makes and then run all project built with all possible parameter combinations
        Args:
                allParams: a list of all possible executable parameter combinations (nested list)
                fileName: input .fits file (String)
                
        Returns: 
                NONE
        """
        for i in range(0, len(allParams), 1):
                newProject = assemble(i, allParams[i][0].item(), allParams[i][1], allParams[i][2], fileName)
                newProject.run()