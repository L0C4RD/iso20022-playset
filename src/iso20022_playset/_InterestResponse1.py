from . import base_types
from ._Max35Text import Max35Text
from ._RejectionReason21FormatChoice import RejectionReason21FormatChoice
from ._Status4Code import Status4Code
from ._Max140Text import Max140Text

class InterestResponse1(base_types._BaseFieldType):

	__slots__ = ["_IntrstPmtReqId", "_RjctnRsn", "_RjctnRsnInf", "_RspnTp"]
	@property
	def IntrstPmtReqId(self):
		return self._IntrstPmtReqId

	@IntrstPmtReqId.setter
	def IntrstPmtReqId(self, value):
		self._IntrstPmtReqId = value if type(value) != base_types.auto else self.make_default("IntrstPmtReqId")

	@IntrstPmtReqId.deleter
	def IntrstPmtReqId(self):
		del self._IntrstPmtReqId
		self._IntrstPmtReqId = None

	@property
	def RjctnRsn(self):
		return self._RjctnRsn

	@RjctnRsn.setter
	def RjctnRsn(self, value):
		self._RjctnRsn = value if type(value) != base_types.auto else self.make_default("RjctnRsn")

	@RjctnRsn.deleter
	def RjctnRsn(self):
		del self._RjctnRsn
		self._RjctnRsn = None

	@property
	def RjctnRsnInf(self):
		return self._RjctnRsnInf

	@RjctnRsnInf.setter
	def RjctnRsnInf(self, value):
		self._RjctnRsnInf = value if type(value) != base_types.auto else self.make_default("RjctnRsnInf")

	@RjctnRsnInf.deleter
	def RjctnRsnInf(self):
		del self._RjctnRsnInf
		self._RjctnRsnInf = None

	@property
	def RspnTp(self):
		return self._RspnTp

	@RspnTp.setter
	def RspnTp(self, value):
		self._RspnTp = value if type(value) != base_types.auto else self.make_default("RspnTp")

	@RspnTp.deleter
	def RspnTp(self):
		del self._RspnTp
		self._RspnTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IntrstPmtReqId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctnRsn', type=RejectionReason21FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctnRsnInf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnTp', type=Status4Code, min=1, max=1, mutex_group=None, array=False),
	))

