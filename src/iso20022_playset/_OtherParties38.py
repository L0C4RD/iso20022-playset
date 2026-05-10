from . import base_types
from ._PartyIdentification136 import PartyIdentification136
from ._PartyIdentification149 import PartyIdentification149

class OtherParties38(base_types._BaseFieldType):

	__slots__ = ["_Invstr", "_Issr"]
	@property
	def Invstr(self):
		return self._Invstr

	@Invstr.setter
	def Invstr(self, value):
		self._Invstr = value if type(value) != base_types.auto else self.make_default("Invstr")

	@Invstr.deleter
	def Invstr(self):
		del self._Invstr
		self._Invstr = None

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if type(value) != base_types.auto else self.make_default("Issr")

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Invstr', type=PartyIdentification149, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Issr', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
	))

