from . import base_types
import Max350Text
import YesNoIndicator
import ISOTime
import ActiveCurrencyCode
import Number
import EventFrequency5Code
import PriceMethod1Code
import AdditionalInformation15

class ValuationDealingProcessingCharacteristics3(base_types._BaseFieldType):

	__slots__ = ["_ValtnTm", "_ValtnFrqcy", "_AddtlInf", "_DualFndInd", "_PricCcy", "_ValtnFrqcyDesc", "_PricMtd", "_DcmlstnUnits", "_DcmlstnPric"]
	@property
	def ValtnTm(self):
		return self._ValtnTm

	@ValtnTm.setter
	def ValtnTm(self, value):
		self._ValtnTm = value if type(value) != auto else self.make_default("ValtnTm")

	@ValtnTm.deleter
	def ValtnTm(self):
		del self._ValtnTm
		self._ValtnTm = None

	@property
	def ValtnFrqcy(self):
		return self._ValtnFrqcy

	@ValtnFrqcy.setter
	def ValtnFrqcy(self, value):
		self._ValtnFrqcy = value if type(value) != auto else self.make_default("ValtnFrqcy")

	@ValtnFrqcy.deleter
	def ValtnFrqcy(self):
		del self._ValtnFrqcy
		self._ValtnFrqcy = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def DualFndInd(self):
		return self._DualFndInd

	@DualFndInd.setter
	def DualFndInd(self, value):
		self._DualFndInd = value if type(value) != auto else self.make_default("DualFndInd")

	@DualFndInd.deleter
	def DualFndInd(self):
		del self._DualFndInd
		self._DualFndInd = None

	@property
	def PricCcy(self):
		return self._PricCcy

	@PricCcy.setter
	def PricCcy(self, value):
		self._PricCcy = value if type(value) != auto else self.make_default("PricCcy")

	@PricCcy.deleter
	def PricCcy(self):
		del self._PricCcy
		self._PricCcy = None

	@property
	def ValtnFrqcyDesc(self):
		return self._ValtnFrqcyDesc

	@ValtnFrqcyDesc.setter
	def ValtnFrqcyDesc(self, value):
		self._ValtnFrqcyDesc = value if type(value) != auto else self.make_default("ValtnFrqcyDesc")

	@ValtnFrqcyDesc.deleter
	def ValtnFrqcyDesc(self):
		del self._ValtnFrqcyDesc
		self._ValtnFrqcyDesc = None

	@property
	def PricMtd(self):
		return self._PricMtd

	@PricMtd.setter
	def PricMtd(self, value):
		self._PricMtd = value if type(value) != auto else self.make_default("PricMtd")

	@PricMtd.deleter
	def PricMtd(self):
		del self._PricMtd
		self._PricMtd = None

	@property
	def DcmlstnUnits(self):
		return self._DcmlstnUnits

	@DcmlstnUnits.setter
	def DcmlstnUnits(self, value):
		self._DcmlstnUnits = value if type(value) != auto else self.make_default("DcmlstnUnits")

	@DcmlstnUnits.deleter
	def DcmlstnUnits(self):
		del self._DcmlstnUnits
		self._DcmlstnUnits = None

	@property
	def DcmlstnPric(self):
		return self._DcmlstnPric

	@DcmlstnPric.setter
	def DcmlstnPric(self, value):
		self._DcmlstnPric = value if type(value) != auto else self.make_default("DcmlstnPric")

	@DcmlstnPric.deleter
	def DcmlstnPric(self):
		del self._DcmlstnPric
		self._DcmlstnPric = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ValtnTm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnFrqcy', type=EventFrequency5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DualFndInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricCcy', type=ActiveCurrencyCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ValtnFrqcyDesc', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricMtd', type=PriceMethod1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DcmlstnUnits', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DcmlstnPric', type=Number, min=0, max=1, mutex_group=None, array=False),
	))

