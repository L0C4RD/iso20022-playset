# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._RegulatoryMetadataReportV01 import RegulatoryMetadataReportV01

class AUTH_114_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01"
		_docname = "auth.114.001.01"

		__slots__ = ["_RgltryMetadataRpt"]
		@property
		def RgltryMetadataRpt(self):
			return self._RgltryMetadataRpt

		@RgltryMetadataRpt.setter
		def RgltryMetadataRpt(self, value):
			self._RgltryMetadataRpt = value if type(value) != base_types.auto else self.make_default("RgltryMetadataRpt")

		@RgltryMetadataRpt.deleter
		def RgltryMetadataRpt(self):
			del self._RgltryMetadataRpt
			self._RgltryMetadataRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RgltryMetadataRpt', type=RegulatoryMetadataReportV01, min=1, max=1, mutex_group=None, array=False),
		))