#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/5/5
# @Author: zhouzihan

import random
import asyncio


# list_of_list: [[..], [..]]
def join_list(list_of_list):
	list = []
	for item in list_of_list:
		list.extend(item)
	return list

# [..], [..], ..
def join_list_arg(*argv):
	list = []
	for item in argv:
		list.extend(item)
	return list
		
def num_to_hex_str(byte):
	return "{:0>2x}".format(byte)
	
def bytes_to_hex_str(bytes):
	return "".join(map(num_to_hex_str, bytes))
	
def hex_str_to_bytes_fixed_length(hex_str, fixed_length):
	hex_str = data_hex_str_fixed_length(hex_str, fixed_length)
	l = []
	count = 2
	while len(hex_str) > count:
		part = int(hex_str[-count:], 16)
		hex_str = hex_str[:-count]
		l.insert(0, part)
	if len(hex_str) > 0:
		l.insert(0, int(data_hex_str_fixed_length(hex_str, 1), 16))
	return l

def num_to_bytes(num, fixed_length):
	return hex_str_to_bytes_fixed_length(num_to_hex_str(num), fixed_length)

# ("aa", 4) -> "000000aa"
def data_hex_str_fixed_length(data_hex_str, fixed_length):
	padding_zero_count = fixed_length * 2 - len(data_hex_str)
	if padding_zero_count <= 0:
		return data_hex_str
	padding_zero_str = "".join(["0" for _ in range(0, padding_zero_count)])
	return padding_zero_str + data_hex_str


class CurrentDataFrame:

	static_header = [
		0x63, 
		0x22, 0x83, 
		0x14, 
		0x32, 0x31, 0x39, 0x38, 0x30, 0x31, 0x41, 0x30, 0x57, 0x4c, 0x39, 0x31, 0x37, 0x41, 0x51, 0x30, 0x30, 0x30, 0x35, 0x36,
		0x14,
		0x32, 0x31, 0x39, 0x38, 0x30, 0x31, 0x41, 0x30, 0x57, 0x4c, 0x39, 0x31, 0x37, 0x41, 0x51, 0x30, 0x30, 0x30, 0x35, 0x36
	]
	shop_id_field = [0x02, 0x03]
	crc_field = [0x33, 0x06]

	def __init__(self, data_type, shop_id, module_id_min = 0, module_id_max = 5, current_value_min = 0, current_value_max = 100, tmn_sn_min = 1, tmn_sn_max = 10, status_tuple= (0,)):
		self.shop_id = shop_id
		if data_type == 0:
			self.data_gen = CurrentDataGen(shop_id, module_id_min, module_id_max, current_value_min, current_value_max, tmn_sn_min, tmn_sn_max, status_tuple)
		else:
			self.data_gen = AssetDataGen(shop_id, module_id_min, module_id_max, tmn_sn_min, tmn_sn_max, status_tuple)
		self.gen()

	def gen(self):
		biz_data_list = self.data_gen.gen_biz_data()
		self.all_bytes_hex_str_list = []
		for biz_data in biz_data_list:
			biz_data_array = [biz_data]
			self.biz_data_array_len_field = [len(biz_data_array)]

			shop_id_byte_array = num_to_bytes(self.shop_id, 3)

			self.all_byte_array = join_list_arg(
    	    			self.static_header, 
				self.biz_data_array_len_field, 
				self.shop_id_field,
				shop_id_byte_array, 
				join_list(biz_data_array), 
				self.crc_field)
			self.all_bytes_hex_str_list.append(bytes_to_hex_str(self.all_byte_array))

	def to_hex_str_list(self):
		return self.all_bytes_hex_str_list

class AssetDataGen():
	TMN_SN_FIELD_LEN = 4
	HEADER_FIELD = [0x10, 0x65, 0x81, 0x01, 0xb0, 0x00]	
	TYPE_FIELD = [0x20]
	CHECK_SUM_FIELD = [0x00]
	RESERVE_FIELD = [0x00, 0x00]
	VERSION_FIELD = [0x10]
	OTHER_FIELD = [0x36]

	def __init__(self, shop_id, module_id_min = 0, module_id_max = 5, tmn_sn_min = 1, tmn_sn_max = 10, status_tuple = (0,)):
		self.shop_id = shop_id
		self.module_id_min = module_id_min
		self.module_id_max = module_id_max
		self.tmn_sn_min = tmn_sn_min
		self.tmn_sn_max = tmn_sn_max
		self.current_tmn_sn = tmn_sn_min
		self.status_tuple = status_tuple
		self.tmn_sn_generator = self.gen_tmn_sn()

	def gen_tmn_sn_list(self):
		list = []
		for tmn_sn in range(self.tmn_sn_min, self.tmn_sn_max):
			tmn_sn_hex_str = data_hex_str_fixed_length(str(hex(tmn_sn))[2:], self.TMN_SN_FIELD_LEN)
			list.append(tmn_sn_hex_str)
		return list
	
	def gen_tmn_sn(self):
		while self.current_tmn_sn <= self.tmn_sn_max:
			yield self.current_tmn_sn
			self.current_tmn_sn += 1
		
	def gen_current_value(self):
		return random.randint(self.current_value_min, self.current_value_max)

	def gen_module_id(self):
		return random.randint(self.module_id_min, self.module_id_max)

	def gen_status(self):
		return self.status_tuple[random.randint(0, len(self.status_tuple)) - 1]

	def gen_biz_data(self):
		for tmn_sn in self.tmn_sn_generator:
			biz_data = join_list_arg(
				num_to_bytes(self.gen_module_id(), 1), 
				self.HEADER_FIELD, 
				self.TYPE_FIELD, 
				num_to_bytes(tmn_sn, 4),
				self.CHECK_SUM_FIELD, 
				self.RESERVE_FIELD,
				num_to_bytes(self.gen_status(), 1), 
				self.VERSION_FIELD, 
				self.OTHER_FIELD)
			yield biz_data

class CurrentDataGen():
	TMN_SN_FIELD_LEN = 4
	HEADER_FIELD = [0x10, 0x65, 0x81, 0x01, 0xb0, 0x00]	
	TYPE_FIELD = [0x21]
	CHECK_SUM_FIELD = [0x00]
	VERSION_FIELD = [0x10]
	OTHER_FIELD = [0x36]

	def __init__(self, shop_id, module_id_min = 0, module_id_max = 5, current_value_min = 0, current_value_max = 100, tmn_sn_min = 1, tmn_sn_max = 10, status_tuple = (0,)):
		self.shop_id = shop_id
		self.module_id_min = module_id_min
		self.module_id_max = module_id_max
		self.current_value_min = current_value_min
		self.current_value_max = current_value_max
		self.tmn_sn_min = tmn_sn_min
		self.tmn_sn_max = tmn_sn_max
		self.current_tmn_sn = tmn_sn_min
		self.status_tuple = status_tuple
		self.tmn_sn_generator = self.gen_tmn_sn()

	def gen_tmn_sn_list(self):
		list = []
		for tmn_sn in range(self.tmn_sn_min, self.tmn_sn_max):
			tmn_sn_hex_str = data_hex_str_fixed_length(str(hex(tmn_sn))[2:], self.TMN_SN_FIELD_LEN)
			list.append(tmn_sn_hex_str)
		return list
	
	def gen_tmn_sn(self):
		while self.current_tmn_sn <= self.tmn_sn_max:
			yield self.current_tmn_sn
			self.current_tmn_sn += 1
		
	def gen_current_value(self):
		return random.randint(self.current_value_min, self.current_value_max)

	def gen_module_id(self):
		return random.randint(self.module_id_min, self.module_id_max)

	def gen_status(self):
		return self.status_tuple[random.randint(0, len(self.status_tuple)) - 1]

	def gen_biz_data(self):
		for tmn_sn in self.tmn_sn_generator:
			biz_data = join_list_arg(
				num_to_bytes(self.gen_module_id(), 1), 
				self.HEADER_FIELD, 
				self.TYPE_FIELD, 
				num_to_bytes(tmn_sn, 4),
				self.CHECK_SUM_FIELD, 
				num_to_bytes(self.gen_current_value(), 2), 
				num_to_bytes(self.gen_status(), 1), 
				self.VERSION_FIELD, 
				self.OTHER_FIELD)
			yield biz_data
