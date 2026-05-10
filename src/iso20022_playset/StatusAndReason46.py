from . import base_types
import UnaffirmedReason3Choice
import Max210Text
import AffirmationStatus10Choice

class StatusAndReason46(base_types._BaseFieldType):

	__slots__ = ["_AffirmSts", "_UaffrmdRsn", "_AddtlRsnInf"]
	@property
	def AffirmSts(self):
		return self._AffirmSts

	@AffirmSts.setter
	def AffirmSts(self, value):
		self._AffirmSts = value if type(value) != auto else self.make_default("AffirmSts")

	@AffirmSts.deleter
	def AffirmSts(self):
		del self._AffirmSts
		self._AffirmSts = None

	@property
	def UaffrmdRsn(self):
		return self._UaffrmdRsn

	@UaffrmdRsn.setter
	def UaffrmdRsn(self, value):
		self._UaffrmdRsn = value if type(value) != auto else self.make_default("UaffrmdRsn")

	@UaffrmdRsn.deleter
	def UaffrmdRsn(self):
		del self._UaffrmdRsn
		self._UaffrmdRsn = None

	@property
	def AddtlRsnInf(self):
		return self._AddtlRsnInf

	@AddtlRsnInf.setter
	def AddtlRsnInf(self, value):
		self._AddtlRsnInf = value if type(value) != auto else self.make_default("AddtlRsnInf")

	@AddtlRsnInf.deleter
	def AddtlRsnInf(self):
		del self._AddtlRsnInf
		self._AddtlRsnInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AffirmSts', type=AffirmationStatus10Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UaffrmdRsn', type=UnaffirmedReason3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlRsnInf', type=Max210Text, min=0, max=1, mutex_group=None, array=False),
	))

