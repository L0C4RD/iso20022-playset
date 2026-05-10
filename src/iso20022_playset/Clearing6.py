import base_types
import PartyIdentification243Choice
import PartyIdentificationAndAccount219

class Clearing6(base_types._BaseFieldType):

	__slots__ = ["_ClrSgmt", "_ClrMmb"]
	@property
	def ClrSgmt(self):
		return self._ClrSgmt

	@ClrSgmt.setter
	def ClrSgmt(self, value):
		self._ClrSgmt = value if type(value) != auto else self.make_default("ClrSgmt")

	@ClrSgmt.deleter
	def ClrSgmt(self):
		del self._ClrSgmt
		self._ClrSgmt = None

	@property
	def ClrMmb(self):
		return self._ClrMmb

	@ClrMmb.setter
	def ClrMmb(self, value):
		self._ClrMmb = value if type(value) != auto else self.make_default("ClrMmb")

	@ClrMmb.deleter
	def ClrMmb(self):
		del self._ClrMmb
		self._ClrMmb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrSgmt', type=PartyIdentification243Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrMmb', type=PartyIdentificationAndAccount219, min=1, max=None, mutex_group=None, array=True),
	))

