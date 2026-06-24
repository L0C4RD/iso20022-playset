# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CCPBackTestingDefinitionReportV01 import CCPBackTestingDefinitionReportV01

class AUTH_065_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:auth.065.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_CCPBckTstgDefRpt"]
		@property
		def CCPBckTstgDefRpt(self):
			return self._CCPBckTstgDefRpt

		@CCPBckTstgDefRpt.setter
		def CCPBckTstgDefRpt(self, value):
			self._CCPBckTstgDefRpt = value if type(value) != base_types.auto else self.make_default("CCPBckTstgDefRpt")

		@CCPBckTstgDefRpt.deleter
		def CCPBckTstgDefRpt(self):
			del self._CCPBckTstgDefRpt
			self._CCPBckTstgDefRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPBckTstgDefRpt', type=CCPBackTestingDefinitionReportV01, min=1, max=1, mutex_group=None, array=False),
		))