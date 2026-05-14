# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyAnd24Amount import ActiveCurrencyAnd24Amount
from ._FinancialInstrument104 import FinancialInstrument104

class SpecificCollateral3(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmId", "_MktVal"]
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

	@property
	def MktVal(self):
		return self._MktVal

	@MktVal.setter
	def MktVal(self, value):
		self._MktVal = value if type(value) != base_types.auto else self.make_default("MktVal")

	@MktVal.deleter
	def MktVal(self):
		del self._MktVal
		self._MktVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FinInstrmId', type=FinancialInstrument104, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktVal', type=ActiveCurrencyAnd24Amount, min=1, max=1, mutex_group=None, array=False),
	))