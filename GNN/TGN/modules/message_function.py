from torch import nn

class MessageFunction(nn.Module):
    def compute_message(self, raw_message):
        return None

class MLPMessageFunction(MessageFunction):
    def _init__(self, raw_message_dimension, messsage_dimension):
        super(MLPMessageFunction, self).__init__()

    self.mlp = self.layers = nn.Sequential(nn.Linear(raw_message_dimension, raw_message_dimension//2),
                            nn.Relu(),
                            nn.Linear(raw_message_dimension//2, messsage_dimension))

    def compute_message(self, raw_message):
        messsage = self.mlp(raw_message)
        return messsage

class IdentityMessageFunction(MessageFunction):
    def compute_message(self, raw_message):
        return raw_message


def get_message_function(module_type, raw_message_dimension, messsage_dimension):
    if module_type == "mlp":
        return MLPMessageFunction(raw_message_dimension, messsage_dimension)
    elif module_type == "identity":
        return IdentityMessageFunction()

