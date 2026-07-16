# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdministrativeInitiationV03

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
			self._AdmstvInitn = value if value is not None else base_types.UninitialisedField(self, 'AdmstvInitn', AdministrativeInitiationV03, False)

		@AdmstvInitn.deleter
		def AdmstvInitn(self):
			del self._AdmstvInitn
			self._AdmstvInitn = base_types.UninitialisedField(self, 'AdmstvInitn', AdministrativeInitiationV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AdmstvInitn', type=AdministrativeInitiationV03, min=1, max=1, mutex_group=None, array=False),
		))