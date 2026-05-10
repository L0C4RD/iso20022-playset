import base_types
import SafekeepingPlaceFormat29Choice
import LEIIdentifier

class SafeKeepingPlace3(base_types._BaseFieldType):

	__slots__ = ["_SfkpgPlcFrmt", "_LEI"]
	@property
	def SfkpgPlcFrmt(self):
		return self._SfkpgPlcFrmt

	@SfkpgPlcFrmt.setter
	def SfkpgPlcFrmt(self, value):
		self._SfkpgPlcFrmt = value if type(value) != auto else self.make_default("SfkpgPlcFrmt")

	@SfkpgPlcFrmt.deleter
	def SfkpgPlcFrmt(self):
		del self._SfkpgPlcFrmt
		self._SfkpgPlcFrmt = None

	@property
	def LEI(self):
		return self._LEI

	@LEI.setter
	def LEI(self, value):
		self._LEI = value if type(value) != auto else self.make_default("LEI")

	@LEI.deleter
	def LEI(self):
		del self._LEI
		self._LEI = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SfkpgPlcFrmt', type=SafekeepingPlaceFormat29Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
	))

