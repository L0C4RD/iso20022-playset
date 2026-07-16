# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IntraBalanceMovementStatusAdviceV02

class CAMT_067_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.067.001.02"
		_docname = "camt.067.001.02"

		__slots__ = ["_IntraBalMvmntStsAdvc"]
		@property
		def IntraBalMvmntStsAdvc(self):
			return self._IntraBalMvmntStsAdvc

		@IntraBalMvmntStsAdvc.setter
		def IntraBalMvmntStsAdvc(self, value):
			self._IntraBalMvmntStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'IntraBalMvmntStsAdvc', IntraBalanceMovementStatusAdviceV02, False)

		@IntraBalMvmntStsAdvc.deleter
		def IntraBalMvmntStsAdvc(self):
			del self._IntraBalMvmntStsAdvc
			self._IntraBalMvmntStsAdvc = base_types.UninitialisedField(self, 'IntraBalMvmntStsAdvc', IntraBalanceMovementStatusAdviceV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntStsAdvc', type=IntraBalanceMovementStatusAdviceV02, min=1, max=1, mutex_group=None, array=False),
		))