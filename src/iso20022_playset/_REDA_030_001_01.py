# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecurityDeletionStatusAdviceV01

class REDA_030_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.030.001.01"
		_docname = "reda.030.001.01"

		__slots__ = ["_SctyDeltnStsAdvc"]
		@property
		def SctyDeltnStsAdvc(self):
			return self._SctyDeltnStsAdvc

		@SctyDeltnStsAdvc.setter
		def SctyDeltnStsAdvc(self, value):
			self._SctyDeltnStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'SctyDeltnStsAdvc', SecurityDeletionStatusAdviceV01, False)

		@SctyDeltnStsAdvc.deleter
		def SctyDeltnStsAdvc(self):
			del self._SctyDeltnStsAdvc
			self._SctyDeltnStsAdvc = base_types.UninitialisedField(self, 'SctyDeltnStsAdvc', SecurityDeletionStatusAdviceV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctyDeltnStsAdvc', type=SecurityDeletionStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))