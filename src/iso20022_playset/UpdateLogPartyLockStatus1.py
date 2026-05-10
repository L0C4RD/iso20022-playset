from . import base_types
import PartyLockStatus1

class UpdateLogPartyLockStatus1(base_types._BaseFieldType):

	__slots__ = ["_New", "_Od"]
	@property
	def New(self):
		return self._New

	@New.setter
	def New(self, value):
		self._New = value if type(value) != auto else self.make_default("New")

	@New.deleter
	def New(self):
		del self._New
		self._New = None

	@property
	def Od(self):
		return self._Od

	@Od.setter
	def Od(self, value):
		self._Od = value if type(value) != auto else self.make_default("Od")

	@Od.deleter
	def Od(self):
		del self._Od
		self._Od = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='New', type=PartyLockStatus1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Od', type=PartyLockStatus1, min=1, max=1, mutex_group=None, array=False),
	))

