from . import base_types
from .Max35Text import Max35Text
from .YesNoIndicator import YesNoIndicator
from .DateAndDateTime2Choice import DateAndDateTime2Choice
from .EventFrequency6Code import EventFrequency6Code
from .Exact5NumericText import Exact5NumericText
from .StatementUpdateType1Code import StatementUpdateType1Code

class Statement86(base_types._BaseFieldType):

	__slots__ = ["_StmtId", "_Frqcy", "_StmtDtAndTm", "_ActvtyInd", "_UpdTp", "_RptNb"]
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
	def StmtDtAndTm(self):
		return self._StmtDtAndTm

	@StmtDtAndTm.setter
	def StmtDtAndTm(self, value):
		self._StmtDtAndTm = value if type(value) != auto else self.make_default("StmtDtAndTm")

	@StmtDtAndTm.deleter
	def StmtDtAndTm(self):
		del self._StmtDtAndTm
		self._StmtDtAndTm = None

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
	def UpdTp(self):
		return self._UpdTp

	@UpdTp.setter
	def UpdTp(self, value):
		self._UpdTp = value if type(value) != auto else self.make_default("UpdTp")

	@UpdTp.deleter
	def UpdTp(self):
		del self._UpdTp
		self._UpdTp = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='StmtId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=EventFrequency6Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtDtAndTm', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActvtyInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdTp', type=StatementUpdateType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptNb', type=Exact5NumericText, min=0, max=1, mutex_group=None, array=False),
	))

