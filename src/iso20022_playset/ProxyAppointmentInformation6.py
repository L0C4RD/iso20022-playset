import base_types
import Proxy11
import Max350Text
import DateFormat58Choice

class ProxyAppointmentInformation6(base_types._BaseFieldType):

	__slots__ = ["_RegnMtd", "_AuthrsdPrxy", "_Ddln", "_MktDdln"]
	@property
	def RegnMtd(self):
		return self._RegnMtd

	@RegnMtd.setter
	def RegnMtd(self, value):
		self._RegnMtd = value if type(value) != auto else self.make_default("RegnMtd")

	@RegnMtd.deleter
	def RegnMtd(self):
		del self._RegnMtd
		self._RegnMtd = None

	@property
	def AuthrsdPrxy(self):
		return self._AuthrsdPrxy

	@AuthrsdPrxy.setter
	def AuthrsdPrxy(self, value):
		self._AuthrsdPrxy = value if type(value) != auto else self.make_default("AuthrsdPrxy")

	@AuthrsdPrxy.deleter
	def AuthrsdPrxy(self):
		del self._AuthrsdPrxy
		self._AuthrsdPrxy = None

	@property
	def Ddln(self):
		return self._Ddln

	@Ddln.setter
	def Ddln(self, value):
		self._Ddln = value if type(value) != auto else self.make_default("Ddln")

	@Ddln.deleter
	def Ddln(self):
		del self._Ddln
		self._Ddln = None

	@property
	def MktDdln(self):
		return self._MktDdln

	@MktDdln.setter
	def MktDdln(self, value):
		self._MktDdln = value if type(value) != auto else self.make_default("MktDdln")

	@MktDdln.deleter
	def MktDdln(self):
		del self._MktDdln
		self._MktDdln = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RegnMtd', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthrsdPrxy', type=Proxy11, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ddln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
	))

