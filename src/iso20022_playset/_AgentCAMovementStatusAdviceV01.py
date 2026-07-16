# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionInformation1
from . import CorporateActionMovementStatus1Choice
from . import CorporateMovementStatus2
from . import DocumentIdentification8

class AgentCAMovementStatusAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_AgtCAElctnStsAdvcId", "_AgtCAGblDstrbtnStsAdvcId", "_AgtCAMvmntCxlReqId", "_AgtCAMvmntInstrId", "_CorpActnGnlInf", "_Id", "_MvmntCxlStsDtls", "_MvmntStsDtls"]
	@property
	def AgtCAElctnStsAdvcId(self):
		return self._AgtCAElctnStsAdvcId

	@AgtCAElctnStsAdvcId.setter
	def AgtCAElctnStsAdvcId(self, value):
		self._AgtCAElctnStsAdvcId = value if value is not None else base_types.UninitialisedField(self, 'AgtCAElctnStsAdvcId', DocumentIdentification8, False)

	@AgtCAElctnStsAdvcId.deleter
	def AgtCAElctnStsAdvcId(self):
		del self._AgtCAElctnStsAdvcId
		self._AgtCAElctnStsAdvcId = base_types.UninitialisedField(self, 'AgtCAElctnStsAdvcId', DocumentIdentification8, False)

	@property
	def AgtCAGblDstrbtnStsAdvcId(self):
		return self._AgtCAGblDstrbtnStsAdvcId

	@AgtCAGblDstrbtnStsAdvcId.setter
	def AgtCAGblDstrbtnStsAdvcId(self, value):
		self._AgtCAGblDstrbtnStsAdvcId = value if value is not None else base_types.UninitialisedField(self, 'AgtCAGblDstrbtnStsAdvcId', DocumentIdentification8, False)

	@AgtCAGblDstrbtnStsAdvcId.deleter
	def AgtCAGblDstrbtnStsAdvcId(self):
		del self._AgtCAGblDstrbtnStsAdvcId
		self._AgtCAGblDstrbtnStsAdvcId = base_types.UninitialisedField(self, 'AgtCAGblDstrbtnStsAdvcId', DocumentIdentification8, False)

	@property
	def AgtCAMvmntCxlReqId(self):
		return self._AgtCAMvmntCxlReqId

	@AgtCAMvmntCxlReqId.setter
	def AgtCAMvmntCxlReqId(self, value):
		self._AgtCAMvmntCxlReqId = value if value is not None else base_types.UninitialisedField(self, 'AgtCAMvmntCxlReqId', DocumentIdentification8, False)

	@AgtCAMvmntCxlReqId.deleter
	def AgtCAMvmntCxlReqId(self):
		del self._AgtCAMvmntCxlReqId
		self._AgtCAMvmntCxlReqId = base_types.UninitialisedField(self, 'AgtCAMvmntCxlReqId', DocumentIdentification8, False)

	@property
	def AgtCAMvmntInstrId(self):
		return self._AgtCAMvmntInstrId

	@AgtCAMvmntInstrId.setter
	def AgtCAMvmntInstrId(self, value):
		self._AgtCAMvmntInstrId = value if value is not None else base_types.UninitialisedField(self, 'AgtCAMvmntInstrId', DocumentIdentification8, False)

	@AgtCAMvmntInstrId.deleter
	def AgtCAMvmntInstrId(self):
		del self._AgtCAMvmntInstrId
		self._AgtCAMvmntInstrId = base_types.UninitialisedField(self, 'AgtCAMvmntInstrId', DocumentIdentification8, False)

	@property
	def CorpActnGnlInf(self):
		return self._CorpActnGnlInf

	@CorpActnGnlInf.setter
	def CorpActnGnlInf(self, value):
		self._CorpActnGnlInf = value if value is not None else base_types.UninitialisedField(self, 'CorpActnGnlInf', CorporateActionInformation1, False)

	@CorpActnGnlInf.deleter
	def CorpActnGnlInf(self):
		del self._CorpActnGnlInf
		self._CorpActnGnlInf = base_types.UninitialisedField(self, 'CorpActnGnlInf', CorporateActionInformation1, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', DocumentIdentification8, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', DocumentIdentification8, False)

	@property
	def MvmntCxlStsDtls(self):
		return self._MvmntCxlStsDtls

	@MvmntCxlStsDtls.setter
	def MvmntCxlStsDtls(self, value):
		self._MvmntCxlStsDtls = value if value is not None else base_types.UninitialisedField(self, 'MvmntCxlStsDtls', CorporateMovementStatus2, False)

	@MvmntCxlStsDtls.deleter
	def MvmntCxlStsDtls(self):
		del self._MvmntCxlStsDtls
		self._MvmntCxlStsDtls = base_types.UninitialisedField(self, 'MvmntCxlStsDtls', CorporateMovementStatus2, False)

	@property
	def MvmntStsDtls(self):
		return self._MvmntStsDtls

	@MvmntStsDtls.setter
	def MvmntStsDtls(self, value):
		self._MvmntStsDtls = value if value is not None else base_types.UninitialisedField(self, 'MvmntStsDtls', CorporateActionMovementStatus1Choice, False)

	@MvmntStsDtls.deleter
	def MvmntStsDtls(self):
		del self._MvmntStsDtls
		self._MvmntStsDtls = base_types.UninitialisedField(self, 'MvmntStsDtls', CorporateActionMovementStatus1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgtCAElctnStsAdvcId', type=DocumentIdentification8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AgtCAGblDstrbtnStsAdvcId', type=DocumentIdentification8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AgtCAMvmntCxlReqId', type=DocumentIdentification8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AgtCAMvmntInstrId', type=DocumentIdentification8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MvmntCxlStsDtls', type=CorporateMovementStatus2, min=0, max=1, mutex_group=2, array=False),
		base_types.FieldEntry(name='MvmntStsDtls', type=CorporateActionMovementStatus1Choice, min=0, max=1, mutex_group=2, array=False),
	))