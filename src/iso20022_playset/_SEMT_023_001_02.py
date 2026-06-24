# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesEndOfProcessReportV02 import SecuritiesEndOfProcessReportV02

class SEMT_023_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:semt.023.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_SctiesEndOfPrcRpt"]
		@property
		def SctiesEndOfPrcRpt(self):
			return self._SctiesEndOfPrcRpt

		@SctiesEndOfPrcRpt.setter
		def SctiesEndOfPrcRpt(self, value):
			self._SctiesEndOfPrcRpt = value if type(value) != base_types.auto else self.make_default("SctiesEndOfPrcRpt")

		@SctiesEndOfPrcRpt.deleter
		def SctiesEndOfPrcRpt(self):
			del self._SctiesEndOfPrcRpt
			self._SctiesEndOfPrcRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesEndOfPrcRpt', type=SecuritiesEndOfProcessReportV02, min=1, max=1, mutex_group=None, array=False),
		))