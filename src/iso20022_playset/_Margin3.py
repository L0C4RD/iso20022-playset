from . import base_types
from ._Margin4 import Margin4
from ._Amount2 import Amount2
from ._VariationMargin3 import VariationMargin3

class Margin3(base_types._BaseFieldType):

	__slots__ = ["_OthrMrgn", "_InitlMrgn", "_VartnMrgn"]
	@property
	def InitlMrgn(self):
		return self._InitlMrgn

	@InitlMrgn.setter
	def InitlMrgn(self, value):
		self._InitlMrgn = value if type(value) != base_types.auto else self.make_default("InitlMrgn")

	@InitlMrgn.deleter
	def InitlMrgn(self):
		del self._InitlMrgn
		self._InitlMrgn = None

	@property
	def OthrMrgn(self):
		return self._OthrMrgn

	@OthrMrgn.setter
	def OthrMrgn(self, value):
		self._OthrMrgn = value if type(value) != base_types.auto else self.make_default("OthrMrgn")

	@OthrMrgn.deleter
	def OthrMrgn(self):
		del self._OthrMrgn
		self._OthrMrgn = None

	@property
	def VartnMrgn(self):
		return self._VartnMrgn

	@VartnMrgn.setter
	def VartnMrgn(self, value):
		self._VartnMrgn = value if type(value) != base_types.auto else self.make_default("VartnMrgn")

	@VartnMrgn.deleter
	def VartnMrgn(self):
		del self._VartnMrgn
		self._VartnMrgn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InitlMrgn', type=Amount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrMrgn', type=Margin4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='VartnMrgn', type=VariationMargin3, min=0, max=None, mutex_group=None, array=True),
	))

