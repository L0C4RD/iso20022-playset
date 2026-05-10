from . import base_types
from .Max35Text import Max35Text
from .CardSecurityCapability1Code import CardSecurityCapability1Code

class CardSecurityCapability1(base_types._BaseFieldType):

	__slots__ = ["_Cpblty", "_OthrCpblty"]
	@property
	def Cpblty(self):
		return self._Cpblty

	@Cpblty.setter
	def Cpblty(self, value):
		self._Cpblty = value if type(value) != auto else self.make_default("Cpblty")

	@Cpblty.deleter
	def Cpblty(self):
		del self._Cpblty
		self._Cpblty = None

	@property
	def OthrCpblty(self):
		return self._OthrCpblty

	@OthrCpblty.setter
	def OthrCpblty(self, value):
		self._OthrCpblty = value if type(value) != auto else self.make_default("OthrCpblty")

	@OthrCpblty.deleter
	def OthrCpblty(self):
		del self._OthrCpblty
		self._OthrCpblty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cpblty', type=CardSecurityCapability1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrCpblty', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

