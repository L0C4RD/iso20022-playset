from . import base_types
from ._Frequency25Choice import Frequency25Choice
from ._Number3Choice import Number3Choice
from ._UpdateType15Choice import UpdateType15Choice
from ._Max35Text import Max35Text
from ._YesNoIndicator import YesNoIndicator
from ._DateAndDateTime2Choice import DateAndDateTime2Choice

class Statement63(base_types._BaseFieldType):

	__slots__ = ["_StmtDtTm", "_Frqcy", "_StmtId", "_QryRef", "_UpdTp", "_RptNb", "_ActvtyInd"]
	@property
	def StmtDtTm(self):
		return self._StmtDtTm

	@StmtDtTm.setter
	def StmtDtTm(self, value):
		self._StmtDtTm = value if type(value) != base_types.auto else self.make_default("StmtDtTm")

	@StmtDtTm.deleter
	def StmtDtTm(self):
		del self._StmtDtTm
		self._StmtDtTm = None

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
	def ActvtyInd(self):
		return self._ActvtyInd

	@ActvtyInd.setter
	def ActvtyInd(self, value):
		self._ActvtyInd = value if type(value) != base_types.auto else self.make_default("ActvtyInd")

	@ActvtyInd.deleter
	def ActvtyInd(self):
		del self._ActvtyInd
		self._ActvtyInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='StmtDtTm', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=Frequency25Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdTp', type=UpdateType15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptNb', type=Number3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActvtyInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))

