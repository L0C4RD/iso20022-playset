import base_types
import ElectionAmendmentStatus1Choice
import DocumentIdentification8
import ElectionCancellationStatus1Choice
import ElectionAdviceStatus1Choice
import CorporateActionInformation1

class AgentCAElectionStatusAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_CorpActnGnlInf", "_AgtCAElctnAdvcId", "_ElctnCxlReqSts", "_ElctnAmdmntReqSts", "_Id", "_AgtCAElctnCxlReqId", "_ElctnAdvcSts", "_AgtCAElctnAmdmntReqId"]
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
	def AgtCAElctnAdvcId(self):
		return self._AgtCAElctnAdvcId

	@AgtCAElctnAdvcId.setter
	def AgtCAElctnAdvcId(self, value):
		self._AgtCAElctnAdvcId = value if type(value) != auto else self.make_default("AgtCAElctnAdvcId")

	@AgtCAElctnAdvcId.deleter
	def AgtCAElctnAdvcId(self):
		del self._AgtCAElctnAdvcId
		self._AgtCAElctnAdvcId = None

	@property
	def ElctnCxlReqSts(self):
		return self._ElctnCxlReqSts

	@ElctnCxlReqSts.setter
	def ElctnCxlReqSts(self, value):
		self._ElctnCxlReqSts = value if type(value) != auto else self.make_default("ElctnCxlReqSts")

	@ElctnCxlReqSts.deleter
	def ElctnCxlReqSts(self):
		del self._ElctnCxlReqSts
		self._ElctnCxlReqSts = None

	@property
	def ElctnAmdmntReqSts(self):
		return self._ElctnAmdmntReqSts

	@ElctnAmdmntReqSts.setter
	def ElctnAmdmntReqSts(self, value):
		self._ElctnAmdmntReqSts = value if type(value) != auto else self.make_default("ElctnAmdmntReqSts")

	@ElctnAmdmntReqSts.deleter
	def ElctnAmdmntReqSts(self):
		del self._ElctnAmdmntReqSts
		self._ElctnAmdmntReqSts = None

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
	def AgtCAElctnCxlReqId(self):
		return self._AgtCAElctnCxlReqId

	@AgtCAElctnCxlReqId.setter
	def AgtCAElctnCxlReqId(self, value):
		self._AgtCAElctnCxlReqId = value if type(value) != auto else self.make_default("AgtCAElctnCxlReqId")

	@AgtCAElctnCxlReqId.deleter
	def AgtCAElctnCxlReqId(self):
		del self._AgtCAElctnCxlReqId
		self._AgtCAElctnCxlReqId = None

	@property
	def ElctnAdvcSts(self):
		return self._ElctnAdvcSts

	@ElctnAdvcSts.setter
	def ElctnAdvcSts(self, value):
		self._ElctnAdvcSts = value if type(value) != auto else self.make_default("ElctnAdvcSts")

	@ElctnAdvcSts.deleter
	def ElctnAdvcSts(self):
		del self._ElctnAdvcSts
		self._ElctnAdvcSts = None

	@property
	def AgtCAElctnAmdmntReqId(self):
		return self._AgtCAElctnAmdmntReqId

	@AgtCAElctnAmdmntReqId.setter
	def AgtCAElctnAmdmntReqId(self, value):
		self._AgtCAElctnAmdmntReqId = value if type(value) != auto else self.make_default("AgtCAElctnAmdmntReqId")

	@AgtCAElctnAmdmntReqId.deleter
	def AgtCAElctnAmdmntReqId(self):
		del self._AgtCAElctnAmdmntReqId
		self._AgtCAElctnAmdmntReqId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtCAElctnAdvcId', type=DocumentIdentification8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ElctnCxlReqSts', type=ElectionCancellationStatus1Choice, min=0, max=1, mutex_group=2, array=False),
		base_types.FieldEntry(name='ElctnAmdmntReqSts', type=ElectionAmendmentStatus1Choice, min=0, max=1, mutex_group=2, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtCAElctnCxlReqId', type=DocumentIdentification8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ElctnAdvcSts', type=ElectionAdviceStatus1Choice, min=0, max=1, mutex_group=2, array=False),
		base_types.FieldEntry(name='AgtCAElctnAmdmntReqId', type=DocumentIdentification8, min=0, max=1, mutex_group=1, array=False),
	))

