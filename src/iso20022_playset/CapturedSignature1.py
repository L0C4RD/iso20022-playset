from . import base_types
from .Max35Text import Max35Text
from .Max140Text import Max140Text
from .Max2MBBinary import Max2MBBinary
from .Max500Text import Max500Text

class CapturedSignature1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_ImgData", "_ImgFrmt", "_ImgRef"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def ImgData(self):
		return self._ImgData

	@ImgData.setter
	def ImgData(self, value):
		self._ImgData = value if type(value) != auto else self.make_default("ImgData")

	@ImgData.deleter
	def ImgData(self):
		del self._ImgData
		self._ImgData = None

	@property
	def ImgFrmt(self):
		return self._ImgFrmt

	@ImgFrmt.setter
	def ImgFrmt(self, value):
		self._ImgFrmt = value if type(value) != auto else self.make_default("ImgFrmt")

	@ImgFrmt.deleter
	def ImgFrmt(self):
		del self._ImgFrmt
		self._ImgFrmt = None

	@property
	def ImgRef(self):
		return self._ImgRef

	@ImgRef.setter
	def ImgRef(self, value):
		self._ImgRef = value if type(value) != auto else self.make_default("ImgRef")

	@ImgRef.deleter
	def ImgRef(self):
		del self._ImgRef
		self._ImgRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ImgData', type=Max2MBBinary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ImgFrmt', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ImgRef', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
	))

