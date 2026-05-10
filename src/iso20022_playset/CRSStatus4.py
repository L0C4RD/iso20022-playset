from . import base_types
from .CountryCode import CountryCode
from .CRSStatus3Choice import CRSStatus3Choice
from .CRSSource1Choice import CRSSource1Choice

class CRSStatus4(base_types._BaseFieldType):

	__slots__ = ["_XcptnlRptgCtry", "_Src", "_Tp"]
	@property
	def XcptnlRptgCtry(self):
		return self._XcptnlRptgCtry

	@XcptnlRptgCtry.setter
	def XcptnlRptgCtry(self, value):
		self._XcptnlRptgCtry = value if type(value) != auto else self.make_default("XcptnlRptgCtry")

	@XcptnlRptgCtry.deleter
	def XcptnlRptgCtry(self):
		del self._XcptnlRptgCtry
		self._XcptnlRptgCtry = None

	@property
	def Src(self):
		return self._Src

	@Src.setter
	def Src(self, value):
		self._Src = value if type(value) != auto else self.make_default("Src")

	@Src.deleter
	def Src(self):
		del self._Src
		self._Src = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='XcptnlRptgCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Src', type=CRSSource1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=CRSStatus3Choice, min=1, max=1, mutex_group=None, array=False),
	))

