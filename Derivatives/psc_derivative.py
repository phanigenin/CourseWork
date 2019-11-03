class PSC_Derivative():
    pass

class PSC_EquityDerivative(PSC_Derivative):

    def __init__(self):
        self.underlying_type = 'EQ'

class PSC_Future(PSC_Derivative):

    def __init__(self):
        self.instr_type = 'FUT'

class PSC_EquityFuture(PSC_Future):
    def __init__(self):
        PSC_Future.__init__()
        self.underlying_type = 'EQ'