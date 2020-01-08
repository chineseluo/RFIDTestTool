#!/usr/bin/python3
from curio import run, sleep, TaskGroup, spawn
from curio.socket import *
from base.data_form_nb import CurrentDataFrame
import click



@click.command()
@click.option('--label-type', default = 0, help='0: current label, 1: asset label')
@click.option('--shop-id', required = True, type = int, help='shopId')
@click.option('--module-id-range', nargs = 2, default = (1, 5), help='module id min and max value')
@click.option('--tmn-sn-range', nargs = 2, default = (1, 100), help='tmn sn min and max value')
@click.option('--current-value-range', nargs = 2, default = (0, 100), help='current min and max value')
@click.option('--status', default = [0], multiple = True, type = int, help='status value, multiple')
@click.option('--ip', required = True, type = str, help='ip')
@click.option('--port', default = 4005, type = int, help='port')
@click.option('--send-interval', default = 10, type = int, help='send interval')
@click.option('--monitor-interval', default = 10, type = int, help='monitor interval')
def cli(label_type, shop_id, module_id_range, tmn_sn_range, current_value_range, status, ip, port, send_interval, monitor_interval):
	run(main(label_type, shop_id, module_id_range, tmn_sn_range, current_value_range, status, ip, port, send_interval, monitor_interval))


async def main(label_type, shop_id, module_id_range, tmn_sn_range, current_value_range, status_tuple, ip, port, send_interval, monitor_interval):
	print("label_type: {}, shop_id: {}, module_id_min: {}, module_id_max: {}, tmn_sn_min: {}, tmn_sn_max: {}, current_value_min: {}, current_value_max: {}, status_tuple: {}, ip: {}, port: {}, send_interval: {}, monitor_interval: {}".format(
	label_type,
 	shop_id, 
	module_id_range[0], 
	module_id_range[1], 
	tmn_sn_range[0], 
	tmn_sn_range[1], 
	current_value_range[0], 
	current_value_range[1], 
	status_tuple,
	ip,
	port,
	send_interval,
	monitor_interval))

	data_frame = CurrentDataFrame(
			data_type=label_type, 
			shop_id=shop_id, 
			module_id_min=module_id_range[0], 
			module_id_max=module_id_range[1], 
			current_value_min=current_value_range[0], 
			current_value_max=current_value_range[1], 
			tmn_sn_min=tmn_sn_range[0], 
			tmn_sn_max=tmn_sn_range[1], 
			status_tuple=status_tuple)

	tg = TaskGroup()
	counters = [0 for _ in range(0, len(data_frame.to_hex_str_list()))]
	print("tmn count:", len(counters))
	monitor_task = await spawn(monitor, counters, monitor_interval)
	for i, msg in enumerate(data_frame.to_hex_str_list()):
		await tg.spawn(task, i, msg, ip, port, send_interval, counters)
	await monitor_task.join()
	#await tg.join()
	

async def task(idx, msg, ip, port, send_interval, counters):
	sock = socket(AF_INET, SOCK_DGRAM)
	await sock.connect((ip, port))
	count = 0
	async with sock:
		while True:
			await sock.sendall(bytes.fromhex(msg))
			count += 1
			counters[idx] = count
			await sleep(send_interval)


async def monitor(counters, interval):
	while True:
		total_count = 0
		for count in counters:
			total_count += count
		print("packets sent count:", total_count)
		await sleep(interval)


if __name__ == '__main__':
	cli()
