class config_gfgc:
    def __init__(self, config):
        self.config = dict(config._sections["gfgc"])

    def get_momentum(self) -> float:
        return float(self.config["momentum"])

    def get_fusing_ratio(self) -> list:
        fr = self.config["fusing_ratio"]
        if fr[0] == "[" and fr[-1] == "]":
            fr = fr[1:-1].split(",")
            fr = [float(i) for i in fr]
        else:
            fr = [float(fr)]
        return fr

    def get_global_momentum(self) -> float:
        return float(self.config["global_momentum"])
