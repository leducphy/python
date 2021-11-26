def tiemBanh(tenTiemBanh, *danhSachBanh):
    print("Tiem banh "+ tenTiemBanh)
    for banh in danhSachBanh:
        print("-" + banh )

tiemBanh(" Phi Le ", 'banh quy', 'banh trung', 'banh ran')