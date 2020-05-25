import sys
import math
import time
from mpi4py import MPI
comm = MPI.COMM_WORLD
num_procs = comm.Get_size()
rank = comm.Get_rank()
print("Proceso verificador ! ", rank, " con argumento ", sys.argv[1])
status = MPI.Status()


def isPrime(n):
    sw = True
    if(n < 2):
        return False
    j = 2
    while(j <= math.sqrt(n) and sw):
        if n % j == 0:
            sw = False
        j += 1
    return sw


if rank == 0:
    actualLimit = 0
    limit = int(sys.argv[1])
    process_statistics = [-1]*(num_procs-1)
    t1 = time.process_time()
    for i in range(1, num_procs):
        actualLimit = actualLimit + 100
        comm.send(actualLimit, dest=i)
    iterador = 0
    while iterador < limit/100:
        tt = comm.recv(source=MPI.ANY_SOURCE, status=status)
        dest = status.Get_source()
        if process_statistics[dest - 1] < tt:
            process_statistics[dest - 1] = tt
        iterador += 1
        if actualLimit < limit:
            actualLimit = actualLimit+100
            comm.send(actualLimit, dest=dest)
    for i in range(1, num_procs):
        comm.send(-1, dest=i)
    tiempo = time.process_time() - t1
    print("The process was done in", tiempo, "with",
          sum(process_statistics), "of primes")
else:
    (constraint, groups, primes) = (0, 0, 0)
    while constraint != -1:
        constraint = comm.recv(source=0)
        if constraint != -1:
            groups += 1
            leftd = constraint-100
            for i in range(leftd, constraint):
                if isPrime(i):
                    primes += 1
            comm.send(primes, dest=0)
        else:
            print("limit of groups checked:", groups)
