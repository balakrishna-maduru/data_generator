import numpy as np


class DataSelector:

    def __init__(self) -> None:
        pass

    def select(self, data: list, row_count: int, p_: dict = {}):
        return np.random.choice(data,
                                row_count, 
                                p=self._probabilities(data, p_))
    
    def _probabilities(self, data: list, p_: dict):
        prob = [self._validate_probabilities(data.__len__(),p_)] * data.__len__()
        return self._over_write_probabilities(prob, data, p_)

    def _validate_probabilities(self, data_len:int, p_: dict):
        p_val = sum(p_.values())
        if p_val < 1:
            return (1 - p_val) / (data_len - p_.__len__())
        elif p_val == 1:
            return 0
        else:
            raise ValueError(f"Sum of probabilities are > 1 - '{p_}'")    

    def _over_write_probabilities(self, prob: list ,data: list, p_: dict):
        for key, value in p_.items():
            prob[data.index(key)] = value
        return prob