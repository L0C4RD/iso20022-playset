from . import base_types
from .RestrictedFINXMax16Text import RestrictedFINXMax16Text
from .SettlementTypeAndIdentification22 import SettlementTypeAndIdentification22

class References79Choice(base_types._BaseFieldType):

	__slots__ = ["_IntraPosMvmntPstngRptId", "_TrptyCollAndXpsrRptId", "_SctiesTxPdgRptId", "_SctiesBalCtdyRptId", "_OthrMsgId", "_SctiesBalAcctgRptId", "_TrptyCollStsAdvcId", "_TtlPrtflValtnRptId", "_SctiesSttlmTxConfId", "_SctiesTxPstngRptId", "_SctiesSttlmTxAllgmtNtfctnTxId", "_IntraPosMvmntConfId", "_SctiesSttlmTxGnrtnNtfctnId", "_PrtflTrfNtfctnId", "_TrptyCollTxInstrPrcgStsAdvcId", "_SctiesSttlmTxAllgmtRptId", "_SctiesFincgConfId"]
	@property
	def IntraPosMvmntPstngRptId(self):
		return self._IntraPosMvmntPstngRptId

	@IntraPosMvmntPstngRptId.setter
	def IntraPosMvmntPstngRptId(self, value):
		self._IntraPosMvmntPstngRptId = value if type(value) != base_types.auto else self.make_default("IntraPosMvmntPstngRptId")

	@IntraPosMvmntPstngRptId.deleter
	def IntraPosMvmntPstngRptId(self):
		del self._IntraPosMvmntPstngRptId
		self._IntraPosMvmntPstngRptId = None

	@property
	def TrptyCollAndXpsrRptId(self):
		return self._TrptyCollAndXpsrRptId

	@TrptyCollAndXpsrRptId.setter
	def TrptyCollAndXpsrRptId(self, value):
		self._TrptyCollAndXpsrRptId = value if type(value) != base_types.auto else self.make_default("TrptyCollAndXpsrRptId")

	@TrptyCollAndXpsrRptId.deleter
	def TrptyCollAndXpsrRptId(self):
		del self._TrptyCollAndXpsrRptId
		self._TrptyCollAndXpsrRptId = None

	@property
	def SctiesTxPdgRptId(self):
		return self._SctiesTxPdgRptId

	@SctiesTxPdgRptId.setter
	def SctiesTxPdgRptId(self, value):
		self._SctiesTxPdgRptId = value if type(value) != base_types.auto else self.make_default("SctiesTxPdgRptId")

	@SctiesTxPdgRptId.deleter
	def SctiesTxPdgRptId(self):
		del self._SctiesTxPdgRptId
		self._SctiesTxPdgRptId = None

	@property
	def SctiesBalCtdyRptId(self):
		return self._SctiesBalCtdyRptId

	@SctiesBalCtdyRptId.setter
	def SctiesBalCtdyRptId(self, value):
		self._SctiesBalCtdyRptId = value if type(value) != base_types.auto else self.make_default("SctiesBalCtdyRptId")

	@SctiesBalCtdyRptId.deleter
	def SctiesBalCtdyRptId(self):
		del self._SctiesBalCtdyRptId
		self._SctiesBalCtdyRptId = None

	@property
	def OthrMsgId(self):
		return self._OthrMsgId

	@OthrMsgId.setter
	def OthrMsgId(self, value):
		self._OthrMsgId = value if type(value) != base_types.auto else self.make_default("OthrMsgId")

	@OthrMsgId.deleter
	def OthrMsgId(self):
		del self._OthrMsgId
		self._OthrMsgId = None

	@property
	def SctiesBalAcctgRptId(self):
		return self._SctiesBalAcctgRptId

	@SctiesBalAcctgRptId.setter
	def SctiesBalAcctgRptId(self, value):
		self._SctiesBalAcctgRptId = value if type(value) != base_types.auto else self.make_default("SctiesBalAcctgRptId")

	@SctiesBalAcctgRptId.deleter
	def SctiesBalAcctgRptId(self):
		del self._SctiesBalAcctgRptId
		self._SctiesBalAcctgRptId = None

	@property
	def TrptyCollStsAdvcId(self):
		return self._TrptyCollStsAdvcId

	@TrptyCollStsAdvcId.setter
	def TrptyCollStsAdvcId(self, value):
		self._TrptyCollStsAdvcId = value if type(value) != base_types.auto else self.make_default("TrptyCollStsAdvcId")

	@TrptyCollStsAdvcId.deleter
	def TrptyCollStsAdvcId(self):
		del self._TrptyCollStsAdvcId
		self._TrptyCollStsAdvcId = None

	@property
	def TtlPrtflValtnRptId(self):
		return self._TtlPrtflValtnRptId

	@TtlPrtflValtnRptId.setter
	def TtlPrtflValtnRptId(self, value):
		self._TtlPrtflValtnRptId = value if type(value) != base_types.auto else self.make_default("TtlPrtflValtnRptId")

	@TtlPrtflValtnRptId.deleter
	def TtlPrtflValtnRptId(self):
		del self._TtlPrtflValtnRptId
		self._TtlPrtflValtnRptId = None

	@property
	def SctiesSttlmTxConfId(self):
		return self._SctiesSttlmTxConfId

	@SctiesSttlmTxConfId.setter
	def SctiesSttlmTxConfId(self, value):
		self._SctiesSttlmTxConfId = value if type(value) != base_types.auto else self.make_default("SctiesSttlmTxConfId")

	@SctiesSttlmTxConfId.deleter
	def SctiesSttlmTxConfId(self):
		del self._SctiesSttlmTxConfId
		self._SctiesSttlmTxConfId = None

	@property
	def SctiesTxPstngRptId(self):
		return self._SctiesTxPstngRptId

	@SctiesTxPstngRptId.setter
	def SctiesTxPstngRptId(self, value):
		self._SctiesTxPstngRptId = value if type(value) != base_types.auto else self.make_default("SctiesTxPstngRptId")

	@SctiesTxPstngRptId.deleter
	def SctiesTxPstngRptId(self):
		del self._SctiesTxPstngRptId
		self._SctiesTxPstngRptId = None

	@property
	def SctiesSttlmTxAllgmtNtfctnTxId(self):
		return self._SctiesSttlmTxAllgmtNtfctnTxId

	@SctiesSttlmTxAllgmtNtfctnTxId.setter
	def SctiesSttlmTxAllgmtNtfctnTxId(self, value):
		self._SctiesSttlmTxAllgmtNtfctnTxId = value if type(value) != base_types.auto else self.make_default("SctiesSttlmTxAllgmtNtfctnTxId")

	@SctiesSttlmTxAllgmtNtfctnTxId.deleter
	def SctiesSttlmTxAllgmtNtfctnTxId(self):
		del self._SctiesSttlmTxAllgmtNtfctnTxId
		self._SctiesSttlmTxAllgmtNtfctnTxId = None

	@property
	def IntraPosMvmntConfId(self):
		return self._IntraPosMvmntConfId

	@IntraPosMvmntConfId.setter
	def IntraPosMvmntConfId(self, value):
		self._IntraPosMvmntConfId = value if type(value) != base_types.auto else self.make_default("IntraPosMvmntConfId")

	@IntraPosMvmntConfId.deleter
	def IntraPosMvmntConfId(self):
		del self._IntraPosMvmntConfId
		self._IntraPosMvmntConfId = None

	@property
	def SctiesSttlmTxGnrtnNtfctnId(self):
		return self._SctiesSttlmTxGnrtnNtfctnId

	@SctiesSttlmTxGnrtnNtfctnId.setter
	def SctiesSttlmTxGnrtnNtfctnId(self, value):
		self._SctiesSttlmTxGnrtnNtfctnId = value if type(value) != base_types.auto else self.make_default("SctiesSttlmTxGnrtnNtfctnId")

	@SctiesSttlmTxGnrtnNtfctnId.deleter
	def SctiesSttlmTxGnrtnNtfctnId(self):
		del self._SctiesSttlmTxGnrtnNtfctnId
		self._SctiesSttlmTxGnrtnNtfctnId = None

	@property
	def PrtflTrfNtfctnId(self):
		return self._PrtflTrfNtfctnId

	@PrtflTrfNtfctnId.setter
	def PrtflTrfNtfctnId(self, value):
		self._PrtflTrfNtfctnId = value if type(value) != base_types.auto else self.make_default("PrtflTrfNtfctnId")

	@PrtflTrfNtfctnId.deleter
	def PrtflTrfNtfctnId(self):
		del self._PrtflTrfNtfctnId
		self._PrtflTrfNtfctnId = None

	@property
	def TrptyCollTxInstrPrcgStsAdvcId(self):
		return self._TrptyCollTxInstrPrcgStsAdvcId

	@TrptyCollTxInstrPrcgStsAdvcId.setter
	def TrptyCollTxInstrPrcgStsAdvcId(self, value):
		self._TrptyCollTxInstrPrcgStsAdvcId = value if type(value) != base_types.auto else self.make_default("TrptyCollTxInstrPrcgStsAdvcId")

	@TrptyCollTxInstrPrcgStsAdvcId.deleter
	def TrptyCollTxInstrPrcgStsAdvcId(self):
		del self._TrptyCollTxInstrPrcgStsAdvcId
		self._TrptyCollTxInstrPrcgStsAdvcId = None

	@property
	def SctiesSttlmTxAllgmtRptId(self):
		return self._SctiesSttlmTxAllgmtRptId

	@SctiesSttlmTxAllgmtRptId.setter
	def SctiesSttlmTxAllgmtRptId(self, value):
		self._SctiesSttlmTxAllgmtRptId = value if type(value) != base_types.auto else self.make_default("SctiesSttlmTxAllgmtRptId")

	@SctiesSttlmTxAllgmtRptId.deleter
	def SctiesSttlmTxAllgmtRptId(self):
		del self._SctiesSttlmTxAllgmtRptId
		self._SctiesSttlmTxAllgmtRptId = None

	@property
	def SctiesFincgConfId(self):
		return self._SctiesFincgConfId

	@SctiesFincgConfId.setter
	def SctiesFincgConfId(self, value):
		self._SctiesFincgConfId = value if type(value) != base_types.auto else self.make_default("SctiesFincgConfId")

	@SctiesFincgConfId.deleter
	def SctiesFincgConfId(self):
		del self._SctiesFincgConfId
		self._SctiesFincgConfId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IntraPosMvmntPstngRptId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TrptyCollAndXpsrRptId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesTxPdgRptId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesBalCtdyRptId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OthrMsgId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesBalAcctgRptId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TrptyCollStsAdvcId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TtlPrtflValtnRptId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesSttlmTxConfId', type=SettlementTypeAndIdentification22, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesTxPstngRptId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesSttlmTxAllgmtNtfctnTxId', type=SettlementTypeAndIdentification22, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IntraPosMvmntConfId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesSttlmTxGnrtnNtfctnId', type=SettlementTypeAndIdentification22, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtflTrfNtfctnId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TrptyCollTxInstrPrcgStsAdvcId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesSttlmTxAllgmtRptId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesFincgConfId', type=SettlementTypeAndIdentification22, min=0, max=1, mutex_group=1, array=False),
	))

