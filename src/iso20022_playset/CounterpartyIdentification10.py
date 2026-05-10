import base_types
import CollateralRole1Code
import OrganisationIdentification15Choice

class CounterpartyIdentification10(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Sd"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Sd(self):
		return self._Sd

	@Sd.setter
	def Sd(self, value):
		self._Sd = value if type(value) != auto else self.make_default("Sd")

	@Sd.deleter
	def Sd(self):
		del self._Sd
		self._Sd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sd', type=CollateralRole1Code, min=0, max=1, mutex_group=None, array=False),
	))

