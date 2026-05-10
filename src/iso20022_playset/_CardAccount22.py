from . import base_types
from ._PartyIdentification177Choice import PartyIdentification177Choice
from ._Max70Text import Max70Text
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._AmountAndDirection111 import AmountAndDirection111
from ._AccountIdentification80Choice import AccountIdentification80Choice
from ._CardAccountType3Code import CardAccountType3Code
from ._NameAndAddress3 import NameAndAddress3
from ._TrueFalseIndicator import TrueFalseIndicator
from ._Max35Text import Max35Text
from ._AccountChoiceMethod1Code import AccountChoiceMethod1Code

class CardAccount22(base_types._BaseFieldType):

	__slots__ = ["_SelctnMtd", "_CdtRef", "_SelctdAcctTp", "_Svcr", "_AcctNm", "_AcctIdr", "_Ccy", "_Bal", "_BalDispFlg", "_DfltAcctInd", "_AcctOwnr"]
	@property
	def SelctnMtd(self):
		return self._SelctnMtd

	@SelctnMtd.setter
	def SelctnMtd(self, value):
		self._SelctnMtd = value if type(value) != base_types.auto else self.make_default("SelctnMtd")

	@SelctnMtd.deleter
	def SelctnMtd(self):
		del self._SelctnMtd
		self._SelctnMtd = None

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
	def SelctdAcctTp(self):
		return self._SelctdAcctTp

	@SelctdAcctTp.setter
	def SelctdAcctTp(self, value):
		self._SelctdAcctTp = value if type(value) != base_types.auto else self.make_default("SelctdAcctTp")

	@SelctdAcctTp.deleter
	def SelctdAcctTp(self):
		del self._SelctdAcctTp
		self._SelctdAcctTp = None

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
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if type(value) != base_types.auto else self.make_default("AcctOwnr")

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SelctnMtd', type=AccountChoiceMethod1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SelctdAcctTp', type=CardAccountType3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Svcr', type=PartyIdentification177Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctIdr', type=AccountIdentification80Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bal', type=AmountAndDirection111, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalDispFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DfltAcctInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=NameAndAddress3, min=0, max=1, mutex_group=None, array=False),
	))

