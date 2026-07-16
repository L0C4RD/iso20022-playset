# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BlockChainAddressWallet7
from . import ClassificationType33Choice
from . import DateAndDateTime2Choice
from . import FinancialInstrumentQuantity36Choice
from . import PartyIdentification157
from . import PartyIdentificationAndAccount215
from . import RestrictedFINXMax16Text
from . import SecuritiesAccount30
from . import SecurityIdentification20
from . import YesNoIndicator

class AdditionalInformation28(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnrTxId", "_BlckChainAdrOrWllt", "_ClssfctnTp", "_CutOffDt", "_DlvrgPty1", "_FctvDt", "_FinInstrmId", "_Invstr", "_Qty", "_RcvgPty1", "_SfkpgAcct", "_TxSbjtToBuyIn", "_XpryDt"]
	@property
	def AcctOwnrTxId(self):
		return self._AcctOwnrTxId

	@AcctOwnrTxId.setter
	def AcctOwnrTxId(self, value):
		self._AcctOwnrTxId = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnrTxId', RestrictedFINXMax16Text, False)

	@AcctOwnrTxId.deleter
	def AcctOwnrTxId(self):
		del self._AcctOwnrTxId
		self._AcctOwnrTxId = base_types.UninitialisedField(self, 'AcctOwnrTxId', RestrictedFINXMax16Text, False)

	@property
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if value is not None else base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', BlockChainAddressWallet7, False)

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', BlockChainAddressWallet7, False)

	@property
	def ClssfctnTp(self):
		return self._ClssfctnTp

	@ClssfctnTp.setter
	def ClssfctnTp(self, value):
		self._ClssfctnTp = value if value is not None else base_types.UninitialisedField(self, 'ClssfctnTp', ClassificationType33Choice, False)

	@ClssfctnTp.deleter
	def ClssfctnTp(self):
		del self._ClssfctnTp
		self._ClssfctnTp = base_types.UninitialisedField(self, 'ClssfctnTp', ClassificationType33Choice, False)

	@property
	def CutOffDt(self):
		return self._CutOffDt

	@CutOffDt.setter
	def CutOffDt(self, value):
		self._CutOffDt = value if value is not None else base_types.UninitialisedField(self, 'CutOffDt', DateAndDateTime2Choice, False)

	@CutOffDt.deleter
	def CutOffDt(self):
		del self._CutOffDt
		self._CutOffDt = base_types.UninitialisedField(self, 'CutOffDt', DateAndDateTime2Choice, False)

	@property
	def DlvrgPty1(self):
		return self._DlvrgPty1

	@DlvrgPty1.setter
	def DlvrgPty1(self, value):
		self._DlvrgPty1 = value if value is not None else base_types.UninitialisedField(self, 'DlvrgPty1', PartyIdentificationAndAccount215, False)

	@DlvrgPty1.deleter
	def DlvrgPty1(self):
		del self._DlvrgPty1
		self._DlvrgPty1 = base_types.UninitialisedField(self, 'DlvrgPty1', PartyIdentificationAndAccount215, False)

	@property
	def FctvDt(self):
		return self._FctvDt

	@FctvDt.setter
	def FctvDt(self, value):
		self._FctvDt = value if value is not None else base_types.UninitialisedField(self, 'FctvDt', DateAndDateTime2Choice, False)

	@FctvDt.deleter
	def FctvDt(self):
		del self._FctvDt
		self._FctvDt = base_types.UninitialisedField(self, 'FctvDt', DateAndDateTime2Choice, False)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification20, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification20, False)

	@property
	def Invstr(self):
		return self._Invstr

	@Invstr.setter
	def Invstr(self, value):
		self._Invstr = value if value is not None else base_types.UninitialisedField(self, 'Invstr', PartyIdentification157, False)

	@Invstr.deleter
	def Invstr(self):
		del self._Invstr
		self._Invstr = base_types.UninitialisedField(self, 'Invstr', PartyIdentification157, False)

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', FinancialInstrumentQuantity36Choice, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', FinancialInstrumentQuantity36Choice, False)

	@property
	def RcvgPty1(self):
		return self._RcvgPty1

	@RcvgPty1.setter
	def RcvgPty1(self, value):
		self._RcvgPty1 = value if value is not None else base_types.UninitialisedField(self, 'RcvgPty1', PartyIdentificationAndAccount215, False)

	@RcvgPty1.deleter
	def RcvgPty1(self):
		del self._RcvgPty1
		self._RcvgPty1 = base_types.UninitialisedField(self, 'RcvgPty1', PartyIdentificationAndAccount215, False)

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if value is not None else base_types.UninitialisedField(self, 'SfkpgAcct', SecuritiesAccount30, False)

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = base_types.UninitialisedField(self, 'SfkpgAcct', SecuritiesAccount30, False)

	@property
	def TxSbjtToBuyIn(self):
		return self._TxSbjtToBuyIn

	@TxSbjtToBuyIn.setter
	def TxSbjtToBuyIn(self, value):
		self._TxSbjtToBuyIn = value if value is not None else base_types.UninitialisedField(self, 'TxSbjtToBuyIn', YesNoIndicator, False)

	@TxSbjtToBuyIn.deleter
	def TxSbjtToBuyIn(self):
		del self._TxSbjtToBuyIn
		self._TxSbjtToBuyIn = base_types.UninitialisedField(self, 'TxSbjtToBuyIn', YesNoIndicator, False)

	@property
	def XpryDt(self):
		return self._XpryDt

	@XpryDt.setter
	def XpryDt(self, value):
		self._XpryDt = value if value is not None else base_types.UninitialisedField(self, 'XpryDt', DateAndDateTime2Choice, False)

	@XpryDt.deleter
	def XpryDt(self):
		del self._XpryDt
		self._XpryDt = base_types.UninitialisedField(self, 'XpryDt', DateAndDateTime2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnrTxId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClssfctnTp', type=ClassificationType33Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CutOffDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrgPty1', type=PartyIdentificationAndAccount215, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Invstr', type=PartyIdentification157, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity36Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvgPty1', type=PartyIdentificationAndAccount215, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSbjtToBuyIn', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
	))