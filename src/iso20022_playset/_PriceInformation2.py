# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTimeChoice
from . import Extended350Code
from . import PriceRateOrAmountOrUnknownChoice
from . import PriceSourceFormatChoice
from . import PriceValueType2Code
from . import TypeOfPrice11Code
from . import YesNoIndicator

class PriceInformation2(base_types._BaseFieldType):

	__slots__ = ["_QtnDt", "_SrcOfPric", "_Tp", "_Val", "_ValTp", "_XtndedTp", "_Yldd"]
	@property
	def QtnDt(self):
		return self._QtnDt

	@QtnDt.setter
	def QtnDt(self, value):
		self._QtnDt = value if value is not None else base_types.UninitialisedField(self, 'QtnDt', DateAndDateTimeChoice, False)

	@QtnDt.deleter
	def QtnDt(self):
		del self._QtnDt
		self._QtnDt = base_types.UninitialisedField(self, 'QtnDt', DateAndDateTimeChoice, False)

	@property
	def SrcOfPric(self):
		return self._SrcOfPric

	@SrcOfPric.setter
	def SrcOfPric(self, value):
		self._SrcOfPric = value if value is not None else base_types.UninitialisedField(self, 'SrcOfPric', PriceSourceFormatChoice, False)

	@SrcOfPric.deleter
	def SrcOfPric(self):
		del self._SrcOfPric
		self._SrcOfPric = base_types.UninitialisedField(self, 'SrcOfPric', PriceSourceFormatChoice, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', TypeOfPrice11Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', TypeOfPrice11Code, False)

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if value is not None else base_types.UninitialisedField(self, 'Val', PriceRateOrAmountOrUnknownChoice, False)

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = base_types.UninitialisedField(self, 'Val', PriceRateOrAmountOrUnknownChoice, False)

	@property
	def ValTp(self):
		return self._ValTp

	@ValTp.setter
	def ValTp(self, value):
		self._ValTp = value if value is not None else base_types.UninitialisedField(self, 'ValTp', PriceValueType2Code, False)

	@ValTp.deleter
	def ValTp(self):
		del self._ValTp
		self._ValTp = base_types.UninitialisedField(self, 'ValTp', PriceValueType2Code, False)

	@property
	def XtndedTp(self):
		return self._XtndedTp

	@XtndedTp.setter
	def XtndedTp(self, value):
		self._XtndedTp = value if value is not None else base_types.UninitialisedField(self, 'XtndedTp', Extended350Code, False)

	@XtndedTp.deleter
	def XtndedTp(self):
		del self._XtndedTp
		self._XtndedTp = base_types.UninitialisedField(self, 'XtndedTp', Extended350Code, False)

	@property
	def Yldd(self):
		return self._Yldd

	@Yldd.setter
	def Yldd(self, value):
		self._Yldd = value if value is not None else base_types.UninitialisedField(self, 'Yldd', YesNoIndicator, False)

	@Yldd.deleter
	def Yldd(self):
		del self._Yldd
		self._Yldd = base_types.UninitialisedField(self, 'Yldd', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='QtnDt', type=DateAndDateTimeChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrcOfPric', type=PriceSourceFormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=TypeOfPrice11Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Val', type=PriceRateOrAmountOrUnknownChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValTp', type=PriceValueType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XtndedTp', type=Extended350Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Yldd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))