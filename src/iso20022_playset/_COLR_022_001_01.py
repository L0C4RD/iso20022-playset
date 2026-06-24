# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._TripartyCollateralAndExposureReportV01 import TripartyCollateralAndExposureReportV01

class COLR_022_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:colr.022.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_TrptyCollAndXpsrRpt"]
		@property
		def TrptyCollAndXpsrRpt(self):
			return self._TrptyCollAndXpsrRpt

		@TrptyCollAndXpsrRpt.setter
		def TrptyCollAndXpsrRpt(self, value):
			self._TrptyCollAndXpsrRpt = value if type(value) != base_types.auto else self.make_default("TrptyCollAndXpsrRpt")

		@TrptyCollAndXpsrRpt.deleter
		def TrptyCollAndXpsrRpt(self):
			del self._TrptyCollAndXpsrRpt
			self._TrptyCollAndXpsrRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TrptyCollAndXpsrRpt', type=TripartyCollateralAndExposureReportV01, min=1, max=1, mutex_group=None, array=False),
		))