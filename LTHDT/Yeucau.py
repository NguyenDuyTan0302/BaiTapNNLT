from drive import XeMay
def main():
    cub=XeMay(50,"Cub","Nhat")
    dream=XeMay(100,"Dream","Thai Lan")
    wave=XeMay(100,"Wave","Trung Quoc")
    print(cub.outputXeMay())
    print(dream.outputXeMay())
    print(wave.outputXeMay())
if __name__=="__main__":
    main()