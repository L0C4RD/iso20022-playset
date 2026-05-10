from . import base_types
from ._OpeningBalance6Choice import OpeningBalance6Choice
from ._ShortLong1Code import ShortLong1Code

class OpeningBalance5(base_types._BaseFieldType):

	__slots__ = ["_OpngBal", "_ShrtLngInd"]
	@property
	def OpngBal(self):
		return self._OpngBal

	@OpngBal.setter
	def OpngBal(self, value):
		self._OpngBal = value if type(value) != base_types.auto else self.make_default("OpngBal")

	@OpngBal.deleter
	def OpngBal(self):
		del self._OpngBal
		self._OpngBal = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='OpngBal', type=OpeningBalance6Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtLngInd', type=ShortLong1Code, min=1, max=1, mutex_group=None, array=False),
	))

