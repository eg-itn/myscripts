def set_logger(args):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s %(levelname)-5s %(filename)-20s %(funcName)-10s : %(message)s')

    # logging handler1(標準出力)
    handler_std = logging.StreamHandler()
    handler_std.setLevel(logging.INFO)
    # handler_std.setFormatter(formatter)

    # logging handler2(debug出力)
    logfile = os.path.join(args.dst_dir, 'log{}.txt'.format(args.tstamp))
    handler_dbg = logging.FileHandler(logfile)
    handler_dbg.setLevel(logging.DEBUG)
    handler_dbg.setFormatter(formatter)

    # logging handler3(error出力)
    errlogfile = os.path.join(args.dst_dir, 'log{}-ERROR.txt'.format(args.tstamp))
    handler_err = logging.FileHandler(errlogfile)
    handler_err.setLevel(logging.ERROR)
    handler_err.setFormatter(formatter)

    # loggerにhandlerを設定
    logger.addHandler(handler_std)
    logger.addHandler(handler_dbg)
    logger.addHandler(handler_err)

    logger.__setattr__('errlogfile', errlogfile)

    return logger