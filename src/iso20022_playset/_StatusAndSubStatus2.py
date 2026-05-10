from . import base_types
from ._Exact4AlphaNumericText import Exact4AlphaNumericText
from ._Status27Choice import Status27Choice

class StatusAndSubStatus2(base_types._BaseFieldType):

	__slots__ = ["_SubStsCd", "_StsCd"]
	@property
	def SubStsCd(self):
		return self._SubStsCd

	@SubStsCd.setter
	def SubStsCd(self, value):
		self._SubStsCd = value if type(value) != base_types.auto else self.make_default("SubStsCd")

	@SubStsCd.deleter
	def SubStsCd(self):
		del self._SubStsCd
		self._SubStsCd = None

	@property
	def StsCd(self):
		return self._StsCd

	@StsCd.setter
	def StsCd(self, value):
		self._StsCd = value if type(value) != base_types.auto else self.make_default("StsCd")

	@StsCd.deleter
	def StsCd(self):
		del self._StsCd
		self._StsCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SubStsCd', type=Exact4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsCd', type=Status27Choice, min=1, max=1, mutex_group=None, array=False),
	))

