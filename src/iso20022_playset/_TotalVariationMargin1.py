from . import base_types
from .ShortLong1Code import ShortLong1Code
from .Amount2 import Amount2

class TotalVariationMargin1(base_types._BaseFieldType):

	__slots__ = ["_ShrtLngInd", "_AmtDtls"]
	@property
	def ShrtLngInd(self):
		return self._ShrtLngInd

	@ShrtLngInd.setter
	def ShrtLngInd(self, value):
		self._ShrtLngInd = value if type(value) != base_types.auto else self.make_default("ShrtLngInd")

	@ShrtLngInd.deleter
	def ShrtLngInd(self):
		del self._ShrtLngInd
		self._ShrtLngInd = None

	@property
	def AmtDtls(self):
		return self._AmtDtls

	@AmtDtls.setter
	def AmtDtls(self, value):
		self._AmtDtls = value if type(value) != base_types.auto else self.make_default("AmtDtls")

	@AmtDtls.deleter
	def AmtDtls(self):
		del self._AmtDtls
		self._AmtDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ShrtLngInd', type=ShortLong1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtDtls', type=Amount2, min=1, max=1, mutex_group=None, array=False),
	))

