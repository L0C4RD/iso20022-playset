# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PriceRateOrAmountChoice
from . import PriceSource2Code
from . import TypeOfPrice13Code

class Price6(base_types._BaseFieldType):

	__slots__ = ["_RateOrAmt", "_Src", "_Tp"]
	@property
	def RateOrAmt(self):
		return self._RateOrAmt

	@RateOrAmt.setter
	def RateOrAmt(self, value):
		self._RateOrAmt = value if value is not None else base_types.UninitialisedField(self, 'RateOrAmt', PriceRateOrAmountChoice, False)

	@RateOrAmt.deleter
	def RateOrAmt(self):
		del self._RateOrAmt
		self._RateOrAmt = base_types.UninitialisedField(self, 'RateOrAmt', PriceRateOrAmountChoice, False)

	@property
	def Src(self):
		return self._Src

	@Src.setter
	def Src(self, value):
		self._Src = value if value is not None else base_types.UninitialisedField(self, 'Src', PriceSource2Code, False)

	@Src.deleter
	def Src(self):
		del self._Src
		self._Src = base_types.UninitialisedField(self, 'Src', PriceSource2Code, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', TypeOfPrice13Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', TypeOfPrice13Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RateOrAmt', type=PriceRateOrAmountChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Src', type=PriceSource2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=TypeOfPrice13Code, min=1, max=1, mutex_group=None, array=False),
	))