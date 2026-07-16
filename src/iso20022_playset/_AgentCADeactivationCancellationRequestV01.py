# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionDeactivationInstruction1
from . import CorporateActionInformation1
from . import DocumentIdentification8

class AgentCADeactivationCancellationRequestV01(base_types._BaseFieldType):

	__slots__ = ["_AgtCADeactvtnInstrId", "_CorpActnGnlInf", "_DeactvtnInstrDtls", "_Id"]
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
	def DeactvtnInstrDtls(self):
		return self._DeactvtnInstrDtls

	@DeactvtnInstrDtls.setter
	def DeactvtnInstrDtls(self, value):
		self._DeactvtnInstrDtls = value if value is not None else base_types.UninitialisedField(self, 'DeactvtnInstrDtls', CorporateActionDeactivationInstruction1, False)

	@DeactvtnInstrDtls.deleter
	def DeactvtnInstrDtls(self):
		del self._DeactvtnInstrDtls
		self._DeactvtnInstrDtls = base_types.UninitialisedField(self, 'DeactvtnInstrDtls', CorporateActionDeactivationInstruction1, False)

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
		base_types.FieldEntry(name='AgtCADeactvtnInstrId', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DeactvtnInstrDtls', type=CorporateActionDeactivationInstruction1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
	))