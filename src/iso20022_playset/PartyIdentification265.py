from . import base_types
from .AnyBICDec2014Identifier import AnyBICDec2014Identifier
from .Max35Text import Max35Text

class PartyIdentification265(base_types._BaseFieldType):

	__slots__ = ["_AnyBIC", "_AltrntvIdr"]
	@property
	def AnyBIC(self):
		return self._AnyBIC

	@AnyBIC.setter
	def AnyBIC(self, value):
		self._AnyBIC = value if type(value) != auto else self.make_default("AnyBIC")

	@AnyBIC.deleter
	def AnyBIC(self):
		del self._AnyBIC
		self._AnyBIC = None

	@property
	def AltrntvIdr(self):
		return self._AltrntvIdr

	@AltrntvIdr.setter
	def AltrntvIdr(self, value):
		self._AltrntvIdr = value if type(value) != auto else self.make_default("AltrntvIdr")

	@AltrntvIdr.deleter
	def AltrntvIdr(self):
		del self._AltrntvIdr
		self._AltrntvIdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AnyBIC', type=AnyBICDec2014Identifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AltrntvIdr', type=Max35Text, min=0, max=10, mutex_group=None, array=True),
	))

