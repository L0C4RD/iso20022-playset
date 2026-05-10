import base_types
import CorporateActionInformation1
import CashMovement3
import CorporateActionSecuritiesMovement1
import DocumentIdentification8

class AgentCAMovementConfirmationV01(base_types._BaseFieldType):

	__slots__ = ["_CorpActnGnlInf", "_Id", "_CshMvmntDtls", "_AgtCAMvmntInstrId", "_SctiesMvmntDtls", "_AgtCAElctnStsAdvcId", "_AgtCAGblDstrbtnStsAdvcId"]
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
	def CshMvmntDtls(self):
		return self._CshMvmntDtls

	@CshMvmntDtls.setter
	def CshMvmntDtls(self, value):
		self._CshMvmntDtls = value if type(value) != auto else self.make_default("CshMvmntDtls")

	@CshMvmntDtls.deleter
	def CshMvmntDtls(self):
		del self._CshMvmntDtls
		self._CshMvmntDtls = None

	@property
	def AgtCAMvmntInstrId(self):
		return self._AgtCAMvmntInstrId

	@AgtCAMvmntInstrId.setter
	def AgtCAMvmntInstrId(self, value):
		self._AgtCAMvmntInstrId = value if type(value) != auto else self.make_default("AgtCAMvmntInstrId")

	@AgtCAMvmntInstrId.deleter
	def AgtCAMvmntInstrId(self):
		del self._AgtCAMvmntInstrId
		self._AgtCAMvmntInstrId = None

	@property
	def SctiesMvmntDtls(self):
		return self._SctiesMvmntDtls

	@SctiesMvmntDtls.setter
	def SctiesMvmntDtls(self, value):
		self._SctiesMvmntDtls = value if type(value) != auto else self.make_default("SctiesMvmntDtls")

	@SctiesMvmntDtls.deleter
	def SctiesMvmntDtls(self):
		del self._SctiesMvmntDtls
		self._SctiesMvmntDtls = None

	@property
	def AgtCAElctnStsAdvcId(self):
		return self._AgtCAElctnStsAdvcId

	@AgtCAElctnStsAdvcId.setter
	def AgtCAElctnStsAdvcId(self, value):
		self._AgtCAElctnStsAdvcId = value if type(value) != auto else self.make_default("AgtCAElctnStsAdvcId")

	@AgtCAElctnStsAdvcId.deleter
	def AgtCAElctnStsAdvcId(self):
		del self._AgtCAElctnStsAdvcId
		self._AgtCAElctnStsAdvcId = None

	@property
	def AgtCAGblDstrbtnStsAdvcId(self):
		return self._AgtCAGblDstrbtnStsAdvcId

	@AgtCAGblDstrbtnStsAdvcId.setter
	def AgtCAGblDstrbtnStsAdvcId(self, value):
		self._AgtCAGblDstrbtnStsAdvcId = value if type(value) != auto else self.make_default("AgtCAGblDstrbtnStsAdvcId")

	@AgtCAGblDstrbtnStsAdvcId.deleter
	def AgtCAGblDstrbtnStsAdvcId(self):
		del self._AgtCAGblDstrbtnStsAdvcId
		self._AgtCAGblDstrbtnStsAdvcId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshMvmntDtls', type=CashMovement3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AgtCAMvmntInstrId', type=DocumentIdentification8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesMvmntDtls', type=CorporateActionSecuritiesMovement1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AgtCAElctnStsAdvcId', type=DocumentIdentification8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AgtCAGblDstrbtnStsAdvcId', type=DocumentIdentification8, min=0, max=1, mutex_group=1, array=False),
	))

