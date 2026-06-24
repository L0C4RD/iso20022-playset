# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._MarginReportV02 import MarginReportV02

class SECL_005_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:secl.005.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_MrgnRpt"]
		@property
		def MrgnRpt(self):
			return self._MrgnRpt

		@MrgnRpt.setter
		def MrgnRpt(self, value):
			self._MrgnRpt = value if type(value) != base_types.auto else self.make_default("MrgnRpt")

		@MrgnRpt.deleter
		def MrgnRpt(self):
			del self._MrgnRpt
			self._MrgnRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MrgnRpt', type=MarginReportV02, min=1, max=1, mutex_group=None, array=False),
		))