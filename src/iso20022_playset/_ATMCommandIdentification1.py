from . import base_types
from ._Max140Text import Max140Text
from ._Max35Text import Max35Text

class ATMCommandIdentification1(base_types._BaseFieldType):

	__slots__ = ["_Orgn", "_Prcr", "_Ref"]
	@property
	def Orgn(self):
		return self._Orgn

	@Orgn.setter
	def Orgn(self, value):
		self._Orgn = value if type(value) != base_types.auto else self.make_default("Orgn")

	@Orgn.deleter
	def Orgn(self):
		del self._Orgn
		self._Orgn = None

	@property
	def Prcr(self):
		return self._Prcr

	@Prcr.setter
	def Prcr(self, value):
		self._Prcr = value if type(value) != base_types.auto else self.make_default("Prcr")

	@Prcr.deleter
	def Prcr(self):
		del self._Prcr
		self._Prcr = None

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if type(value) != base_types.auto else self.make_default("Ref")

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Orgn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prcr', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

