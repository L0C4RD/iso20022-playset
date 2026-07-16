# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionInformation1
from . import DocumentIdentification8
from . import GlobalDistributionStatus1
from . import IndividualMovementStatus1

class AgentCAGlobalDistributionStatusAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_AgtCAGblDstrbtnAuthstnReqId", "_CorpActnGnlInf", "_GblMvmntSts", "_Id", "_IndvMvmntSts"]
	@property
	def AgtCAGblDstrbtnAuthstnReqId(self):
		return self._AgtCAGblDstrbtnAuthstnReqId

	@AgtCAGblDstrbtnAuthstnReqId.setter
	def AgtCAGblDstrbtnAuthstnReqId(self, value):
		self._AgtCAGblDstrbtnAuthstnReqId = value if value is not None else base_types.UninitialisedField(self, 'AgtCAGblDstrbtnAuthstnReqId', DocumentIdentification8, False)

	@AgtCAGblDstrbtnAuthstnReqId.deleter
	def AgtCAGblDstrbtnAuthstnReqId(self):
		del self._AgtCAGblDstrbtnAuthstnReqId
		self._AgtCAGblDstrbtnAuthstnReqId = base_types.UninitialisedField(self, 'AgtCAGblDstrbtnAuthstnReqId', DocumentIdentification8, False)

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
	def GblMvmntSts(self):
		return self._GblMvmntSts

	@GblMvmntSts.setter
	def GblMvmntSts(self, value):
		self._GblMvmntSts = value if value is not None else base_types.UninitialisedField(self, 'GblMvmntSts', GlobalDistributionStatus1, False)

	@GblMvmntSts.deleter
	def GblMvmntSts(self):
		del self._GblMvmntSts
		self._GblMvmntSts = base_types.UninitialisedField(self, 'GblMvmntSts', GlobalDistributionStatus1, False)

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
	def IndvMvmntSts(self):
		return self._IndvMvmntSts

	@IndvMvmntSts.setter
	def IndvMvmntSts(self, value):
		self._IndvMvmntSts = value if value is not None else base_types.UninitialisedField(self, 'IndvMvmntSts', IndividualMovementStatus1, True)

	@IndvMvmntSts.deleter
	def IndvMvmntSts(self):
		del self._IndvMvmntSts
		self._IndvMvmntSts = base_types.UninitialisedField(self, 'IndvMvmntSts', IndividualMovementStatus1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgtCAGblDstrbtnAuthstnReqId', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GblMvmntSts', type=GlobalDistributionStatus1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndvMvmntSts', type=IndividualMovementStatus1, min=1, max=None, mutex_group=1, array=True),
	))