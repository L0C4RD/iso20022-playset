from . import base_types
import Max30DecimalNumber
import SecurityIdentification19

class NetworkFee1(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmId", "_NtwkFeeQty"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtwkFeeQty', type=Max30DecimalNumber, min=1, max=1, mutex_group=None, array=False),
	))

