# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CCPAccountPositionReportV01 import CCPAccountPositionReportV01

class AUTH_068_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CCPAcctPosRpt"]
		@property
		def CCPAcctPosRpt(self):
			return self._CCPAcctPosRpt

		@CCPAcctPosRpt.setter
		def CCPAcctPosRpt(self, value):
			self._CCPAcctPosRpt = value if type(value) != base_types.auto else self.make_default("CCPAcctPosRpt")

		@CCPAcctPosRpt.deleter
		def CCPAcctPosRpt(self):
			del self._CCPAcctPosRpt
			self._CCPAcctPosRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPAcctPosRpt', type=CCPAccountPositionReportV01, min=1, max=1, mutex_group=None, array=False),
		))