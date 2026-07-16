# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import StaticDataReportV02

class ADMI_010_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:admi.010.001.02"
		_docname = "admi.010.001.02"

		__slots__ = ["_StatcDataRpt"]
		@property
		def StatcDataRpt(self):
			return self._StatcDataRpt

		@StatcDataRpt.setter
		def StatcDataRpt(self, value):
			self._StatcDataRpt = value if value is not None else base_types.UninitialisedField(self, 'StatcDataRpt', StaticDataReportV02, False)

		@StatcDataRpt.deleter
		def StatcDataRpt(self):
			del self._StatcDataRpt
			self._StatcDataRpt = base_types.UninitialisedField(self, 'StatcDataRpt', StaticDataReportV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='StatcDataRpt', type=StaticDataReportV02, min=1, max=1, mutex_group=None, array=False),
		))