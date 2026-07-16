# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesEndOfProcessReportV02

class SEMT_023_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02"
		_docname = "semt.023.001.02"

		__slots__ = ["_SctiesEndOfPrcRpt"]
		@property
		def SctiesEndOfPrcRpt(self):
			return self._SctiesEndOfPrcRpt

		@SctiesEndOfPrcRpt.setter
		def SctiesEndOfPrcRpt(self, value):
			self._SctiesEndOfPrcRpt = value if value is not None else base_types.UninitialisedField(self, 'SctiesEndOfPrcRpt', SecuritiesEndOfProcessReportV02, False)

		@SctiesEndOfPrcRpt.deleter
		def SctiesEndOfPrcRpt(self):
			del self._SctiesEndOfPrcRpt
			self._SctiesEndOfPrcRpt = base_types.UninitialisedField(self, 'SctiesEndOfPrcRpt', SecuritiesEndOfProcessReportV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesEndOfPrcRpt', type=SecuritiesEndOfProcessReportV02, min=1, max=1, mutex_group=None, array=False),
		))