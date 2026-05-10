from . import base_types
from .SubscriptionInformation2 import SubscriptionInformation2
from .PreviousYear4 import PreviousYear4
from .TaxEfficientProductType2Choice import TaxEfficientProductType2Choice
from .AdditionalInformation15 import AdditionalInformation15
from .YesNoIndicator import YesNoIndicator

class TaxEfficientProduct6(base_types._BaseFieldType):

	__slots__ = ["_TaxEffcntPdctTp", "_CshCmpntInd", "_AddtlInf", "_CurYr", "_CurYrSbcptDtls", "_PrvsYrs"]
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

	@property
	def CshCmpntInd(self):
		return self._CshCmpntInd

	@CshCmpntInd.setter
	def CshCmpntInd(self, value):
		self._CshCmpntInd = value if type(value) != base_types.auto else self.make_default("CshCmpntInd")

	@CshCmpntInd.deleter
	def CshCmpntInd(self):
		del self._CshCmpntInd
		self._CshCmpntInd = None

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
	def CurYrSbcptDtls(self):
		return self._CurYrSbcptDtls

	@CurYrSbcptDtls.setter
	def CurYrSbcptDtls(self, value):
		self._CurYrSbcptDtls = value if type(value) != base_types.auto else self.make_default("CurYrSbcptDtls")

	@CurYrSbcptDtls.deleter
	def CurYrSbcptDtls(self):
		del self._CurYrSbcptDtls
		self._CurYrSbcptDtls = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='TaxEffcntPdctTp', type=TaxEfficientProductType2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshCmpntInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CurYr', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurYrSbcptDtls', type=SubscriptionInformation2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsYrs', type=PreviousYear4, min=0, max=1, mutex_group=None, array=False),
	))

