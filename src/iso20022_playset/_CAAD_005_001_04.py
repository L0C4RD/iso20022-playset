# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ReconciliationInitiationV04 import ReconciliationInitiationV04

class CAAD_005_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_RcncltnInitn"]
		@property
		def RcncltnInitn(self):
			return self._RcncltnInitn

		@RcncltnInitn.setter
		def RcncltnInitn(self, value):
			self._RcncltnInitn = value if type(value) != base_types.auto else self.make_default("RcncltnInitn")

		@RcncltnInitn.deleter
		def RcncltnInitn(self):
			del self._RcncltnInitn
			self._RcncltnInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RcncltnInitn', type=ReconciliationInitiationV04, min=1, max=1, mutex_group=None, array=False),
		))