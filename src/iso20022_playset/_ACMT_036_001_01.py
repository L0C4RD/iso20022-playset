# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountSwitchTerminationSwitchV01 import AccountSwitchTerminationSwitchV01

class ACMT_036_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AcctSwtchTermntnSwtch"]
		@property
		def AcctSwtchTermntnSwtch(self):
			return self._AcctSwtchTermntnSwtch

		@AcctSwtchTermntnSwtch.setter
		def AcctSwtchTermntnSwtch(self, value):
			self._AcctSwtchTermntnSwtch = value if type(value) != base_types.auto else self.make_default("AcctSwtchTermntnSwtch")

		@AcctSwtchTermntnSwtch.deleter
		def AcctSwtchTermntnSwtch(self):
			del self._AcctSwtchTermntnSwtch
			self._AcctSwtchTermntnSwtch = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctSwtchTermntnSwtch', type=AccountSwitchTerminationSwitchV01, min=1, max=1, mutex_group=None, array=False),
		))