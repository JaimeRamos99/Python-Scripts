from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    data = [(i) for i in range(size)]
else:
    data = None
    data = comm.scatter(data, root=0)

data = comm.gather(data*data, root=0)
if rank == 0:
    print ("received ",data)
