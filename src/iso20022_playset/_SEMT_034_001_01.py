# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._IntraPositionMovementPendingReportV01 import IntraPositionMovementPendingReportV01

class SEMT_034_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:semt.034.001.01"
		_docname = "semt.034.001.01"

		__slots__ = ["_IntraPosMvmntPdgRpt"]
		@property
		def IntraPosMvmntPdgRpt(self):
			return self._IntraPosMvmntPdgRpt

		@IntraPosMvmntPdgRpt.setter
		def IntraPosMvmntPdgRpt(self, value):
			self._IntraPosMvmntPdgRpt = value if type(value) != base_types.auto else self.make_default("IntraPosMvmntPdgRpt")

		@IntraPosMvmntPdgRpt.deleter
		def IntraPosMvmntPdgRpt(self):
			del self._IntraPosMvmntPdgRpt
			self._IntraPosMvmntPdgRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraPosMvmntPdgRpt', type=IntraPositionMovementPendingReportV01, min=1, max=1, mutex_group=None, array=False),
		))