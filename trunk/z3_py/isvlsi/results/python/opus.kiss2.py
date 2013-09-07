from z3 import *
from math import *
for bits in range(int(ceil(log(11)/log(2))+4),  int(ceil(log(11)/log(2))-1), -1):
	st_START, st_init0, st_init1, st_init2, st_init4, st_IOwait, st_read0, st_write0, st_RMACK, st_WMACK, st_read1 = BitVecs('st_START st_init0 st_init1 st_init2 st_init4 st_IOwait st_read0 st_write0 st_RMACK st_WMACK st_read1',bits)

	s = Solver();
	s.set("timeout", 30000)
	s.add(Distinct(st_START,st_init0,st_init1,st_init2,st_init4,st_IOwait,st_read0,st_write0,st_RMACK,st_WMACK,st_read1))

	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_START)) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_init0)) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_START ^ st_init0))) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_write0 ^ st_IOwait))) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_init0)) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_init0)) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_init0 ^ st_init0))) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_write0 ^ st_IOwait))) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_init0)) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_init1)) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_init0 ^ st_init1))) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_write0 ^ st_IOwait))) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_init1)) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_init1)) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_init1 ^ st_init1))) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_write0 ^ st_IOwait))) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_init1)) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_init2)) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_init1 ^ st_init2))) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_write0 ^ st_IOwait))) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_init2)) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_init4)) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_init2 ^ st_init4))) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_write0 ^ st_IOwait))) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_init4)) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_init4)) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_init4 ^ st_init4))) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_write0 ^ st_IOwait))) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_init4)) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_IOwait)) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_init4 ^ st_IOwait))) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_write0 ^ st_IOwait))) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_IOwait)) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_IOwait)) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_IOwait ^ st_IOwait))) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_write0 ^ st_IOwait))) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_IOwait)) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_init1)) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_IOwait ^ st_init1))) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_write0 ^ st_IOwait))) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_IOwait)) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_read0)) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_IOwait ^ st_read0))) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_write0 ^ st_IOwait))) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_IOwait)) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_write0)) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_IOwait ^ st_write0))) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_write0 ^ st_IOwait))) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_IOwait)) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_RMACK)) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_IOwait ^ st_RMACK))) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_write0 ^ st_IOwait))) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_IOwait)) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_WMACK)) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_IOwait ^ st_WMACK))) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_write0 ^ st_IOwait))) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_IOwait)) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_init2)) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_IOwait ^ st_init2))) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_write0 ^ st_IOwait))) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_RMACK)) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_RMACK)) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_RMACK ^ st_RMACK))) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_write0 ^ st_IOwait))) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_RMACK)) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_read0)) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_RMACK ^ st_read0))) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_write0 ^ st_IOwait))) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_WMACK)) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_WMACK)) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_WMACK ^ st_WMACK))) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_write0 ^ st_IOwait))) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_WMACK)) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_write0)) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_WMACK ^ st_write0))) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_write0 ^ st_IOwait))) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_read0)) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_read1)) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_read0 ^ st_read1))) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_write0 ^ st_IOwait))) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_read1)) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_IOwait)) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_read1 ^ st_IOwait))) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_write0 ^ st_IOwait))) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_write0)) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,st_IOwait)) for i in range(bits) ])
	)
	s.add(
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_write0 ^ st_IOwait))) for i in range(bits) ]) ==
	Sum([ ZeroExt(int(ceil(log(bits)/log(2))+1), Extract(i,i,(st_write0 ^ st_IOwait))) for i in range(bits) ])
	)
        if(s.check() == sat):
          print "Sat, %d," %(bits),
          m = s.model()
          for d in m.decls():
              print "%s," % (d.name()),
          print " "
          print "ASSIGN, %d," %(bits),
          for d in m.decls():
              print "%s," % (m[d]),
        else:
           print "NotSat, %d," %(bits),
           print " "
        print " "
        sys.stdout.flush()
