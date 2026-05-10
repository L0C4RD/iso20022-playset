from . import base_types
from ._DateAndDateTimeChoice import DateAndDateTimeChoice
from ._Extended350Code import Extended350Code
from ._YesNoIndicator import YesNoIndicator
from ._PriceSourceFormatChoice import PriceSourceFormatChoice
from ._PriceRateOrAmountOrUnknownChoice import PriceRateOrAmountOrUnknownChoice
from ._TypeOfPrice11Code import TypeOfPrice11Code
from ._PriceValueType2Code import PriceValueType2Code

class PriceInformation2(base_types._BaseFieldType):

	__slots__ = ["_SrcOfPric", "_Tp", "_Val", "_Yldd", "_XtndedTp", "_ValTp", "_QtnDt"]
	@property
	def QtnDt(self):
		return self._QtnDt

	@QtnDt.setter
	def QtnDt(self, value):
		self._QtnDt = value if type(value) != base_types.auto else self.make_default("QtnDt")

	@QtnDt.deleter
	def QtnDt(self):
		del self._QtnDt
		self._QtnDt = None

	@property
	def SrcOfPric(self):
		return self._SrcOfPric

	@SrcOfPric.setter
	def SrcOfPric(self, value):
		self._SrcOfPric = value if type(value) != base_types.auto else self.make_default("SrcOfPric")

	@SrcOfPric.deleter
	def SrcOfPric(self):
		del self._SrcOfPric
		self._SrcOfPric = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if type(value) != base_types.auto else self.make_default("Val")

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = None

	@property
	def ValTp(self):
		return self._ValTp

	@ValTp.setter
	def ValTp(self, value):
		self._ValTp = value if type(value) != base_types.auto else self.make_default("ValTp")

	@ValTp.deleter
	def ValTp(self):
		del self._ValTp
		self._ValTp = None

	@property
	def XtndedTp(self):
		return self._XtndedTp

	@XtndedTp.setter
	def XtndedTp(self, value):
		self._XtndedTp = value if type(value) != base_types.auto else self.make_default("XtndedTp")

	@XtndedTp.deleter
	def XtndedTp(self):
		del self._XtndedTp
		self._XtndedTp = None

	@property
	def Yldd(self):
		return self._Yldd

	@Yldd.setter
	def Yldd(self, value):
		self._Yldd = value if type(value) != base_types.auto else self.make_default("Yldd")

	@Yldd.deleter
	def Yldd(self):
		del self._Yldd
		self._Yldd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='QtnDt', type=DateAndDateTimeChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrcOfPric', type=PriceSourceFormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=TypeOfPrice11Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Val', type=PriceRateOrAmountOrUnknownChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValTp', type=PriceValueType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XtndedTp', type=Extended350Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Yldd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))

