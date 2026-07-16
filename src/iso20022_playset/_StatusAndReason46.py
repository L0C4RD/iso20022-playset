# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AffirmationStatus10Choice
from . import Max210Text
from . import UnaffirmedReason3Choice

class StatusAndReason46(base_types._BaseFieldType):

	__slots__ = ["_AddtlRsnInf", "_AffirmSts", "_UaffrmdRsn"]
	@property
	def AddtlRsnInf(self):
		return self._AddtlRsnInf

	@AddtlRsnInf.setter
	def AddtlRsnInf(self, value):
		self._AddtlRsnInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlRsnInf', Max210Text, False)

	@AddtlRsnInf.deleter
	def AddtlRsnInf(self):
		del self._AddtlRsnInf
		self._AddtlRsnInf = base_types.UninitialisedField(self, 'AddtlRsnInf', Max210Text, False)

	@property
	def AffirmSts(self):
		return self._AffirmSts

	@AffirmSts.setter
	def AffirmSts(self, value):
		self._AffirmSts = value if value is not None else base_types.UninitialisedField(self, 'AffirmSts', AffirmationStatus10Choice, False)

	@AffirmSts.deleter
	def AffirmSts(self):
		del self._AffirmSts
		self._AffirmSts = base_types.UninitialisedField(self, 'AffirmSts', AffirmationStatus10Choice, False)

	@property
	def UaffrmdRsn(self):
		return self._UaffrmdRsn

	@UaffrmdRsn.setter
	def UaffrmdRsn(self, value):
		self._UaffrmdRsn = value if value is not None else base_types.UninitialisedField(self, 'UaffrmdRsn', UnaffirmedReason3Choice, False)

	@UaffrmdRsn.deleter
	def UaffrmdRsn(self):
		del self._UaffrmdRsn
		self._UaffrmdRsn = base_types.UninitialisedField(self, 'UaffrmdRsn', UnaffirmedReason3Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlRsnInf', type=Max210Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AffirmSts', type=AffirmationStatus10Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UaffrmdRsn', type=UnaffirmedReason3Choice, min=0, max=1, mutex_group=None, array=False),
	))