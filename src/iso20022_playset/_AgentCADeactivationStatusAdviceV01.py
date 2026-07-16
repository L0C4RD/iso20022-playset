# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionDeactivationCancellationStatus1Choice
from . import CorporateActionDeactivationInstructionStatus1
from . import CorporateActionInformation1
from . import DocumentIdentification8

class AgentCADeactivationStatusAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_AgtCADeactvtnCxlReqId", "_AgtCADeactvtnInstrId", "_CorpActnGnlInf", "_DeactvtnCxlReqSts", "_DeactvtnInstrSts", "_Id"]
	@property
	def AgtCADeactvtnCxlReqId(self):
		return self._AgtCADeactvtnCxlReqId

	@AgtCADeactvtnCxlReqId.setter
	def AgtCADeactvtnCxlReqId(self, value):
		self._AgtCADeactvtnCxlReqId = value if value is not None else base_types.UninitialisedField(self, 'AgtCADeactvtnCxlReqId', DocumentIdentification8, False)

	@AgtCADeactvtnCxlReqId.deleter
	def AgtCADeactvtnCxlReqId(self):
		del self._AgtCADeactvtnCxlReqId
		self._AgtCADeactvtnCxlReqId = base_types.UninitialisedField(self, 'AgtCADeactvtnCxlReqId', DocumentIdentification8, False)

	@property
	def AgtCADeactvtnInstrId(self):
		return self._AgtCADeactvtnInstrId

	@AgtCADeactvtnInstrId.setter
	def AgtCADeactvtnInstrId(self, value):
		self._AgtCADeactvtnInstrId = value if value is not None else base_types.UninitialisedField(self, 'AgtCADeactvtnInstrId', DocumentIdentification8, False)

	@AgtCADeactvtnInstrId.deleter
	def AgtCADeactvtnInstrId(self):
		del self._AgtCADeactvtnInstrId
		self._AgtCADeactvtnInstrId = base_types.UninitialisedField(self, 'AgtCADeactvtnInstrId', DocumentIdentification8, False)

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
	def DeactvtnCxlReqSts(self):
		return self._DeactvtnCxlReqSts

	@DeactvtnCxlReqSts.setter
	def DeactvtnCxlReqSts(self, value):
		self._DeactvtnCxlReqSts = value if value is not None else base_types.UninitialisedField(self, 'DeactvtnCxlReqSts', CorporateActionDeactivationCancellationStatus1Choice, False)

	@DeactvtnCxlReqSts.deleter
	def DeactvtnCxlReqSts(self):
		del self._DeactvtnCxlReqSts
		self._DeactvtnCxlReqSts = base_types.UninitialisedField(self, 'DeactvtnCxlReqSts', CorporateActionDeactivationCancellationStatus1Choice, False)

	@property
	def DeactvtnInstrSts(self):
		return self._DeactvtnInstrSts

	@DeactvtnInstrSts.setter
	def DeactvtnInstrSts(self, value):
		self._DeactvtnInstrSts = value if value is not None else base_types.UninitialisedField(self, 'DeactvtnInstrSts', CorporateActionDeactivationInstructionStatus1, True)

	@DeactvtnInstrSts.deleter
	def DeactvtnInstrSts(self):
		del self._DeactvtnInstrSts
		self._DeactvtnInstrSts = base_types.UninitialisedField(self, 'DeactvtnInstrSts', CorporateActionDeactivationInstructionStatus1, True)

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
		base_types.FieldEntry(name='AgtCADeactvtnCxlReqId', type=DocumentIdentification8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AgtCADeactvtnInstrId', type=DocumentIdentification8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DeactvtnCxlReqSts', type=CorporateActionDeactivationCancellationStatus1Choice, min=0, max=1, mutex_group=2, array=False),
		base_types.FieldEntry(name='DeactvtnInstrSts', type=CorporateActionDeactivationInstructionStatus1, min=1, max=None, mutex_group=2, array=True),
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
	))