# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._IdentificationVerificationReportV04 import IdentificationVerificationReportV04

class ACMT_024_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_IdVrfctnRpt"]
		@property
		def IdVrfctnRpt(self):
			return self._IdVrfctnRpt

		@IdVrfctnRpt.setter
		def IdVrfctnRpt(self, value):
			self._IdVrfctnRpt = value if type(value) != base_types.auto else self.make_default("IdVrfctnRpt")

		@IdVrfctnRpt.deleter
		def IdVrfctnRpt(self):
			del self._IdVrfctnRpt
			self._IdVrfctnRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IdVrfctnRpt', type=IdentificationVerificationReportV04, min=1, max=1, mutex_group=None, array=False),
		))