# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._UndertakingStatusReportV01 import UndertakingStatusReportV01

class TSRV_019_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:tsrv.019.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_UdrtkgStsRpt"]
		@property
		def UdrtkgStsRpt(self):
			return self._UdrtkgStsRpt

		@UdrtkgStsRpt.setter
		def UdrtkgStsRpt(self, value):
			self._UdrtkgStsRpt = value if type(value) != base_types.auto else self.make_default("UdrtkgStsRpt")

		@UdrtkgStsRpt.deleter
		def UdrtkgStsRpt(self):
			del self._UdrtkgStsRpt
			self._UdrtkgStsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='UdrtkgStsRpt', type=UndertakingStatusReportV01, min=1, max=1, mutex_group=None, array=False),
		))