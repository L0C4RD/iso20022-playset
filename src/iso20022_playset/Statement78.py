from . import base_types
import Frequency22Choice
import YesNoIndicator
import DateAndDateTime2Choice
import Number3Choice
import Max35Text
import StatementStatusType1Code
import UpdateType15Choice
import StatementBasis14Choice
import CollateralRole1Code

class Statement78(base_types._BaseFieldType):

	__slots__ = ["_ActvtyInd", "_CollSd", "_StsTp", "_StmtId", "_StmtBsis", "_StmtDtTm", "_SummryInd", "_Frqcy", "_QryRef", "_RptNb", "_UpdTp"]
	@property
	def ActvtyInd(self):
		return self._ActvtyInd

	@ActvtyInd.setter
	def ActvtyInd(self, value):
		self._ActvtyInd = value if type(value) != auto else self.make_default("ActvtyInd")

	@ActvtyInd.deleter
	def ActvtyInd(self):
		del self._ActvtyInd
		self._ActvtyInd = None

	@property
	def CollSd(self):
		return self._CollSd

	@CollSd.setter
	def CollSd(self, value):
		self._CollSd = value if type(value) != auto else self.make_default("CollSd")

	@CollSd.deleter
	def CollSd(self):
		del self._CollSd
		self._CollSd = None

	@property
	def StsTp(self):
		return self._StsTp

	@StsTp.setter
	def StsTp(self, value):
		self._StsTp = value if type(value) != auto else self.make_default("StsTp")

	@StsTp.deleter
	def StsTp(self):
		del self._StsTp
		self._StsTp = None

	@property
	def StmtId(self):
		return self._StmtId

	@StmtId.setter
	def StmtId(self, value):
		self._StmtId = value if type(value) != auto else self.make_default("StmtId")

	@StmtId.deleter
	def StmtId(self):
		del self._StmtId
		self._StmtId = None

	@property
	def StmtBsis(self):
		return self._StmtBsis

	@StmtBsis.setter
	def StmtBsis(self, value):
		self._StmtBsis = value if type(value) != auto else self.make_default("StmtBsis")

	@StmtBsis.deleter
	def StmtBsis(self):
		del self._StmtBsis
		self._StmtBsis = None

	@property
	def StmtDtTm(self):
		return self._StmtDtTm

	@StmtDtTm.setter
	def StmtDtTm(self, value):
		self._StmtDtTm = value if type(value) != auto else self.make_default("StmtDtTm")

	@StmtDtTm.deleter
	def StmtDtTm(self):
		del self._StmtDtTm
		self._StmtDtTm = None

	@property
	def SummryInd(self):
		return self._SummryInd

	@SummryInd.setter
	def SummryInd(self, value):
		self._SummryInd = value if type(value) != auto else self.make_default("SummryInd")

	@SummryInd.deleter
	def SummryInd(self):
		del self._SummryInd
		self._SummryInd = None

	@property
	def Frqcy(self):
		return self._Frqcy

	@Frqcy.setter
	def Frqcy(self, value):
		self._Frqcy = value if type(value) != auto else self.make_default("Frqcy")

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = None

	@property
	def QryRef(self):
		return self._QryRef

	@QryRef.setter
	def QryRef(self, value):
		self._QryRef = value if type(value) != auto else self.make_default("QryRef")

	@QryRef.deleter
	def QryRef(self):
		del self._QryRef
		self._QryRef = None

	@property
	def RptNb(self):
		return self._RptNb

	@RptNb.setter
	def RptNb(self, value):
		self._RptNb = value if type(value) != auto else self.make_default("RptNb")

	@RptNb.deleter
	def RptNb(self):
		del self._RptNb
		self._RptNb = None

	@property
	def UpdTp(self):
		return self._UpdTp

	@UpdTp.setter
	def UpdTp(self, value):
		self._UpdTp = value if type(value) != auto else self.make_default("UpdTp")

	@UpdTp.deleter
	def UpdTp(self):
		del self._UpdTp
		self._UpdTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActvtyInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollSd', type=CollateralRole1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsTp', type=StatementStatusType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtBsis', type=StatementBasis14Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtDtTm', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SummryInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=Frequency22Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptNb', type=Number3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdTp', type=UpdateType15Choice, min=1, max=1, mutex_group=None, array=False),
	))

