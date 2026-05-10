import base_types
import ExtendedParty13
import ContactAttributes5

class FundParties1(base_types._BaseFieldType):

	__slots__ = ["_Trstee", "_Guarntr", "_OthrPty", "_Audtr"]
	@property
	def Trstee(self):
		return self._Trstee

	@Trstee.setter
	def Trstee(self, value):
		self._Trstee = value if type(value) != auto else self.make_default("Trstee")

	@Trstee.deleter
	def Trstee(self):
		del self._Trstee
		self._Trstee = None

	@property
	def Guarntr(self):
		return self._Guarntr

	@Guarntr.setter
	def Guarntr(self, value):
		self._Guarntr = value if type(value) != auto else self.make_default("Guarntr")

	@Guarntr.deleter
	def Guarntr(self):
		del self._Guarntr
		self._Guarntr = None

	@property
	def OthrPty(self):
		return self._OthrPty

	@OthrPty.setter
	def OthrPty(self, value):
		self._OthrPty = value if type(value) != auto else self.make_default("OthrPty")

	@OthrPty.deleter
	def OthrPty(self):
		del self._OthrPty
		self._OthrPty = None

	@property
	def Audtr(self):
		return self._Audtr

	@Audtr.setter
	def Audtr(self, value):
		self._Audtr = value if type(value) != auto else self.make_default("Audtr")

	@Audtr.deleter
	def Audtr(self):
		del self._Audtr
		self._Audtr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Trstee', type=ContactAttributes5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Guarntr', type=ContactAttributes5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPty', type=ExtendedParty13, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Audtr', type=ContactAttributes5, min=0, max=1, mutex_group=None, array=False),
	))

