from . import base_types
from .AttendanceContext1Code import AttendanceContext1Code
from .Max35Text import Max35Text

class SaleTerminalData1(base_types._BaseFieldType):

	__slots__ = ["_SaleRcncltnId", "_TermnlEnvt"]
	@property
	def SaleRcncltnId(self):
		return self._SaleRcncltnId

	@SaleRcncltnId.setter
	def SaleRcncltnId(self, value):
		self._SaleRcncltnId = value if type(value) != auto else self.make_default("SaleRcncltnId")

	@SaleRcncltnId.deleter
	def SaleRcncltnId(self):
		del self._SaleRcncltnId
		self._SaleRcncltnId = None

	@property
	def TermnlEnvt(self):
		return self._TermnlEnvt

	@TermnlEnvt.setter
	def TermnlEnvt(self, value):
		self._TermnlEnvt = value if type(value) != auto else self.make_default("TermnlEnvt")

	@TermnlEnvt.deleter
	def TermnlEnvt(self):
		del self._TermnlEnvt
		self._TermnlEnvt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SaleRcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermnlEnvt', type=AttendanceContext1Code, min=0, max=1, mutex_group=None, array=False),
	))

