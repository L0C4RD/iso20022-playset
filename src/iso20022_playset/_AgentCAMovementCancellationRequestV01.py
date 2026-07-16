# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionInformation1
from . import DocumentIdentification8
from . import MovementInstruction1

class AgentCAMovementCancellationRequestV01(base_types._BaseFieldType):

	__slots__ = ["_AgtCAMvmntInstrId", "_CorpActnGnlInf", "_Id", "_MvmntDtls"]
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
	def MvmntDtls(self):
		return self._MvmntDtls

	@MvmntDtls.setter
	def MvmntDtls(self, value):
		self._MvmntDtls = value if value is not None else base_types.UninitialisedField(self, 'MvmntDtls', MovementInstruction1, False)

	@MvmntDtls.deleter
	def MvmntDtls(self):
		del self._MvmntDtls
		self._MvmntDtls = base_types.UninitialisedField(self, 'MvmntDtls', MovementInstruction1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgtCAMvmntInstrId', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MvmntDtls', type=MovementInstruction1, min=0, max=1, mutex_group=None, array=False),
	))