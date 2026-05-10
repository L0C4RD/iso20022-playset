from . import base_types
from ._DateFormat58Choice import DateFormat58Choice
from ._Max350Text import Max350Text
from ._Proxy11 import Proxy11

class ProxyAppointmentInformation6(base_types._BaseFieldType):

	__slots__ = ["_AuthrsdPrxy", "_Ddln", "_MktDdln", "_RegnMtd"]
	@property
	def AuthrsdPrxy(self):
		return self._AuthrsdPrxy

	@AuthrsdPrxy.setter
	def AuthrsdPrxy(self, value):
		self._AuthrsdPrxy = value if type(value) != base_types.auto else self.make_default("AuthrsdPrxy")

	@AuthrsdPrxy.deleter
	def AuthrsdPrxy(self):
		del self._AuthrsdPrxy
		self._AuthrsdPrxy = None

	@property
	def Ddln(self):
		return self._Ddln

	@Ddln.setter
	def Ddln(self, value):
		self._Ddln = value if type(value) != base_types.auto else self.make_default("Ddln")

	@Ddln.deleter
	def Ddln(self):
		del self._Ddln
		self._Ddln = None

	@property
	def MktDdln(self):
		return self._MktDdln

	@MktDdln.setter
	def MktDdln(self, value):
		self._MktDdln = value if type(value) != base_types.auto else self.make_default("MktDdln")

	@MktDdln.deleter
	def MktDdln(self):
		del self._MktDdln
		self._MktDdln = None

	@property
	def RegnMtd(self):
		return self._RegnMtd

	@RegnMtd.setter
	def RegnMtd(self, value):
		self._RegnMtd = value if type(value) != base_types.auto else self.make_default("RegnMtd")

	@RegnMtd.deleter
	def RegnMtd(self):
		del self._RegnMtd
		self._RegnMtd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AuthrsdPrxy', type=Proxy11, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ddln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnMtd', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))

