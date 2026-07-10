# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CollateralAndExposureReportV05 import CollateralAndExposureReportV05

class COLR_016_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05"
		_docname = "colr.016.001.05"

		__slots__ = ["_CollAndXpsrRpt"]
		@property
		def CollAndXpsrRpt(self):
			return self._CollAndXpsrRpt

		@CollAndXpsrRpt.setter
		def CollAndXpsrRpt(self, value):
			self._CollAndXpsrRpt = value if type(value) != base_types.auto else self.make_default("CollAndXpsrRpt")

		@CollAndXpsrRpt.deleter
		def CollAndXpsrRpt(self):
			del self._CollAndXpsrRpt
			self._CollAndXpsrRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CollAndXpsrRpt', type=CollateralAndExposureReportV05, min=1, max=1, mutex_group=None, array=False),
		))