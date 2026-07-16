# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IntraPositionMovementQueryResponseV01

class SEMT_029_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:semt.029.001.01"
		_docname = "semt.029.001.01"

		__slots__ = ["_IntraPosMvmntQryRspn"]
		@property
		def IntraPosMvmntQryRspn(self):
			return self._IntraPosMvmntQryRspn

		@IntraPosMvmntQryRspn.setter
		def IntraPosMvmntQryRspn(self, value):
			self._IntraPosMvmntQryRspn = value if value is not None else base_types.UninitialisedField(self, 'IntraPosMvmntQryRspn', IntraPositionMovementQueryResponseV01, False)

		@IntraPosMvmntQryRspn.deleter
		def IntraPosMvmntQryRspn(self):
			del self._IntraPosMvmntQryRspn
			self._IntraPosMvmntQryRspn = base_types.UninitialisedField(self, 'IntraPosMvmntQryRspn', IntraPositionMovementQueryResponseV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraPosMvmntQryRspn', type=IntraPositionMovementQueryResponseV01, min=1, max=1, mutex_group=None, array=False),
		))