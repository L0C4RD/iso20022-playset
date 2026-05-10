from . import base_types
from .Number3Choice import Number3Choice
from .Period7Choice import Period7Choice
from .StatementBasis8Choice import StatementBasis8Choice
from .Frequency25Choice import Frequency25Choice
from .YesNoIndicator import YesNoIndicator
from .UpdateType15Choice import UpdateType15Choice
from .Max35Text import Max35Text

class Statement79(base_types._BaseFieldType):

	__slots__ = ["_StmtId", "_ActvtyInd", "_SubAcctInd", "_UpdTp", "_RptNb", "_StmtBsis", "_Frqcy", "_QryRef", "_StmtPrd"]
	@property
	def StmtId(self):
		return self._StmtId

	@StmtId.setter
	def StmtId(self, value):
		self._StmtId = value if type(value) != base_types.auto else self.make_default("StmtId")

	@StmtId.deleter
	def StmtId(self):
		del self._StmtId
		self._StmtId = None

	@property
	def ActvtyInd(self):
		return self._ActvtyInd

	@ActvtyInd.setter
	def ActvtyInd(self, value):
		self._ActvtyInd = value if type(value) != base_types.auto else self.make_default("ActvtyInd")

	@ActvtyInd.deleter
	def ActvtyInd(self):
		del self._ActvtyInd
		self._ActvtyInd = None

	@property
	def SubAcctInd(self):
		return self._SubAcctInd

	@SubAcctInd.setter
	def SubAcctInd(self, value):
		self._SubAcctInd = value if type(value) != base_types.auto else self.make_default("SubAcctInd")

	@SubAcctInd.deleter
	def SubAcctInd(self):
		del self._SubAcctInd
		self._SubAcctInd = None

	@property
	def UpdTp(self):
		return self._UpdTp

	@UpdTp.setter
	def UpdTp(self, value):
		self._UpdTp = value if type(value) != base_types.auto else self.make_default("UpdTp")

	@UpdTp.deleter
	def UpdTp(self):
		del self._UpdTp
		self._UpdTp = None

	@property
	def RptNb(self):
		return self._RptNb

	@RptNb.setter
	def RptNb(self, value):
		self._RptNb = value if type(value) != base_types.auto else self.make_default("RptNb")

	@RptNb.deleter
	def RptNb(self):
		del self._RptNb
		self._RptNb = None

	@property
	def StmtBsis(self):
		return self._StmtBsis

	@StmtBsis.setter
	def StmtBsis(self, value):
		self._StmtBsis = value if type(value) != base_types.auto else self.make_default("StmtBsis")

	@StmtBsis.deleter
	def StmtBsis(self):
		del self._StmtBsis
		self._StmtBsis = None

	@property
	def Frqcy(self):
		return self._Frqcy

	@Frqcy.setter
	def Frqcy(self, value):
		self._Frqcy = value if type(value) != base_types.auto else self.make_default("Frqcy")

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = None

	@property
	def QryRef(self):
		return self._QryRef

	@QryRef.setter
	def QryRef(self, value):
		self._QryRef = value if type(value) != base_types.auto else self.make_default("QryRef")

	@QryRef.deleter
	def QryRef(self):
		del self._QryRef
		self._QryRef = None

	@property
	def StmtPrd(self):
		return self._StmtPrd

	@StmtPrd.setter
	def StmtPrd(self, value):
		self._StmtPrd = value if type(value) != base_types.auto else self.make_default("StmtPrd")

	@StmtPrd.deleter
	def StmtPrd(self):
		del self._StmtPrd
		self._StmtPrd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='StmtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActvtyInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubAcctInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdTp', type=UpdateType15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptNb', type=Number3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtBsis', type=StatementBasis8Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=Frequency25Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtPrd', type=Period7Choice, min=1, max=1, mutex_group=None, array=False),
	))

