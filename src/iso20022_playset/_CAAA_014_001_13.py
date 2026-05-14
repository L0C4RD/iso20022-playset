# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AcceptorDiagnosticResponseV13 import AcceptorDiagnosticResponseV13

class CAAA_014_001_13():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AccptrDgnstcRspn"]
		@property
		def AccptrDgnstcRspn(self):
			return self._AccptrDgnstcRspn

		@AccptrDgnstcRspn.setter
		def AccptrDgnstcRspn(self, value):
			self._AccptrDgnstcRspn = value if type(value) != base_types.auto else self.make_default("AccptrDgnstcRspn")

		@AccptrDgnstcRspn.deleter
		def AccptrDgnstcRspn(self):
			del self._AccptrDgnstcRspn
			self._AccptrDgnstcRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrDgnstcRspn', type=AcceptorDiagnosticResponseV13, min=1, max=1, mutex_group=None, array=False),
		))