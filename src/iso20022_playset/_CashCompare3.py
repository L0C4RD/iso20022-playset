# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CompareAmountAndDirection2
from . import ComparePercentageRate3

class CashCompare3(base_types._BaseFieldType):

	__slots__ = ["_HrcutOrMrgn", "_Val"]
	@property
	def HrcutOrMrgn(self):
		return self._HrcutOrMrgn

	@HrcutOrMrgn.setter
	def HrcutOrMrgn(self, value):
		self._HrcutOrMrgn = value if value is not None else base_types.UninitialisedField(self, 'HrcutOrMrgn', ComparePercentageRate3, False)

	@HrcutOrMrgn.deleter
	def HrcutOrMrgn(self):
		del self._HrcutOrMrgn
		self._HrcutOrMrgn = base_types.UninitialisedField(self, 'HrcutOrMrgn', ComparePercentageRate3, False)

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if value is not None else base_types.UninitialisedField(self, 'Val', CompareAmountAndDirection2, False)

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = base_types.UninitialisedField(self, 'Val', CompareAmountAndDirection2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='HrcutOrMrgn', type=ComparePercentageRate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=CompareAmountAndDirection2, min=0, max=1, mutex_group=None, array=False),
	))