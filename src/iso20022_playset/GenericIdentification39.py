import base_types
import RestrictedFINMax30Text
import RestrictedFINMax8Text

class GenericIdentification39(base_types._BaseFieldType):

	__slots__ = ["_Issr", "_Id"]
	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if type(value) != auto else self.make_default("Issr")

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Issr', type=RestrictedFINMax8Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=RestrictedFINMax30Text, min=1, max=1, mutex_group=None, array=False),
	))

