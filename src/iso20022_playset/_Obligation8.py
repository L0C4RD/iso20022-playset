from . import base_types
from .GenericIdentification30 import GenericIdentification30
from .CollateralAccount3 import CollateralAccount3
from .CollateralRole1Code import CollateralRole1Code
from .ClosingDate4Choice import ClosingDate4Choice
from .BlockChainAddressWallet5 import BlockChainAddressWallet5
from .CollateralTransactionType1Choice import CollateralTransactionType1Choice
from .ExposureType21Choice import ExposureType21Choice
from .ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from .PartyIdentification178Choice import PartyIdentification178Choice
from .DateAndDateTime2Choice import DateAndDateTime2Choice

class Obligation8(base_types._BaseFieldType):

	__slots__ = ["_PtyB", "_ValtnDt", "_XpsrAmt", "_XpsrTp", "_BlckChainAdrOrWllt", "_CollSd", "_SvcgPtyA", "_PtyA", "_SvcgPtyB", "_CollTxTp", "_ReqdExctnDt", "_SttlmPrc", "_ClsgDt", "_CollAcctId"]
	@property
	def PtyB(self):
		return self._PtyB

	@PtyB.setter
	def PtyB(self, value):
		self._PtyB = value if type(value) != base_types.auto else self.make_default("PtyB")

	@PtyB.deleter
	def PtyB(self):
		del self._PtyB
		self._PtyB = None

	@property
	def ValtnDt(self):
		return self._ValtnDt

	@ValtnDt.setter
	def ValtnDt(self, value):
		self._ValtnDt = value if type(value) != base_types.auto else self.make_default("ValtnDt")

	@ValtnDt.deleter
	def ValtnDt(self):
		del self._ValtnDt
		self._ValtnDt = None

	@property
	def XpsrAmt(self):
		return self._XpsrAmt

	@XpsrAmt.setter
	def XpsrAmt(self, value):
		self._XpsrAmt = value if type(value) != base_types.auto else self.make_default("XpsrAmt")

	@XpsrAmt.deleter
	def XpsrAmt(self):
		del self._XpsrAmt
		self._XpsrAmt = None

	@property
	def XpsrTp(self):
		return self._XpsrTp

	@XpsrTp.setter
	def XpsrTp(self, value):
		self._XpsrTp = value if type(value) != base_types.auto else self.make_default("XpsrTp")

	@XpsrTp.deleter
	def XpsrTp(self):
		del self._XpsrTp
		self._XpsrTp = None

	@property
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if type(value) != base_types.auto else self.make_default("BlckChainAdrOrWllt")

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = None

	@property
	def CollSd(self):
		return self._CollSd

	@CollSd.setter
	def CollSd(self, value):
		self._CollSd = value if type(value) != base_types.auto else self.make_default("CollSd")

	@CollSd.deleter
	def CollSd(self):
		del self._CollSd
		self._CollSd = None

	@property
	def SvcgPtyA(self):
		return self._SvcgPtyA

	@SvcgPtyA.setter
	def SvcgPtyA(self, value):
		self._SvcgPtyA = value if type(value) != base_types.auto else self.make_default("SvcgPtyA")

	@SvcgPtyA.deleter
	def SvcgPtyA(self):
		del self._SvcgPtyA
		self._SvcgPtyA = None

	@property
	def PtyA(self):
		return self._PtyA

	@PtyA.setter
	def PtyA(self, value):
		self._PtyA = value if type(value) != base_types.auto else self.make_default("PtyA")

	@PtyA.deleter
	def PtyA(self):
		del self._PtyA
		self._PtyA = None

	@property
	def SvcgPtyB(self):
		return self._SvcgPtyB

	@SvcgPtyB.setter
	def SvcgPtyB(self, value):
		self._SvcgPtyB = value if type(value) != base_types.auto else self.make_default("SvcgPtyB")

	@SvcgPtyB.deleter
	def SvcgPtyB(self):
		del self._SvcgPtyB
		self._SvcgPtyB = None

	@property
	def CollTxTp(self):
		return self._CollTxTp

	@CollTxTp.setter
	def CollTxTp(self, value):
		self._CollTxTp = value if type(value) != base_types.auto else self.make_default("CollTxTp")

	@CollTxTp.deleter
	def CollTxTp(self):
		del self._CollTxTp
		self._CollTxTp = None

	@property
	def ReqdExctnDt(self):
		return self._ReqdExctnDt

	@ReqdExctnDt.setter
	def ReqdExctnDt(self, value):
		self._ReqdExctnDt = value if type(value) != base_types.auto else self.make_default("ReqdExctnDt")

	@ReqdExctnDt.deleter
	def ReqdExctnDt(self):
		del self._ReqdExctnDt
		self._ReqdExctnDt = None

	@property
	def SttlmPrc(self):
		return self._SttlmPrc

	@SttlmPrc.setter
	def SttlmPrc(self, value):
		self._SttlmPrc = value if type(value) != base_types.auto else self.make_default("SttlmPrc")

	@SttlmPrc.deleter
	def SttlmPrc(self):
		del self._SttlmPrc
		self._SttlmPrc = None

	@property
	def ClsgDt(self):
		return self._ClsgDt

	@ClsgDt.setter
	def ClsgDt(self, value):
		self._ClsgDt = value if type(value) != base_types.auto else self.make_default("ClsgDt")

	@ClsgDt.deleter
	def ClsgDt(self):
		del self._ClsgDt
		self._ClsgDt = None

	@property
	def CollAcctId(self):
		return self._CollAcctId

	@CollAcctId.setter
	def CollAcctId(self, value):
		self._CollAcctId = value if type(value) != base_types.auto else self.make_default("CollAcctId")

	@CollAcctId.deleter
	def CollAcctId(self):
		del self._CollAcctId
		self._CollAcctId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PtyB', type=PartyIdentification178Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsrAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsrTp', type=ExposureType21Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollSd', type=CollateralRole1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcgPtyA', type=PartyIdentification178Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyA', type=PartyIdentification178Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcgPtyB', type=PartyIdentification178Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollTxTp', type=CollateralTransactionType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdExctnDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPrc', type=GenericIdentification30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsgDt', type=ClosingDate4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollAcctId', type=CollateralAccount3, min=0, max=1, mutex_group=None, array=False),
	))

