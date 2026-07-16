# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ImpliedCurrencyAndAmount
from . import Number

class ATMMediaMix1(base_types._BaseFieldType):

	__slots__ = ["_CshUnitNb", "_Nb", "_UnitVal"]
	@property
	def CshUnitNb(self):
		return self._CshUnitNb

	@CshUnitNb.setter
	def CshUnitNb(self, value):
		self._CshUnitNb = value if value is not None else base_types.UninitialisedField(self, 'CshUnitNb', Number, False)

	@CshUnitNb.deleter
	def CshUnitNb(self):
		del self._CshUnitNb
		self._CshUnitNb = base_types.UninitialisedField(self, 'CshUnitNb', Number, False)

	@property
	def Nb(self):
		return self._Nb

	@Nb.setter
	def Nb(self, value):
		self._Nb = value if value is not None else base_types.UninitialisedField(self, 'Nb', Number, False)

	@Nb.deleter
	def Nb(self):
		del self._Nb
		self._Nb = base_types.UninitialisedField(self, 'Nb', Number, False)

	@property
	def UnitVal(self):
		return self._UnitVal

	@UnitVal.setter
	def UnitVal(self, value):
		self._UnitVal = value if value is not None else base_types.UninitialisedField(self, 'UnitVal', ImpliedCurrencyAndAmount, False)

	@UnitVal.deleter
	def UnitVal(self):
		del self._UnitVal
		self._UnitVal = base_types.UninitialisedField(self, 'UnitVal', ImpliedCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshUnitNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nb', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitVal', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))