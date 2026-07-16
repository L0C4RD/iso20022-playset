# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MaintenanceDelegationResponseV08

class CATM_006_001_08():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08"
		_docname = "catm.006.001.08"

		__slots__ = ["_MntncDlgtnRspn"]
		@property
		def MntncDlgtnRspn(self):
			return self._MntncDlgtnRspn

		@MntncDlgtnRspn.setter
		def MntncDlgtnRspn(self, value):
			self._MntncDlgtnRspn = value if value is not None else base_types.UninitialisedField(self, 'MntncDlgtnRspn', MaintenanceDelegationResponseV08, False)

		@MntncDlgtnRspn.deleter
		def MntncDlgtnRspn(self):
			del self._MntncDlgtnRspn
			self._MntncDlgtnRspn = base_types.UninitialisedField(self, 'MntncDlgtnRspn', MaintenanceDelegationResponseV08, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='MntncDlgtnRspn', type=MaintenanceDelegationResponseV08, min=1, max=1, mutex_group=None, array=False),
		))