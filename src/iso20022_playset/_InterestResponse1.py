# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max140Text
from . import Max35Text
from . import RejectionReason21FormatChoice
from . import Status4Code

class InterestResponse1(base_types._BaseFieldType):

	__slots__ = ["_IntrstPmtReqId", "_RjctnRsn", "_RjctnRsnInf", "_RspnTp"]
	@property
	def IntrstPmtReqId(self):
		return self._IntrstPmtReqId

	@IntrstPmtReqId.setter
	def IntrstPmtReqId(self, value):
		self._IntrstPmtReqId = value if value is not None else base_types.UninitialisedField(self, 'IntrstPmtReqId', Max35Text, False)

	@IntrstPmtReqId.deleter
	def IntrstPmtReqId(self):
		del self._IntrstPmtReqId
		self._IntrstPmtReqId = base_types.UninitialisedField(self, 'IntrstPmtReqId', Max35Text, False)

	@property
	def RjctnRsn(self):
		return self._RjctnRsn

	@RjctnRsn.setter
	def RjctnRsn(self, value):
		self._RjctnRsn = value if value is not None else base_types.UninitialisedField(self, 'RjctnRsn', RejectionReason21FormatChoice, False)

	@RjctnRsn.deleter
	def RjctnRsn(self):
		del self._RjctnRsn
		self._RjctnRsn = base_types.UninitialisedField(self, 'RjctnRsn', RejectionReason21FormatChoice, False)

	@property
	def RjctnRsnInf(self):
		return self._RjctnRsnInf

	@RjctnRsnInf.setter
	def RjctnRsnInf(self, value):
		self._RjctnRsnInf = value if value is not None else base_types.UninitialisedField(self, 'RjctnRsnInf', Max140Text, False)

	@RjctnRsnInf.deleter
	def RjctnRsnInf(self):
		del self._RjctnRsnInf
		self._RjctnRsnInf = base_types.UninitialisedField(self, 'RjctnRsnInf', Max140Text, False)

	@property
	def RspnTp(self):
		return self._RspnTp

	@RspnTp.setter
	def RspnTp(self, value):
		self._RspnTp = value if value is not None else base_types.UninitialisedField(self, 'RspnTp', Status4Code, False)

	@RspnTp.deleter
	def RspnTp(self):
		del self._RspnTp
		self._RspnTp = base_types.UninitialisedField(self, 'RspnTp', Status4Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='IntrstPmtReqId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctnRsn', type=RejectionReason21FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctnRsnInf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnTp', type=Status4Code, min=1, max=1, mutex_group=None, array=False),
	))