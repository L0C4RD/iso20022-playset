# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTime2Choice
from . import MarketIdentification91
from . import PriceRateOrAmountOrUnknown3Choice
from . import TypeOfPrice33Choice
from . import YieldedOrValueType1Choice

class PriceInformation22(base_types._BaseFieldType):

	__slots__ = ["_QtnDt", "_SrcOfPric", "_Tp", "_Val", "_ValTp"]
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
		self._SrcOfPric = value if value is not None else base_types.UninitialisedField(self, 'SrcOfPric', MarketIdentification91, False)

	@SrcOfPric.deleter
	def SrcOfPric(self):
		del self._SrcOfPric
		self._SrcOfPric = base_types.UninitialisedField(self, 'SrcOfPric', MarketIdentification91, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', TypeOfPrice33Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', TypeOfPrice33Choice, False)

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if value is not None else base_types.UninitialisedField(self, 'Val', PriceRateOrAmountOrUnknown3Choice, False)

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = base_types.UninitialisedField(self, 'Val', PriceRateOrAmountOrUnknown3Choice, False)

	@property
	def ValTp(self):
		return self._ValTp

	@ValTp.setter
	def ValTp(self, value):
		self._ValTp = value if value is not None else base_types.UninitialisedField(self, 'ValTp', YieldedOrValueType1Choice, False)

	@ValTp.deleter
	def ValTp(self):
		del self._ValTp
		self._ValTp = base_types.UninitialisedField(self, 'ValTp', YieldedOrValueType1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='QtnDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrcOfPric', type=MarketIdentification91, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=TypeOfPrice33Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=PriceRateOrAmountOrUnknown3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValTp', type=YieldedOrValueType1Choice, min=1, max=1, mutex_group=None, array=False),
	))