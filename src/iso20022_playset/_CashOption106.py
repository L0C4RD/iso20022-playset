from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._CashAccountIdentification9Choice import CashAccountIdentification9Choice
from ._CreditDebitCode import CreditDebitCode
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._DateFormat43Choice import DateFormat43Choice
from ._RateAndAmountFormat55Choice import RateAndAmountFormat55Choice

class CashOption106(base_types._BaseFieldType):

	__slots__ = ["_CdtDbtInd", "_CshAcctId", "_EarlstPmtDt", "_EntitldAmt", "_GrssCshAmt", "_NetCshAmt", "_PmtDt", "_WhldgTaxAmt", "_WhldgTaxRate"]
	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if type(value) != base_types.auto else self.make_default("CdtDbtInd")

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = None

	@property
	def CshAcctId(self):
		return self._CshAcctId

	@CshAcctId.setter
	def CshAcctId(self, value):
		self._CshAcctId = value if type(value) != base_types.auto else self.make_default("CshAcctId")

	@CshAcctId.deleter
	def CshAcctId(self):
		del self._CshAcctId
		self._CshAcctId = None

	@property
	def EarlstPmtDt(self):
		return self._EarlstPmtDt

	@EarlstPmtDt.setter
	def EarlstPmtDt(self, value):
		self._EarlstPmtDt = value if type(value) != base_types.auto else self.make_default("EarlstPmtDt")

	@EarlstPmtDt.deleter
	def EarlstPmtDt(self):
		del self._EarlstPmtDt
		self._EarlstPmtDt = None

	@property
	def EntitldAmt(self):
		return self._EntitldAmt

	@EntitldAmt.setter
	def EntitldAmt(self, value):
		self._EntitldAmt = value if type(value) != base_types.auto else self.make_default("EntitldAmt")

	@EntitldAmt.deleter
	def EntitldAmt(self):
		del self._EntitldAmt
		self._EntitldAmt = None

	@property
	def GrssCshAmt(self):
		return self._GrssCshAmt

	@GrssCshAmt.setter
	def GrssCshAmt(self, value):
		self._GrssCshAmt = value if type(value) != base_types.auto else self.make_default("GrssCshAmt")

	@GrssCshAmt.deleter
	def GrssCshAmt(self):
		del self._GrssCshAmt
		self._GrssCshAmt = None

	@property
	def NetCshAmt(self):
		return self._NetCshAmt

	@NetCshAmt.setter
	def NetCshAmt(self, value):
		self._NetCshAmt = value if type(value) != base_types.auto else self.make_default("NetCshAmt")

	@NetCshAmt.deleter
	def NetCshAmt(self):
		del self._NetCshAmt
		self._NetCshAmt = None

	@property
	def PmtDt(self):
		return self._PmtDt

	@PmtDt.setter
	def PmtDt(self, value):
		self._PmtDt = value if type(value) != base_types.auto else self.make_default("PmtDt")

	@PmtDt.deleter
	def PmtDt(self):
		del self._PmtDt
		self._PmtDt = None

	@property
	def WhldgTaxAmt(self):
		return self._WhldgTaxAmt

	@WhldgTaxAmt.setter
	def WhldgTaxAmt(self, value):
		self._WhldgTaxAmt = value if type(value) != base_types.auto else self.make_default("WhldgTaxAmt")

	@WhldgTaxAmt.deleter
	def WhldgTaxAmt(self):
		del self._WhldgTaxAmt
		self._WhldgTaxAmt = None

	@property
	def WhldgTaxRate(self):
		return self._WhldgTaxRate

	@WhldgTaxRate.setter
	def WhldgTaxRate(self, value):
		self._WhldgTaxRate = value if type(value) != base_types.auto else self.make_default("WhldgTaxRate")

	@WhldgTaxRate.deleter
	def WhldgTaxRate(self):
		del self._WhldgTaxRate
		self._WhldgTaxRate = None

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

