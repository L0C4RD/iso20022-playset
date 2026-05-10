from . import base_types
from ._Max5NumericText import Max5NumericText
from ._YesNoIndicator import YesNoIndicator

class Pagination1(base_types._BaseFieldType):

	__slots__ = ["_LastPgInd", "_PgNb"]
	@property
	def LastPgInd(self):
		return self._LastPgInd

	@LastPgInd.setter
	def LastPgInd(self, value):
		self._LastPgInd = value if type(value) != base_types.auto else self.make_default("LastPgInd")

	@LastPgInd.deleter
	def LastPgInd(self):
		del self._LastPgInd
		self._LastPgInd = None

	@property
	def PgNb(self):
		return self._PgNb

	@PgNb.setter
	def PgNb(self, value):
		self._PgNb = value if type(value) != base_types.auto else self.make_default("PgNb")

	@PgNb.deleter
	def PgNb(self):
		del self._PgNb
		self._PgNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LastPgInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PgNb', type=Max5NumericText, min=1, max=1, mutex_group=None, array=False),
	))

