# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentQuantity18Choice

class ProceedsQuantityBreakdown1(base_types._BaseFieldType):

	__slots__ = ["_CshCompstnQty", "_TrfOfRcvdPrcdsQty"]
	@property
	def CshCompstnQty(self):
		return self._CshCompstnQty

	@CshCompstnQty.setter
	def CshCompstnQty(self, value):
		self._CshCompstnQty = value if value is not None else base_types.UninitialisedField(self, 'CshCompstnQty', FinancialInstrumentQuantity18Choice, False)

	@CshCompstnQty.deleter
	def CshCompstnQty(self):
		del self._CshCompstnQty
		self._CshCompstnQty = base_types.UninitialisedField(self, 'CshCompstnQty', FinancialInstrumentQuantity18Choice, False)

	@property
	def TrfOfRcvdPrcdsQty(self):
		return self._TrfOfRcvdPrcdsQty

	@TrfOfRcvdPrcdsQty.setter
	def TrfOfRcvdPrcdsQty(self, value):
		self._TrfOfRcvdPrcdsQty = value if value is not None else base_types.UninitialisedField(self, 'TrfOfRcvdPrcdsQty', FinancialInstrumentQuantity18Choice, False)

	@TrfOfRcvdPrcdsQty.deleter
	def TrfOfRcvdPrcdsQty(self):
		del self._TrfOfRcvdPrcdsQty
		self._TrfOfRcvdPrcdsQty = base_types.UninitialisedField(self, 'TrfOfRcvdPrcdsQty', FinancialInstrumentQuantity18Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshCompstnQty', type=FinancialInstrumentQuantity18Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfOfRcvdPrcdsQty', type=FinancialInstrumentQuantity18Choice, min=0, max=1, mutex_group=None, array=False),
	))