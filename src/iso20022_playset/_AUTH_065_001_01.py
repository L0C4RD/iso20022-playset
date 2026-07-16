# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CCPBackTestingDefinitionReportV01

class AUTH_065_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.065.001.01"
		_docname = "auth.065.001.01"

		__slots__ = ["_CCPBckTstgDefRpt"]
		@property
		def CCPBckTstgDefRpt(self):
			return self._CCPBckTstgDefRpt

		@CCPBckTstgDefRpt.setter
		def CCPBckTstgDefRpt(self, value):
			self._CCPBckTstgDefRpt = value if value is not None else base_types.UninitialisedField(self, 'CCPBckTstgDefRpt', CCPBackTestingDefinitionReportV01, False)

		@CCPBckTstgDefRpt.deleter
		def CCPBckTstgDefRpt(self):
			del self._CCPBckTstgDefRpt
			self._CCPBckTstgDefRpt = base_types.UninitialisedField(self, 'CCPBckTstgDefRpt', CCPBackTestingDefinitionReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPBckTstgDefRpt', type=CCPBackTestingDefinitionReportV01, min=1, max=1, mutex_group=None, array=False),
		))