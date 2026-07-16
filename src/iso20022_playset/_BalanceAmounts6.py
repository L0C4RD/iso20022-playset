# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection14

class BalanceAmounts6(base_types._BaseFieldType):

	__slots__ = ["_BookVal", "_HldgVal", "_UrlsdGnLoss"]
	@property
	def BookVal(self):
		return self._BookVal

	@BookVal.setter
	def BookVal(self, value):
		self._BookVal = value if value is not None else base_types.UninitialisedField(self, 'BookVal', AmountAndDirection14, False)

	@BookVal.deleter
	def BookVal(self):
		del self._BookVal
		self._BookVal = base_types.UninitialisedField(self, 'BookVal', AmountAndDirection14, False)

	@property
	def HldgVal(self):
		return self._HldgVal

	@HldgVal.setter
	def HldgVal(self, value):
		self._HldgVal = value if value is not None else base_types.UninitialisedField(self, 'HldgVal', AmountAndDirection14, False)

	@HldgVal.deleter
	def HldgVal(self):
		del self._HldgVal
		self._HldgVal = base_types.UninitialisedField(self, 'HldgVal', AmountAndDirection14, False)

	@property
	def UrlsdGnLoss(self):
		return self._UrlsdGnLoss

	@UrlsdGnLoss.setter
	def UrlsdGnLoss(self, value):
		self._UrlsdGnLoss = value if value is not None else base_types.UninitialisedField(self, 'UrlsdGnLoss', AmountAndDirection14, False)

	@UrlsdGnLoss.deleter
	def UrlsdGnLoss(self):
		del self._UrlsdGnLoss
		self._UrlsdGnLoss = base_types.UninitialisedField(self, 'UrlsdGnLoss', AmountAndDirection14, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BookVal', type=AmountAndDirection14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldgVal', type=AmountAndDirection14, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UrlsdGnLoss', type=AmountAndDirection14, min=0, max=1, mutex_group=None, array=False),
	))