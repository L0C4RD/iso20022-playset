# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FeeCollectionInitiationV04

class CAFC_001_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:cafc.001.001.04"
		_docname = "cafc.001.001.04"

		__slots__ = ["_FeeColltnInitn"]
		@property
		def FeeColltnInitn(self):
			return self._FeeColltnInitn

		@FeeColltnInitn.setter
		def FeeColltnInitn(self, value):
			self._FeeColltnInitn = value if value is not None else base_types.UninitialisedField(self, 'FeeColltnInitn', FeeCollectionInitiationV04, False)

		@FeeColltnInitn.deleter
		def FeeColltnInitn(self):
			del self._FeeColltnInitn
			self._FeeColltnInitn = base_types.UninitialisedField(self, 'FeeColltnInitn', FeeCollectionInitiationV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FeeColltnInitn', type=FeeCollectionInitiationV04, min=1, max=1, mutex_group=None, array=False),
		))