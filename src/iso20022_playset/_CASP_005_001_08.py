# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SaleToPOISessionManagementRequestV08 import SaleToPOISessionManagementRequestV08

class CASP_005_001_08():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:casp.005.001.08"
		_docname = "casp.005.001.08"

		__slots__ = ["_SaleToPOISsnMgmtReq"]
		@property
		def SaleToPOISsnMgmtReq(self):
			return self._SaleToPOISsnMgmtReq

		@SaleToPOISsnMgmtReq.setter
		def SaleToPOISsnMgmtReq(self, value):
			self._SaleToPOISsnMgmtReq = value if type(value) != base_types.auto else self.make_default("SaleToPOISsnMgmtReq")

		@SaleToPOISsnMgmtReq.deleter
		def SaleToPOISsnMgmtReq(self):
			del self._SaleToPOISsnMgmtReq
			self._SaleToPOISsnMgmtReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOISsnMgmtReq', type=SaleToPOISessionManagementRequestV08, min=1, max=1, mutex_group=None, array=False),
		))