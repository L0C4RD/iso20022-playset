# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentQuantity33Choice
from . import Quantity52Choice

class SecuritiesOption79(base_types._BaseFieldType):

	__slots__ = ["_AddtlRndUpQty", "_CondlQty", "_InstdQty"]
	@property
	def AddtlRndUpQty(self):
		return self._AddtlRndUpQty

	@AddtlRndUpQty.setter
	def AddtlRndUpQty(self, value):
		self._AddtlRndUpQty = value if value is not None else base_types.UninitialisedField(self, 'AddtlRndUpQty', FinancialInstrumentQuantity33Choice, False)

	@AddtlRndUpQty.deleter
	def AddtlRndUpQty(self):
		del self._AddtlRndUpQty
		self._AddtlRndUpQty = base_types.UninitialisedField(self, 'AddtlRndUpQty', FinancialInstrumentQuantity33Choice, False)

	@property
	def CondlQty(self):
		return self._CondlQty

	@CondlQty.setter
	def CondlQty(self, value):
		self._CondlQty = value if value is not None else base_types.UninitialisedField(self, 'CondlQty', FinancialInstrumentQuantity33Choice, False)

	@CondlQty.deleter
	def CondlQty(self):
		del self._CondlQty
		self._CondlQty = base_types.UninitialisedField(self, 'CondlQty', FinancialInstrumentQuantity33Choice, False)

	@property
	def InstdQty(self):
		return self._InstdQty

	@InstdQty.setter
	def InstdQty(self, value):
		self._InstdQty = value if value is not None else base_types.UninitialisedField(self, 'InstdQty', Quantity52Choice, False)

	@InstdQty.deleter
	def InstdQty(self):
		del self._InstdQty
		self._InstdQty = base_types.UninitialisedField(self, 'InstdQty', Quantity52Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlRndUpQty', type=FinancialInstrumentQuantity33Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CondlQty', type=FinancialInstrumentQuantity33Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdQty', type=Quantity52Choice, min=1, max=1, mutex_group=None, array=False),
	))