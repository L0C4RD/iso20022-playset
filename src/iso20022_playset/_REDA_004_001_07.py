# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FundReferenceDataReportV07

class REDA_004_001_07():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07"
		_docname = "reda.004.001.07"

		__slots__ = ["_FndRefDataRpt"]
		@property
		def FndRefDataRpt(self):
			return self._FndRefDataRpt

		@FndRefDataRpt.setter
		def FndRefDataRpt(self, value):
			self._FndRefDataRpt = value if value is not None else base_types.UninitialisedField(self, 'FndRefDataRpt', FundReferenceDataReportV07, False)

		@FndRefDataRpt.deleter
		def FndRefDataRpt(self):
			del self._FndRefDataRpt
			self._FndRefDataRpt = base_types.UninitialisedField(self, 'FndRefDataRpt', FundReferenceDataReportV07, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FndRefDataRpt', type=FundReferenceDataReportV07, min=1, max=1, mutex_group=None, array=False),
		))