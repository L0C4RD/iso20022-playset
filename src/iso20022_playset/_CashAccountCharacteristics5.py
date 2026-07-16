# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentification4Choice
from . import AccountLevel2Code
from . import AccountTax1
from . import ActiveOrHistoricCurrencyCode
from . import BranchAndFinancialInstitutionIdentification8
from . import CashAccount40
from . import CompensationMethod1Code
from . import Contact13
from . import ISODate
from . import Max105Text
from . import ParentCashAccount5

class CashAccountCharacteristics5(base_types._BaseFieldType):

	__slots__ = ["_AcctBalCcyCd", "_AcctLvl", "_AcctSvcr", "_AcctSvcrCtct", "_CompstnMtd", "_CshAcct", "_DbtAcct", "_DelydDbtDt", "_HstCcyCd", "_PrntAcct", "_SttlmAdvc", "_SttlmCcyCd", "_Tax"]
	@property
	def AcctBalCcyCd(self):
		return self._AcctBalCcyCd

	@AcctBalCcyCd.setter
	def AcctBalCcyCd(self, value):
		self._AcctBalCcyCd = value if value is not None else base_types.UninitialisedField(self, 'AcctBalCcyCd', ActiveOrHistoricCurrencyCode, False)

	@AcctBalCcyCd.deleter
	def AcctBalCcyCd(self):
		del self._AcctBalCcyCd
		self._AcctBalCcyCd = base_types.UninitialisedField(self, 'AcctBalCcyCd', ActiveOrHistoricCurrencyCode, False)

	@property
	def AcctLvl(self):
		return self._AcctLvl

	@AcctLvl.setter
	def AcctLvl(self, value):
		self._AcctLvl = value if value is not None else base_types.UninitialisedField(self, 'AcctLvl', AccountLevel2Code, False)

	@AcctLvl.deleter
	def AcctLvl(self):
		del self._AcctLvl
		self._AcctLvl = base_types.UninitialisedField(self, 'AcctLvl', AccountLevel2Code, False)

	@property
	def AcctSvcr(self):
		return self._AcctSvcr

	@AcctSvcr.setter
	def AcctSvcr(self, value):
		self._AcctSvcr = value if value is not None else base_types.UninitialisedField(self, 'AcctSvcr', BranchAndFinancialInstitutionIdentification8, False)

	@AcctSvcr.deleter
	def AcctSvcr(self):
		del self._AcctSvcr
		self._AcctSvcr = base_types.UninitialisedField(self, 'AcctSvcr', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def AcctSvcrCtct(self):
		return self._AcctSvcrCtct

	@AcctSvcrCtct.setter
	def AcctSvcrCtct(self, value):
		self._AcctSvcrCtct = value if value is not None else base_types.UninitialisedField(self, 'AcctSvcrCtct', Contact13, False)

	@AcctSvcrCtct.deleter
	def AcctSvcrCtct(self):
		del self._AcctSvcrCtct
		self._AcctSvcrCtct = base_types.UninitialisedField(self, 'AcctSvcrCtct', Contact13, False)

	@property
	def CompstnMtd(self):
		return self._CompstnMtd

	@CompstnMtd.setter
	def CompstnMtd(self, value):
		self._CompstnMtd = value if value is not None else base_types.UninitialisedField(self, 'CompstnMtd', CompensationMethod1Code, False)

	@CompstnMtd.deleter
	def CompstnMtd(self):
		del self._CompstnMtd
		self._CompstnMtd = base_types.UninitialisedField(self, 'CompstnMtd', CompensationMethod1Code, False)

	@property
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if value is not None else base_types.UninitialisedField(self, 'CshAcct', CashAccount40, False)

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = base_types.UninitialisedField(self, 'CshAcct', CashAccount40, False)

	@property
	def DbtAcct(self):
		return self._DbtAcct

	@DbtAcct.setter
	def DbtAcct(self, value):
		self._DbtAcct = value if value is not None else base_types.UninitialisedField(self, 'DbtAcct', AccountIdentification4Choice, False)

	@DbtAcct.deleter
	def DbtAcct(self):
		del self._DbtAcct
		self._DbtAcct = base_types.UninitialisedField(self, 'DbtAcct', AccountIdentification4Choice, False)

	@property
	def DelydDbtDt(self):
		return self._DelydDbtDt

	@DelydDbtDt.setter
	def DelydDbtDt(self, value):
		self._DelydDbtDt = value if value is not None else base_types.UninitialisedField(self, 'DelydDbtDt', ISODate, False)

	@DelydDbtDt.deleter
	def DelydDbtDt(self):
		del self._DelydDbtDt
		self._DelydDbtDt = base_types.UninitialisedField(self, 'DelydDbtDt', ISODate, False)

	@property
	def HstCcyCd(self):
		return self._HstCcyCd

	@HstCcyCd.setter
	def HstCcyCd(self, value):
		self._HstCcyCd = value if value is not None else base_types.UninitialisedField(self, 'HstCcyCd', ActiveOrHistoricCurrencyCode, False)

	@HstCcyCd.deleter
	def HstCcyCd(self):
		del self._HstCcyCd
		self._HstCcyCd = base_types.UninitialisedField(self, 'HstCcyCd', ActiveOrHistoricCurrencyCode, False)

	@property
	def PrntAcct(self):
		return self._PrntAcct

	@PrntAcct.setter
	def PrntAcct(self, value):
		self._PrntAcct = value if value is not None else base_types.UninitialisedField(self, 'PrntAcct', ParentCashAccount5, False)

	@PrntAcct.deleter
	def PrntAcct(self):
		del self._PrntAcct
		self._PrntAcct = base_types.UninitialisedField(self, 'PrntAcct', ParentCashAccount5, False)

	@property
	def SttlmAdvc(self):
		return self._SttlmAdvc

	@SttlmAdvc.setter
	def SttlmAdvc(self, value):
		self._SttlmAdvc = value if value is not None else base_types.UninitialisedField(self, 'SttlmAdvc', Max105Text, False)

	@SttlmAdvc.deleter
	def SttlmAdvc(self):
		del self._SttlmAdvc
		self._SttlmAdvc = base_types.UninitialisedField(self, 'SttlmAdvc', Max105Text, False)

	@property
	def SttlmCcyCd(self):
		return self._SttlmCcyCd

	@SttlmCcyCd.setter
	def SttlmCcyCd(self, value):
		self._SttlmCcyCd = value if value is not None else base_types.UninitialisedField(self, 'SttlmCcyCd', ActiveOrHistoricCurrencyCode, False)

	@SttlmCcyCd.deleter
	def SttlmCcyCd(self):
		del self._SttlmCcyCd
		self._SttlmCcyCd = base_types.UninitialisedField(self, 'SttlmCcyCd', ActiveOrHistoricCurrencyCode, False)

	@property
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if value is not None else base_types.UninitialisedField(self, 'Tax', AccountTax1, False)

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = base_types.UninitialisedField(self, 'Tax', AccountTax1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctBalCcyCd', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctLvl', type=AccountLevel2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcrCtct', type=Contact13, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CompstnMtd', type=CompensationMethod1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcct', type=CashAccount40, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtAcct', type=AccountIdentification4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DelydDbtDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstCcyCd', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrntAcct', type=ParentCashAccount5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAdvc', type=Max105Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmCcyCd', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tax', type=AccountTax1, min=0, max=1, mutex_group=None, array=False),
	))