# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashMovement3
from . import CorporateActionInformation1
from . import CorporateActionSecuritiesMovement1
from . import DocumentIdentification8

class AgentCAMovementConfirmationV01(base_types._BaseFieldType):

	__slots__ = ["_AgtCAElctnStsAdvcId", "_AgtCAGblDstrbtnStsAdvcId", "_AgtCAMvmntInstrId", "_CorpActnGnlInf", "_CshMvmntDtls", "_Id", "_SctiesMvmntDtls"]
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
	def CshMvmntDtls(self):
		return self._CshMvmntDtls

	@CshMvmntDtls.setter
	def CshMvmntDtls(self, value):
		self._CshMvmntDtls = value if value is not None else base_types.UninitialisedField(self, 'CshMvmntDtls', CashMovement3, True)

	@CshMvmntDtls.deleter
	def CshMvmntDtls(self):
		del self._CshMvmntDtls
		self._CshMvmntDtls = base_types.UninitialisedField(self, 'CshMvmntDtls', CashMovement3, True)

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
	def SctiesMvmntDtls(self):
		return self._SctiesMvmntDtls

	@SctiesMvmntDtls.setter
	def SctiesMvmntDtls(self, value):
		self._SctiesMvmntDtls = value if value is not None else base_types.UninitialisedField(self, 'SctiesMvmntDtls', CorporateActionSecuritiesMovement1, True)

	@SctiesMvmntDtls.deleter
	def SctiesMvmntDtls(self):
		del self._SctiesMvmntDtls
		self._SctiesMvmntDtls = base_types.UninitialisedField(self, 'SctiesMvmntDtls', CorporateActionSecuritiesMovement1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgtCAElctnStsAdvcId', type=DocumentIdentification8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AgtCAGblDstrbtnStsAdvcId', type=DocumentIdentification8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AgtCAMvmntInstrId', type=DocumentIdentification8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshMvmntDtls', type=CashMovement3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesMvmntDtls', type=CorporateActionSecuritiesMovement1, min=0, max=None, mutex_group=None, array=True),
	))