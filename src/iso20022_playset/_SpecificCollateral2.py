from . import base_types
from ._FinancialInstrument59 import FinancialInstrument59

class SpecificCollateral2(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmId"]
	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != base_types.auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FinInstrmId', type=FinancialInstrument59, min=1, max=1, mutex_group=None, array=False),
	))

