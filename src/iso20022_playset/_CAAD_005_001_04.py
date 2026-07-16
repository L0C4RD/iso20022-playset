# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ReconciliationInitiationV04

class CAAD_005_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04"
		_docname = "caad.005.001.04"

		__slots__ = ["_RcncltnInitn"]
		@property
		def RcncltnInitn(self):
			return self._RcncltnInitn

		@RcncltnInitn.setter
		def RcncltnInitn(self, value):
			self._RcncltnInitn = value if value is not None else base_types.UninitialisedField(self, 'RcncltnInitn', ReconciliationInitiationV04, False)

		@RcncltnInitn.deleter
		def RcncltnInitn(self):
			del self._RcncltnInitn
			self._RcncltnInitn = base_types.UninitialisedField(self, 'RcncltnInitn', ReconciliationInitiationV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='RcncltnInitn', type=ReconciliationInitiationV04, min=1, max=1, mutex_group=None, array=False),
		))