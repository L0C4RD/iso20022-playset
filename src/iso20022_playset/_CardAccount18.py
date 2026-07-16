# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMAccountUsage1Code
from . import ATMService29
from . import AccountIdentification80Choice
from . import ActiveCurrencyCode
from . import AmountAndDirection111
from . import CardAccountType3Code
from . import Max35Text
from . import Max70Text
from . import PartyIdentification177Choice
from . import TrueFalseIndicator

class CardAccount18(base_types._BaseFieldType):

	__slots__ = ["_AcctIdr", "_AcctNm", "_AcctTp", "_AcctUsgCd", "_AllwdSvc", "_Bal", "_BalDispFlg", "_Ccy", "_CdtRef", "_DfltAcctInd", "_Svcr"]
	@property
	def AcctIdr(self):
		return self._AcctIdr

	@AcctIdr.setter
	def AcctIdr(self, value):
		self._AcctIdr = value if value is not None else base_types.UninitialisedField(self, 'AcctIdr', AccountIdentification80Choice, False)

	@AcctIdr.deleter
	def AcctIdr(self):
		del self._AcctIdr
		self._AcctIdr = base_types.UninitialisedField(self, 'AcctIdr', AccountIdentification80Choice, False)

	@property
	def AcctNm(self):
		return self._AcctNm

	@AcctNm.setter
	def AcctNm(self, value):
		self._AcctNm = value if value is not None else base_types.UninitialisedField(self, 'AcctNm', Max70Text, False)

	@AcctNm.deleter
	def AcctNm(self):
		del self._AcctNm
		self._AcctNm = base_types.UninitialisedField(self, 'AcctNm', Max70Text, False)

	@property
	def AcctTp(self):
		return self._AcctTp

	@AcctTp.setter
	def AcctTp(self, value):
		self._AcctTp = value if value is not None else base_types.UninitialisedField(self, 'AcctTp', CardAccountType3Code, False)

	@AcctTp.deleter
	def AcctTp(self):
		del self._AcctTp
		self._AcctTp = base_types.UninitialisedField(self, 'AcctTp', CardAccountType3Code, False)

	@property
	def AcctUsgCd(self):
		return self._AcctUsgCd

	@AcctUsgCd.setter
	def AcctUsgCd(self, value):
		self._AcctUsgCd = value if value is not None else base_types.UninitialisedField(self, 'AcctUsgCd', ATMAccountUsage1Code, False)

	@AcctUsgCd.deleter
	def AcctUsgCd(self):
		del self._AcctUsgCd
		self._AcctUsgCd = base_types.UninitialisedField(self, 'AcctUsgCd', ATMAccountUsage1Code, False)

	@property
	def AllwdSvc(self):
		return self._AllwdSvc

	@AllwdSvc.setter
	def AllwdSvc(self, value):
		self._AllwdSvc = value if value is not None else base_types.UninitialisedField(self, 'AllwdSvc', ATMService29, True)

	@AllwdSvc.deleter
	def AllwdSvc(self):
		del self._AllwdSvc
		self._AllwdSvc = base_types.UninitialisedField(self, 'AllwdSvc', ATMService29, True)

	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if value is not None else base_types.UninitialisedField(self, 'Bal', AmountAndDirection111, True)

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = base_types.UninitialisedField(self, 'Bal', AmountAndDirection111, True)

	@property
	def BalDispFlg(self):
		return self._BalDispFlg

	@BalDispFlg.setter
	def BalDispFlg(self, value):
		self._BalDispFlg = value if value is not None else base_types.UninitialisedField(self, 'BalDispFlg', TrueFalseIndicator, False)

	@BalDispFlg.deleter
	def BalDispFlg(self):
		del self._BalDispFlg
		self._BalDispFlg = base_types.UninitialisedField(self, 'BalDispFlg', TrueFalseIndicator, False)

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@property
	def CdtRef(self):
		return self._CdtRef

	@CdtRef.setter
	def CdtRef(self, value):
		self._CdtRef = value if value is not None else base_types.UninitialisedField(self, 'CdtRef', Max35Text, False)

	@CdtRef.deleter
	def CdtRef(self):
		del self._CdtRef
		self._CdtRef = base_types.UninitialisedField(self, 'CdtRef', Max35Text, False)

	@property
	def DfltAcctInd(self):
		return self._DfltAcctInd

	@DfltAcctInd.setter
	def DfltAcctInd(self, value):
		self._DfltAcctInd = value if value is not None else base_types.UninitialisedField(self, 'DfltAcctInd', TrueFalseIndicator, False)

	@DfltAcctInd.deleter
	def DfltAcctInd(self):
		del self._DfltAcctInd
		self._DfltAcctInd = base_types.UninitialisedField(self, 'DfltAcctInd', TrueFalseIndicator, False)

	@property
	def Svcr(self):
		return self._Svcr

	@Svcr.setter
	def Svcr(self, value):
		self._Svcr = value if value is not None else base_types.UninitialisedField(self, 'Svcr', PartyIdentification177Choice, False)

	@Svcr.deleter
	def Svcr(self):
		del self._Svcr
		self._Svcr = base_types.UninitialisedField(self, 'Svcr', PartyIdentification177Choice, False)

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