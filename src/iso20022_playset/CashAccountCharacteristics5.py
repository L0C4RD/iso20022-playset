from . import base_types
import ISODate
import AccountLevel2Code
import AccountIdentification4Choice
import CompensationMethod1Code
import Max105Text
import BranchAndFinancialInstitutionIdentification8
import Contact13
import ParentCashAccount5
import CashAccount40
import ActiveOrHistoricCurrencyCode
import AccountTax1

class CashAccountCharacteristics5(base_types._BaseFieldType):

	__slots__ = ["_DelydDbtDt", "_AcctBalCcyCd", "_HstCcyCd", "_DbtAcct", "_AcctSvcr", "_SttlmAdvc", "_SttlmCcyCd", "_Tax", "_AcctLvl", "_CompstnMtd", "_PrntAcct", "_CshAcct", "_AcctSvcrCtct"]
	@property
	def DelydDbtDt(self):
		return self._DelydDbtDt

	@DelydDbtDt.setter
	def DelydDbtDt(self, value):
		self._DelydDbtDt = value if type(value) != auto else self.make_default("DelydDbtDt")

	@DelydDbtDt.deleter
	def DelydDbtDt(self):
		del self._DelydDbtDt
		self._DelydDbtDt = None

	@property
	def AcctBalCcyCd(self):
		return self._AcctBalCcyCd

	@AcctBalCcyCd.setter
	def AcctBalCcyCd(self, value):
		self._AcctBalCcyCd = value if type(value) != auto else self.make_default("AcctBalCcyCd")

	@AcctBalCcyCd.deleter
	def AcctBalCcyCd(self):
		del self._AcctBalCcyCd
		self._AcctBalCcyCd = None

	@property
	def HstCcyCd(self):
		return self._HstCcyCd

	@HstCcyCd.setter
	def HstCcyCd(self, value):
		self._HstCcyCd = value if type(value) != auto else self.make_default("HstCcyCd")

	@HstCcyCd.deleter
	def HstCcyCd(self):
		del self._HstCcyCd
		self._HstCcyCd = None

	@property
	def DbtAcct(self):
		return self._DbtAcct

	@DbtAcct.setter
	def DbtAcct(self, value):
		self._DbtAcct = value if type(value) != auto else self.make_default("DbtAcct")

	@DbtAcct.deleter
	def DbtAcct(self):
		del self._DbtAcct
		self._DbtAcct = None

	@property
	def AcctSvcr(self):
		return self._AcctSvcr

	@AcctSvcr.setter
	def AcctSvcr(self, value):
		self._AcctSvcr = value if type(value) != auto else self.make_default("AcctSvcr")

	@AcctSvcr.deleter
	def AcctSvcr(self):
		del self._AcctSvcr
		self._AcctSvcr = None

	@property
	def SttlmAdvc(self):
		return self._SttlmAdvc

	@SttlmAdvc.setter
	def SttlmAdvc(self, value):
		self._SttlmAdvc = value if type(value) != auto else self.make_default("SttlmAdvc")

	@SttlmAdvc.deleter
	def SttlmAdvc(self):
		del self._SttlmAdvc
		self._SttlmAdvc = None

	@property
	def SttlmCcyCd(self):
		return self._SttlmCcyCd

	@SttlmCcyCd.setter
	def SttlmCcyCd(self, value):
		self._SttlmCcyCd = value if type(value) != auto else self.make_default("SttlmCcyCd")

	@SttlmCcyCd.deleter
	def SttlmCcyCd(self):
		del self._SttlmCcyCd
		self._SttlmCcyCd = None

	@property
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if type(value) != auto else self.make_default("Tax")

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = None

	@property
	def AcctLvl(self):
		return self._AcctLvl

	@AcctLvl.setter
	def AcctLvl(self, value):
		self._AcctLvl = value if type(value) != auto else self.make_default("AcctLvl")

	@AcctLvl.deleter
	def AcctLvl(self):
		del self._AcctLvl
		self._AcctLvl = None

	@property
	def CompstnMtd(self):
		return self._CompstnMtd

	@CompstnMtd.setter
	def CompstnMtd(self, value):
		self._CompstnMtd = value if type(value) != auto else self.make_default("CompstnMtd")

	@CompstnMtd.deleter
	def CompstnMtd(self):
		del self._CompstnMtd
		self._CompstnMtd = None

	@property
	def PrntAcct(self):
		return self._PrntAcct

	@PrntAcct.setter
	def PrntAcct(self, value):
		self._PrntAcct = value if type(value) != auto else self.make_default("PrntAcct")

	@PrntAcct.deleter
	def PrntAcct(self):
		del self._PrntAcct
		self._PrntAcct = None

	@property
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if type(value) != auto else self.make_default("CshAcct")

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = None

	@property
	def AcctSvcrCtct(self):
		return self._AcctSvcrCtct

	@AcctSvcrCtct.setter
	def AcctSvcrCtct(self, value):
		self._AcctSvcrCtct = value if type(value) != auto else self.make_default("AcctSvcrCtct")

	@AcctSvcrCtct.deleter
	def AcctSvcrCtct(self):
		del self._AcctSvcrCtct
		self._AcctSvcrCtct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DelydDbtDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctBalCcyCd', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstCcyCd', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtAcct', type=AccountIdentification4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAdvc', type=Max105Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmCcyCd', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tax', type=AccountTax1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctLvl', type=AccountLevel2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CompstnMtd', type=CompensationMethod1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrntAcct', type=ParentCashAccount5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcct', type=CashAccount40, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcrCtct', type=Contact13, min=1, max=1, mutex_group=None, array=False),
	))

