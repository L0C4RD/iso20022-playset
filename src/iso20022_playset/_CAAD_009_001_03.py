# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdministrativeResponseV03

class CAAD_009_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caad.009.001.03"
		_docname = "caad.009.001.03"

		__slots__ = ["_AdmstvRspn"]
		@property
		def AdmstvRspn(self):
			return self._AdmstvRspn

		@AdmstvRspn.setter
		def AdmstvRspn(self, value):
			self._AdmstvRspn = value if value is not None else base_types.UninitialisedField(self, 'AdmstvRspn', AdministrativeResponseV03, False)

		@AdmstvRspn.deleter
		def AdmstvRspn(self):
			del self._AdmstvRspn
			self._AdmstvRspn = base_types.UninitialisedField(self, 'AdmstvRspn', AdministrativeResponseV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AdmstvRspn', type=AdministrativeResponseV03, min=1, max=1, mutex_group=None, array=False),
		))