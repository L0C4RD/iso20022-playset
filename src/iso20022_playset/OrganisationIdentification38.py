import base_types
import Max105Text
import GenericIdentification175
import Max500Text

class OrganisationIdentification38(base_types._BaseFieldType):

	__slots__ = ["_Nm", "_Id", "_Dmcl"]
	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

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
	def Dmcl(self):
		return self._Dmcl

	@Dmcl.setter
	def Dmcl(self, value):
		self._Dmcl = value if type(value) != auto else self.make_default("Dmcl")

	@Dmcl.deleter
	def Dmcl(self):
		del self._Dmcl
		self._Dmcl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Nm', type=Max105Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=GenericIdentification175, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dmcl', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
	))

