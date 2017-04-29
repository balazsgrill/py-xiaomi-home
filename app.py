from mihome.base import XiaomiConnection
from mihome.gateway import Gateway

conn = XiaomiConnection()
gateway_data = conn.whois()

gateway = Gateway(
	connection=conn,
	sid=gateway_data['sid'],
	ip=gateway_data['ip'],
	port=gateway_data['port']
)
gateway.register_subdevices()


def switch_cb(item):
	# publish to mqtt / kafka / redis
	print item



for switch in gateway.connected_devices['motion']:
	switch.listen(callback=switch_cb)
