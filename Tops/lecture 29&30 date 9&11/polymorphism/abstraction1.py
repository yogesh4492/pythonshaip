from abc import ABC,abstractmethod


class RBI(ABC):
    @abstractmethod
    def ROI():
        pass
class SBI(RBI):
    def ROI(self):
        return 8.5
class HDFC(RBI):
    def ROI(self):
        return 7.5

sbi=SBI()
hdfc=HDFC()

print(sbi.ROI())
print(hdfc.ROI())