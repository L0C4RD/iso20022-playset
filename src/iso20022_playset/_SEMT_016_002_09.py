# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IntraPositionMovementPostingReport002V09

class SEMT_016_002_09():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:semt.016.002.09"
		_docname = "semt.016.002.09"

		__slots__ = ["_IntraPosMvmntPstngRpt"]
		@property
		def IntraPosMvmntPstngRpt(self):
			return self._IntraPosMvmntPstngRpt

		@IntraPosMvmntPstngRpt.setter
		def IntraPosMvmntPstngRpt(self, value):
			self._IntraPosMvmntPstngRpt = value if value is not None else base_types.UninitialisedField(self, 'IntraPosMvmntPstngRpt', IntraPositionMovementPostingReport002V09, False)

		@IntraPosMvmntPstngRpt.deleter
		def IntraPosMvmntPstngRpt(self):
			del self._IntraPosMvmntPstngRpt
			self._IntraPosMvmntPstngRpt = base_types.UninitialisedField(self, 'IntraPosMvmntPstngRpt', IntraPositionMovementPostingReport002V09, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraPosMvmntPstngRpt', type=IntraPositionMovementPostingReport002V09, min=1, max=1, mutex_group=None, array=False),
		))