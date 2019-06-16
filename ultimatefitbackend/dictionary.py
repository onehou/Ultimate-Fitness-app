# -*- coding: utf-8 -*- 
import json

def dictionary_translation():
	dict_trans = {
		'lbl_gallery': {
			'vn': 'Ảnh',
			'en': 'gallery'
		},
		'lbl_ADD_TO_CART': {
			'vn': 'THÊM VÀO GIỎ',
			'en': 'ADD TO CART'
		},
		'watermelon': {
			'vn': 'dưa hấu',
			'en': 'watermelon'
		},
		'lbl_Home': {
			'vn': 'Trang Chủ',
			'en': 'Home'
		},
		'lbl_About_us': {
			'vn': 'Giới thiệu',
			'en': 'About us'
		},
		'lbl_Shop': {
			'vn': 'cửa hàng',
			'en': 'Shop'
		},
		'lbl_Shop_By_Calendar': {
			'vn': 'Lịch Đặt Hàng',
			'en': 'Shop By Calendar'
		},
		'lbl_Contact_us': {
			'vn': 'Liên Hệ',
			'en': 'Contact us'
		},
		'lbl_My_Cart': {
			'vn': 'Giỏ Hàng',
			'en': 'My Cart'
		},
		'lbl_Account_Info': {
			'vn': 'Thông Tin Tài Khoản',
			'en': 'Account Info'
		},
		'lbl_Address_Book': {
			'vn': 'Địa Chỉ Giao Hàng',
			'en': 'Address Book'
		},
		'lbl_Orders_History': {
			'vn': 'Lịch Sử Giao Hàng',
			'en': 'Orders History'
		},
		'lbl_Log_Out': {
			'vn': 'Đăng Xuất',
			'en': 'Log Out'
		},
		'lbl_Sign_In': {
			'vn': 'Đăng Nhập',
			'en': 'Sign In'
		},
		'lbl_Register_Here': {
			'vn': 'Đăng Ký',
			'en': 'Register Here'
		},
		'lbl_Total': {
			'vn': 'Tổng',
			'en': 'Total'
		},
		'FEATURED PRODUCTS': {
			'vn': 'SAN PHAM TIEU BIEU',
			'en': 'FEATURED PRODUCTS'
		},
		'Chicken Wing': {
			'vn': 'Cánh Gà',
			'en': 'Chicken Wing'
		},
		"Steak": {
			'vn': 'Bít Tết',
			'en': 'Steak'
		}
	}

	return json.dumps(dict_trans, ensure_ascii=False).decode('utf8')