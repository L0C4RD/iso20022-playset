from . import base_types
import DateAndDateTime2Choice
import MarketIdentification98
import PriceRateOrAmountOrUnknown2Choice
import YieldedOrValueType1Choice
import TypeOfPrice48Choice

class PriceInformation30(base_types._BaseFieldType):

	__slots__ = ["_Val", "_ValTp", "_QtnDt", "_Tp", "_SrcOfPric"]
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

	@property
	def ValTp(self):
		return self._ValTp

	@ValTp.setter
	def ValTp(self, value):
		self._ValTp = value if type(value) != auto else self.make_default("ValTp")

	@ValTp.deleter
	def ValTp(self):
		del self._ValTp
		self._ValTp = None

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
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Val', type=PriceRateOrAmountOrUnknown2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValTp', type=YieldedOrValueType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtnDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=TypeOfPrice48Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrcOfPric', type=MarketIdentification98, min=0, max=1, mutex_group=None, array=False),
	))

