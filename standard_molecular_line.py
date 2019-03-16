#!/usr/bin/env casarun
import admit
p = admit.Project('molecular-line.admit', dataserver=True)
t0  = p.addtask(admit.Ingest_AT(file='../uid___A002_Xb20b6d_X3c34__Serpens_South.C17O_3-2.pbcor.fits'))
t1  = p.addtask(admit.CubeStats_AT(ppp=True), [t0])
t2  = p.addtask(admit.Moment_AT(mom0clip=2.0, numsigma=[3.0]), [t0, t1])
t3  = p.addtask(admit.CubeSpectrum_AT(), [t0, t2])

#molecular line identification task
#t4  = p.addtask(admit.LineID_AT(csub=[0, 0], minchan=4, maxgap=6, numsigma=5.0), [t1, t3])

t4 = p.addtask(admit.LineID_AT(
    vlsr = 8.0,
    numsigma = 2.0,
    minchan = 2,
    maxgap = 3, #default value
    identifylines = True,
    allowexotics = True,
    recomblevel = 'deep',
), [t1, t3])

p.run()
