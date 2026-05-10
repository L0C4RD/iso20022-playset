import base_types
import Priority1Code
import YesNoIndicator

class InformationQualifierType1(base_types._BaseFieldType):

	__slots__ = ["_IsFrmtd", "_Prty"]
	@property
	def IsFrmtd(self):
		return self._IsFrmtd

	@IsFrmtd.setter
	def IsFrmtd(self, value):
		self._IsFrmtd = value if type(value) != auto else self.make_default("IsFrmtd")

	@IsFrmtd.deleter
	def IsFrmtd(self):
		del self._IsFrmtd
		self._IsFrmtd = None

	@property
	def Prty(self):
		return self._Prty

	@Prty.setter
	def Prty(self, value):
		self._Prty = value if type(value) != auto else self.make_default("Prty")

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IsFrmtd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prty', type=Priority1Code, min=0, max=1, mutex_group=None, array=False),
	))

