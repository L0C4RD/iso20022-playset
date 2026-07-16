# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralDataStatusAdviceV01

class REDA_028_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01"
		_docname = "reda.028.001.01"

		__slots__ = ["_CollDataStsAdvc"]
		@property
		def CollDataStsAdvc(self):
			return self._CollDataStsAdvc

		@CollDataStsAdvc.setter
		def CollDataStsAdvc(self, value):
			self._CollDataStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'CollDataStsAdvc', CollateralDataStatusAdviceV01, False)

		@CollDataStsAdvc.deleter
		def CollDataStsAdvc(self):
			del self._CollDataStsAdvc
			self._CollDataStsAdvc = base_types.UninitialisedField(self, 'CollDataStsAdvc', CollateralDataStatusAdviceV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CollDataStsAdvc', type=CollateralDataStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))