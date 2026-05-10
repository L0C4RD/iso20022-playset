from . import base_types
from .Max35Text import Max35Text
from .Max140Text import Max140Text
from .Max350Text import Max350Text

class ElementIdentification3(base_types._BaseFieldType):

	__slots__ = ["_ElmtPth", "_ElmtNm", "_ElmtVal"]
	@property
	def ElmtPth(self):
		return self._ElmtPth

	@ElmtPth.setter
	def ElmtPth(self, value):
		self._ElmtPth = value if type(value) != base_types.auto else self.make_default("ElmtPth")

	@ElmtPth.deleter
	def ElmtPth(self):
		del self._ElmtPth
		self._ElmtPth = None

	@property
	def ElmtNm(self):
		return self._ElmtNm

	@ElmtNm.setter
	def ElmtNm(self, value):
		self._ElmtNm = value if type(value) != base_types.auto else self.make_default("ElmtNm")

	@ElmtNm.deleter
	def ElmtNm(self):
		del self._ElmtNm
		self._ElmtNm = None

	@property
	def ElmtVal(self):
		return self._ElmtVal

	@ElmtVal.setter
	def ElmtVal(self, value):
		self._ElmtVal = value if type(value) != base_types.auto else self.make_default("ElmtVal")

	@ElmtVal.deleter
	def ElmtVal(self):
		del self._ElmtVal
		self._ElmtVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ElmtPth', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElmtNm', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElmtVal', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))

