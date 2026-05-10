import base_types
import ClosingBalance3Choice
import OpeningBalance3Choice

class PaginationBalance2(base_types._BaseFieldType):

	__slots__ = ["_ClsgBal", "_OpngBal"]
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
		base_types.FieldEntry(name='ClsgBal', type=ClosingBalance3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngBal', type=OpeningBalance3Choice, min=0, max=1, mutex_group=None, array=False),
	))

