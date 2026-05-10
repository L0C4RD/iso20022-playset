from . import base_types
from ._IndividualPerson29 import IndividualPerson29
from ._Organisation23 import Organisation23

class RegisteredShareholderName1Choice(base_types._BaseFieldType):

	__slots__ = ["_IndvPrsn", "_Org"]
	@property
	def IndvPrsn(self):
		return self._IndvPrsn

	@IndvPrsn.setter
	def IndvPrsn(self, value):
		self._IndvPrsn = value if type(value) != base_types.auto else self.make_default("IndvPrsn")

	@IndvPrsn.deleter
	def IndvPrsn(self):
		del self._IndvPrsn
		self._IndvPrsn = None

	@property
	def Org(self):
		return self._Org

	@Org.setter
	def Org(self, value):
		self._Org = value if type(value) != base_types.auto else self.make_default("Org")

	@Org.deleter
	def Org(self):
		del self._Org
		self._Org = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IndvPrsn', type=IndividualPerson29, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Org', type=Organisation23, min=0, max=1, mutex_group=1, array=False),
	))

