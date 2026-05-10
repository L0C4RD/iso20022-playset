from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._Max210Text import Max210Text
from ._Max35Text import Max35Text

class Amount1(base_types._BaseFieldType):

	__slots__ = ["_MrgnCallReqId", "_AgrdAmt", "_AddtlInf"]
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
	def AgrdAmt(self):
		return self._AgrdAmt

	@AgrdAmt.setter
	def AgrdAmt(self, value):
		self._AgrdAmt = value if type(value) != base_types.auto else self.make_default("AgrdAmt")

	@AgrdAmt.deleter
	def AgrdAmt(self):
		del self._AgrdAmt
		self._AgrdAmt = None

	@property
	def MrgnCallReqId(self):
		return self._MrgnCallReqId

	@MrgnCallReqId.setter
	def MrgnCallReqId(self, value):
		self._MrgnCallReqId = value if type(value) != base_types.auto else self.make_default("MrgnCallReqId")

	@MrgnCallReqId.deleter
	def MrgnCallReqId(self):
		del self._MrgnCallReqId
		self._MrgnCallReqId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max210Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgrdAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnCallReqId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

