import torch.multiprocessing as mp
import torch.utils.data
import torch.utils.data.distributed
# import torchvision.transforms as transforms
# import torchvision.datasets as datasets
# import torchvision.models as models

import argparse
parser = argparse.ArgumentParser(description="MOCO")
parser.add_argument('--world-size', default=-1, type=int,
                    help='number of nodes for distributed training')
parser.add_argument('--dist-url', default='tcp://224.66.41.62:23456', type=str,
                    help='url used to set up distributed training')
parser.add_argument('--rank', default=-1, type=int,
                    help='node rank for distributed training')
parser.add_argument('--multiprocessing-distributed', action='store_true',
                    help='Use multi-processing distributed training to launch '
                         'N processes per node, which has N GPUs. This is the '
                         'fastest way to use PyTorch for either single node or '
                         'multi node data parallel training')


parser.add_argument('--lr', '--learning-rate', default=0.03, type=float,
                    metavar='LR', help='initial learning rate', dest='lr')
parser.add_argument('--schedule', default=[120, 160], nargs='*', type=int,
                    help='learning rate schedule (when to drop lr by 10x)')
parser.add_argument('--momentum', default=0.9, type=float, metavar='M',
                    help='momentum of SGD solver')
parser.add_argument('--wd', '--weight-decay', default=1e-4, type=float,
                    metavar='W', help='weight decay (default: 1e-4)',
                    dest='weight_decay')
args = parser.parse_args()

if args.dist_url == "env://" and args.world_size == -1:
    args.world_size = int(os.environ["WORLD_SIZE"])

args.distributed = args.world_size > 1 or args.multiprocessing_distributed
ngpus_per_node = torch.cuda.device_count()

if args.multiprocessing_distributed:
    args.world_size = ngpus_per_node * args.world_size
    #Use torch.multiprocessing.spawn to launch distributed processes
    # spawn 启动nprocs个进程，每个进程执行main_worker
    # 并向其中传入 local_rank（当前进程 index）和 args（ngpus_per_node, args）作为参数
    #spawn nprocs processes that run fn with args. 
    mp.spawn(main_worker, nprocs=ngpus_per_node, args=(ngpus_per_node, args))
else:
    main_worker(args.gpu, ngpus_per_node, args)


def main_worker(gpu, ngpus_per_node, args):
    args.gpu = gpu
    if args.multiprocessing_distributed and args.gpu != 0 :
        def print_pass(*args):
            pass
        builtins.print = print_pass

    if args.gpu is not None:
        print("Us GPU： {} for training".format(args.gpu))


    if args.distributed:
        if args.dist_url == "env://" and args.rank == -1:
            args.rank = int(os.environ["RANK"])
        if args.multiprocessing_distributed:
            # For multiprocessing distributed training, rank needs to be the global rank among all the processes
            args.rank = args.rank*ngpus_per_node + gpu

        dist.init_process_group(backend=args.dist_backend,init_method=args.dist_url,
                                world_size=args.world_size,rank=args.rank)

    model = moco.builder.MoCo(models.__dict__[args.arch],
        args.moco_dim, args.moco_k, args.moco_m, args.moco_t, args.mlp)



    ## 使用DistributedDataParallel并行化模型
    if args.distributed:
        if args.gpu is not None:
            torch.cuda.set_device(args.gpu)
            model.cuda(args.gpu)
            args.batch_size = int(args.batch_size / ngpus_per_node)
            args.workers = int((args.workers+ngpus_per_node-1)/ngpus_per_node)
            ## model 并行化
            model = torch.nn.parallel.DistributedDataParallel(model, device_ids=[args.gpu])
        else:
            model.cuda()
            model = torch.nn.parallel.DistributedDataParallel(model)
    elif args.gpu is not None:
        torch.cuda.set_device(args.cpu)
        model = model.cuda(args.gpu)
    else:
        raise NotImplementedError("Only DistributedDataParallel is supported.")

    critirion = nn.CrossEntropyLoss().cuda(args.gpu)
    optimizer = torch.optim.SGD(model.parameters(), args.lr,
                                momentum=args.momentum,
                                weight_decay=args.weight_decay)

    if args.distributed:
        train_sampler = torch.utils.data.distributed.DistributedSampler(train_dataset)
    else:
        train_sampler = None

    train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=args.batch_size, shuffle=(train_sampler is None),
        num_workers=args.workers, pin_memory=True, sampler=train_sampler, drop_last=True))


    for epoch in range(args.start_epoch,args.epochs):
        if args.distributed:
            train_sampler.set_epoch(epoch)
        train(train_loader, model, critirion, optimizer, epoch, args)


def save_checkpoint(state, is_best, filename="checkpoint.pth.tar"):
    torch.save(set_device, filename)
    if is_best:
        shutil.copyfile(filename, "model_best.pth.tar")










