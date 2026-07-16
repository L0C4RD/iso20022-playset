# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import AdditionalInformation15
from . import EventFrequency5Code
from . import ISOTime
from . import Max350Text
from . import Number
from . import PriceMethod1Code
from . import YesNoIndicator

class ValuationDealingProcessingCharacteristics3(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_DcmlstnPric", "_DcmlstnUnits", "_DualFndInd", "_PricCcy", "_PricMtd", "_ValtnFrqcy", "_ValtnFrqcyDesc", "_ValtnTm"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@property
	def DcmlstnPric(self):
		return self._DcmlstnPric

	@DcmlstnPric.setter
	def DcmlstnPric(self, value):
		self._DcmlstnPric = value if value is not None else base_types.UninitialisedField(self, 'DcmlstnPric', Number, False)

	@DcmlstnPric.deleter
	def DcmlstnPric(self):
		del self._DcmlstnPric
		self._DcmlstnPric = base_types.UninitialisedField(self, 'DcmlstnPric', Number, False)

	@property
	def DcmlstnUnits(self):
		return self._DcmlstnUnits

	@DcmlstnUnits.setter
	def DcmlstnUnits(self, value):
		self._DcmlstnUnits = value if value is not None else base_types.UninitialisedField(self, 'DcmlstnUnits', Number, False)

	@DcmlstnUnits.deleter
	def DcmlstnUnits(self):
		del self._DcmlstnUnits
		self._DcmlstnUnits = base_types.UninitialisedField(self, 'DcmlstnUnits', Number, False)

	@property
	def DualFndInd(self):
		return self._DualFndInd

	@DualFndInd.setter
	def DualFndInd(self, value):
		self._DualFndInd = value if value is not None else base_types.UninitialisedField(self, 'DualFndInd', YesNoIndicator, False)

	@DualFndInd.deleter
	def DualFndInd(self):
		del self._DualFndInd
		self._DualFndInd = base_types.UninitialisedField(self, 'DualFndInd', YesNoIndicator, False)

	@property
	def PricCcy(self):
		return self._PricCcy

	@PricCcy.setter
	def PricCcy(self, value):
		self._PricCcy = value if value is not None else base_types.UninitialisedField(self, 'PricCcy', ActiveCurrencyCode, True)

	@PricCcy.deleter
	def PricCcy(self):
		del self._PricCcy
		self._PricCcy = base_types.UninitialisedField(self, 'PricCcy', ActiveCurrencyCode, True)

	@property
	def PricMtd(self):
		return self._PricMtd

	@PricMtd.setter
	def PricMtd(self, value):
		self._PricMtd = value if value is not None else base_types.UninitialisedField(self, 'PricMtd', PriceMethod1Code, False)

	@PricMtd.deleter
	def PricMtd(self):
		del self._PricMtd
		self._PricMtd = base_types.UninitialisedField(self, 'PricMtd', PriceMethod1Code, False)

	@property
	def ValtnFrqcy(self):
		return self._ValtnFrqcy

	@ValtnFrqcy.setter
	def ValtnFrqcy(self, value):
		self._ValtnFrqcy = value if value is not None else base_types.UninitialisedField(self, 'ValtnFrqcy', EventFrequency5Code, False)

	@ValtnFrqcy.deleter
	def ValtnFrqcy(self):
		del self._ValtnFrqcy
		self._ValtnFrqcy = base_types.UninitialisedField(self, 'ValtnFrqcy', EventFrequency5Code, False)

	@property
	def ValtnFrqcyDesc(self):
		return self._ValtnFrqcyDesc

	@ValtnFrqcyDesc.setter
	def ValtnFrqcyDesc(self, value):
		self._ValtnFrqcyDesc = value if value is not None else base_types.UninitialisedField(self, 'ValtnFrqcyDesc', Max350Text, False)

	@ValtnFrqcyDesc.deleter
	def ValtnFrqcyDesc(self):
		del self._ValtnFrqcyDesc
		self._ValtnFrqcyDesc = base_types.UninitialisedField(self, 'ValtnFrqcyDesc', Max350Text, False)

	@property
	def ValtnTm(self):
		return self._ValtnTm

	@ValtnTm.setter
	def ValtnTm(self, value):
		self._ValtnTm = value if value is not None else base_types.UninitialisedField(self, 'ValtnTm', ISOTime, False)

	@ValtnTm.deleter
	def ValtnTm(self):
		del self._ValtnTm
		self._ValtnTm = base_types.UninitialisedField(self, 'ValtnTm', ISOTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DcmlstnPric', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DcmlstnUnits', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DualFndInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricCcy', type=ActiveCurrencyCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PricMtd', type=PriceMethod1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnFrqcy', type=EventFrequency5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnFrqcyDesc', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnTm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
	))