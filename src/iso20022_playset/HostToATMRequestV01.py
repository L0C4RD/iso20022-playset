import base_types
import HostToATMRequest1
import Header20
import ContentInformationType15
import ContentInformationType10

class HostToATMRequestV01(base_types._BaseFieldType):

	__slots__ = ["_PrtctdHstToATMReq", "_SctyTrlr", "_Hdr", "_HstToATMReq"]
	@property
	def PrtctdHstToATMReq(self):
		return self._PrtctdHstToATMReq

	@PrtctdHstToATMReq.setter
	def PrtctdHstToATMReq(self, value):
		self._PrtctdHstToATMReq = value if type(value) != auto else self.make_default("PrtctdHstToATMReq")

	@PrtctdHstToATMReq.deleter
	def PrtctdHstToATMReq(self):
		del self._PrtctdHstToATMReq
		self._PrtctdHstToATMReq = None

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
	def HstToATMReq(self):
		return self._HstToATMReq

	@HstToATMReq.setter
	def HstToATMReq(self, value):
		self._HstToATMReq = value if type(value) != auto else self.make_default("HstToATMReq")

	@HstToATMReq.deleter
	def HstToATMReq(self):
		del self._HstToATMReq
		self._HstToATMReq = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtctdHstToATMReq', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstToATMReq', type=HostToATMRequest1, min=0, max=1, mutex_group=None, array=False),
	))

