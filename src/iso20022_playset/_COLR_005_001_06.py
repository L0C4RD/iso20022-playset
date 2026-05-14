# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CollateralManagementCancellationRequestV06 import CollateralManagementCancellationRequestV06

class COLR_005_001_06():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CollMgmtCxlReq"]
		@property
		def CollMgmtCxlReq(self):
			return self._CollMgmtCxlReq

		@CollMgmtCxlReq.setter
		def CollMgmtCxlReq(self, value):
			self._CollMgmtCxlReq = value if type(value) != base_types.auto else self.make_default("CollMgmtCxlReq")

		@CollMgmtCxlReq.deleter
		def CollMgmtCxlReq(self):
			del self._CollMgmtCxlReq
			self._CollMgmtCxlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CollMgmtCxlReq', type=CollateralManagementCancellationRequestV06, min=1, max=1, mutex_group=None, array=False),
		))