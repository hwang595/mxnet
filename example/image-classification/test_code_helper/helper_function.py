def add_fit_args(parser):
    """
    parser : argparse.ArgumentParser
    return a parser added with args required by fit
    """
    train = parser.add_argument_group('Training', 'model training')
    train.add_argument('--network', type=str,
                       help='the neural network to use')
    train.add_argument('--num-layers', type=int,
                       help='number of layers in the neural network, required by some networks such as resnet')
    train.add_argument('--gpus', type=str,
                       help='list of gpus to run, e.g. 0 or 0,2,5. empty means using cpu')
    train.add_argument('--kv-store', type=str, default='device',
                       help='key-value store type')
    train.add_argument('--num-epochs', type=int, default=100,
                       help='max num of epochs')
    train.add_argument('--lr', type=float, default=0.1,
                       help='initial learning rate')
    train.add_argument('--lr-factor', type=float, default=0.1,
                       help='the ratio to reduce lr on each step')
    train.add_argument('--lr-step-epochs', type=str,
                       help='the epochs to reduce the lr, e.g. 30,60')
    train.add_argument('--optimizer', type=str, default='sgd',
                       help='the optimizer type')
    train.add_argument('--mom', type=float, default=0.9,
                       help='momentum for sgd')
    train.add_argument('--wd', type=float, default=0.0001,
                       help='weight decay for sgd')
    train.add_argument('--batch-size', type=int, default=128,
                       help='the batch size')
    train.add_argument('--disp-batches', type=int, default=20,
                       help='show progress for every n batches')
    train.add_argument('--model-prefix', type=str,
                       help='model prefix')
    parser.add_argument('--monitor', dest='monitor', type=int, default=0,
                        help='log network parameters every N iters if larger than 0')
    train.add_argument('--load-epoch', type=int,
                       help='load the model on an epoch using the model-load-prefix')
    train.add_argument('--top-k', type=int, default=0,
                       help='report the top-k accuracy. 0 means no report.')
    train.add_argument('--test-io', type=int, default=0,
                       help='1 means test reading speed without training')
    return train