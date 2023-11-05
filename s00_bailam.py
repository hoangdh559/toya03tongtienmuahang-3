#region debai
"""
--- ma debai / id
tongtienmuahang(gia_truoc_thue)

--- nopbai
00 fork tu bainopmau tren replit tu trang web duoiday 
   https://replit.com/@NamG1/toya03tongtienmuahang

01 lam bai vao tep s00_bailam.py, chay Run de co ketqua tatca la 1
02a tao github repo, mo trinhduyetweb de kiemtra tep s00_bailam.py, va lay diachi/url aka githubbailamurl

02b dán diachi githubbailamurl theo mẫu ở trang web duoiday
    https://forms.gle/ruveoDbhxesSKBu77

--- debai / problem
Viết hàm 
  tongtienmuahang(gia_truoc_thue) 
tính tổng tiền sau thuế khi mua hàng với giá tiền :gia_truoc_thue
Tiền thuế = 10% tổng tiền
Kết quả số nguyên / int

--- vidu mau / testcase
Khi chay voi input                      | Ketqua output
--------------------------------------- | -----------------
tongtienmuahang(1000000)                | 1100000
tongtienmuahang(gia_truoc_thue=1000000) | 1100000
tongtienmuahang(None)                   | None
"""
#endregion debai

#region bailam
def tongtienmuahang(gia_truoc_thue):

  tien_thue = gia_truoc_thue * 0.1
  tien_thue = int(tien_thue)
  tong_tien = gia_truoc_thue + tien_thue
  return tong_tien


if __name__=='__main__':
  print( tongtienmuahang(1000000) )
  print( tongtienmuahang(gia_truoc_thue=1000000) )
  print( tongtienmuahang(None) )
#endregion bailam
