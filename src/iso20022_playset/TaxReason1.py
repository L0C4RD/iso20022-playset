import base_types
import Max105Text
import Max10Text

class TaxReason1(base_types._BaseFieldType):

	__slots__ = ["_Expltn", "_Cd"]
	@property
	def Expltn(self):
		return self._Expltn

	@Expltn.setter
	def Expltn(self, value):
		self._Expltn = value if type(value) != auto else self.make_default("Expltn")

	@Expltn.deleter
	def Expltn(self):
		del self._Expltn
		self._Expltn = None

	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if type(value) != auto else self.make_default("Cd")

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Expltn', type=Max105Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cd', type=Max10Text, min=1, max=1, mutex_group=None, array=False),
	))

