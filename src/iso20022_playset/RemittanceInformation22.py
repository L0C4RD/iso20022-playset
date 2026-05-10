from . import base_types
import Max140Text
import StructuredRemittanceInformation18

class RemittanceInformation22(base_types._BaseFieldType):

	__slots__ = ["_Strd", "_Ustrd"]
	@property
	def Strd(self):
		return self._Strd

	@Strd.setter
	def Strd(self, value):
		self._Strd = value if type(value) != auto else self.make_default("Strd")

	@Strd.deleter
	def Strd(self):
		del self._Strd
		self._Strd = None

	@property
	def Ustrd(self):
		return self._Ustrd

	@Ustrd.setter
	def Ustrd(self, value):
		self._Ustrd = value if type(value) != auto else self.make_default("Ustrd")

	@Ustrd.deleter
	def Ustrd(self):
		del self._Ustrd
		self._Ustrd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Strd', type=StructuredRemittanceInformation18, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ustrd', type=Max140Text, min=0, max=None, mutex_group=None, array=True),
	))

