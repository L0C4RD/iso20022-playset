from . import base_types
from .PercentageRate import PercentageRate

class AdditionalProductInformation3(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmTxCostsExPstUK", "_FinInstrmTxCostsExAnteUK"]
	@property
	def FinInstrmTxCostsExPstUK(self):
		return self._FinInstrmTxCostsExPstUK

	@FinInstrmTxCostsExPstUK.setter
	def FinInstrmTxCostsExPstUK(self, value):
		self._FinInstrmTxCostsExPstUK = value if type(value) != base_types.auto else self.make_default("FinInstrmTxCostsExPstUK")

	@FinInstrmTxCostsExPstUK.deleter
	def FinInstrmTxCostsExPstUK(self):
		del self._FinInstrmTxCostsExPstUK
		self._FinInstrmTxCostsExPstUK = None

	@property
	def FinInstrmTxCostsExAnteUK(self):
		return self._FinInstrmTxCostsExAnteUK

	@FinInstrmTxCostsExAnteUK.setter
	def FinInstrmTxCostsExAnteUK(self, value):
		self._FinInstrmTxCostsExAnteUK = value if type(value) != base_types.auto else self.make_default("FinInstrmTxCostsExAnteUK")

	@FinInstrmTxCostsExAnteUK.deleter
	def FinInstrmTxCostsExAnteUK(self):
		del self._FinInstrmTxCostsExAnteUK
		self._FinInstrmTxCostsExAnteUK = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FinInstrmTxCostsExPstUK', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmTxCostsExAnteUK', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
	))

