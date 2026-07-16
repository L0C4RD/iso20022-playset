# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdjustmentDirection1Code
from . import AdjustmentType1Choice
from . import AmountOrPercentage2Choice

class Adjustment7(base_types._BaseFieldType):

	__slots__ = ["_AmtOrPctg", "_Drctn", "_Tp"]
	@property
	def AmtOrPctg(self):
		return self._AmtOrPctg

	@AmtOrPctg.setter
	def AmtOrPctg(self, value):
		self._AmtOrPctg = value if value is not None else base_types.UninitialisedField(self, 'AmtOrPctg', AmountOrPercentage2Choice, False)

	@AmtOrPctg.deleter
	def AmtOrPctg(self):
		del self._AmtOrPctg
		self._AmtOrPctg = base_types.UninitialisedField(self, 'AmtOrPctg', AmountOrPercentage2Choice, False)

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
		base_types.FieldEntry(name='AmtOrPctg', type=AmountOrPercentage2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Drctn', type=AdjustmentDirection1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=AdjustmentType1Choice, min=1, max=1, mutex_group=None, array=False),
	))