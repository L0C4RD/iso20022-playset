# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalInformation15
from . import PreviousYear2Choice
from . import TaxEfficientProductType2Choice
from . import YesNoIndicator

class TaxEfficientProduct4(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_CurYr", "_PrvsYrs", "_TaxEffcntPdctTp"]
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
	def CurYr(self):
		return self._CurYr

	@CurYr.setter
	def CurYr(self, value):
		self._CurYr = value if value is not None else base_types.UninitialisedField(self, 'CurYr', YesNoIndicator, False)

	@CurYr.deleter
	def CurYr(self):
		del self._CurYr
		self._CurYr = base_types.UninitialisedField(self, 'CurYr', YesNoIndicator, False)

	@property
	def PrvsYrs(self):
		return self._PrvsYrs

	@PrvsYrs.setter
	def PrvsYrs(self, value):
		self._PrvsYrs = value if value is not None else base_types.UninitialisedField(self, 'PrvsYrs', PreviousYear2Choice, False)

	@PrvsYrs.deleter
	def PrvsYrs(self):
		del self._PrvsYrs
		self._PrvsYrs = base_types.UninitialisedField(self, 'PrvsYrs', PreviousYear2Choice, False)

	@property
	def TaxEffcntPdctTp(self):
		return self._TaxEffcntPdctTp

	@TaxEffcntPdctTp.setter
	def TaxEffcntPdctTp(self, value):
		self._TaxEffcntPdctTp = value if value is not None else base_types.UninitialisedField(self, 'TaxEffcntPdctTp', TaxEfficientProductType2Choice, False)

	@TaxEffcntPdctTp.deleter
	def TaxEffcntPdctTp(self):
		del self._TaxEffcntPdctTp
		self._TaxEffcntPdctTp = base_types.UninitialisedField(self, 'TaxEffcntPdctTp', TaxEfficientProductType2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CurYr', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsYrs', type=PreviousYear2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxEffcntPdctTp', type=TaxEfficientProductType2Choice, min=1, max=1, mutex_group=None, array=False),
	))