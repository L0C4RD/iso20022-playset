# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NettingCutOff2
from . import PartyIdentification242Choice

class CutOffData2(base_types._BaseFieldType):

	__slots__ = ["_NetgCutOffDtls", "_PtcptId"]
	@property
	def NetgCutOffDtls(self):
		return self._NetgCutOffDtls

	@NetgCutOffDtls.setter
	def NetgCutOffDtls(self, value):
		self._NetgCutOffDtls = value if value is not None else base_types.UninitialisedField(self, 'NetgCutOffDtls', NettingCutOff2, True)

	@NetgCutOffDtls.deleter
	def NetgCutOffDtls(self):
		del self._NetgCutOffDtls
		self._NetgCutOffDtls = base_types.UninitialisedField(self, 'NetgCutOffDtls', NettingCutOff2, True)

	@property
	def PtcptId(self):
		return self._PtcptId

	@PtcptId.setter
	def PtcptId(self, value):
		self._PtcptId = value if value is not None else base_types.UninitialisedField(self, 'PtcptId', PartyIdentification242Choice, False)

	@PtcptId.deleter
	def PtcptId(self):
		del self._PtcptId
		self._PtcptId = base_types.UninitialisedField(self, 'PtcptId', PartyIdentification242Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NetgCutOffDtls', type=NettingCutOff2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PtcptId', type=PartyIdentification242Choice, min=1, max=1, mutex_group=None, array=False),
	))