# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import EligibleSecuritiesDeletionRequestV01

class REDA_075_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.075.001.01"
		_docname = "reda.075.001.01"

		__slots__ = ["_ElgblSctiesDeltnReq"]
		@property
		def ElgblSctiesDeltnReq(self):
			return self._ElgblSctiesDeltnReq

		@ElgblSctiesDeltnReq.setter
		def ElgblSctiesDeltnReq(self, value):
			self._ElgblSctiesDeltnReq = value if value is not None else base_types.UninitialisedField(self, 'ElgblSctiesDeltnReq', EligibleSecuritiesDeletionRequestV01, False)

		@ElgblSctiesDeltnReq.deleter
		def ElgblSctiesDeltnReq(self):
			del self._ElgblSctiesDeltnReq
			self._ElgblSctiesDeltnReq = base_types.UninitialisedField(self, 'ElgblSctiesDeltnReq', EligibleSecuritiesDeletionRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ElgblSctiesDeltnReq', type=EligibleSecuritiesDeletionRequestV01, min=1, max=1, mutex_group=None, array=False),
		))