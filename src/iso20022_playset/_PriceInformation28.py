# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTime1Choice
from . import DateTimePeriod1Choice
from . import MarketIdentification93
from . import Price14

class PriceInformation28(base_types._BaseFieldType):

	__slots__ = ["_PricClctnPrd", "_QtnDt", "_SrcOfPric", "_Val"]
	@property
	def PricClctnPrd(self):
		return self._PricClctnPrd

	@PricClctnPrd.setter
	def PricClctnPrd(self, value):
		self._PricClctnPrd = value if value is not None else base_types.UninitialisedField(self, 'PricClctnPrd', DateTimePeriod1Choice, False)

	@PricClctnPrd.deleter
	def PricClctnPrd(self):
		del self._PricClctnPrd
		self._PricClctnPrd = base_types.UninitialisedField(self, 'PricClctnPrd', DateTimePeriod1Choice, False)

	@property
	def QtnDt(self):
		return self._QtnDt

	@QtnDt.setter
	def QtnDt(self, value):
		self._QtnDt = value if value is not None else base_types.UninitialisedField(self, 'QtnDt', DateAndDateTime1Choice, False)

	@QtnDt.deleter
	def QtnDt(self):
		del self._QtnDt
		self._QtnDt = base_types.UninitialisedField(self, 'QtnDt', DateAndDateTime1Choice, False)

	@property
	def SrcOfPric(self):
		return self._SrcOfPric

	@SrcOfPric.setter
	def SrcOfPric(self, value):
		self._SrcOfPric = value if value is not None else base_types.UninitialisedField(self, 'SrcOfPric', MarketIdentification93, False)

	@SrcOfPric.deleter
	def SrcOfPric(self):
		del self._SrcOfPric
		self._SrcOfPric = base_types.UninitialisedField(self, 'SrcOfPric', MarketIdentification93, False)

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if value is not None else base_types.UninitialisedField(self, 'Val', Price14, False)

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = base_types.UninitialisedField(self, 'Val', Price14, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PricClctnPrd', type=DateTimePeriod1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtnDt', type=DateAndDateTime1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrcOfPric', type=MarketIdentification93, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=Price14, min=1, max=1, mutex_group=None, array=False),
	))