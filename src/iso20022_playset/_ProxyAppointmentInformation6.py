# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateFormat58Choice
from . import Max350Text
from . import Proxy11

class ProxyAppointmentInformation6(base_types._BaseFieldType):

	__slots__ = ["_AuthrsdPrxy", "_Ddln", "_MktDdln", "_RegnMtd"]
	@property
	def AuthrsdPrxy(self):
		return self._AuthrsdPrxy

	@AuthrsdPrxy.setter
	def AuthrsdPrxy(self, value):
		self._AuthrsdPrxy = value if value is not None else base_types.UninitialisedField(self, 'AuthrsdPrxy', Proxy11, True)

	@AuthrsdPrxy.deleter
	def AuthrsdPrxy(self):
		del self._AuthrsdPrxy
		self._AuthrsdPrxy = base_types.UninitialisedField(self, 'AuthrsdPrxy', Proxy11, True)

	@property
	def Ddln(self):
		return self._Ddln

	@Ddln.setter
	def Ddln(self, value):
		self._Ddln = value if value is not None else base_types.UninitialisedField(self, 'Ddln', DateFormat58Choice, False)

	@Ddln.deleter
	def Ddln(self):
		del self._Ddln
		self._Ddln = base_types.UninitialisedField(self, 'Ddln', DateFormat58Choice, False)

	@property
	def MktDdln(self):
		return self._MktDdln

	@MktDdln.setter
	def MktDdln(self, value):
		self._MktDdln = value if value is not None else base_types.UninitialisedField(self, 'MktDdln', DateFormat58Choice, False)

	@MktDdln.deleter
	def MktDdln(self):
		del self._MktDdln
		self._MktDdln = base_types.UninitialisedField(self, 'MktDdln', DateFormat58Choice, False)

	@property
	def RegnMtd(self):
		return self._RegnMtd

	@RegnMtd.setter
	def RegnMtd(self, value):
		self._RegnMtd = value if value is not None else base_types.UninitialisedField(self, 'RegnMtd', Max350Text, False)

	@RegnMtd.deleter
	def RegnMtd(self):
		del self._RegnMtd
		self._RegnMtd = base_types.UninitialisedField(self, 'RegnMtd', Max350Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AuthrsdPrxy', type=Proxy11, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ddln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnMtd', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))