import base_types
import Max140Text

class KEKIdentifier4(base_types._BaseFieldType):

	__slots__ = ["_KeyId", "_Nm", "_KeyVrsn"]
	@property
	def KeyId(self):
		return self._KeyId

	@KeyId.setter
	def KeyId(self, value):
		self._KeyId = value if type(value) != auto else self.make_default("KeyId")

	@KeyId.deleter
	def KeyId(self):
		del self._KeyId
		self._KeyId = None

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
	def KeyVrsn(self):
		return self._KeyVrsn

	@KeyVrsn.setter
	def KeyVrsn(self, value):
		self._KeyVrsn = value if type(value) != auto else self.make_default("KeyVrsn")

	@KeyVrsn.deleter
	def KeyVrsn(self):
		del self._KeyVrsn
		self._KeyVrsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='KeyId', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyVrsn', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))

