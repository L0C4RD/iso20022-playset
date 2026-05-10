import base_types
import ContentInformationType38
import DeviceRequest8
import Header41

class SaleToPOIDeviceRequestV07(base_types._BaseFieldType):

	__slots__ = ["_DvcReq", "_Hdr", "_SctyTrlr"]
	@property
	def DvcReq(self):
		return self._DvcReq

	@DvcReq.setter
	def DvcReq(self, value):
		self._DvcReq = value if type(value) != auto else self.make_default("DvcReq")

	@DvcReq.deleter
	def DvcReq(self):
		del self._DvcReq
		self._DvcReq = None

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if type(value) != auto else self.make_default("SctyTrlr")

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DvcReq', type=DeviceRequest8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header41, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType38, min=0, max=1, mutex_group=None, array=False),
	))

