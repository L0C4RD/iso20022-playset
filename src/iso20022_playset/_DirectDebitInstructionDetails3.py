# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import ISODate
from . import Max35Text
from . import PartyIdentification272
from . import TransferInstruction1
from . import YesNoIndicator

class DirectDebitInstructionDetails3(base_types._BaseFieldType):

	__slots__ = ["_AutomtdDrctDbtInstrInd", "_Cdtr", "_DrctDbtTrfblInd", "_LastColltnCcyAmt", "_LastColltnDt", "_MndtId", "_OthrDtls"]
	@property
	def AutomtdDrctDbtInstrInd(self):
		return self._AutomtdDrctDbtInstrInd

	@AutomtdDrctDbtInstrInd.setter
	def AutomtdDrctDbtInstrInd(self, value):
		self._AutomtdDrctDbtInstrInd = value if value is not None else base_types.UninitialisedField(self, 'AutomtdDrctDbtInstrInd', YesNoIndicator, False)

	@AutomtdDrctDbtInstrInd.deleter
	def AutomtdDrctDbtInstrInd(self):
		del self._AutomtdDrctDbtInstrInd
		self._AutomtdDrctDbtInstrInd = base_types.UninitialisedField(self, 'AutomtdDrctDbtInstrInd', YesNoIndicator, False)

	@property
	def Cdtr(self):
		return self._Cdtr

	@Cdtr.setter
	def Cdtr(self, value):
		self._Cdtr = value if value is not None else base_types.UninitialisedField(self, 'Cdtr', PartyIdentification272, False)

	@Cdtr.deleter
	def Cdtr(self):
		del self._Cdtr
		self._Cdtr = base_types.UninitialisedField(self, 'Cdtr', PartyIdentification272, False)

	@property
	def DrctDbtTrfblInd(self):
		return self._DrctDbtTrfblInd

	@DrctDbtTrfblInd.setter
	def DrctDbtTrfblInd(self, value):
		self._DrctDbtTrfblInd = value if value is not None else base_types.UninitialisedField(self, 'DrctDbtTrfblInd', YesNoIndicator, False)

	@DrctDbtTrfblInd.deleter
	def DrctDbtTrfblInd(self):
		del self._DrctDbtTrfblInd
		self._DrctDbtTrfblInd = base_types.UninitialisedField(self, 'DrctDbtTrfblInd', YesNoIndicator, False)

	@property
	def LastColltnCcyAmt(self):
		return self._LastColltnCcyAmt

	@LastColltnCcyAmt.setter
	def LastColltnCcyAmt(self, value):
		self._LastColltnCcyAmt = value if value is not None else base_types.UninitialisedField(self, 'LastColltnCcyAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@LastColltnCcyAmt.deleter
	def LastColltnCcyAmt(self):
		del self._LastColltnCcyAmt
		self._LastColltnCcyAmt = base_types.UninitialisedField(self, 'LastColltnCcyAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def LastColltnDt(self):
		return self._LastColltnDt

	@LastColltnDt.setter
	def LastColltnDt(self, value):
		self._LastColltnDt = value if value is not None else base_types.UninitialisedField(self, 'LastColltnDt', ISODate, False)

	@LastColltnDt.deleter
	def LastColltnDt(self):
		del self._LastColltnDt
		self._LastColltnDt = base_types.UninitialisedField(self, 'LastColltnDt', ISODate, False)

	@property
	def MndtId(self):
		return self._MndtId

	@MndtId.setter
	def MndtId(self, value):
		self._MndtId = value if value is not None else base_types.UninitialisedField(self, 'MndtId', Max35Text, False)

	@MndtId.deleter
	def MndtId(self):
		del self._MndtId
		self._MndtId = base_types.UninitialisedField(self, 'MndtId', Max35Text, False)

	@property
	def OthrDtls(self):
		return self._OthrDtls

	@OthrDtls.setter
	def OthrDtls(self, value):
		self._OthrDtls = value if value is not None else base_types.UninitialisedField(self, 'OthrDtls', TransferInstruction1, True)

	@OthrDtls.deleter
	def OthrDtls(self):
		del self._OthrDtls
		self._OthrDtls = base_types.UninitialisedField(self, 'OthrDtls', TransferInstruction1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AutomtdDrctDbtInstrInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cdtr', type=PartyIdentification272, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrctDbtTrfblInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastColltnCcyAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastColltnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MndtId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrDtls', type=TransferInstruction1, min=0, max=None, mutex_group=None, array=True),
	))