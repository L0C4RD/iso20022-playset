# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RestrictedFINXMax16Text
from . import SettlementTypeAndIdentification22

class References79Choice(base_types._BaseFieldType):

	__slots__ = ["_IntraPosMvmntConfId", "_IntraPosMvmntPstngRptId", "_OthrMsgId", "_PrtflTrfNtfctnId", "_SctiesBalAcctgRptId", "_SctiesBalCtdyRptId", "_SctiesFincgConfId", "_SctiesSttlmTxAllgmtNtfctnTxId", "_SctiesSttlmTxAllgmtRptId", "_SctiesSttlmTxConfId", "_SctiesSttlmTxGnrtnNtfctnId", "_SctiesTxPdgRptId", "_SctiesTxPstngRptId", "_TrptyCollAndXpsrRptId", "_TrptyCollStsAdvcId", "_TrptyCollTxInstrPrcgStsAdvcId", "_TtlPrtflValtnRptId"]
	@property
	def IntraPosMvmntConfId(self):
		return self._IntraPosMvmntConfId

	@IntraPosMvmntConfId.setter
	def IntraPosMvmntConfId(self, value):
		self._IntraPosMvmntConfId = value if value is not None else base_types.UninitialisedField(self, 'IntraPosMvmntConfId', RestrictedFINXMax16Text, False)

	@IntraPosMvmntConfId.deleter
	def IntraPosMvmntConfId(self):
		del self._IntraPosMvmntConfId
		self._IntraPosMvmntConfId = base_types.UninitialisedField(self, 'IntraPosMvmntConfId', RestrictedFINXMax16Text, False)

	@property
	def IntraPosMvmntPstngRptId(self):
		return self._IntraPosMvmntPstngRptId

	@IntraPosMvmntPstngRptId.setter
	def IntraPosMvmntPstngRptId(self, value):
		self._IntraPosMvmntPstngRptId = value if value is not None else base_types.UninitialisedField(self, 'IntraPosMvmntPstngRptId', RestrictedFINXMax16Text, False)

	@IntraPosMvmntPstngRptId.deleter
	def IntraPosMvmntPstngRptId(self):
		del self._IntraPosMvmntPstngRptId
		self._IntraPosMvmntPstngRptId = base_types.UninitialisedField(self, 'IntraPosMvmntPstngRptId', RestrictedFINXMax16Text, False)

	@property
	def OthrMsgId(self):
		return self._OthrMsgId

	@OthrMsgId.setter
	def OthrMsgId(self, value):
		self._OthrMsgId = value if value is not None else base_types.UninitialisedField(self, 'OthrMsgId', RestrictedFINXMax16Text, False)

	@OthrMsgId.deleter
	def OthrMsgId(self):
		del self._OthrMsgId
		self._OthrMsgId = base_types.UninitialisedField(self, 'OthrMsgId', RestrictedFINXMax16Text, False)

	@property
	def PrtflTrfNtfctnId(self):
		return self._PrtflTrfNtfctnId

	@PrtflTrfNtfctnId.setter
	def PrtflTrfNtfctnId(self, value):
		self._PrtflTrfNtfctnId = value if value is not None else base_types.UninitialisedField(self, 'PrtflTrfNtfctnId', RestrictedFINXMax16Text, False)

	@PrtflTrfNtfctnId.deleter
	def PrtflTrfNtfctnId(self):
		del self._PrtflTrfNtfctnId
		self._PrtflTrfNtfctnId = base_types.UninitialisedField(self, 'PrtflTrfNtfctnId', RestrictedFINXMax16Text, False)

	@property
	def SctiesBalAcctgRptId(self):
		return self._SctiesBalAcctgRptId

	@SctiesBalAcctgRptId.setter
	def SctiesBalAcctgRptId(self, value):
		self._SctiesBalAcctgRptId = value if value is not None else base_types.UninitialisedField(self, 'SctiesBalAcctgRptId', RestrictedFINXMax16Text, False)

	@SctiesBalAcctgRptId.deleter
	def SctiesBalAcctgRptId(self):
		del self._SctiesBalAcctgRptId
		self._SctiesBalAcctgRptId = base_types.UninitialisedField(self, 'SctiesBalAcctgRptId', RestrictedFINXMax16Text, False)

	@property
	def SctiesBalCtdyRptId(self):
		return self._SctiesBalCtdyRptId

	@SctiesBalCtdyRptId.setter
	def SctiesBalCtdyRptId(self, value):
		self._SctiesBalCtdyRptId = value if value is not None else base_types.UninitialisedField(self, 'SctiesBalCtdyRptId', RestrictedFINXMax16Text, False)

	@SctiesBalCtdyRptId.deleter
	def SctiesBalCtdyRptId(self):
		del self._SctiesBalCtdyRptId
		self._SctiesBalCtdyRptId = base_types.UninitialisedField(self, 'SctiesBalCtdyRptId', RestrictedFINXMax16Text, False)

	@property
	def SctiesFincgConfId(self):
		return self._SctiesFincgConfId

	@SctiesFincgConfId.setter
	def SctiesFincgConfId(self, value):
		self._SctiesFincgConfId = value if value is not None else base_types.UninitialisedField(self, 'SctiesFincgConfId', SettlementTypeAndIdentification22, False)

	@SctiesFincgConfId.deleter
	def SctiesFincgConfId(self):
		del self._SctiesFincgConfId
		self._SctiesFincgConfId = base_types.UninitialisedField(self, 'SctiesFincgConfId', SettlementTypeAndIdentification22, False)

	@property
	def SctiesSttlmTxAllgmtNtfctnTxId(self):
		return self._SctiesSttlmTxAllgmtNtfctnTxId

	@SctiesSttlmTxAllgmtNtfctnTxId.setter
	def SctiesSttlmTxAllgmtNtfctnTxId(self, value):
		self._SctiesSttlmTxAllgmtNtfctnTxId = value if value is not None else base_types.UninitialisedField(self, 'SctiesSttlmTxAllgmtNtfctnTxId', SettlementTypeAndIdentification22, False)

	@SctiesSttlmTxAllgmtNtfctnTxId.deleter
	def SctiesSttlmTxAllgmtNtfctnTxId(self):
		del self._SctiesSttlmTxAllgmtNtfctnTxId
		self._SctiesSttlmTxAllgmtNtfctnTxId = base_types.UninitialisedField(self, 'SctiesSttlmTxAllgmtNtfctnTxId', SettlementTypeAndIdentification22, False)

	@property
	def SctiesSttlmTxAllgmtRptId(self):
		return self._SctiesSttlmTxAllgmtRptId

	@SctiesSttlmTxAllgmtRptId.setter
	def SctiesSttlmTxAllgmtRptId(self, value):
		self._SctiesSttlmTxAllgmtRptId = value if value is not None else base_types.UninitialisedField(self, 'SctiesSttlmTxAllgmtRptId', RestrictedFINXMax16Text, False)

	@SctiesSttlmTxAllgmtRptId.deleter
	def SctiesSttlmTxAllgmtRptId(self):
		del self._SctiesSttlmTxAllgmtRptId
		self._SctiesSttlmTxAllgmtRptId = base_types.UninitialisedField(self, 'SctiesSttlmTxAllgmtRptId', RestrictedFINXMax16Text, False)

	@property
	def SctiesSttlmTxConfId(self):
		return self._SctiesSttlmTxConfId

	@SctiesSttlmTxConfId.setter
	def SctiesSttlmTxConfId(self, value):
		self._SctiesSttlmTxConfId = value if value is not None else base_types.UninitialisedField(self, 'SctiesSttlmTxConfId', SettlementTypeAndIdentification22, False)

	@SctiesSttlmTxConfId.deleter
	def SctiesSttlmTxConfId(self):
		del self._SctiesSttlmTxConfId
		self._SctiesSttlmTxConfId = base_types.UninitialisedField(self, 'SctiesSttlmTxConfId', SettlementTypeAndIdentification22, False)

	@property
	def SctiesSttlmTxGnrtnNtfctnId(self):
		return self._SctiesSttlmTxGnrtnNtfctnId

	@SctiesSttlmTxGnrtnNtfctnId.setter
	def SctiesSttlmTxGnrtnNtfctnId(self, value):
		self._SctiesSttlmTxGnrtnNtfctnId = value if value is not None else base_types.UninitialisedField(self, 'SctiesSttlmTxGnrtnNtfctnId', SettlementTypeAndIdentification22, False)

	@SctiesSttlmTxGnrtnNtfctnId.deleter
	def SctiesSttlmTxGnrtnNtfctnId(self):
		del self._SctiesSttlmTxGnrtnNtfctnId
		self._SctiesSttlmTxGnrtnNtfctnId = base_types.UninitialisedField(self, 'SctiesSttlmTxGnrtnNtfctnId', SettlementTypeAndIdentification22, False)

	@property
	def SctiesTxPdgRptId(self):
		return self._SctiesTxPdgRptId

	@SctiesTxPdgRptId.setter
	def SctiesTxPdgRptId(self, value):
		self._SctiesTxPdgRptId = value if value is not None else base_types.UninitialisedField(self, 'SctiesTxPdgRptId', RestrictedFINXMax16Text, False)

	@SctiesTxPdgRptId.deleter
	def SctiesTxPdgRptId(self):
		del self._SctiesTxPdgRptId
		self._SctiesTxPdgRptId = base_types.UninitialisedField(self, 'SctiesTxPdgRptId', RestrictedFINXMax16Text, False)

	@property
	def SctiesTxPstngRptId(self):
		return self._SctiesTxPstngRptId

	@SctiesTxPstngRptId.setter
	def SctiesTxPstngRptId(self, value):
		self._SctiesTxPstngRptId = value if value is not None else base_types.UninitialisedField(self, 'SctiesTxPstngRptId', RestrictedFINXMax16Text, False)

	@SctiesTxPstngRptId.deleter
	def SctiesTxPstngRptId(self):
		del self._SctiesTxPstngRptId
		self._SctiesTxPstngRptId = base_types.UninitialisedField(self, 'SctiesTxPstngRptId', RestrictedFINXMax16Text, False)

	@property
	def TrptyCollAndXpsrRptId(self):
		return self._TrptyCollAndXpsrRptId

	@TrptyCollAndXpsrRptId.setter
	def TrptyCollAndXpsrRptId(self, value):
		self._TrptyCollAndXpsrRptId = value if value is not None else base_types.UninitialisedField(self, 'TrptyCollAndXpsrRptId', RestrictedFINXMax16Text, False)

	@TrptyCollAndXpsrRptId.deleter
	def TrptyCollAndXpsrRptId(self):
		del self._TrptyCollAndXpsrRptId
		self._TrptyCollAndXpsrRptId = base_types.UninitialisedField(self, 'TrptyCollAndXpsrRptId', RestrictedFINXMax16Text, False)

	@property
	def TrptyCollStsAdvcId(self):
		return self._TrptyCollStsAdvcId

	@TrptyCollStsAdvcId.setter
	def TrptyCollStsAdvcId(self, value):
		self._TrptyCollStsAdvcId = value if value is not None else base_types.UninitialisedField(self, 'TrptyCollStsAdvcId', RestrictedFINXMax16Text, False)

	@TrptyCollStsAdvcId.deleter
	def TrptyCollStsAdvcId(self):
		del self._TrptyCollStsAdvcId
		self._TrptyCollStsAdvcId = base_types.UninitialisedField(self, 'TrptyCollStsAdvcId', RestrictedFINXMax16Text, False)

	@property
	def TrptyCollTxInstrPrcgStsAdvcId(self):
		return self._TrptyCollTxInstrPrcgStsAdvcId

	@TrptyCollTxInstrPrcgStsAdvcId.setter
	def TrptyCollTxInstrPrcgStsAdvcId(self, value):
		self._TrptyCollTxInstrPrcgStsAdvcId = value if value is not None else base_types.UninitialisedField(self, 'TrptyCollTxInstrPrcgStsAdvcId', RestrictedFINXMax16Text, False)

	@TrptyCollTxInstrPrcgStsAdvcId.deleter
	def TrptyCollTxInstrPrcgStsAdvcId(self):
		del self._TrptyCollTxInstrPrcgStsAdvcId
		self._TrptyCollTxInstrPrcgStsAdvcId = base_types.UninitialisedField(self, 'TrptyCollTxInstrPrcgStsAdvcId', RestrictedFINXMax16Text, False)

	@property
	def TtlPrtflValtnRptId(self):
		return self._TtlPrtflValtnRptId

	@TtlPrtflValtnRptId.setter
	def TtlPrtflValtnRptId(self, value):
		self._TtlPrtflValtnRptId = value if value is not None else base_types.UninitialisedField(self, 'TtlPrtflValtnRptId', RestrictedFINXMax16Text, False)

	@TtlPrtflValtnRptId.deleter
	def TtlPrtflValtnRptId(self):
		del self._TtlPrtflValtnRptId
		self._TtlPrtflValtnRptId = base_types.UninitialisedField(self, 'TtlPrtflValtnRptId', RestrictedFINXMax16Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='IntraPosMvmntConfId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IntraPosMvmntPstngRptId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OthrMsgId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtflTrfNtfctnId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesBalAcctgRptId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesBalCtdyRptId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesFincgConfId', type=SettlementTypeAndIdentification22, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesSttlmTxAllgmtNtfctnTxId', type=SettlementTypeAndIdentification22, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesSttlmTxAllgmtRptId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesSttlmTxConfId', type=SettlementTypeAndIdentification22, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesSttlmTxGnrtnNtfctnId', type=SettlementTypeAndIdentification22, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesTxPdgRptId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesTxPstngRptId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TrptyCollAndXpsrRptId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TrptyCollStsAdvcId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TrptyCollTxInstrPrcgStsAdvcId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TtlPrtflValtnRptId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
	))