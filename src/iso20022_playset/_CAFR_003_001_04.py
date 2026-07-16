# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FraudDispositionInitiationV04

class CAFR_003_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:cafr.003.001.04"
		_docname = "cafr.003.001.04"

		__slots__ = ["_FrdDspstnInitn"]
		@property
		def FrdDspstnInitn(self):
			return self._FrdDspstnInitn

		@FrdDspstnInitn.setter
		def FrdDspstnInitn(self, value):
			self._FrdDspstnInitn = value if value is not None else base_types.UninitialisedField(self, 'FrdDspstnInitn', FraudDispositionInitiationV04, False)

		@FrdDspstnInitn.deleter
		def FrdDspstnInitn(self):
			del self._FrdDspstnInitn
			self._FrdDspstnInitn = base_types.UninitialisedField(self, 'FrdDspstnInitn', FraudDispositionInitiationV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FrdDspstnInitn', type=FraudDispositionInitiationV04, min=1, max=1, mutex_group=None, array=False),
		))