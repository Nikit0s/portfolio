class SetRemoteAddrFromForwardedFor(object):
	def process_request(self, requset):
		try:
			real_ip = requset.META['HTTP_X_FORWARDED_FOR']
		except KeyError:
			pass
		else:
			real_ip = real_ip.split(',')[0]
			requset.META['REMOTE_ADDR'] = real_ip