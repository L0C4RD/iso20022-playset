from . import base_types
import References58Choice

class Linkages49(base_types._BaseFieldType):

	__slots__ = ["_Ref"]
	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if type(value) != auto else self.make_default("Ref")

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ref', type=References58Choice, min=1, max=1, mutex_group=None, array=False),
	))

