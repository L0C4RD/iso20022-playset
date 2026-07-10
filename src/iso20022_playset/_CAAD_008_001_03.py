# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AdministrativeInitiationV03 import AdministrativeInitiationV03

class CAAD_008_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caad.008.001.03"
		_docname = "caad.008.001.03"

		__slots__ = ["_AdmstvInitn"]
		@property
		def AdmstvInitn(self):
			return self._AdmstvInitn

		@AdmstvInitn.setter
		def AdmstvInitn(self, value):
			self._AdmstvInitn = value if type(value) != base_types.auto else self.make_default("AdmstvInitn")

		@AdmstvInitn.deleter
		def AdmstvInitn(self):
			del self._AdmstvInitn
			self._AdmstvInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AdmstvInitn', type=AdministrativeInitiationV03, min=1, max=1, mutex_group=None, array=False),
		))