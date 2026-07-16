# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import UndertakingStatusReportV01

class TSRV_019_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsrv.019.001.01"
		_docname = "tsrv.019.001.01"

		__slots__ = ["_UdrtkgStsRpt"]
		@property
		def UdrtkgStsRpt(self):
			return self._UdrtkgStsRpt

		@UdrtkgStsRpt.setter
		def UdrtkgStsRpt(self, value):
			self._UdrtkgStsRpt = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgStsRpt', UndertakingStatusReportV01, False)

		@UdrtkgStsRpt.deleter
		def UdrtkgStsRpt(self):
			del self._UdrtkgStsRpt
			self._UdrtkgStsRpt = base_types.UninitialisedField(self, 'UdrtkgStsRpt', UndertakingStatusReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='UdrtkgStsRpt', type=UndertakingStatusReportV01, min=1, max=1, mutex_group=None, array=False),
		))