# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IntraBalanceMovementConfirmationV02

class CAMT_068_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.068.001.02"
		_docname = "camt.068.001.02"

		__slots__ = ["_IntraBalMvmntConf"]
		@property
		def IntraBalMvmntConf(self):
			return self._IntraBalMvmntConf

		@IntraBalMvmntConf.setter
		def IntraBalMvmntConf(self, value):
			self._IntraBalMvmntConf = value if value is not None else base_types.UninitialisedField(self, 'IntraBalMvmntConf', IntraBalanceMovementConfirmationV02, False)

		@IntraBalMvmntConf.deleter
		def IntraBalMvmntConf(self):
			del self._IntraBalMvmntConf
			self._IntraBalMvmntConf = base_types.UninitialisedField(self, 'IntraBalMvmntConf', IntraBalanceMovementConfirmationV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntConf', type=IntraBalanceMovementConfirmationV02, min=1, max=1, mutex_group=None, array=False),
		))