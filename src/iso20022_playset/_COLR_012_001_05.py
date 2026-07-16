# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralSubstitutionConfirmationV05

class COLR_012_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:colr.012.001.05"
		_docname = "colr.012.001.05"

		__slots__ = ["_CollSbstitnConf"]
		@property
		def CollSbstitnConf(self):
			return self._CollSbstitnConf

		@CollSbstitnConf.setter
		def CollSbstitnConf(self, value):
			self._CollSbstitnConf = value if value is not None else base_types.UninitialisedField(self, 'CollSbstitnConf', CollateralSubstitutionConfirmationV05, False)

		@CollSbstitnConf.deleter
		def CollSbstitnConf(self):
			del self._CollSbstitnConf
			self._CollSbstitnConf = base_types.UninitialisedField(self, 'CollSbstitnConf', CollateralSubstitutionConfirmationV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CollSbstitnConf', type=CollateralSubstitutionConfirmationV05, min=1, max=1, mutex_group=None, array=False),
		))