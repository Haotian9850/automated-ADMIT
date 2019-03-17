#!/usr/bin/env casarun
import admit 

from build_new_param import findAllCombinations


allParams = findAllCombinations()
fileName = "../uid___A002_Xb20b6d_X3c34__Serpens_South.C17O_3-2.pbcor.fits"

def assemble(i, numsigma, minchan, maxchan):
        p = admit.Project('molecular-line.admit' + '_' + str(i), dataserver=True)
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


def runAllProjects():
    for i in range(0, len(allParams), 1):
        newProject = assemble(i, allParams[i][0].item(), allParams[i][1], allParams[i][2])
        newProject.run()



runAllProjects()    #will take some time...