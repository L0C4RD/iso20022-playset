# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionInformation1
from . import DocumentIdentification8
from . import ElectionAdviceStatus1Choice
from . import ElectionAmendmentStatus1Choice
from . import ElectionCancellationStatus1Choice

class AgentCAElectionStatusAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_AgtCAElctnAdvcId", "_AgtCAElctnAmdmntReqId", "_AgtCAElctnCxlReqId", "_CorpActnGnlInf", "_ElctnAdvcSts", "_ElctnAmdmntReqSts", "_ElctnCxlReqSts", "_Id"]
	@property
	def AgtCAElctnAdvcId(self):
		return self._AgtCAElctnAdvcId

	@AgtCAElctnAdvcId.setter
	def AgtCAElctnAdvcId(self, value):
		self._AgtCAElctnAdvcId = value if value is not None else base_types.UninitialisedField(self, 'AgtCAElctnAdvcId', DocumentIdentification8, False)

	@AgtCAElctnAdvcId.deleter
	def AgtCAElctnAdvcId(self):
		del self._AgtCAElctnAdvcId
		self._AgtCAElctnAdvcId = base_types.UninitialisedField(self, 'AgtCAElctnAdvcId', DocumentIdentification8, False)

	@property
	def AgtCAElctnAmdmntReqId(self):
		return self._AgtCAElctnAmdmntReqId

	@AgtCAElctnAmdmntReqId.setter
	def AgtCAElctnAmdmntReqId(self, value):
		self._AgtCAElctnAmdmntReqId = value if value is not None else base_types.UninitialisedField(self, 'AgtCAElctnAmdmntReqId', DocumentIdentification8, False)

	@AgtCAElctnAmdmntReqId.deleter
	def AgtCAElctnAmdmntReqId(self):
		del self._AgtCAElctnAmdmntReqId
		self._AgtCAElctnAmdmntReqId = base_types.UninitialisedField(self, 'AgtCAElctnAmdmntReqId', DocumentIdentification8, False)

	@property
	def AgtCAElctnCxlReqId(self):
		return self._AgtCAElctnCxlReqId

	@AgtCAElctnCxlReqId.setter
	def AgtCAElctnCxlReqId(self, value):
		self._AgtCAElctnCxlReqId = value if value is not None else base_types.UninitialisedField(self, 'AgtCAElctnCxlReqId', DocumentIdentification8, False)

	@AgtCAElctnCxlReqId.deleter
	def AgtCAElctnCxlReqId(self):
		del self._AgtCAElctnCxlReqId
		self._AgtCAElctnCxlReqId = base_types.UninitialisedField(self, 'AgtCAElctnCxlReqId', DocumentIdentification8, False)

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
	def ElctnAdvcSts(self):
		return self._ElctnAdvcSts

	@ElctnAdvcSts.setter
	def ElctnAdvcSts(self, value):
		self._ElctnAdvcSts = value if value is not None else base_types.UninitialisedField(self, 'ElctnAdvcSts', ElectionAdviceStatus1Choice, False)

	@ElctnAdvcSts.deleter
	def ElctnAdvcSts(self):
		del self._ElctnAdvcSts
		self._ElctnAdvcSts = base_types.UninitialisedField(self, 'ElctnAdvcSts', ElectionAdviceStatus1Choice, False)

	@property
	def ElctnAmdmntReqSts(self):
		return self._ElctnAmdmntReqSts

	@ElctnAmdmntReqSts.setter
	def ElctnAmdmntReqSts(self, value):
		self._ElctnAmdmntReqSts = value if value is not None else base_types.UninitialisedField(self, 'ElctnAmdmntReqSts', ElectionAmendmentStatus1Choice, False)

	@ElctnAmdmntReqSts.deleter
	def ElctnAmdmntReqSts(self):
		del self._ElctnAmdmntReqSts
		self._ElctnAmdmntReqSts = base_types.UninitialisedField(self, 'ElctnAmdmntReqSts', ElectionAmendmentStatus1Choice, False)

	@property
	def ElctnCxlReqSts(self):
		return self._ElctnCxlReqSts

	@ElctnCxlReqSts.setter
	def ElctnCxlReqSts(self, value):
		self._ElctnCxlReqSts = value if value is not None else base_types.UninitialisedField(self, 'ElctnCxlReqSts', ElectionCancellationStatus1Choice, False)

	@ElctnCxlReqSts.deleter
	def ElctnCxlReqSts(self):
		del self._ElctnCxlReqSts
		self._ElctnCxlReqSts = base_types.UninitialisedField(self, 'ElctnCxlReqSts', ElectionCancellationStatus1Choice, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgtCAElctnAdvcId', type=DocumentIdentification8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AgtCAElctnAmdmntReqId', type=DocumentIdentification8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AgtCAElctnCxlReqId', type=DocumentIdentification8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElctnAdvcSts', type=ElectionAdviceStatus1Choice, min=0, max=1, mutex_group=2, array=False),
		base_types.FieldEntry(name='ElctnAmdmntReqSts', type=ElectionAmendmentStatus1Choice, min=0, max=1, mutex_group=2, array=False),
		base_types.FieldEntry(name='ElctnCxlReqSts', type=ElectionCancellationStatus1Choice, min=0, max=1, mutex_group=2, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
	))