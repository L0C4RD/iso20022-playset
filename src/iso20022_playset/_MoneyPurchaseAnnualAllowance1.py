# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import YesNoIndicator

class MoneyPurchaseAnnualAllowance1(base_types._BaseFieldType):

	__slots__ = ["_Trggrd", "_TrggrdDt"]
	@property
	def Trggrd(self):
		return self._Trggrd

	@Trggrd.setter
	def Trggrd(self, value):
		self._Trggrd = value if value is not None else base_types.UninitialisedField(self, 'Trggrd', YesNoIndicator, False)

	@Trggrd.deleter
	def Trggrd(self):
		del self._Trggrd
		self._Trggrd = base_types.UninitialisedField(self, 'Trggrd', YesNoIndicator, False)

	@property
	def TrggrdDt(self):
		return self._TrggrdDt

	@TrggrdDt.setter
	def TrggrdDt(self, value):
		self._TrggrdDt = value if value is not None else base_types.UninitialisedField(self, 'TrggrdDt', ISODate, False)

	@TrggrdDt.deleter
	def TrggrdDt(self):
		del self._TrggrdDt
		self._TrggrdDt = base_types.UninitialisedField(self, 'TrggrdDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Trggrd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrggrdDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))