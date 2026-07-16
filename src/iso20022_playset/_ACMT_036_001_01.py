# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountSwitchTerminationSwitchV01

class ACMT_036_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:acmt.036.001.01"
		_docname = "acmt.036.001.01"

		__slots__ = ["_AcctSwtchTermntnSwtch"]
		@property
		def AcctSwtchTermntnSwtch(self):
			return self._AcctSwtchTermntnSwtch

		@AcctSwtchTermntnSwtch.setter
		def AcctSwtchTermntnSwtch(self, value):
			self._AcctSwtchTermntnSwtch = value if value is not None else base_types.UninitialisedField(self, 'AcctSwtchTermntnSwtch', AccountSwitchTerminationSwitchV01, False)

		@AcctSwtchTermntnSwtch.deleter
		def AcctSwtchTermntnSwtch(self):
			del self._AcctSwtchTermntnSwtch
			self._AcctSwtchTermntnSwtch = base_types.UninitialisedField(self, 'AcctSwtchTermntnSwtch', AccountSwitchTerminationSwitchV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctSwtchTermntnSwtch', type=AccountSwitchTerminationSwitchV01, min=1, max=1, mutex_group=None, array=False),
		))