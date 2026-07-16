# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountOrPercentage2Choice
from . import ChargesType1Choice

class ChargesDetails3(base_types._BaseFieldType):

	__slots__ = ["_AmtOrPctg", "_Tp"]
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
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', ChargesType1Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', ChargesType1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtOrPctg', type=AmountOrPercentage2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ChargesType1Choice, min=1, max=1, mutex_group=None, array=False),
	))