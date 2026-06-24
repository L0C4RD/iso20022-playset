# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DeltaReportV03 import DeltaReportV03

class TSMT_015_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_DltaRpt"]
		@property
		def DltaRpt(self):
			return self._DltaRpt

		@DltaRpt.setter
		def DltaRpt(self, value):
			self._DltaRpt = value if type(value) != base_types.auto else self.make_default("DltaRpt")

		@DltaRpt.deleter
		def DltaRpt(self):
			del self._DltaRpt
			self._DltaRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='DltaRpt', type=DeltaReportV03, min=1, max=1, mutex_group=None, array=False),
		))