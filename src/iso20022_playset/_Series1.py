from . import base_types
from ._Max35Text import Max35Text
from ._DateFormat42Choice import DateFormat42Choice

class Series1(base_types._BaseFieldType):

	__slots__ = ["_SrsDt", "_SrsNm"]
	@property
	def SrsDt(self):
		return self._SrsDt

	@SrsDt.setter
	def SrsDt(self, value):
		self._SrsDt = value if type(value) != base_types.auto else self.make_default("SrsDt")

	@SrsDt.deleter
	def SrsDt(self):
		del self._SrsDt
		self._SrsDt = None

	@property
	def SrsNm(self):
		return self._SrsNm

	@SrsNm.setter
	def SrsNm(self, value):
		self._SrsNm = value if type(value) != base_types.auto else self.make_default("SrsNm")

	@SrsNm.deleter
	def SrsNm(self):
		del self._SrsNm
		self._SrsNm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SrsDt', type=DateFormat42Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrsNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

