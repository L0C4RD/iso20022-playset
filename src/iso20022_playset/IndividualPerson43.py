import base_types
import PartyIdentification129Choice
import PartyIdentification232Choice

class IndividualPerson43(base_types._BaseFieldType):

	__slots__ = ["_EmplngPty", "_PrssgndPrxy"]
	@property
	def EmplngPty(self):
		return self._EmplngPty

	@EmplngPty.setter
	def EmplngPty(self, value):
		self._EmplngPty = value if type(value) != auto else self.make_default("EmplngPty")

	@EmplngPty.deleter
	def EmplngPty(self):
		del self._EmplngPty
		self._EmplngPty = None

	@property
	def PrssgndPrxy(self):
		return self._PrssgndPrxy

	@PrssgndPrxy.setter
	def PrssgndPrxy(self, value):
		self._PrssgndPrxy = value if type(value) != auto else self.make_default("PrssgndPrxy")

	@PrssgndPrxy.deleter
	def PrssgndPrxy(self):
		del self._PrssgndPrxy
		self._PrssgndPrxy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='EmplngPty', type=PartyIdentification129Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrssgndPrxy', type=PartyIdentification232Choice, min=0, max=1, mutex_group=None, array=False),
	))

