# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ImpliedCurrencyAndAmount
from . import YesNoIndicator

class AmountRangeBoundary1(base_types._BaseFieldType):

	__slots__ = ["_BdryAmt", "_Incl"]
	@property
	def BdryAmt(self):
		return self._BdryAmt

	@BdryAmt.setter
	def BdryAmt(self, value):
		self._BdryAmt = value if value is not None else base_types.UninitialisedField(self, 'BdryAmt', ImpliedCurrencyAndAmount, False)

	@BdryAmt.deleter
	def BdryAmt(self):
		del self._BdryAmt
		self._BdryAmt = base_types.UninitialisedField(self, 'BdryAmt', ImpliedCurrencyAndAmount, False)

	@property
	def Incl(self):
		return self._Incl

	@Incl.setter
	def Incl(self, value):
		self._Incl = value if value is not None else base_types.UninitialisedField(self, 'Incl', YesNoIndicator, False)

	@Incl.deleter
	def Incl(self):
		del self._Incl
		self._Incl = base_types.UninitialisedField(self, 'Incl', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BdryAmt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Incl', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))