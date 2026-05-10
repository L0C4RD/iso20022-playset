from . import base_types
import AttendanceCard3
import PartyIdentification129Choice
import PartyIdentification232Choice

class IndividualPerson42(base_types._BaseFieldType):

	__slots__ = ["_PrssgndPrxy", "_AttndncCardDtls", "_EmplngPty"]
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

	@property
	def AttndncCardDtls(self):
		return self._AttndncCardDtls

	@AttndncCardDtls.setter
	def AttndncCardDtls(self, value):
		self._AttndncCardDtls = value if type(value) != auto else self.make_default("AttndncCardDtls")

	@AttndncCardDtls.deleter
	def AttndncCardDtls(self):
		del self._AttndncCardDtls
		self._AttndncCardDtls = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrssgndPrxy', type=PartyIdentification232Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AttndncCardDtls', type=AttendanceCard3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EmplngPty', type=PartyIdentification129Choice, min=0, max=1, mutex_group=None, array=False),
	))

