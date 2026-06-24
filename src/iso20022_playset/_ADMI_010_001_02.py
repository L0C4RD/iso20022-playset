# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._StaticDataReportV02 import StaticDataReportV02

class ADMI_010_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:admi.010.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_StatcDataRpt"]
		@property
		def StatcDataRpt(self):
			return self._StatcDataRpt

		@StatcDataRpt.setter
		def StatcDataRpt(self, value):
			self._StatcDataRpt = value if type(value) != base_types.auto else self.make_default("StatcDataRpt")

		@StatcDataRpt.deleter
		def StatcDataRpt(self):
			del self._StatcDataRpt
			self._StatcDataRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='StatcDataRpt', type=StaticDataReportV02, min=1, max=1, mutex_group=None, array=False),
		))