class XeMay:
    phankhoi: int
    tenxe: str
    xuatxu: str

    def __init__(self,phankhoi,tenxe,xuatxu):
        self.phankhoi = phankhoi
        self.tenxe = tenxe
        self.xuatxu = xuatxu
    def outputXeMay(self) -> str:
        result="Phan khoi: "+str(self.phankhoi) + "; Ten xe: " + self.tenxe + "; Xuat xu: " + self.xuatxu
        return result