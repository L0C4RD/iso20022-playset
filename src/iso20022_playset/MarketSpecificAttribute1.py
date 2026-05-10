from . import base_types
import Max350Text
import Max35Text

class MarketSpecificAttribute1(base_types._BaseFieldType):

	__slots__ = ["_Val", "_Nm"]
	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if type(value) != auto else self.make_default("Val")

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Val', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

