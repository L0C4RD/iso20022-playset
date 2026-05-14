# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._MaintenanceDelegationRequestV12 import MaintenanceDelegationRequestV12

class CATM_005_001_12():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MntncDlgtnReq"]
		@property
		def MntncDlgtnReq(self):
			return self._MntncDlgtnReq

		@MntncDlgtnReq.setter
		def MntncDlgtnReq(self, value):
			self._MntncDlgtnReq = value if type(value) != base_types.auto else self.make_default("MntncDlgtnReq")

		@MntncDlgtnReq.deleter
		def MntncDlgtnReq(self):
			del self._MntncDlgtnReq
			self._MntncDlgtnReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MntncDlgtnReq', type=MaintenanceDelegationRequestV12, min=1, max=1, mutex_group=None, array=False),
		))