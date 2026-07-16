# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import AdditionalInformation15
from . import DateFormat42Choice
from . import GenericIdentification36
from . import YesNoIndicator

class EmploymentDetails1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_CmltvTaxInd", "_EndDt", "_OthrTaxCdInd", "_PrvsPay", "_PrvsTax", "_StartDt", "_TaxCd"]
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
	def CmltvTaxInd(self):
		return self._CmltvTaxInd

	@CmltvTaxInd.setter
	def CmltvTaxInd(self, value):
		self._CmltvTaxInd = value if value is not None else base_types.UninitialisedField(self, 'CmltvTaxInd', YesNoIndicator, False)

	@CmltvTaxInd.deleter
	def CmltvTaxInd(self):
		del self._CmltvTaxInd
		self._CmltvTaxInd = base_types.UninitialisedField(self, 'CmltvTaxInd', YesNoIndicator, False)

	@property
	def EndDt(self):
		return self._EndDt

	@EndDt.setter
	def EndDt(self, value):
		self._EndDt = value if value is not None else base_types.UninitialisedField(self, 'EndDt', DateFormat42Choice, False)

	@EndDt.deleter
	def EndDt(self):
		del self._EndDt
		self._EndDt = base_types.UninitialisedField(self, 'EndDt', DateFormat42Choice, False)

	@property
	def OthrTaxCdInd(self):
		return self._OthrTaxCdInd

	@OthrTaxCdInd.setter
	def OthrTaxCdInd(self, value):
		self._OthrTaxCdInd = value if value is not None else base_types.UninitialisedField(self, 'OthrTaxCdInd', YesNoIndicator, False)

	@OthrTaxCdInd.deleter
	def OthrTaxCdInd(self):
		del self._OthrTaxCdInd
		self._OthrTaxCdInd = base_types.UninitialisedField(self, 'OthrTaxCdInd', YesNoIndicator, False)

	@property
	def PrvsPay(self):
		return self._PrvsPay

	@PrvsPay.setter
	def PrvsPay(self, value):
		self._PrvsPay = value if value is not None else base_types.UninitialisedField(self, 'PrvsPay', ActiveCurrencyAndAmount, False)

	@PrvsPay.deleter
	def PrvsPay(self):
		del self._PrvsPay
		self._PrvsPay = base_types.UninitialisedField(self, 'PrvsPay', ActiveCurrencyAndAmount, False)

	@property
	def PrvsTax(self):
		return self._PrvsTax

	@PrvsTax.setter
	def PrvsTax(self, value):
		self._PrvsTax = value if value is not None else base_types.UninitialisedField(self, 'PrvsTax', ActiveCurrencyAndAmount, False)

	@PrvsTax.deleter
	def PrvsTax(self):
		del self._PrvsTax
		self._PrvsTax = base_types.UninitialisedField(self, 'PrvsTax', ActiveCurrencyAndAmount, False)

	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if value is not None else base_types.UninitialisedField(self, 'StartDt', DateFormat42Choice, False)

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = base_types.UninitialisedField(self, 'StartDt', DateFormat42Choice, False)

	@property
	def TaxCd(self):
		return self._TaxCd

	@TaxCd.setter
	def TaxCd(self, value):
		self._TaxCd = value if value is not None else base_types.UninitialisedField(self, 'TaxCd', GenericIdentification36, False)

	@TaxCd.deleter
	def TaxCd(self):
		del self._TaxCd
		self._TaxCd = base_types.UninitialisedField(self, 'TaxCd', GenericIdentification36, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CmltvTaxInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndDt', type=DateFormat42Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTaxCdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsPay', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsTax', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDt', type=DateFormat42Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxCd', type=GenericIdentification36, min=0, max=1, mutex_group=None, array=False),
	))