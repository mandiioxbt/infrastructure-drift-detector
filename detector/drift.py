class DriftDetector:
    def __init__(self, expected, actual): self.exp, self.act = expected, actual
    def detect(self):
        drifts = []
        for k in set(list(self.exp.keys())+list(self.act.keys())):
            if self.exp.get(k) != self.act.get(k):
                drifts.append({"resource": k, "severity": "high" if self.act.get(k) is None else "medium"})
        return drifts
