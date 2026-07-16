# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ClearingPartyAndTime23
from . import NoReasonCode

class ClearingPartyAndTime22Choice(base_types._BaseFieldType):

	__slots__ = ["_Dtls", "_Rsn"]
	@property
	def Dtls(self):
		return self._Dtls

	@Dtls.setter
	def Dtls(self, value):
		self._Dtls = value if value is not None else base_types.UninitialisedField(self, 'Dtls', ClearingPartyAndTime23, False)

	@Dtls.deleter
	def Dtls(self):
		del self._Dtls
		self._Dtls = base_types.UninitialisedField(self, 'Dtls', ClearingPartyAndTime23, False)

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', NoReasonCode, False)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', NoReasonCode, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dtls', type=ClearingPartyAndTime23, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rsn', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
	))