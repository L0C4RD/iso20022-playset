from . import base_types
from ._UnaffirmedReason3Choice import UnaffirmedReason3Choice
from ._Max210Text import Max210Text
from ._AffirmationStatus10Choice import AffirmationStatus10Choice

class StatusAndReason46(base_types._BaseFieldType):

	__slots__ = ["_AddtlRsnInf", "_UaffrmdRsn", "_AffirmSts"]
	@property
	def AddtlRsnInf(self):
		return self._AddtlRsnInf

	@AddtlRsnInf.setter
	def AddtlRsnInf(self, value):
		self._AddtlRsnInf = value if type(value) != base_types.auto else self.make_default("AddtlRsnInf")

	@AddtlRsnInf.deleter
	def AddtlRsnInf(self):
		del self._AddtlRsnInf
		self._AddtlRsnInf = None

	@property
	def AffirmSts(self):
		return self._AffirmSts

	@AffirmSts.setter
	def AffirmSts(self, value):
		self._AffirmSts = value if type(value) != base_types.auto else self.make_default("AffirmSts")

	@AffirmSts.deleter
	def AffirmSts(self):
		del self._AffirmSts
		self._AffirmSts = None

	@property
	def UaffrmdRsn(self):
		return self._UaffrmdRsn

	@UaffrmdRsn.setter
	def UaffrmdRsn(self, value):
		self._UaffrmdRsn = value if type(value) != base_types.auto else self.make_default("UaffrmdRsn")

	@UaffrmdRsn.deleter
	def UaffrmdRsn(self):
		del self._UaffrmdRsn
		self._UaffrmdRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlRsnInf', type=Max210Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AffirmSts', type=AffirmationStatus10Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UaffrmdRsn', type=UnaffirmedReason3Choice, min=0, max=1, mutex_group=None, array=False),
	))

