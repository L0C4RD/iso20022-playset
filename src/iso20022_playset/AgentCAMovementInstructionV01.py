from . import base_types
import DocumentIdentification8
import CashMovement2
import ProceedsMovement1
import CorporateActionInformation1
import CorporateActionMovement1
import UnderlyingSecurityMovement1

class AgentCAMovementInstructionV01(base_types._BaseFieldType):

	__slots__ = ["_MvmntGnlInf", "_PrcdsMvmntDtls", "_UndrlygSctiesMvmntDtls", "_CorpActnGnlInf", "_UndrlygCshMvmntDtls", "_AgtCAElctnAdvcId", "_Id"]
	@property
	def MvmntGnlInf(self):
		return self._MvmntGnlInf

	@MvmntGnlInf.setter
	def MvmntGnlInf(self, value):
		self._MvmntGnlInf = value if type(value) != auto else self.make_default("MvmntGnlInf")

	@MvmntGnlInf.deleter
	def MvmntGnlInf(self):
		del self._MvmntGnlInf
		self._MvmntGnlInf = None

	@property
	def PrcdsMvmntDtls(self):
		return self._PrcdsMvmntDtls

	@PrcdsMvmntDtls.setter
	def PrcdsMvmntDtls(self, value):
		self._PrcdsMvmntDtls = value if type(value) != auto else self.make_default("PrcdsMvmntDtls")

	@PrcdsMvmntDtls.deleter
	def PrcdsMvmntDtls(self):
		del self._PrcdsMvmntDtls
		self._PrcdsMvmntDtls = None

	@property
	def UndrlygSctiesMvmntDtls(self):
		return self._UndrlygSctiesMvmntDtls

	@UndrlygSctiesMvmntDtls.setter
	def UndrlygSctiesMvmntDtls(self, value):
		self._UndrlygSctiesMvmntDtls = value if type(value) != auto else self.make_default("UndrlygSctiesMvmntDtls")

	@UndrlygSctiesMvmntDtls.deleter
	def UndrlygSctiesMvmntDtls(self):
		del self._UndrlygSctiesMvmntDtls
		self._UndrlygSctiesMvmntDtls = None

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
	def UndrlygCshMvmntDtls(self):
		return self._UndrlygCshMvmntDtls

	@UndrlygCshMvmntDtls.setter
	def UndrlygCshMvmntDtls(self, value):
		self._UndrlygCshMvmntDtls = value if type(value) != auto else self.make_default("UndrlygCshMvmntDtls")

	@UndrlygCshMvmntDtls.deleter
	def UndrlygCshMvmntDtls(self):
		del self._UndrlygCshMvmntDtls
		self._UndrlygCshMvmntDtls = None

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
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MvmntGnlInf', type=CorporateActionMovement1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcdsMvmntDtls', type=ProceedsMovement1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygSctiesMvmntDtls', type=UnderlyingSecurityMovement1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygCshMvmntDtls', type=CashMovement2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AgtCAElctnAdvcId', type=DocumentIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
	))

