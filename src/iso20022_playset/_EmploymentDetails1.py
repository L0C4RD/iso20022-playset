from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._AdditionalInformation15 import AdditionalInformation15
from ._GenericIdentification36 import GenericIdentification36
from ._YesNoIndicator import YesNoIndicator
from ._DateFormat42Choice import DateFormat42Choice

class EmploymentDetails1(base_types._BaseFieldType):

	__slots__ = ["_PrvsPay", "_OthrTaxCdInd", "_TaxCd", "_PrvsTax", "_StartDt", "_AddtlInf", "_EndDt", "_CmltvTaxInd"]
	@property
	def PrvsPay(self):
		return self._PrvsPay

	@PrvsPay.setter
	def PrvsPay(self, value):
		self._PrvsPay = value if type(value) != base_types.auto else self.make_default("PrvsPay")

	@PrvsPay.deleter
	def PrvsPay(self):
		del self._PrvsPay
		self._PrvsPay = None

	@property
	def OthrTaxCdInd(self):
		return self._OthrTaxCdInd

	@OthrTaxCdInd.setter
	def OthrTaxCdInd(self, value):
		self._OthrTaxCdInd = value if type(value) != base_types.auto else self.make_default("OthrTaxCdInd")

	@OthrTaxCdInd.deleter
	def OthrTaxCdInd(self):
		del self._OthrTaxCdInd
		self._OthrTaxCdInd = None

	@property
	def TaxCd(self):
		return self._TaxCd

	@TaxCd.setter
	def TaxCd(self, value):
		self._TaxCd = value if type(value) != base_types.auto else self.make_default("TaxCd")

	@TaxCd.deleter
	def TaxCd(self):
		del self._TaxCd
		self._TaxCd = None

	@property
	def PrvsTax(self):
		return self._PrvsTax

	@PrvsTax.setter
	def PrvsTax(self, value):
		self._PrvsTax = value if type(value) != base_types.auto else self.make_default("PrvsTax")

	@PrvsTax.deleter
	def PrvsTax(self):
		del self._PrvsTax
		self._PrvsTax = None

	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if type(value) != base_types.auto else self.make_default("StartDt")

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = None

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
	def EndDt(self):
		return self._EndDt

	@EndDt.setter
	def EndDt(self, value):
		self._EndDt = value if type(value) != base_types.auto else self.make_default("EndDt")

	@EndDt.deleter
	def EndDt(self):
		del self._EndDt
		self._EndDt = None

	@property
	def CmltvTaxInd(self):
		return self._CmltvTaxInd

	@CmltvTaxInd.setter
	def CmltvTaxInd(self, value):
		self._CmltvTaxInd = value if type(value) != base_types.auto else self.make_default("CmltvTaxInd")

	@CmltvTaxInd.deleter
	def CmltvTaxInd(self):
		del self._CmltvTaxInd
		self._CmltvTaxInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrvsPay', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTaxCdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxCd', type=GenericIdentification36, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsTax', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDt', type=DateFormat42Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EndDt', type=DateFormat42Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmltvTaxInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))

