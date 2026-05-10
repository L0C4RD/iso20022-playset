import base_types
import IndividualMovementStatus1
import DocumentIdentification8
import GlobalDistributionStatus1
import CorporateActionInformation1

class AgentCAGlobalDistributionStatusAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_Id", "_AgtCAGblDstrbtnAuthstnReqId", "_GblMvmntSts", "_CorpActnGnlInf", "_IndvMvmntSts"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def AgtCAGblDstrbtnAuthstnReqId(self):
		return self._AgtCAGblDstrbtnAuthstnReqId

	@AgtCAGblDstrbtnAuthstnReqId.setter
	def AgtCAGblDstrbtnAuthstnReqId(self, value):
		self._AgtCAGblDstrbtnAuthstnReqId = value if type(value) != auto else self.make_default("AgtCAGblDstrbtnAuthstnReqId")

	@AgtCAGblDstrbtnAuthstnReqId.deleter
	def AgtCAGblDstrbtnAuthstnReqId(self):
		del self._AgtCAGblDstrbtnAuthstnReqId
		self._AgtCAGblDstrbtnAuthstnReqId = None

	@property
	def GblMvmntSts(self):
		return self._GblMvmntSts

	@GblMvmntSts.setter
	def GblMvmntSts(self, value):
		self._GblMvmntSts = value if type(value) != auto else self.make_default("GblMvmntSts")

	@GblMvmntSts.deleter
	def GblMvmntSts(self):
		del self._GblMvmntSts
		self._GblMvmntSts = None

	@property
	def CorpActnGnlInf(self):
		return self._CorpActnGnlInf

	@CorpActnGnlInf.setter
	def CorpActnGnlInf(self, value):
		self._CorpActnGnlInf = value if type(value) != auto else self.make_default("CorpActnGnlInf")

	@CorpActnGnlInf.deleter
	def CorpActnGnlInf(self):
		del self._CorpActnGnlInf
		self._CorpActnGnlInf = None

	@property
	def IndvMvmntSts(self):
		return self._IndvMvmntSts

	@IndvMvmntSts.setter
	def IndvMvmntSts(self, value):
		self._IndvMvmntSts = value if type(value) != auto else self.make_default("IndvMvmntSts")

	@IndvMvmntSts.deleter
	def IndvMvmntSts(self):
		del self._IndvMvmntSts
		self._IndvMvmntSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtCAGblDstrbtnAuthstnReqId', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GblMvmntSts', type=GlobalDistributionStatus1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndvMvmntSts', type=IndividualMovementStatus1, min=1, max=None, mutex_group=1, array=True),
	))

