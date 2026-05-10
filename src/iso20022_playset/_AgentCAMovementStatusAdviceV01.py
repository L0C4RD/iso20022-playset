from . import base_types
from ._CorporateActionInformation1 import CorporateActionInformation1
from ._DocumentIdentification8 import DocumentIdentification8
from ._CorporateActionMovementStatus1Choice import CorporateActionMovementStatus1Choice
from ._CorporateMovementStatus2 import CorporateMovementStatus2

class AgentCAMovementStatusAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_AgtCAMvmntInstrId", "_AgtCAElctnStsAdvcId", "_CorpActnGnlInf", "_AgtCAMvmntCxlReqId", "_AgtCAGblDstrbtnStsAdvcId", "_MvmntStsDtls", "_Id", "_MvmntCxlStsDtls"]
	@property
	def AgtCAMvmntInstrId(self):
		return self._AgtCAMvmntInstrId

	@AgtCAMvmntInstrId.setter
	def AgtCAMvmntInstrId(self, value):
		self._AgtCAMvmntInstrId = value if type(value) != base_types.auto else self.make_default("AgtCAMvmntInstrId")

	@AgtCAMvmntInstrId.deleter
	def AgtCAMvmntInstrId(self):
		del self._AgtCAMvmntInstrId
		self._AgtCAMvmntInstrId = None

	@property
	def AgtCAElctnStsAdvcId(self):
		return self._AgtCAElctnStsAdvcId

	@AgtCAElctnStsAdvcId.setter
	def AgtCAElctnStsAdvcId(self, value):
		self._AgtCAElctnStsAdvcId = value if type(value) != base_types.auto else self.make_default("AgtCAElctnStsAdvcId")

	@AgtCAElctnStsAdvcId.deleter
	def AgtCAElctnStsAdvcId(self):
		del self._AgtCAElctnStsAdvcId
		self._AgtCAElctnStsAdvcId = None

	@property
	def CorpActnGnlInf(self):
		return self._CorpActnGnlInf

	@CorpActnGnlInf.setter
	def CorpActnGnlInf(self, value):
		self._CorpActnGnlInf = value if type(value) != base_types.auto else self.make_default("CorpActnGnlInf")

	@CorpActnGnlInf.deleter
	def CorpActnGnlInf(self):
		del self._CorpActnGnlInf
		self._CorpActnGnlInf = None

	@property
	def AgtCAMvmntCxlReqId(self):
		return self._AgtCAMvmntCxlReqId

	@AgtCAMvmntCxlReqId.setter
	def AgtCAMvmntCxlReqId(self, value):
		self._AgtCAMvmntCxlReqId = value if type(value) != base_types.auto else self.make_default("AgtCAMvmntCxlReqId")

	@AgtCAMvmntCxlReqId.deleter
	def AgtCAMvmntCxlReqId(self):
		del self._AgtCAMvmntCxlReqId
		self._AgtCAMvmntCxlReqId = None

	@property
	def AgtCAGblDstrbtnStsAdvcId(self):
		return self._AgtCAGblDstrbtnStsAdvcId

	@AgtCAGblDstrbtnStsAdvcId.setter
	def AgtCAGblDstrbtnStsAdvcId(self, value):
		self._AgtCAGblDstrbtnStsAdvcId = value if type(value) != base_types.auto else self.make_default("AgtCAGblDstrbtnStsAdvcId")

	@AgtCAGblDstrbtnStsAdvcId.deleter
	def AgtCAGblDstrbtnStsAdvcId(self):
		del self._AgtCAGblDstrbtnStsAdvcId
		self._AgtCAGblDstrbtnStsAdvcId = None

	@property
	def MvmntStsDtls(self):
		return self._MvmntStsDtls

	@MvmntStsDtls.setter
	def MvmntStsDtls(self, value):
		self._MvmntStsDtls = value if type(value) != base_types.auto else self.make_default("MvmntStsDtls")

	@MvmntStsDtls.deleter
	def MvmntStsDtls(self):
		del self._MvmntStsDtls
		self._MvmntStsDtls = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def MvmntCxlStsDtls(self):
		return self._MvmntCxlStsDtls

	@MvmntCxlStsDtls.setter
	def MvmntCxlStsDtls(self, value):
		self._MvmntCxlStsDtls = value if type(value) != base_types.auto else self.make_default("MvmntCxlStsDtls")

	@MvmntCxlStsDtls.deleter
	def MvmntCxlStsDtls(self):
		del self._MvmntCxlStsDtls
		self._MvmntCxlStsDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgtCAMvmntInstrId', type=DocumentIdentification8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AgtCAElctnStsAdvcId', type=DocumentIdentification8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtCAMvmntCxlReqId', type=DocumentIdentification8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AgtCAGblDstrbtnStsAdvcId', type=DocumentIdentification8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MvmntStsDtls', type=CorporateActionMovementStatus1Choice, min=0, max=1, mutex_group=2, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MvmntCxlStsDtls', type=CorporateMovementStatus2, min=0, max=1, mutex_group=2, array=False),
	))

