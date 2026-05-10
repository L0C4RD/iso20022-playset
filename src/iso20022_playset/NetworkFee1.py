from . import base_types
from .SecurityIdentification19 import SecurityIdentification19
from .Max30DecimalNumber import Max30DecimalNumber

class NetworkFee1(base_types._BaseFieldType):

	__slots__ = ["_NtwkFeeQty", "_FinInstrmId"]
	@property
	def NtwkFeeQty(self):
		return self._NtwkFeeQty

	@NtwkFeeQty.setter
	def NtwkFeeQty(self, value):
		self._NtwkFeeQty = value if type(value) != auto else self.make_default("NtwkFeeQty")

	@NtwkFeeQty.deleter
	def NtwkFeeQty(self):
		del self._NtwkFeeQty
		self._NtwkFeeQty = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NtwkFeeQty', type=Max30DecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
	))

