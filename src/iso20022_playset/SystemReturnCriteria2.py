from . import base_types
from .RequestedIndicator import RequestedIndicator

class SystemReturnCriteria2(base_types._BaseFieldType):

	__slots__ = ["_CtryIdInd", "_AcctIdInd", "_SysIdInd", "_MmbIdInd"]
	@property
	def CtryIdInd(self):
		return self._CtryIdInd

	@CtryIdInd.setter
	def CtryIdInd(self, value):
		self._CtryIdInd = value if type(value) != auto else self.make_default("CtryIdInd")

	@CtryIdInd.deleter
	def CtryIdInd(self):
		del self._CtryIdInd
		self._CtryIdInd = None

	@property
	def AcctIdInd(self):
		return self._AcctIdInd

	@AcctIdInd.setter
	def AcctIdInd(self, value):
		self._AcctIdInd = value if type(value) != auto else self.make_default("AcctIdInd")

	@AcctIdInd.deleter
	def AcctIdInd(self):
		del self._AcctIdInd
		self._AcctIdInd = None

	@property
	def SysIdInd(self):
		return self._SysIdInd

	@SysIdInd.setter
	def SysIdInd(self, value):
		self._SysIdInd = value if type(value) != auto else self.make_default("SysIdInd")

	@SysIdInd.deleter
	def SysIdInd(self):
		del self._SysIdInd
		self._SysIdInd = None

	@property
	def MmbIdInd(self):
		return self._MmbIdInd

	@MmbIdInd.setter
	def MmbIdInd(self, value):
		self._MmbIdInd = value if type(value) != auto else self.make_default("MmbIdInd")

	@MmbIdInd.deleter
	def MmbIdInd(self):
		del self._MmbIdInd
		self._MmbIdInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtryIdInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctIdInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysIdInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MmbIdInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
	))

