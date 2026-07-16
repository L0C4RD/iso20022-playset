# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralManagementCancellationRequestV06

class COLR_005_001_06():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06"
		_docname = "colr.005.001.06"

		__slots__ = ["_CollMgmtCxlReq"]
		@property
		def CollMgmtCxlReq(self):
			return self._CollMgmtCxlReq

		@CollMgmtCxlReq.setter
		def CollMgmtCxlReq(self, value):
			self._CollMgmtCxlReq = value if value is not None else base_types.UninitialisedField(self, 'CollMgmtCxlReq', CollateralManagementCancellationRequestV06, False)

		@CollMgmtCxlReq.deleter
		def CollMgmtCxlReq(self):
			del self._CollMgmtCxlReq
			self._CollMgmtCxlReq = base_types.UninitialisedField(self, 'CollMgmtCxlReq', CollateralManagementCancellationRequestV06, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CollMgmtCxlReq', type=CollateralManagementCancellationRequestV06, min=1, max=1, mutex_group=None, array=False),
		))