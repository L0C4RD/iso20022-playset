# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PercentageRate

class AdditionalProductInformation3(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmTxCostsExAnteUK", "_FinInstrmTxCostsExPstUK"]
	@property
	def FinInstrmTxCostsExAnteUK(self):
		return self._FinInstrmTxCostsExAnteUK

	@FinInstrmTxCostsExAnteUK.setter
	def FinInstrmTxCostsExAnteUK(self, value):
		self._FinInstrmTxCostsExAnteUK = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmTxCostsExAnteUK', PercentageRate, False)

	@FinInstrmTxCostsExAnteUK.deleter
	def FinInstrmTxCostsExAnteUK(self):
		del self._FinInstrmTxCostsExAnteUK
		self._FinInstrmTxCostsExAnteUK = base_types.UninitialisedField(self, 'FinInstrmTxCostsExAnteUK', PercentageRate, False)

	@property
	def FinInstrmTxCostsExPstUK(self):
		return self._FinInstrmTxCostsExPstUK

	@FinInstrmTxCostsExPstUK.setter
	def FinInstrmTxCostsExPstUK(self, value):
		self._FinInstrmTxCostsExPstUK = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmTxCostsExPstUK', PercentageRate, False)

	@FinInstrmTxCostsExPstUK.deleter
	def FinInstrmTxCostsExPstUK(self):
		del self._FinInstrmTxCostsExPstUK
		self._FinInstrmTxCostsExPstUK = base_types.UninitialisedField(self, 'FinInstrmTxCostsExPstUK', PercentageRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FinInstrmTxCostsExAnteUK', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmTxCostsExPstUK', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
	))