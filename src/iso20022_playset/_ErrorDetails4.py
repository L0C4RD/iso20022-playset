from . import base_types
from ._ISO8583MessageErrorCode import ISO8583MessageErrorCode
from ._Max2NumericText import Max2NumericText
from ._Max4000Text import Max4000Text
from ._Max500Text import Max500Text

class ErrorDetails4(base_types._BaseFieldType):

	__slots__ = ["_DataElmtInErr", "_Desc", "_ErrCd", "_svrtyCd"]
	@property
	def DataElmtInErr(self):
		return self._DataElmtInErr

	@DataElmtInErr.setter
	def DataElmtInErr(self, value):
		self._DataElmtInErr = value if type(value) != base_types.auto else self.make_default("DataElmtInErr")

	@DataElmtInErr.deleter
	def DataElmtInErr(self):
		del self._DataElmtInErr
		self._DataElmtInErr = None

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != base_types.auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	@property
	def ErrCd(self):
		return self._ErrCd

	@ErrCd.setter
	def ErrCd(self, value):
		self._ErrCd = value if type(value) != base_types.auto else self.make_default("ErrCd")

	@ErrCd.deleter
	def ErrCd(self):
		del self._ErrCd
		self._ErrCd = None

	@property
	def svrtyCd(self):
		return self._svrtyCd

	@svrtyCd.setter
	def svrtyCd(self, value):
		self._svrtyCd = value if type(value) != base_types.auto else self.make_default("svrtyCd")

	@svrtyCd.deleter
	def svrtyCd(self):
		del self._svrtyCd
		self._svrtyCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DataElmtInErr', type=Max4000Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Desc', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ErrCd', type=ISO8583MessageErrorCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='svrtyCd', type=Max2NumericText, min=0, max=1, mutex_group=None, array=False),
	))

