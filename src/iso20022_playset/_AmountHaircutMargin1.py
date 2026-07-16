# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection53
from . import PercentageRate

class AmountHaircutMargin1(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_HrcutOrMrgn"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', AmountAndDirection53, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', AmountAndDirection53, False)

	@property
	def HrcutOrMrgn(self):
		return self._HrcutOrMrgn

	@HrcutOrMrgn.setter
	def HrcutOrMrgn(self, value):
		self._HrcutOrMrgn = value if value is not None else base_types.UninitialisedField(self, 'HrcutOrMrgn', PercentageRate, False)

	@HrcutOrMrgn.deleter
	def HrcutOrMrgn(self):
		del self._HrcutOrMrgn
		self._HrcutOrMrgn = base_types.UninitialisedField(self, 'HrcutOrMrgn', PercentageRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=AmountAndDirection53, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HrcutOrMrgn', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
	))