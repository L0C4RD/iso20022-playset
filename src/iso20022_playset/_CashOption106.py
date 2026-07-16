# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import CashAccountIdentification9Choice
from . import CreditDebitCode
from . import DateAndDateTime2Choice
from . import DateFormat43Choice
from . import RateAndAmountFormat55Choice

class CashOption106(base_types._BaseFieldType):

	__slots__ = ["_CdtDbtInd", "_CshAcctId", "_EarlstPmtDt", "_EntitldAmt", "_GrssCshAmt", "_NetCshAmt", "_PmtDt", "_WhldgTaxAmt", "_WhldgTaxRate"]
	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if value is not None else base_types.UninitialisedField(self, 'CdtDbtInd', CreditDebitCode, False)

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = base_types.UninitialisedField(self, 'CdtDbtInd', CreditDebitCode, False)

	@property
	def CshAcctId(self):
		return self._CshAcctId

	@CshAcctId.setter
	def CshAcctId(self, value):
		self._CshAcctId = value if value is not None else base_types.UninitialisedField(self, 'CshAcctId', CashAccountIdentification9Choice, False)

	@CshAcctId.deleter
	def CshAcctId(self):
		del self._CshAcctId
		self._CshAcctId = base_types.UninitialisedField(self, 'CshAcctId', CashAccountIdentification9Choice, False)

	@property
	def EarlstPmtDt(self):
		return self._EarlstPmtDt

	@EarlstPmtDt.setter
	def EarlstPmtDt(self, value):
		self._EarlstPmtDt = value if value is not None else base_types.UninitialisedField(self, 'EarlstPmtDt', DateAndDateTime2Choice, False)

	@EarlstPmtDt.deleter
	def EarlstPmtDt(self):
		del self._EarlstPmtDt
		self._EarlstPmtDt = base_types.UninitialisedField(self, 'EarlstPmtDt', DateAndDateTime2Choice, False)

	@property
	def EntitldAmt(self):
		return self._EntitldAmt

	@EntitldAmt.setter
	def EntitldAmt(self, value):
		self._EntitldAmt = value if value is not None else base_types.UninitialisedField(self, 'EntitldAmt', ActiveCurrencyAndAmount, False)

	@EntitldAmt.deleter
	def EntitldAmt(self):
		del self._EntitldAmt
		self._EntitldAmt = base_types.UninitialisedField(self, 'EntitldAmt', ActiveCurrencyAndAmount, False)

	@property
	def GrssCshAmt(self):
		return self._GrssCshAmt

	@GrssCshAmt.setter
	def GrssCshAmt(self, value):
		self._GrssCshAmt = value if value is not None else base_types.UninitialisedField(self, 'GrssCshAmt', ActiveCurrencyAndAmount, False)

	@GrssCshAmt.deleter
	def GrssCshAmt(self):
		del self._GrssCshAmt
		self._GrssCshAmt = base_types.UninitialisedField(self, 'GrssCshAmt', ActiveCurrencyAndAmount, False)

	@property
	def NetCshAmt(self):
		return self._NetCshAmt

	@NetCshAmt.setter
	def NetCshAmt(self, value):
		self._NetCshAmt = value if value is not None else base_types.UninitialisedField(self, 'NetCshAmt', ActiveCurrencyAndAmount, False)

	@NetCshAmt.deleter
	def NetCshAmt(self):
		del self._NetCshAmt
		self._NetCshAmt = base_types.UninitialisedField(self, 'NetCshAmt', ActiveCurrencyAndAmount, False)

	@property
	def PmtDt(self):
		return self._PmtDt

	@PmtDt.setter
	def PmtDt(self, value):
		self._PmtDt = value if value is not None else base_types.UninitialisedField(self, 'PmtDt', DateFormat43Choice, False)

	@PmtDt.deleter
	def PmtDt(self):
		del self._PmtDt
		self._PmtDt = base_types.UninitialisedField(self, 'PmtDt', DateFormat43Choice, False)

	@property
	def WhldgTaxAmt(self):
		return self._WhldgTaxAmt

	@WhldgTaxAmt.setter
	def WhldgTaxAmt(self, value):
		self._WhldgTaxAmt = value if value is not None else base_types.UninitialisedField(self, 'WhldgTaxAmt', ActiveCurrencyAndAmount, False)

	@WhldgTaxAmt.deleter
	def WhldgTaxAmt(self):
		del self._WhldgTaxAmt
		self._WhldgTaxAmt = base_types.UninitialisedField(self, 'WhldgTaxAmt', ActiveCurrencyAndAmount, False)

	@property
	def WhldgTaxRate(self):
		return self._WhldgTaxRate

	@WhldgTaxRate.setter
	def WhldgTaxRate(self, value):
		self._WhldgTaxRate = value if value is not None else base_types.UninitialisedField(self, 'WhldgTaxRate', RateAndAmountFormat55Choice, True)

	@WhldgTaxRate.deleter
	def WhldgTaxRate(self):
		del self._WhldgTaxRate
		self._WhldgTaxRate = base_types.UninitialisedField(self, 'WhldgTaxRate', RateAndAmountFormat55Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcctId', type=CashAccountIdentification9Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlstPmtDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EntitldAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrssCshAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetCshAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtDt', type=DateFormat43Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgTaxAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgTaxRate', type=RateAndAmountFormat55Choice, min=0, max=None, mutex_group=None, array=True),
	))