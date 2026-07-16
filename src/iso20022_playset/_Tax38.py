# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import CountryCode
from . import ExemptionReason1Choice
from . import PartyIdentification139
from . import TaxBasis1Choice
from . import TaxCalculationInformation11
from . import TaxType1Choice
from . import YesNoIndicator

class Tax38(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Bsis", "_Ctry", "_RcptId", "_TaxClctnDtls", "_Tp", "_XmptnInd", "_XmptnRsn"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@property
	def Bsis(self):
		return self._Bsis

	@Bsis.setter
	def Bsis(self, value):
		self._Bsis = value if value is not None else base_types.UninitialisedField(self, 'Bsis', TaxBasis1Choice, False)

	@Bsis.deleter
	def Bsis(self):
		del self._Bsis
		self._Bsis = base_types.UninitialisedField(self, 'Bsis', TaxBasis1Choice, False)

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if value is not None else base_types.UninitialisedField(self, 'Ctry', CountryCode, False)

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = base_types.UninitialisedField(self, 'Ctry', CountryCode, False)

	@property
	def RcptId(self):
		return self._RcptId

	@RcptId.setter
	def RcptId(self, value):
		self._RcptId = value if value is not None else base_types.UninitialisedField(self, 'RcptId', PartyIdentification139, False)

	@RcptId.deleter
	def RcptId(self):
		del self._RcptId
		self._RcptId = base_types.UninitialisedField(self, 'RcptId', PartyIdentification139, False)

	@property
	def TaxClctnDtls(self):
		return self._TaxClctnDtls

	@TaxClctnDtls.setter
	def TaxClctnDtls(self, value):
		self._TaxClctnDtls = value if value is not None else base_types.UninitialisedField(self, 'TaxClctnDtls', TaxCalculationInformation11, False)

	@TaxClctnDtls.deleter
	def TaxClctnDtls(self):
		del self._TaxClctnDtls
		self._TaxClctnDtls = base_types.UninitialisedField(self, 'TaxClctnDtls', TaxCalculationInformation11, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', TaxType1Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', TaxType1Choice, False)

	@property
	def XmptnInd(self):
		return self._XmptnInd

	@XmptnInd.setter
	def XmptnInd(self, value):
		self._XmptnInd = value if value is not None else base_types.UninitialisedField(self, 'XmptnInd', YesNoIndicator, False)

	@XmptnInd.deleter
	def XmptnInd(self):
		del self._XmptnInd
		self._XmptnInd = base_types.UninitialisedField(self, 'XmptnInd', YesNoIndicator, False)

	@property
	def XmptnRsn(self):
		return self._XmptnRsn

	@XmptnRsn.setter
	def XmptnRsn(self, value):
		self._XmptnRsn = value if value is not None else base_types.UninitialisedField(self, 'XmptnRsn', ExemptionReason1Choice, False)

	@XmptnRsn.deleter
	def XmptnRsn(self):
		del self._XmptnRsn
		self._XmptnRsn = base_types.UninitialisedField(self, 'XmptnRsn', ExemptionReason1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bsis', type=TaxBasis1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcptId', type=PartyIdentification139, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxClctnDtls', type=TaxCalculationInformation11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=TaxType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XmptnInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XmptnRsn', type=ExemptionReason1Choice, min=0, max=1, mutex_group=None, array=False),
	))