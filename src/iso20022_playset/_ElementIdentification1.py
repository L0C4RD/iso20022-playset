from . import base_types
from ._Max3NumericText import Max3NumericText
from ._Max350Text import Max350Text
from ._Max140Text import Max140Text
from ._Max35Text import Max35Text

class ElementIdentification1(base_types._BaseFieldType):

	__slots__ = ["_DocIndx", "_ElmtNm", "_ElmtVal", "_ElmtPth"]
	@property
	def DocIndx(self):
		return self._DocIndx

	@DocIndx.setter
	def DocIndx(self, value):
		self._DocIndx = value if type(value) != base_types.auto else self.make_default("DocIndx")

	@DocIndx.deleter
	def DocIndx(self):
		del self._DocIndx
		self._DocIndx = None

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
		base_types.FieldEntry(name='DocIndx', type=Max3NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElmtNm', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElmtPth', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElmtVal', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))

