# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SaleToPOIReconciliationRequestV08 import SaleToPOIReconciliationRequestV08

class CASP_003_001_08():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:casp.003.001.08",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_SaleToPOIRcncltnReq"]
		@property
		def SaleToPOIRcncltnReq(self):
			return self._SaleToPOIRcncltnReq

		@SaleToPOIRcncltnReq.setter
		def SaleToPOIRcncltnReq(self, value):
			self._SaleToPOIRcncltnReq = value if type(value) != base_types.auto else self.make_default("SaleToPOIRcncltnReq")

		@SaleToPOIRcncltnReq.deleter
		def SaleToPOIRcncltnReq(self):
			del self._SaleToPOIRcncltnReq
			self._SaleToPOIRcncltnReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIRcncltnReq', type=SaleToPOIReconciliationRequestV08, min=1, max=1, mutex_group=None, array=False),
		))