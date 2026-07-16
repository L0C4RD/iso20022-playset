# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MaintenanceDelegationRequestV11

class CATM_005_001_11():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11"
		_docname = "catm.005.001.11"

		__slots__ = ["_MntncDlgtnReq"]
		@property
		def MntncDlgtnReq(self):
			return self._MntncDlgtnReq

		@MntncDlgtnReq.setter
		def MntncDlgtnReq(self, value):
			self._MntncDlgtnReq = value if value is not None else base_types.UninitialisedField(self, 'MntncDlgtnReq', MaintenanceDelegationRequestV11, False)

		@MntncDlgtnReq.deleter
		def MntncDlgtnReq(self):
			del self._MntncDlgtnReq
			self._MntncDlgtnReq = base_types.UninitialisedField(self, 'MntncDlgtnReq', MaintenanceDelegationRequestV11, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='MntncDlgtnReq', type=MaintenanceDelegationRequestV11, min=1, max=1, mutex_group=None, array=False),
		))