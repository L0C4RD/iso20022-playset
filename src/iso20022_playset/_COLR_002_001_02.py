# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralValueReportV02

class COLR_002_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:colr.002.001.02"
		_docname = "colr.002.001.02"

		__slots__ = ["_CollValRpt"]
		@property
		def CollValRpt(self):
			return self._CollValRpt

		@CollValRpt.setter
		def CollValRpt(self, value):
			self._CollValRpt = value if value is not None else base_types.UninitialisedField(self, 'CollValRpt', CollateralValueReportV02, False)

		@CollValRpt.deleter
		def CollValRpt(self):
			del self._CollValRpt
			self._CollValRpt = base_types.UninitialisedField(self, 'CollValRpt', CollateralValueReportV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CollValRpt', type=CollateralValueReportV02, min=1, max=1, mutex_group=None, array=False),
		))