from . import base_types
from ._AdditionalInformation15 import AdditionalInformation15
from ._PreviousYear2Choice import PreviousYear2Choice
from ._TaxEfficientProductType2Choice import TaxEfficientProductType2Choice
from ._YesNoIndicator import YesNoIndicator

class TaxEfficientProduct4(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_CurYr", "_PrvsYrs", "_TaxEffcntPdctTp"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def CurYr(self):
		return self._CurYr

	@CurYr.setter
	def CurYr(self, value):
		self._CurYr = value if type(value) != base_types.auto else self.make_default("CurYr")

	@CurYr.deleter
	def CurYr(self):
		del self._CurYr
		self._CurYr = None

	@property
	def PrvsYrs(self):
		return self._PrvsYrs

	@PrvsYrs.setter
	def PrvsYrs(self, value):
		self._PrvsYrs = value if type(value) != base_types.auto else self.make_default("PrvsYrs")

	@PrvsYrs.deleter
	def PrvsYrs(self):
		del self._PrvsYrs
		self._PrvsYrs = None

	@property
	def TaxEffcntPdctTp(self):
		return self._TaxEffcntPdctTp

	@TaxEffcntPdctTp.setter
	def TaxEffcntPdctTp(self, value):
		self._TaxEffcntPdctTp = value if type(value) != base_types.auto else self.make_default("TaxEffcntPdctTp")

	@TaxEffcntPdctTp.deleter
	def TaxEffcntPdctTp(self):
		del self._TaxEffcntPdctTp
		self._TaxEffcntPdctTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CurYr', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsYrs', type=PreviousYear2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxEffcntPdctTp', type=TaxEfficientProductType2Choice, min=1, max=1, mutex_group=None, array=False),
	))

