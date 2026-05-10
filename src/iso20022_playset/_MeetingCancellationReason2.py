from . import base_types
from ._Max140Text import Max140Text
from ._MeetingCancellationReason1Choice import MeetingCancellationReason1Choice

class MeetingCancellationReason2(base_types._BaseFieldType):

	__slots__ = ["_CxlRsn", "_CxlRsnCd"]
	@property
	def CxlRsn(self):
		return self._CxlRsn

	@CxlRsn.setter
	def CxlRsn(self, value):
		self._CxlRsn = value if type(value) != base_types.auto else self.make_default("CxlRsn")

	@CxlRsn.deleter
	def CxlRsn(self):
		del self._CxlRsn
		self._CxlRsn = None

	@property
	def CxlRsnCd(self):
		return self._CxlRsnCd

	@CxlRsnCd.setter
	def CxlRsnCd(self, value):
		self._CxlRsnCd = value if type(value) != base_types.auto else self.make_default("CxlRsnCd")

	@CxlRsnCd.deleter
	def CxlRsnCd(self):
		del self._CxlRsnCd
		self._CxlRsnCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CxlRsn', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlRsnCd', type=MeetingCancellationReason1Choice, min=0, max=1, mutex_group=None, array=False),
	))

