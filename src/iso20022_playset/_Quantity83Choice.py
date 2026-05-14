from . import base_types
from ._Max30DecimalNumber import Max30DecimalNumber

class Quantity83Choice(base_types._BaseFieldType):

	__slots__ = ["_ElctrncMnyTknSttlmQty", "_NtwkFeeQty"]
	@property
	def ElctrncMnyTknSttlmQty(self):
		return self._ElctrncMnyTknSttlmQty

	@ElctrncMnyTknSttlmQty.setter
	def ElctrncMnyTknSttlmQty(self, value):
		self._ElctrncMnyTknSttlmQty = value if type(value) != base_types.auto else self.make_default("ElctrncMnyTknSttlmQty")

	@ElctrncMnyTknSttlmQty.deleter
	def ElctrncMnyTknSttlmQty(self):
		del self._ElctrncMnyTknSttlmQty
		self._ElctrncMnyTknSttlmQty = None

	@property
	def NtwkFeeQty(self):
		return self._NtwkFeeQty

	@NtwkFeeQty.setter
	def NtwkFeeQty(self, value):
		self._NtwkFeeQty = value if type(value) != base_types.auto else self.make_default("NtwkFeeQty")

	@NtwkFeeQty.deleter
	def NtwkFeeQty(self):
		del self._NtwkFeeQty
		self._NtwkFeeQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ElctrncMnyTknSttlmQty', type=Max30DecimalNumber, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NtwkFeeQty', type=Max30DecimalNumber, min=0, max=1, mutex_group=1, array=False),
	))

