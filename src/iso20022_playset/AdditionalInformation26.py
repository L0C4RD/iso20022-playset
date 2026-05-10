import base_types
import YesNoIndicator
import FinancialInstrumentQuantity33Choice
import ClassificationType32Choice
import PartyIdentificationAndAccount195
import SecuritiesAccount19
import DateAndDateTime2Choice
import Max35Text
import SecurityIdentification19
import PartyIdentification136
import BlockChainAddressWallet3

class AdditionalInformation26(base_types._BaseFieldType):

	__slots__ = ["_Qty", "_Invstr", "_TxSbjtToBuyIn", "_ClssfctnTp", "_DlvrgPty1", "_AcctOwnrTxId", "_RcvgPty1", "_XpryDt", "_CutOffDt", "_BlckChainAdrOrWllt", "_FctvDt", "_FinInstrmId", "_SfkpgAcct"]
	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	@property
	def Invstr(self):
		return self._Invstr

	@Invstr.setter
	def Invstr(self, value):
		self._Invstr = value if type(value) != auto else self.make_default("Invstr")

	@Invstr.deleter
	def Invstr(self):
		del self._Invstr
		self._Invstr = None

	@property
	def TxSbjtToBuyIn(self):
		return self._TxSbjtToBuyIn

	@TxSbjtToBuyIn.setter
	def TxSbjtToBuyIn(self, value):
		self._TxSbjtToBuyIn = value if type(value) != auto else self.make_default("TxSbjtToBuyIn")

	@TxSbjtToBuyIn.deleter
	def TxSbjtToBuyIn(self):
		del self._TxSbjtToBuyIn
		self._TxSbjtToBuyIn = None

	@property
	def ClssfctnTp(self):
		return self._ClssfctnTp

	@ClssfctnTp.setter
	def ClssfctnTp(self, value):
		self._ClssfctnTp = value if type(value) != auto else self.make_default("ClssfctnTp")

	@ClssfctnTp.deleter
	def ClssfctnTp(self):
		del self._ClssfctnTp
		self._ClssfctnTp = None

	@property
	def DlvrgPty1(self):
		return self._DlvrgPty1

	@DlvrgPty1.setter
	def DlvrgPty1(self, value):
		self._DlvrgPty1 = value if type(value) != auto else self.make_default("DlvrgPty1")

	@DlvrgPty1.deleter
	def DlvrgPty1(self):
		del self._DlvrgPty1
		self._DlvrgPty1 = None

	@property
	def AcctOwnrTxId(self):
		return self._AcctOwnrTxId

	@AcctOwnrTxId.setter
	def AcctOwnrTxId(self, value):
		self._AcctOwnrTxId = value if type(value) != auto else self.make_default("AcctOwnrTxId")

	@AcctOwnrTxId.deleter
	def AcctOwnrTxId(self):
		del self._AcctOwnrTxId
		self._AcctOwnrTxId = None

	@property
	def RcvgPty1(self):
		return self._RcvgPty1

	@RcvgPty1.setter
	def RcvgPty1(self, value):
		self._RcvgPty1 = value if type(value) != auto else self.make_default("RcvgPty1")

	@RcvgPty1.deleter
	def RcvgPty1(self):
		del self._RcvgPty1
		self._RcvgPty1 = None

	@property
	def XpryDt(self):
		return self._XpryDt

	@XpryDt.setter
	def XpryDt(self, value):
		self._XpryDt = value if type(value) != auto else self.make_default("XpryDt")

	@XpryDt.deleter
	def XpryDt(self):
		del self._XpryDt
		self._XpryDt = None

	@property
	def CutOffDt(self):
		return self._CutOffDt

	@CutOffDt.setter
	def CutOffDt(self, value):
		self._CutOffDt = value if type(value) != auto else self.make_default("CutOffDt")

	@CutOffDt.deleter
	def CutOffDt(self):
		del self._CutOffDt
		self._CutOffDt = None

	@property
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if type(value) != auto else self.make_default("BlckChainAdrOrWllt")

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = None

	@property
	def FctvDt(self):
		return self._FctvDt

	@FctvDt.setter
	def FctvDt(self, value):
		self._FctvDt = value if type(value) != auto else self.make_default("FctvDt")

	@FctvDt.deleter
	def FctvDt(self):
		del self._FctvDt
		self._FctvDt = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if type(value) != auto else self.make_default("SfkpgAcct")

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity33Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Invstr', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSbjtToBuyIn', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClssfctnTp', type=ClassificationType32Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrgPty1', type=PartyIdentificationAndAccount195, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvgPty1', type=PartyIdentificationAndAccount195, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CutOffDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
	))

