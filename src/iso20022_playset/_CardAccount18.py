from . import base_types
from ._TrueFalseIndicator import TrueFalseIndicator
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._ATMService29 import ATMService29
from ._ATMAccountUsage1Code import ATMAccountUsage1Code
from ._AmountAndDirection111 import AmountAndDirection111
from ._AccountIdentification80Choice import AccountIdentification80Choice
from ._PartyIdentification177Choice import PartyIdentification177Choice
from ._Max35Text import Max35Text
from ._Max70Text import Max70Text
from ._CardAccountType3Code import CardAccountType3Code

class CardAccount18(base_types._BaseFieldType):

	__slots__ = ["_AcctNm", "_CdtRef", "_Svcr", "_AllwdSvc", "_AcctTp", "_BalDispFlg", "_AcctIdr", "_DfltAcctInd", "_AcctUsgCd", "_Bal", "_Ccy"]
	@property
	def AcctIdr(self):
		return self._AcctIdr

	@AcctIdr.setter
	def AcctIdr(self, value):
		self._AcctIdr = value if type(value) != base_types.auto else self.make_default("AcctIdr")

	@AcctIdr.deleter
	def AcctIdr(self):
		del self._AcctIdr
		self._AcctIdr = None

	@property
	def AcctNm(self):
		return self._AcctNm

	@AcctNm.setter
	def AcctNm(self, value):
		self._AcctNm = value if type(value) != base_types.auto else self.make_default("AcctNm")

	@AcctNm.deleter
	def AcctNm(self):
		del self._AcctNm
		self._AcctNm = None

	@property
	def AcctTp(self):
		return self._AcctTp

	@AcctTp.setter
	def AcctTp(self, value):
		self._AcctTp = value if type(value) != base_types.auto else self.make_default("AcctTp")

	@AcctTp.deleter
	def AcctTp(self):
		del self._AcctTp
		self._AcctTp = None

	@property
	def AcctUsgCd(self):
		return self._AcctUsgCd

	@AcctUsgCd.setter
	def AcctUsgCd(self, value):
		self._AcctUsgCd = value if type(value) != base_types.auto else self.make_default("AcctUsgCd")

	@AcctUsgCd.deleter
	def AcctUsgCd(self):
		del self._AcctUsgCd
		self._AcctUsgCd = None

	@property
	def AllwdSvc(self):
		return self._AllwdSvc

	@AllwdSvc.setter
	def AllwdSvc(self, value):
		self._AllwdSvc = value if type(value) != base_types.auto else self.make_default("AllwdSvc")

	@AllwdSvc.deleter
	def AllwdSvc(self):
		del self._AllwdSvc
		self._AllwdSvc = None

	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if type(value) != base_types.auto else self.make_default("Bal")

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = None

	@property
	def BalDispFlg(self):
		return self._BalDispFlg

	@BalDispFlg.setter
	def BalDispFlg(self, value):
		self._BalDispFlg = value if type(value) != base_types.auto else self.make_default("BalDispFlg")

	@BalDispFlg.deleter
	def BalDispFlg(self):
		del self._BalDispFlg
		self._BalDispFlg = None

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != base_types.auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def CdtRef(self):
		return self._CdtRef

	@CdtRef.setter
	def CdtRef(self, value):
		self._CdtRef = value if type(value) != base_types.auto else self.make_default("CdtRef")

	@CdtRef.deleter
	def CdtRef(self):
		del self._CdtRef
		self._CdtRef = None

	@property
	def DfltAcctInd(self):
		return self._DfltAcctInd

	@DfltAcctInd.setter
	def DfltAcctInd(self, value):
		self._DfltAcctInd = value if type(value) != base_types.auto else self.make_default("DfltAcctInd")

	@DfltAcctInd.deleter
	def DfltAcctInd(self):
		del self._DfltAcctInd
		self._DfltAcctInd = None

	@property
	def Svcr(self):
		return self._Svcr

	@Svcr.setter
	def Svcr(self, value):
		self._Svcr = value if type(value) != base_types.auto else self.make_default("Svcr")

	@Svcr.deleter
	def Svcr(self):
		del self._Svcr
		self._Svcr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctIdr', type=AccountIdentification80Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctTp', type=CardAccountType3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctUsgCd', type=ATMAccountUsage1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AllwdSvc', type=ATMService29, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Bal', type=AmountAndDirection111, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BalDispFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DfltAcctInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Svcr', type=PartyIdentification177Choice, min=0, max=1, mutex_group=None, array=False),
	))

