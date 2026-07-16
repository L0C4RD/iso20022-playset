# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountOrRate1Choice
from . import PlusOrMinusIndicator

class SpreadRate1(base_types._BaseFieldType):

	__slots__ = ["_RateOrAmt", "_Sgn"]
	@property
	def RateOrAmt(self):
		return self._RateOrAmt

	@RateOrAmt.setter
	def RateOrAmt(self, value):
		self._RateOrAmt = value if value is not None else base_types.UninitialisedField(self, 'RateOrAmt', AmountOrRate1Choice, False)

	@RateOrAmt.deleter
	def RateOrAmt(self):
		del self._RateOrAmt
		self._RateOrAmt = base_types.UninitialisedField(self, 'RateOrAmt', AmountOrRate1Choice, False)

	@property
	def Sgn(self):
		return self._Sgn

	@Sgn.setter
	def Sgn(self, value):
		self._Sgn = value if value is not None else base_types.UninitialisedField(self, 'Sgn', PlusOrMinusIndicator, False)

	@Sgn.deleter
	def Sgn(self):
		del self._Sgn
		self._Sgn = base_types.UninitialisedField(self, 'Sgn', PlusOrMinusIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RateOrAmt', type=AmountOrRate1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sgn', type=PlusOrMinusIndicator, min=1, max=1, mutex_group=None, array=False),
	))