# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecurityMaintenanceStatusAdviceV01

class REDA_029_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.029.001.01"
		_docname = "reda.029.001.01"

		__slots__ = ["_SctyMntncStsAdvc"]
		@property
		def SctyMntncStsAdvc(self):
			return self._SctyMntncStsAdvc

		@SctyMntncStsAdvc.setter
		def SctyMntncStsAdvc(self, value):
			self._SctyMntncStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'SctyMntncStsAdvc', SecurityMaintenanceStatusAdviceV01, False)

		@SctyMntncStsAdvc.deleter
		def SctyMntncStsAdvc(self):
			del self._SctyMntncStsAdvc
			self._SctyMntncStsAdvc = base_types.UninitialisedField(self, 'SctyMntncStsAdvc', SecurityMaintenanceStatusAdviceV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctyMntncStsAdvc', type=SecurityMaintenanceStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))