from . import base_types
from .Max35Text import Max35Text
from .YesNoIndicator import YesNoIndicator
from .DateAndDateTime2Choice import DateAndDateTime2Choice
from .EventFrequency6Code import EventFrequency6Code
from .Exact5NumericText import Exact5NumericText
from .StatementUpdateType1Code import StatementUpdateType1Code

class ReportParameters7(base_types._BaseFieldType):

	__slots__ = ["_RptDtAndTm", "_NetPosId", "_Frqcy", "_ActvtyInd", "_UpdTp", "_RptNb"]
	@property
	def RptDtAndTm(self):
		return self._RptDtAndTm

	@RptDtAndTm.setter
	def RptDtAndTm(self, value):
		self._RptDtAndTm = value if type(value) != auto else self.make_default("RptDtAndTm")

	@RptDtAndTm.deleter
	def RptDtAndTm(self):
		del self._RptDtAndTm
		self._RptDtAndTm = None

	@property
	def NetPosId(self):
		return self._NetPosId

	@NetPosId.setter
	def NetPosId(self, value):
		self._NetPosId = value if type(value) != auto else self.make_default("NetPosId")

	@NetPosId.deleter
	def NetPosId(self):
		del self._NetPosId
		self._NetPosId = None

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
		base_types.FieldEntry(name='RptDtAndTm', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetPosId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=EventFrequency6Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActvtyInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdTp', type=StatementUpdateType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptNb', type=Exact5NumericText, min=0, max=1, mutex_group=None, array=False),
	))

