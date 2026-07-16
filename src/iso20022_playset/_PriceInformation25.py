# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTime2Choice
from . import MarketIdentification89
from . import PriceRateOrAmount4Choice

class PriceInformation25(base_types._BaseFieldType):

	__slots__ = ["_QtnDt", "_SrcOfPric", "_Val"]
	@property
	def QtnDt(self):
		return self._QtnDt

	@QtnDt.setter
	def QtnDt(self, value):
		self._QtnDt = value if value is not None else base_types.UninitialisedField(self, 'QtnDt', DateAndDateTime2Choice, False)

	@QtnDt.deleter
	def QtnDt(self):
		del self._QtnDt
		self._QtnDt = base_types.UninitialisedField(self, 'QtnDt', DateAndDateTime2Choice, False)

	@property
	def SrcOfPric(self):
		return self._SrcOfPric

	@SrcOfPric.setter
	def SrcOfPric(self, value):
		self._SrcOfPric = value if value is not None else base_types.UninitialisedField(self, 'SrcOfPric', MarketIdentification89, False)

	@SrcOfPric.deleter
	def SrcOfPric(self):
		del self._SrcOfPric
		self._SrcOfPric = base_types.UninitialisedField(self, 'SrcOfPric', MarketIdentification89, False)

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if value is not None else base_types.UninitialisedField(self, 'Val', PriceRateOrAmount4Choice, False)

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = base_types.UninitialisedField(self, 'Val', PriceRateOrAmount4Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='QtnDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrcOfPric', type=MarketIdentification89, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=PriceRateOrAmount4Choice, min=1, max=1, mutex_group=None, array=False),
	))