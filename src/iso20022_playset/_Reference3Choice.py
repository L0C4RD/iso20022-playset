# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import Max52Text

class Reference3Choice(base_types._BaseFieldType):

	__slots__ = ["_ClntCollInstrId", "_ClntCollTxId", "_CmonTxId", "_CollPrpslId", "_CollPrpslRspnId", "_CollSbstitnConfId", "_CollSbstitnReqId", "_CollSbstitnRspnId", "_DsptNtfctnId", "_IntrstPmtReqId", "_IntrstPmtRspnId", "_IntrstPmtStmtId", "_MrgnCallReqId", "_MrgnCallRspnId", "_TrptyAgtSvcPrvdrCollInstrId", "_TrptyAgtSvcPrvdrCollTxId"]
	@property
	def ClntCollInstrId(self):
		return self._ClntCollInstrId

	@ClntCollInstrId.setter
	def ClntCollInstrId(self, value):
		self._ClntCollInstrId = value if value is not None else base_types.UninitialisedField(self, 'ClntCollInstrId', Max35Text, False)

	@ClntCollInstrId.deleter
	def ClntCollInstrId(self):
		del self._ClntCollInstrId
		self._ClntCollInstrId = base_types.UninitialisedField(self, 'ClntCollInstrId', Max35Text, False)

	@property
	def ClntCollTxId(self):
		return self._ClntCollTxId

	@ClntCollTxId.setter
	def ClntCollTxId(self, value):
		self._ClntCollTxId = value if value is not None else base_types.UninitialisedField(self, 'ClntCollTxId', Max35Text, False)

	@ClntCollTxId.deleter
	def ClntCollTxId(self):
		del self._ClntCollTxId
		self._ClntCollTxId = base_types.UninitialisedField(self, 'ClntCollTxId', Max35Text, False)

	@property
	def CmonTxId(self):
		return self._CmonTxId

	@CmonTxId.setter
	def CmonTxId(self, value):
		self._CmonTxId = value if value is not None else base_types.UninitialisedField(self, 'CmonTxId', Max52Text, False)

	@CmonTxId.deleter
	def CmonTxId(self):
		del self._CmonTxId
		self._CmonTxId = base_types.UninitialisedField(self, 'CmonTxId', Max52Text, False)

	@property
	def CollPrpslId(self):
		return self._CollPrpslId

	@CollPrpslId.setter
	def CollPrpslId(self, value):
		self._CollPrpslId = value if value is not None else base_types.UninitialisedField(self, 'CollPrpslId', Max35Text, False)

	@CollPrpslId.deleter
	def CollPrpslId(self):
		del self._CollPrpslId
		self._CollPrpslId = base_types.UninitialisedField(self, 'CollPrpslId', Max35Text, False)

	@property
	def CollPrpslRspnId(self):
		return self._CollPrpslRspnId

	@CollPrpslRspnId.setter
	def CollPrpslRspnId(self, value):
		self._CollPrpslRspnId = value if value is not None else base_types.UninitialisedField(self, 'CollPrpslRspnId', Max35Text, False)

	@CollPrpslRspnId.deleter
	def CollPrpslRspnId(self):
		del self._CollPrpslRspnId
		self._CollPrpslRspnId = base_types.UninitialisedField(self, 'CollPrpslRspnId', Max35Text, False)

	@property
	def CollSbstitnConfId(self):
		return self._CollSbstitnConfId

	@CollSbstitnConfId.setter
	def CollSbstitnConfId(self, value):
		self._CollSbstitnConfId = value if value is not None else base_types.UninitialisedField(self, 'CollSbstitnConfId', Max35Text, False)

	@CollSbstitnConfId.deleter
	def CollSbstitnConfId(self):
		del self._CollSbstitnConfId
		self._CollSbstitnConfId = base_types.UninitialisedField(self, 'CollSbstitnConfId', Max35Text, False)

	@property
	def CollSbstitnReqId(self):
		return self._CollSbstitnReqId

	@CollSbstitnReqId.setter
	def CollSbstitnReqId(self, value):
		self._CollSbstitnReqId = value if value is not None else base_types.UninitialisedField(self, 'CollSbstitnReqId', Max35Text, False)

	@CollSbstitnReqId.deleter
	def CollSbstitnReqId(self):
		del self._CollSbstitnReqId
		self._CollSbstitnReqId = base_types.UninitialisedField(self, 'CollSbstitnReqId', Max35Text, False)

	@property
	def CollSbstitnRspnId(self):
		return self._CollSbstitnRspnId

	@CollSbstitnRspnId.setter
	def CollSbstitnRspnId(self, value):
		self._CollSbstitnRspnId = value if value is not None else base_types.UninitialisedField(self, 'CollSbstitnRspnId', Max35Text, False)

	@CollSbstitnRspnId.deleter
	def CollSbstitnRspnId(self):
		del self._CollSbstitnRspnId
		self._CollSbstitnRspnId = base_types.UninitialisedField(self, 'CollSbstitnRspnId', Max35Text, False)

	@property
	def DsptNtfctnId(self):
		return self._DsptNtfctnId

	@DsptNtfctnId.setter
	def DsptNtfctnId(self, value):
		self._DsptNtfctnId = value if value is not None else base_types.UninitialisedField(self, 'DsptNtfctnId', Max35Text, False)

	@DsptNtfctnId.deleter
	def DsptNtfctnId(self):
		del self._DsptNtfctnId
		self._DsptNtfctnId = base_types.UninitialisedField(self, 'DsptNtfctnId', Max35Text, False)

	@property
	def IntrstPmtReqId(self):
		return self._IntrstPmtReqId

	@IntrstPmtReqId.setter
	def IntrstPmtReqId(self, value):
		self._IntrstPmtReqId = value if value is not None else base_types.UninitialisedField(self, 'IntrstPmtReqId', Max35Text, False)

	@IntrstPmtReqId.deleter
	def IntrstPmtReqId(self):
		del self._IntrstPmtReqId
		self._IntrstPmtReqId = base_types.UninitialisedField(self, 'IntrstPmtReqId', Max35Text, False)

	@property
	def IntrstPmtRspnId(self):
		return self._IntrstPmtRspnId

	@IntrstPmtRspnId.setter
	def IntrstPmtRspnId(self, value):
		self._IntrstPmtRspnId = value if value is not None else base_types.UninitialisedField(self, 'IntrstPmtRspnId', Max35Text, False)

	@IntrstPmtRspnId.deleter
	def IntrstPmtRspnId(self):
		del self._IntrstPmtRspnId
		self._IntrstPmtRspnId = base_types.UninitialisedField(self, 'IntrstPmtRspnId', Max35Text, False)

	@property
	def IntrstPmtStmtId(self):
		return self._IntrstPmtStmtId

	@IntrstPmtStmtId.setter
	def IntrstPmtStmtId(self, value):
		self._IntrstPmtStmtId = value if value is not None else base_types.UninitialisedField(self, 'IntrstPmtStmtId', Max35Text, False)

	@IntrstPmtStmtId.deleter
	def IntrstPmtStmtId(self):
		del self._IntrstPmtStmtId
		self._IntrstPmtStmtId = base_types.UninitialisedField(self, 'IntrstPmtStmtId', Max35Text, False)

	@property
	def MrgnCallReqId(self):
		return self._MrgnCallReqId

	@MrgnCallReqId.setter
	def MrgnCallReqId(self, value):
		self._MrgnCallReqId = value if value is not None else base_types.UninitialisedField(self, 'MrgnCallReqId', Max35Text, False)

	@MrgnCallReqId.deleter
	def MrgnCallReqId(self):
		del self._MrgnCallReqId
		self._MrgnCallReqId = base_types.UninitialisedField(self, 'MrgnCallReqId', Max35Text, False)

	@property
	def MrgnCallRspnId(self):
		return self._MrgnCallRspnId

	@MrgnCallRspnId.setter
	def MrgnCallRspnId(self, value):
		self._MrgnCallRspnId = value if value is not None else base_types.UninitialisedField(self, 'MrgnCallRspnId', Max35Text, False)

	@MrgnCallRspnId.deleter
	def MrgnCallRspnId(self):
		del self._MrgnCallRspnId
		self._MrgnCallRspnId = base_types.UninitialisedField(self, 'MrgnCallRspnId', Max35Text, False)

	@property
	def TrptyAgtSvcPrvdrCollInstrId(self):
		return self._TrptyAgtSvcPrvdrCollInstrId

	@TrptyAgtSvcPrvdrCollInstrId.setter
	def TrptyAgtSvcPrvdrCollInstrId(self, value):
		self._TrptyAgtSvcPrvdrCollInstrId = value if value is not None else base_types.UninitialisedField(self, 'TrptyAgtSvcPrvdrCollInstrId', Max35Text, False)

	@TrptyAgtSvcPrvdrCollInstrId.deleter
	def TrptyAgtSvcPrvdrCollInstrId(self):
		del self._TrptyAgtSvcPrvdrCollInstrId
		self._TrptyAgtSvcPrvdrCollInstrId = base_types.UninitialisedField(self, 'TrptyAgtSvcPrvdrCollInstrId', Max35Text, False)

	@property
	def TrptyAgtSvcPrvdrCollTxId(self):
		return self._TrptyAgtSvcPrvdrCollTxId

	@TrptyAgtSvcPrvdrCollTxId.setter
	def TrptyAgtSvcPrvdrCollTxId(self, value):
		self._TrptyAgtSvcPrvdrCollTxId = value if value is not None else base_types.UninitialisedField(self, 'TrptyAgtSvcPrvdrCollTxId', Max35Text, False)

	@TrptyAgtSvcPrvdrCollTxId.deleter
	def TrptyAgtSvcPrvdrCollTxId(self):
		del self._TrptyAgtSvcPrvdrCollTxId
		self._TrptyAgtSvcPrvdrCollTxId = base_types.UninitialisedField(self, 'TrptyAgtSvcPrvdrCollTxId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClntCollInstrId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ClntCollTxId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CmonTxId', type=Max52Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CollPrpslId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CollPrpslRspnId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CollSbstitnConfId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CollSbstitnReqId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CollSbstitnRspnId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DsptNtfctnId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IntrstPmtReqId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IntrstPmtRspnId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IntrstPmtStmtId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MrgnCallReqId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MrgnCallRspnId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TrptyAgtSvcPrvdrCollInstrId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TrptyAgtSvcPrvdrCollTxId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))