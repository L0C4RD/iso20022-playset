from . import base_types
from .Max52Text import Max52Text
from .Max35Text import Max35Text

class Reference3Choice(base_types._BaseFieldType):

	__slots__ = ["_CollSbstitnConfId", "_TrptyAgtSvcPrvdrCollInstrId", "_IntrstPmtStmtId", "_CollPrpslRspnId", "_IntrstPmtReqId", "_CollPrpslId", "_IntrstPmtRspnId", "_CollSbstitnRspnId", "_MrgnCallReqId", "_DsptNtfctnId", "_CollSbstitnReqId", "_TrptyAgtSvcPrvdrCollTxId", "_ClntCollInstrId", "_CmonTxId", "_MrgnCallRspnId", "_ClntCollTxId"]
	@property
	def CollSbstitnConfId(self):
		return self._CollSbstitnConfId

	@CollSbstitnConfId.setter
	def CollSbstitnConfId(self, value):
		self._CollSbstitnConfId = value if type(value) != base_types.auto else self.make_default("CollSbstitnConfId")

	@CollSbstitnConfId.deleter
	def CollSbstitnConfId(self):
		del self._CollSbstitnConfId
		self._CollSbstitnConfId = None

	@property
	def TrptyAgtSvcPrvdrCollInstrId(self):
		return self._TrptyAgtSvcPrvdrCollInstrId

	@TrptyAgtSvcPrvdrCollInstrId.setter
	def TrptyAgtSvcPrvdrCollInstrId(self, value):
		self._TrptyAgtSvcPrvdrCollInstrId = value if type(value) != base_types.auto else self.make_default("TrptyAgtSvcPrvdrCollInstrId")

	@TrptyAgtSvcPrvdrCollInstrId.deleter
	def TrptyAgtSvcPrvdrCollInstrId(self):
		del self._TrptyAgtSvcPrvdrCollInstrId
		self._TrptyAgtSvcPrvdrCollInstrId = None

	@property
	def IntrstPmtStmtId(self):
		return self._IntrstPmtStmtId

	@IntrstPmtStmtId.setter
	def IntrstPmtStmtId(self, value):
		self._IntrstPmtStmtId = value if type(value) != base_types.auto else self.make_default("IntrstPmtStmtId")

	@IntrstPmtStmtId.deleter
	def IntrstPmtStmtId(self):
		del self._IntrstPmtStmtId
		self._IntrstPmtStmtId = None

	@property
	def CollPrpslRspnId(self):
		return self._CollPrpslRspnId

	@CollPrpslRspnId.setter
	def CollPrpslRspnId(self, value):
		self._CollPrpslRspnId = value if type(value) != base_types.auto else self.make_default("CollPrpslRspnId")

	@CollPrpslRspnId.deleter
	def CollPrpslRspnId(self):
		del self._CollPrpslRspnId
		self._CollPrpslRspnId = None

	@property
	def IntrstPmtReqId(self):
		return self._IntrstPmtReqId

	@IntrstPmtReqId.setter
	def IntrstPmtReqId(self, value):
		self._IntrstPmtReqId = value if type(value) != base_types.auto else self.make_default("IntrstPmtReqId")

	@IntrstPmtReqId.deleter
	def IntrstPmtReqId(self):
		del self._IntrstPmtReqId
		self._IntrstPmtReqId = None

	@property
	def CollPrpslId(self):
		return self._CollPrpslId

	@CollPrpslId.setter
	def CollPrpslId(self, value):
		self._CollPrpslId = value if type(value) != base_types.auto else self.make_default("CollPrpslId")

	@CollPrpslId.deleter
	def CollPrpslId(self):
		del self._CollPrpslId
		self._CollPrpslId = None

	@property
	def IntrstPmtRspnId(self):
		return self._IntrstPmtRspnId

	@IntrstPmtRspnId.setter
	def IntrstPmtRspnId(self, value):
		self._IntrstPmtRspnId = value if type(value) != base_types.auto else self.make_default("IntrstPmtRspnId")

	@IntrstPmtRspnId.deleter
	def IntrstPmtRspnId(self):
		del self._IntrstPmtRspnId
		self._IntrstPmtRspnId = None

	@property
	def CollSbstitnRspnId(self):
		return self._CollSbstitnRspnId

	@CollSbstitnRspnId.setter
	def CollSbstitnRspnId(self, value):
		self._CollSbstitnRspnId = value if type(value) != base_types.auto else self.make_default("CollSbstitnRspnId")

	@CollSbstitnRspnId.deleter
	def CollSbstitnRspnId(self):
		del self._CollSbstitnRspnId
		self._CollSbstitnRspnId = None

	@property
	def MrgnCallReqId(self):
		return self._MrgnCallReqId

	@MrgnCallReqId.setter
	def MrgnCallReqId(self, value):
		self._MrgnCallReqId = value if type(value) != base_types.auto else self.make_default("MrgnCallReqId")

	@MrgnCallReqId.deleter
	def MrgnCallReqId(self):
		del self._MrgnCallReqId
		self._MrgnCallReqId = None

	@property
	def DsptNtfctnId(self):
		return self._DsptNtfctnId

	@DsptNtfctnId.setter
	def DsptNtfctnId(self, value):
		self._DsptNtfctnId = value if type(value) != base_types.auto else self.make_default("DsptNtfctnId")

	@DsptNtfctnId.deleter
	def DsptNtfctnId(self):
		del self._DsptNtfctnId
		self._DsptNtfctnId = None

	@property
	def CollSbstitnReqId(self):
		return self._CollSbstitnReqId

	@CollSbstitnReqId.setter
	def CollSbstitnReqId(self, value):
		self._CollSbstitnReqId = value if type(value) != base_types.auto else self.make_default("CollSbstitnReqId")

	@CollSbstitnReqId.deleter
	def CollSbstitnReqId(self):
		del self._CollSbstitnReqId
		self._CollSbstitnReqId = None

	@property
	def TrptyAgtSvcPrvdrCollTxId(self):
		return self._TrptyAgtSvcPrvdrCollTxId

	@TrptyAgtSvcPrvdrCollTxId.setter
	def TrptyAgtSvcPrvdrCollTxId(self, value):
		self._TrptyAgtSvcPrvdrCollTxId = value if type(value) != base_types.auto else self.make_default("TrptyAgtSvcPrvdrCollTxId")

	@TrptyAgtSvcPrvdrCollTxId.deleter
	def TrptyAgtSvcPrvdrCollTxId(self):
		del self._TrptyAgtSvcPrvdrCollTxId
		self._TrptyAgtSvcPrvdrCollTxId = None

	@property
	def ClntCollInstrId(self):
		return self._ClntCollInstrId

	@ClntCollInstrId.setter
	def ClntCollInstrId(self, value):
		self._ClntCollInstrId = value if type(value) != base_types.auto else self.make_default("ClntCollInstrId")

	@ClntCollInstrId.deleter
	def ClntCollInstrId(self):
		del self._ClntCollInstrId
		self._ClntCollInstrId = None

	@property
	def CmonTxId(self):
		return self._CmonTxId

	@CmonTxId.setter
	def CmonTxId(self, value):
		self._CmonTxId = value if type(value) != base_types.auto else self.make_default("CmonTxId")

	@CmonTxId.deleter
	def CmonTxId(self):
		del self._CmonTxId
		self._CmonTxId = None

	@property
	def MrgnCallRspnId(self):
		return self._MrgnCallRspnId

	@MrgnCallRspnId.setter
	def MrgnCallRspnId(self, value):
		self._MrgnCallRspnId = value if type(value) != base_types.auto else self.make_default("MrgnCallRspnId")

	@MrgnCallRspnId.deleter
	def MrgnCallRspnId(self):
		del self._MrgnCallRspnId
		self._MrgnCallRspnId = None

	@property
	def ClntCollTxId(self):
		return self._ClntCollTxId

	@ClntCollTxId.setter
	def ClntCollTxId(self, value):
		self._ClntCollTxId = value if type(value) != base_types.auto else self.make_default("ClntCollTxId")

	@ClntCollTxId.deleter
	def ClntCollTxId(self):
		del self._ClntCollTxId
		self._ClntCollTxId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollSbstitnConfId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TrptyAgtSvcPrvdrCollInstrId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IntrstPmtStmtId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CollPrpslRspnId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IntrstPmtReqId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CollPrpslId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IntrstPmtRspnId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CollSbstitnRspnId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MrgnCallReqId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DsptNtfctnId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CollSbstitnReqId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TrptyAgtSvcPrvdrCollTxId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ClntCollInstrId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CmonTxId', type=Max52Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MrgnCallRspnId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ClntCollTxId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))

