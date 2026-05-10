from . import base_types
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from ._ISODate import ISODate
from ._Max35Text import Max35Text
from ._PartyIdentification272 import PartyIdentification272
from ._TransferInstruction1 import TransferInstruction1
from ._YesNoIndicator import YesNoIndicator

class DirectDebitInstructionDetails3(base_types._BaseFieldType):

	__slots__ = ["_AutomtdDrctDbtInstrInd", "_Cdtr", "_DrctDbtTrfblInd", "_LastColltnCcyAmt", "_LastColltnDt", "_MndtId", "_OthrDtls"]
	@property
	def AutomtdDrctDbtInstrInd(self):
		return self._AutomtdDrctDbtInstrInd

	@AutomtdDrctDbtInstrInd.setter
	def AutomtdDrctDbtInstrInd(self, value):
		self._AutomtdDrctDbtInstrInd = value if type(value) != base_types.auto else self.make_default("AutomtdDrctDbtInstrInd")

	@AutomtdDrctDbtInstrInd.deleter
	def AutomtdDrctDbtInstrInd(self):
		del self._AutomtdDrctDbtInstrInd
		self._AutomtdDrctDbtInstrInd = None

	@property
	def Cdtr(self):
		return self._Cdtr

	@Cdtr.setter
	def Cdtr(self, value):
		self._Cdtr = value if type(value) != base_types.auto else self.make_default("Cdtr")

	@Cdtr.deleter
	def Cdtr(self):
		del self._Cdtr
		self._Cdtr = None

	@property
	def DrctDbtTrfblInd(self):
		return self._DrctDbtTrfblInd

	@DrctDbtTrfblInd.setter
	def DrctDbtTrfblInd(self, value):
		self._DrctDbtTrfblInd = value if type(value) != base_types.auto else self.make_default("DrctDbtTrfblInd")

	@DrctDbtTrfblInd.deleter
	def DrctDbtTrfblInd(self):
		del self._DrctDbtTrfblInd
		self._DrctDbtTrfblInd = None

	@property
	def LastColltnCcyAmt(self):
		return self._LastColltnCcyAmt

	@LastColltnCcyAmt.setter
	def LastColltnCcyAmt(self, value):
		self._LastColltnCcyAmt = value if type(value) != base_types.auto else self.make_default("LastColltnCcyAmt")

	@LastColltnCcyAmt.deleter
	def LastColltnCcyAmt(self):
		del self._LastColltnCcyAmt
		self._LastColltnCcyAmt = None

	@property
	def LastColltnDt(self):
		return self._LastColltnDt

	@LastColltnDt.setter
	def LastColltnDt(self, value):
		self._LastColltnDt = value if type(value) != base_types.auto else self.make_default("LastColltnDt")

	@LastColltnDt.deleter
	def LastColltnDt(self):
		del self._LastColltnDt
		self._LastColltnDt = None

	@property
	def MndtId(self):
		return self._MndtId

	@MndtId.setter
	def MndtId(self, value):
		self._MndtId = value if type(value) != base_types.auto else self.make_default("MndtId")

	@MndtId.deleter
	def MndtId(self):
		del self._MndtId
		self._MndtId = None

	@property
	def OthrDtls(self):
		return self._OthrDtls

	@OthrDtls.setter
	def OthrDtls(self, value):
		self._OthrDtls = value if type(value) != base_types.auto else self.make_default("OthrDtls")

	@OthrDtls.deleter
	def OthrDtls(self):
		del self._OthrDtls
		self._OthrDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AutomtdDrctDbtInstrInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cdtr', type=PartyIdentification272, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrctDbtTrfblInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastColltnCcyAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastColltnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MndtId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrDtls', type=TransferInstruction1, min=0, max=None, mutex_group=None, array=True),
	))

