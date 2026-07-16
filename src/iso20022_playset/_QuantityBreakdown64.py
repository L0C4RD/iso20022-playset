# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentQuantity36Choice
from . import GenericIdentification39

class QuantityBreakdown64(base_types._BaseFieldType):

	__slots__ = ["_LotNb", "_LotQty"]
	@property
	def LotNb(self):
		return self._LotNb

	@LotNb.setter
	def LotNb(self, value):
		self._LotNb = value if value is not None else base_types.UninitialisedField(self, 'LotNb', GenericIdentification39, False)

	@LotNb.deleter
	def LotNb(self):
		del self._LotNb
		self._LotNb = base_types.UninitialisedField(self, 'LotNb', GenericIdentification39, False)

	@property
	def LotQty(self):
		return self._LotQty

	@LotQty.setter
	def LotQty(self, value):
		self._LotQty = value if value is not None else base_types.UninitialisedField(self, 'LotQty', FinancialInstrumentQuantity36Choice, False)

	@LotQty.deleter
	def LotQty(self):
		del self._LotQty
		self._LotQty = base_types.UninitialisedField(self, 'LotQty', FinancialInstrumentQuantity36Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LotNb', type=GenericIdentification39, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LotQty', type=FinancialInstrumentQuantity36Choice, min=0, max=1, mutex_group=None, array=False),
	))