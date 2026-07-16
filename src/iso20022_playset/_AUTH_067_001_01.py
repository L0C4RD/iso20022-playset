# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CCPCollateralReportV01

class AUTH_067_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01"
		_docname = "auth.067.001.01"

		__slots__ = ["_CCPCollRpt"]
		@property
		def CCPCollRpt(self):
			return self._CCPCollRpt

		@CCPCollRpt.setter
		def CCPCollRpt(self, value):
			self._CCPCollRpt = value if value is not None else base_types.UninitialisedField(self, 'CCPCollRpt', CCPCollateralReportV01, False)

		@CCPCollRpt.deleter
		def CCPCollRpt(self):
			del self._CCPCollRpt
			self._CCPCollRpt = base_types.UninitialisedField(self, 'CCPCollRpt', CCPCollateralReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPCollRpt', type=CCPCollateralReportV01, min=1, max=1, mutex_group=None, array=False),
		))