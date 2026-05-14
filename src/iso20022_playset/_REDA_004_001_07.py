# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FundReferenceDataReportV07 import FundReferenceDataReportV07

class REDA_004_001_07():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FndRefDataRpt"]
		@property
		def FndRefDataRpt(self):
			return self._FndRefDataRpt

		@FndRefDataRpt.setter
		def FndRefDataRpt(self, value):
			self._FndRefDataRpt = value if type(value) != base_types.auto else self.make_default("FndRefDataRpt")

		@FndRefDataRpt.deleter
		def FndRefDataRpt(self):
			del self._FndRefDataRpt
			self._FndRefDataRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FndRefDataRpt', type=FundReferenceDataReportV07, min=1, max=1, mutex_group=None, array=False),
		))