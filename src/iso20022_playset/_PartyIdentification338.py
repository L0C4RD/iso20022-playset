from . import base_types
from ._Max35Text import Max35Text
from ._PartyIdentification335Choice import PartyIdentification335Choice

class PartyIdentification338(base_types._BaseFieldType):

	__slots__ = ["_BlckgRef", "_LglPrsn"]
	@property
	def BlckgRef(self):
		return self._BlckgRef

	@BlckgRef.setter
	def BlckgRef(self, value):
		self._BlckgRef = value if type(value) != base_types.auto else self.make_default("BlckgRef")

	@BlckgRef.deleter
	def BlckgRef(self):
		del self._BlckgRef
		self._BlckgRef = None

	@property
	def LglPrsn(self):
		return self._LglPrsn

	@LglPrsn.setter
	def LglPrsn(self, value):
		self._LglPrsn = value if type(value) != base_types.auto else self.make_default("LglPrsn")

	@LglPrsn.deleter
	def LglPrsn(self):
		del self._LglPrsn
		self._LglPrsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BlckgRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglPrsn', type=PartyIdentification335Choice, min=0, max=1, mutex_group=None, array=False),
	))

