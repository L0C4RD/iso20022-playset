# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CCPAvailableFinancialResourcesReportV02 import CCPAvailableFinancialResourcesReportV02

class AUTH_064_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CCPAvlblFinRsrcsRpt"]
		@property
		def CCPAvlblFinRsrcsRpt(self):
			return self._CCPAvlblFinRsrcsRpt

		@CCPAvlblFinRsrcsRpt.setter
		def CCPAvlblFinRsrcsRpt(self, value):
			self._CCPAvlblFinRsrcsRpt = value if type(value) != base_types.auto else self.make_default("CCPAvlblFinRsrcsRpt")

		@CCPAvlblFinRsrcsRpt.deleter
		def CCPAvlblFinRsrcsRpt(self):
			del self._CCPAvlblFinRsrcsRpt
			self._CCPAvlblFinRsrcsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPAvlblFinRsrcsRpt', type=CCPAvailableFinancialResourcesReportV02, min=1, max=1, mutex_group=None, array=False),
		))