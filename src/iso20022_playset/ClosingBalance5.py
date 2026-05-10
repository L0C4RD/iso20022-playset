import base_types
import ShortLong1Code
import ClosingBalance6Choice

class ClosingBalance5(base_types._BaseFieldType):

	__slots__ = ["_ClsgBal", "_ShrtLngInd"]
	@property
	def ClsgBal(self):
		return self._ClsgBal

	@ClsgBal.setter
	def ClsgBal(self, value):
		self._ClsgBal = value if type(value) != auto else self.make_default("ClsgBal")

	@ClsgBal.deleter
	def ClsgBal(self):
		del self._ClsgBal
		self._ClsgBal = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClsgBal', type=ClosingBalance6Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtLngInd', type=ShortLong1Code, min=1, max=1, mutex_group=None, array=False),
	))

