import base_types
import CountryCode
import Max70Text

class NameAndLocation1(base_types._BaseFieldType):

	__slots__ = ["_Nm", "_Lctn"]
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
	def Lctn(self):
		return self._Lctn

	@Lctn.setter
	def Lctn(self, value):
		self._Lctn = value if type(value) != auto else self.make_default("Lctn")

	@Lctn.deleter
	def Lctn(self):
		del self._Lctn
		self._Lctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Nm', type=Max70Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lctn', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
	))

