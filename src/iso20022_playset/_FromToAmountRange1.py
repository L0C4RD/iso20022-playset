# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountRangeBoundary1

class FromToAmountRange1(base_types._BaseFieldType):

	__slots__ = ["_FrAmt", "_ToAmt"]
	@property
	def FrAmt(self):
		return self._FrAmt

	@FrAmt.setter
	def FrAmt(self, value):
		self._FrAmt = value if value is not None else base_types.UninitialisedField(self, 'FrAmt', AmountRangeBoundary1, False)

	@FrAmt.deleter
	def FrAmt(self):
		del self._FrAmt
		self._FrAmt = base_types.UninitialisedField(self, 'FrAmt', AmountRangeBoundary1, False)

	@property
	def ToAmt(self):
		return self._ToAmt

	@ToAmt.setter
	def ToAmt(self, value):
		self._ToAmt = value if value is not None else base_types.UninitialisedField(self, 'ToAmt', AmountRangeBoundary1, False)

	@ToAmt.deleter
	def ToAmt(self):
		del self._ToAmt
		self._ToAmt = base_types.UninitialisedField(self, 'ToAmt', AmountRangeBoundary1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrAmt', type=AmountRangeBoundary1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ToAmt', type=AmountRangeBoundary1, min=1, max=1, mutex_group=None, array=False),
	))