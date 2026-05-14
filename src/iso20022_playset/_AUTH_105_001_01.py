# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesFinancingReportingPositionSetReportV01 import SecuritiesFinancingReportingPositionSetReportV01

class AUTH_105_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesFincgRptgPosSetRpt"]
		@property
		def SctiesFincgRptgPosSetRpt(self):
			return self._SctiesFincgRptgPosSetRpt

		@SctiesFincgRptgPosSetRpt.setter
		def SctiesFincgRptgPosSetRpt(self, value):
			self._SctiesFincgRptgPosSetRpt = value if type(value) != base_types.auto else self.make_default("SctiesFincgRptgPosSetRpt")

		@SctiesFincgRptgPosSetRpt.deleter
		def SctiesFincgRptgPosSetRpt(self):
			del self._SctiesFincgRptgPosSetRpt
			self._SctiesFincgRptgPosSetRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgRptgPosSetRpt', type=SecuritiesFinancingReportingPositionSetReportV01, min=1, max=1, mutex_group=None, array=False),
		))