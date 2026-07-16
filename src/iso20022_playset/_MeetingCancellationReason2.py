# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max140Text
from . import MeetingCancellationReason1Choice

class MeetingCancellationReason2(base_types._BaseFieldType):

	__slots__ = ["_CxlRsn", "_CxlRsnCd"]
	@property
	def CxlRsn(self):
		return self._CxlRsn

	@CxlRsn.setter
	def CxlRsn(self, value):
		self._CxlRsn = value if value is not None else base_types.UninitialisedField(self, 'CxlRsn', Max140Text, False)

	@CxlRsn.deleter
	def CxlRsn(self):
		del self._CxlRsn
		self._CxlRsn = base_types.UninitialisedField(self, 'CxlRsn', Max140Text, False)

	@property
	def CxlRsnCd(self):
		return self._CxlRsnCd

	@CxlRsnCd.setter
	def CxlRsnCd(self, value):
		self._CxlRsnCd = value if value is not None else base_types.UninitialisedField(self, 'CxlRsnCd', MeetingCancellationReason1Choice, False)

	@CxlRsnCd.deleter
	def CxlRsnCd(self):
		del self._CxlRsnCd
		self._CxlRsnCd = base_types.UninitialisedField(self, 'CxlRsnCd', MeetingCancellationReason1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CxlRsn', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlRsnCd', type=MeetingCancellationReason1Choice, min=0, max=1, mutex_group=None, array=False),
	))