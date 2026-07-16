# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptorToAcquirerBatchFileExchangeV02

class CAAA_026_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caaa.026.001.02"
		_docname = "caaa.026.001.02"

		__slots__ = ["_AccptrToAcqrrBtchFileXchg"]
		@property
		def AccptrToAcqrrBtchFileXchg(self):
			return self._AccptrToAcqrrBtchFileXchg

		@AccptrToAcqrrBtchFileXchg.setter
		def AccptrToAcqrrBtchFileXchg(self, value):
			self._AccptrToAcqrrBtchFileXchg = value if value is not None else base_types.UninitialisedField(self, 'AccptrToAcqrrBtchFileXchg', AcceptorToAcquirerBatchFileExchangeV02, False)

		@AccptrToAcqrrBtchFileXchg.deleter
		def AccptrToAcqrrBtchFileXchg(self):
			del self._AccptrToAcqrrBtchFileXchg
			self._AccptrToAcqrrBtchFileXchg = base_types.UninitialisedField(self, 'AccptrToAcqrrBtchFileXchg', AcceptorToAcquirerBatchFileExchangeV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrToAcqrrBtchFileXchg', type=AcceptorToAcquirerBatchFileExchangeV02, min=1, max=1, mutex_group=None, array=False),
		))