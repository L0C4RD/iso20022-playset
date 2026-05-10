import base_types
import ShortLong1Code
import OpeningBalance7Choice

class OpeningBalance6(base_types._BaseFieldType):

	__slots__ = ["_ShrtLngInd", "_OpngBal"]
	@property
	def ShrtLngInd(self):
		return self._ShrtLngInd

	@ShrtLngInd.setter
	def ShrtLngInd(self, value):
		self._ShrtLngInd = value if type(value) != auto else self.make_default("ShrtLngInd")

	@ShrtLngInd.deleter
	def ShrtLngInd(self):
		del self._ShrtLngInd
		self._ShrtLngInd = None

	@property
	def OpngBal(self):
		return self._OpngBal

	@OpngBal.setter
	def OpngBal(self, value):
		self._OpngBal = value if type(value) != auto else self.make_default("OpngBal")

	@OpngBal.deleter
	def OpngBal(self):
		del self._OpngBal
		self._OpngBal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ShrtLngInd', type=ShortLong1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngBal', type=OpeningBalance7Choice, min=1, max=1, mutex_group=None, array=False),
	))

