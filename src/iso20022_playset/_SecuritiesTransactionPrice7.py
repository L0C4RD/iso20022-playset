# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection61
from . import DigitalTokenAmount2

class SecuritiesTransactionPrice7(base_types._BaseFieldType):

	__slots__ = ["_DgtlTknQty", "_MntryVal"]
	@property
	def DgtlTknQty(self):
		return self._DgtlTknQty

	@DgtlTknQty.setter
	def DgtlTknQty(self, value):
		self._DgtlTknQty = value if value is not None else base_types.UninitialisedField(self, 'DgtlTknQty', DigitalTokenAmount2, False)

	@DgtlTknQty.deleter
	def DgtlTknQty(self):
		del self._DgtlTknQty
		self._DgtlTknQty = base_types.UninitialisedField(self, 'DgtlTknQty', DigitalTokenAmount2, False)

	@property
	def MntryVal(self):
		return self._MntryVal

	@MntryVal.setter
	def MntryVal(self, value):
		self._MntryVal = value if value is not None else base_types.UninitialisedField(self, 'MntryVal', AmountAndDirection61, False)

	@MntryVal.deleter
	def MntryVal(self):
		del self._MntryVal
		self._MntryVal = base_types.UninitialisedField(self, 'MntryVal', AmountAndDirection61, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlTknQty', type=DigitalTokenAmount2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MntryVal', type=AmountAndDirection61, min=1, max=1, mutex_group=None, array=False),
	))