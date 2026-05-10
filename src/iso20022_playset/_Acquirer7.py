from . import base_types
from ._Max35Text import Max35Text

class Acquirer7(base_types._BaseFieldType):

	__slots__ = ["_AcqrgInstn", "_Brnch"]
	@property
	def AcqrgInstn(self):
		return self._AcqrgInstn

	@AcqrgInstn.setter
	def AcqrgInstn(self, value):
		self._AcqrgInstn = value if type(value) != base_types.auto else self.make_default("AcqrgInstn")

	@AcqrgInstn.deleter
	def AcqrgInstn(self):
		del self._AcqrgInstn
		self._AcqrgInstn = None

	@property
	def Brnch(self):
		return self._Brnch

	@Brnch.setter
	def Brnch(self, value):
		self._Brnch = value if type(value) != base_types.auto else self.make_default("Brnch")

	@Brnch.deleter
	def Brnch(self):
		del self._Brnch
		self._Brnch = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcqrgInstn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Brnch', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

