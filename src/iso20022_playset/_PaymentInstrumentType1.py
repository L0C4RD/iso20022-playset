from . import base_types
from ._Max500Text import Max500Text
from ._Min8Max28NumericText import Min8Max28NumericText
from ._AuthorityRequestType1 import AuthorityRequestType1

class PaymentInstrumentType1(base_types._BaseFieldType):

	__slots__ = ["_CardNb", "_AuthrtyReqTp", "_AddtlInf"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def AuthrtyReqTp(self):
		return self._AuthrtyReqTp

	@AuthrtyReqTp.setter
	def AuthrtyReqTp(self, value):
		self._AuthrtyReqTp = value if type(value) != base_types.auto else self.make_default("AuthrtyReqTp")

	@AuthrtyReqTp.deleter
	def AuthrtyReqTp(self):
		del self._AuthrtyReqTp
		self._AuthrtyReqTp = None

	@property
	def CardNb(self):
		return self._CardNb

	@CardNb.setter
	def CardNb(self, value):
		self._CardNb = value if type(value) != base_types.auto else self.make_default("CardNb")

	@CardNb.deleter
	def CardNb(self):
		del self._CardNb
		self._CardNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthrtyReqTp', type=AuthorityRequestType1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CardNb', type=Min8Max28NumericText, min=1, max=1, mutex_group=None, array=False),
	))

