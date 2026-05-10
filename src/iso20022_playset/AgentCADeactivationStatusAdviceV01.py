import base_types
import DocumentIdentification8
import CorporateActionDeactivationInstructionStatus1
import CorporateActionDeactivationCancellationStatus1Choice
import CorporateActionInformation1

class AgentCADeactivationStatusAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_AgtCADeactvtnCxlReqId", "_DeactvtnInstrSts", "_DeactvtnCxlReqSts", "_Id", "_CorpActnGnlInf", "_AgtCADeactvtnInstrId"]
	@property
	def AgtCADeactvtnCxlReqId(self):
		return self._AgtCADeactvtnCxlReqId

	@AgtCADeactvtnCxlReqId.setter
	def AgtCADeactvtnCxlReqId(self, value):
		self._AgtCADeactvtnCxlReqId = value if type(value) != auto else self.make_default("AgtCADeactvtnCxlReqId")

	@AgtCADeactvtnCxlReqId.deleter
	def AgtCADeactvtnCxlReqId(self):
		del self._AgtCADeactvtnCxlReqId
		self._AgtCADeactvtnCxlReqId = None

	@property
	def DeactvtnInstrSts(self):
		return self._DeactvtnInstrSts

	@DeactvtnInstrSts.setter
	def DeactvtnInstrSts(self, value):
		self._DeactvtnInstrSts = value if type(value) != auto else self.make_default("DeactvtnInstrSts")

	@DeactvtnInstrSts.deleter
	def DeactvtnInstrSts(self):
		del self._DeactvtnInstrSts
		self._DeactvtnInstrSts = None

	@property
	def DeactvtnCxlReqSts(self):
		return self._DeactvtnCxlReqSts

	@DeactvtnCxlReqSts.setter
	def DeactvtnCxlReqSts(self, value):
		self._DeactvtnCxlReqSts = value if type(value) != auto else self.make_default("DeactvtnCxlReqSts")

	@DeactvtnCxlReqSts.deleter
	def DeactvtnCxlReqSts(self):
		del self._DeactvtnCxlReqSts
		self._DeactvtnCxlReqSts = None

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
	def AgtCADeactvtnInstrId(self):
		return self._AgtCADeactvtnInstrId

	@AgtCADeactvtnInstrId.setter
	def AgtCADeactvtnInstrId(self, value):
		self._AgtCADeactvtnInstrId = value if type(value) != auto else self.make_default("AgtCADeactvtnInstrId")

	@AgtCADeactvtnInstrId.deleter
	def AgtCADeactvtnInstrId(self):
		del self._AgtCADeactvtnInstrId
		self._AgtCADeactvtnInstrId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgtCADeactvtnCxlReqId', type=DocumentIdentification8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DeactvtnInstrSts', type=CorporateActionDeactivationInstructionStatus1, min=1, max=None, mutex_group=2, array=True),
		base_types.FieldEntry(name='DeactvtnCxlReqSts', type=CorporateActionDeactivationCancellationStatus1Choice, min=0, max=1, mutex_group=2, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtCADeactvtnInstrId', type=DocumentIdentification8, min=0, max=1, mutex_group=1, array=False),
	))

