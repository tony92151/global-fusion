from globalfusion.optimizer import GFDGCSGD as GFDGCSGD_
from torch.optim import Adagrad
from torch.optim import SGD
from torch.optim import Adam
import torch
from copy import deepcopy as dcopy
from torch_optimizer import Yogi
from utils.configer import Configer
from globalfusion.optimizer import GFDGCSGD

SERVEROPT = {"SGD": SGD,
             "ADAGRAD": Adagrad,
             "ADAM": Adam,
             "YOGI": Yogi}


def SERVEROPTS(config: Configer = None, params=None, lr=None, **kwargs):
    if config is None:
        raise ValueError("config shouldn't be none")
    if params is None:
        raise ValueError("params shouldn't be none")
    if lr is None:
        raise ValueError("lr shouldn't be none")
    if config.agg.get_optimizer() not in SERVEROPT.keys():
        raise ValueError("model not define in {}".format(SERVEROPT.keys()))
    args = config.agg.get_optimizer_args()
    args.update(kwargs)
    try:
        opt = SERVEROPT[config.agg.get_optimizer()](params=params, lr=lr, **args)
    except TypeError:
        print("[Warning] Error arguments:\"{}\" for optimizer:\"{}\", using default setting.".format(
            args, config.trainer.get_optimizer()))
        opt = SERVEROPT[config.agg.get_optimizer()](params=params, lr=lr)
    return opt


FEDOPT = {"GFDGCSGD": GFDGCSGD}


def FEDOPTS(config: Configer = None, params=None, lr=None, **kwargs):
    if config is None:
        raise ValueError("config shouldn't be none")
    if params is None:
        raise ValueError("params shouldn't be none")
    if lr is None:
        raise ValueError("lr shouldn't be none")
    if config.trainer.get_optimizer() not in FEDOPT.keys():
        raise ValueError("model not define in {}".format(FEDOPT.keys()))
    args = config.agg.get_optimizer_args()
    args.update(kwargs)
    try:
        opt = FEDOPT[config.agg.get_optimizer()](params=params, lr=lr, **args)
    except TypeError:
        print("[Warning] Error arguments:\"{}\" for optimizer:\"{}\", using default setting.".format(
            args, config.trainer.get_optimizer()))
        opt = FEDOPT[config.agg.get_optimizer()](params=params, lr=lr)
    return opt

#
# class SGD(SGD_):
#     def set_gradient(self, cg):
#         agged_grad = cg
#         for group in self.param_groups:
#             for p in range(len(group['params'])):
#                 group['params'][p].grad = dcopy(agged_grad[p]).to(group['params'][p].device)
#
#
# class Adam(Adam_):
#     def set_gradient(self, cg):
#         agged_grad = cg
#         for group in self.param_groups:
#             for p in range(len(group['params'])):
#                 group['params'][p].grad = dcopy(agged_grad[p]).to(group['params'][p].device)
#
#
# class Adagrad(Adagrad_):
#     def set_gradient(self, cg):
#         agged_grad = cg
#         for group in self.param_groups:
#             for p in range(len(group['params'])):
#                 group['params'][p].grad = dcopy(agged_grad[p]).to(group['params'][p].device)
#
#
# class Adagrad(Adagrad_):
#     def set_gradient(self, cg):
#         agged_grad = cg
#         for group in self.param_groups:
#             for p in range(len(group['params'])):
#                 group['params'][p].grad = dcopy(agged_grad[p]).to(group['params'][p].device)
