import base_types
import MICIdentifier
import PartyIdentification129Choice
import ContactIdentification1

class MeetingContactPerson3(base_types._BaseFieldType):

	__slots__ = ["_CtctPrsn", "_PlcOfListg", "_EmplngPty"]
	@property
	def CtctPrsn(self):
		return self._CtctPrsn

	@CtctPrsn.setter
	def CtctPrsn(self, value):
		self._CtctPrsn = value if type(value) != auto else self.make_default("CtctPrsn")

	@CtctPrsn.deleter
	def CtctPrsn(self):
		del self._CtctPrsn
		self._CtctPrsn = None

	@property
	def PlcOfListg(self):
		return self._PlcOfListg

	@PlcOfListg.setter
	def PlcOfListg(self, value):
		self._PlcOfListg = value if type(value) != auto else self.make_default("PlcOfListg")

	@PlcOfListg.deleter
	def PlcOfListg(self):
		del self._PlcOfListg
		self._PlcOfListg = None

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
		base_types.FieldEntry(name='CtctPrsn', type=ContactIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfListg', type=MICIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EmplngPty', type=PartyIdentification129Choice, min=0, max=1, mutex_group=None, array=False),
	))

