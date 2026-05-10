import base_types
import Header70
import ContentInformationType37
import NonFinancialRequestComponent5

class AcceptorNonFinancialRequestV05(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_SctyTrlr", "_NonFinReq"]
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

	@property
	def NonFinReq(self):
		return self._NonFinReq

	@NonFinReq.setter
	def NonFinReq(self, value):
		self._NonFinReq = value if type(value) != auto else self.make_default("NonFinReq")

	@NonFinReq.deleter
	def NonFinReq(self):
		del self._NonFinReq
		self._NonFinReq = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hdr', type=Header70, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonFinReq', type=NonFinancialRequestComponent5, min=1, max=1, mutex_group=None, array=False),
	))

