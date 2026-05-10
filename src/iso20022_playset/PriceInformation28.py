import base_types
import Price14
import DateTimePeriod1Choice
import MarketIdentification93
import DateAndDateTime1Choice

class PriceInformation28(base_types._BaseFieldType):

	__slots__ = ["_QtnDt", "_PricClctnPrd", "_SrcOfPric", "_Val"]
	@property
	def QtnDt(self):
		return self._QtnDt

	@QtnDt.setter
	def QtnDt(self, value):
		self._QtnDt = value if type(value) != auto else self.make_default("QtnDt")

	@QtnDt.deleter
	def QtnDt(self):
		del self._QtnDt
		self._QtnDt = None

	@property
	def PricClctnPrd(self):
		return self._PricClctnPrd

	@PricClctnPrd.setter
	def PricClctnPrd(self, value):
		self._PricClctnPrd = value if type(value) != auto else self.make_default("PricClctnPrd")

	@PricClctnPrd.deleter
	def PricClctnPrd(self):
		del self._PricClctnPrd
		self._PricClctnPrd = None

	@property
	def SrcOfPric(self):
		return self._SrcOfPric

	@SrcOfPric.setter
	def SrcOfPric(self, value):
		self._SrcOfPric = value if type(value) != auto else self.make_default("SrcOfPric")

	@SrcOfPric.deleter
	def SrcOfPric(self):
		del self._SrcOfPric
		self._SrcOfPric = None

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if type(value) != auto else self.make_default("Val")

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='QtnDt', type=DateAndDateTime1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricClctnPrd', type=DateTimePeriod1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrcOfPric', type=MarketIdentification93, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=Price14, min=1, max=1, mutex_group=None, array=False),
	))

