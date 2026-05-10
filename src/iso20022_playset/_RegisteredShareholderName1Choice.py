from . import base_types
from .Organisation23 import Organisation23
from .IndividualPerson29 import IndividualPerson29

class RegisteredShareholderName1Choice(base_types._BaseFieldType):

	__slots__ = ["_Org", "_IndvPrsn"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Org', type=Organisation23, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IndvPrsn', type=IndividualPerson29, min=0, max=1, mutex_group=1, array=False),
	))

