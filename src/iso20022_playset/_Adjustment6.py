# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdjustmentDirection1Code
from . import AdjustmentType1Choice
from . import CurrencyAndAmount

class Adjustment6(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Drctn", "_Tp"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', CurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', CurrencyAndAmount, False)

	@property
	def Drctn(self):
		return self._Drctn

	@Drctn.setter
	def Drctn(self, value):
		self._Drctn = value if value is not None else base_types.UninitialisedField(self, 'Drctn', AdjustmentDirection1Code, False)

	@Drctn.deleter
	def Drctn(self):
		del self._Drctn
		self._Drctn = base_types.UninitialisedField(self, 'Drctn', AdjustmentDirection1Code, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', AdjustmentType1Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', AdjustmentType1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Drctn', type=AdjustmentDirection1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=AdjustmentType1Choice, min=1, max=1, mutex_group=None, array=False),
	))