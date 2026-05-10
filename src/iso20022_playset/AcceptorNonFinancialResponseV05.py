from . import base_types
import NonFinancialResponseComponent5
import ContentInformationType37
import Header70

class AcceptorNonFinancialResponseV05(base_types._BaseFieldType):

	__slots__ = ["_NonFinRspn", "_SctyTrlr", "_Hdr"]
	@property
	def NonFinRspn(self):
		return self._NonFinRspn

	@NonFinRspn.setter
	def NonFinRspn(self, value):
		self._NonFinRspn = value if type(value) != auto else self.make_default("NonFinRspn")

	@NonFinRspn.deleter
	def NonFinRspn(self):
		del self._NonFinRspn
		self._NonFinRspn = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='NonFinRspn', type=NonFinancialResponseComponent5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header70, min=1, max=1, mutex_group=None, array=False),
	))

