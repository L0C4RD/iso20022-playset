# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ReconciliationResponseV04 import ReconciliationResponseV04

class CAAD_006_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RcncltnRspn"]
		@property
		def RcncltnRspn(self):
			return self._RcncltnRspn

		@RcncltnRspn.setter
		def RcncltnRspn(self, value):
			self._RcncltnRspn = value if type(value) != base_types.auto else self.make_default("RcncltnRspn")

		@RcncltnRspn.deleter
		def RcncltnRspn(self):
			del self._RcncltnRspn
			self._RcncltnRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RcncltnRspn', type=ReconciliationResponseV04, min=1, max=1, mutex_group=None, array=False),
		))