# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import BlockChainAddressWallet5
from . import ClosingDate4Choice
from . import CollateralAccount3
from . import CollateralRole1Code
from . import CollateralTransactionType1Choice
from . import DateAndDateTime2Choice
from . import ExposureType21Choice
from . import GenericIdentification30
from . import PartyIdentification178Choice

class Obligation8(base_types._BaseFieldType):

	__slots__ = ["_BlckChainAdrOrWllt", "_ClsgDt", "_CollAcctId", "_CollSd", "_CollTxTp", "_PtyA", "_PtyB", "_ReqdExctnDt", "_SttlmPrc", "_SvcgPtyA", "_SvcgPtyB", "_ValtnDt", "_XpsrAmt", "_XpsrTp"]
	@property
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if value is not None else base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', BlockChainAddressWallet5, False)

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', BlockChainAddressWallet5, False)

	@property
	def ClsgDt(self):
		return self._ClsgDt

	@ClsgDt.setter
	def ClsgDt(self, value):
		self._ClsgDt = value if value is not None else base_types.UninitialisedField(self, 'ClsgDt', ClosingDate4Choice, False)

	@ClsgDt.deleter
	def ClsgDt(self):
		del self._ClsgDt
		self._ClsgDt = base_types.UninitialisedField(self, 'ClsgDt', ClosingDate4Choice, False)

	@property
	def CollAcctId(self):
		return self._CollAcctId

	@CollAcctId.setter
	def CollAcctId(self, value):
		self._CollAcctId = value if value is not None else base_types.UninitialisedField(self, 'CollAcctId', CollateralAccount3, False)

	@CollAcctId.deleter
	def CollAcctId(self):
		del self._CollAcctId
		self._CollAcctId = base_types.UninitialisedField(self, 'CollAcctId', CollateralAccount3, False)

	@property
	def CollSd(self):
		return self._CollSd

	@CollSd.setter
	def CollSd(self, value):
		self._CollSd = value if value is not None else base_types.UninitialisedField(self, 'CollSd', CollateralRole1Code, False)

	@CollSd.deleter
	def CollSd(self):
		del self._CollSd
		self._CollSd = base_types.UninitialisedField(self, 'CollSd', CollateralRole1Code, False)

	@property
	def CollTxTp(self):
		return self._CollTxTp

	@CollTxTp.setter
	def CollTxTp(self, value):
		self._CollTxTp = value if value is not None else base_types.UninitialisedField(self, 'CollTxTp', CollateralTransactionType1Choice, False)

	@CollTxTp.deleter
	def CollTxTp(self):
		del self._CollTxTp
		self._CollTxTp = base_types.UninitialisedField(self, 'CollTxTp', CollateralTransactionType1Choice, False)

	@property
	def PtyA(self):
		return self._PtyA

	@PtyA.setter
	def PtyA(self, value):
		self._PtyA = value if value is not None else base_types.UninitialisedField(self, 'PtyA', PartyIdentification178Choice, False)

	@PtyA.deleter
	def PtyA(self):
		del self._PtyA
		self._PtyA = base_types.UninitialisedField(self, 'PtyA', PartyIdentification178Choice, False)

	@property
	def PtyB(self):
		return self._PtyB

	@PtyB.setter
	def PtyB(self, value):
		self._PtyB = value if value is not None else base_types.UninitialisedField(self, 'PtyB', PartyIdentification178Choice, False)

	@PtyB.deleter
	def PtyB(self):
		del self._PtyB
		self._PtyB = base_types.UninitialisedField(self, 'PtyB', PartyIdentification178Choice, False)

	@property
	def ReqdExctnDt(self):
		return self._ReqdExctnDt

	@ReqdExctnDt.setter
	def ReqdExctnDt(self, value):
		self._ReqdExctnDt = value if value is not None else base_types.UninitialisedField(self, 'ReqdExctnDt', DateAndDateTime2Choice, False)

	@ReqdExctnDt.deleter
	def ReqdExctnDt(self):
		del self._ReqdExctnDt
		self._ReqdExctnDt = base_types.UninitialisedField(self, 'ReqdExctnDt', DateAndDateTime2Choice, False)

	@property
	def SttlmPrc(self):
		return self._SttlmPrc

	@SttlmPrc.setter
	def SttlmPrc(self, value):
		self._SttlmPrc = value if value is not None else base_types.UninitialisedField(self, 'SttlmPrc', GenericIdentification30, False)

	@SttlmPrc.deleter
	def SttlmPrc(self):
		del self._SttlmPrc
		self._SttlmPrc = base_types.UninitialisedField(self, 'SttlmPrc', GenericIdentification30, False)

	@property
	def SvcgPtyA(self):
		return self._SvcgPtyA

	@SvcgPtyA.setter
	def SvcgPtyA(self, value):
		self._SvcgPtyA = value if value is not None else base_types.UninitialisedField(self, 'SvcgPtyA', PartyIdentification178Choice, False)

	@SvcgPtyA.deleter
	def SvcgPtyA(self):
		del self._SvcgPtyA
		self._SvcgPtyA = base_types.UninitialisedField(self, 'SvcgPtyA', PartyIdentification178Choice, False)

	@property
	def SvcgPtyB(self):
		return self._SvcgPtyB

	@SvcgPtyB.setter
	def SvcgPtyB(self, value):
		self._SvcgPtyB = value if value is not None else base_types.UninitialisedField(self, 'SvcgPtyB', PartyIdentification178Choice, False)

	@SvcgPtyB.deleter
	def SvcgPtyB(self):
		del self._SvcgPtyB
		self._SvcgPtyB = base_types.UninitialisedField(self, 'SvcgPtyB', PartyIdentification178Choice, False)

	@property
	def ValtnDt(self):
		return self._ValtnDt

	@ValtnDt.setter
	def ValtnDt(self, value):
		self._ValtnDt = value if value is not None else base_types.UninitialisedField(self, 'ValtnDt', DateAndDateTime2Choice, False)

	@ValtnDt.deleter
	def ValtnDt(self):
		del self._ValtnDt
		self._ValtnDt = base_types.UninitialisedField(self, 'ValtnDt', DateAndDateTime2Choice, False)

	@property
	def XpsrAmt(self):
		return self._XpsrAmt

	@XpsrAmt.setter
	def XpsrAmt(self, value):
		self._XpsrAmt = value if value is not None else base_types.UninitialisedField(self, 'XpsrAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@XpsrAmt.deleter
	def XpsrAmt(self):
		del self._XpsrAmt
		self._XpsrAmt = base_types.UninitialisedField(self, 'XpsrAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def XpsrTp(self):
		return self._XpsrTp

	@XpsrTp.setter
	def XpsrTp(self, value):
		self._XpsrTp = value if value is not None else base_types.UninitialisedField(self, 'XpsrTp', ExposureType21Choice, False)

	@XpsrTp.deleter
	def XpsrTp(self):
		del self._XpsrTp
		self._XpsrTp = base_types.UninitialisedField(self, 'XpsrTp', ExposureType21Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsgDt', type=ClosingDate4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollAcctId', type=CollateralAccount3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollSd', type=CollateralRole1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollTxTp', type=CollateralTransactionType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyA', type=PartyIdentification178Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyB', type=PartyIdentification178Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdExctnDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPrc', type=GenericIdentification30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcgPtyA', type=PartyIdentification178Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcgPtyB', type=PartyIdentification178Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsrAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsrTp', type=ExposureType21Choice, min=0, max=1, mutex_group=None, array=False),
	))