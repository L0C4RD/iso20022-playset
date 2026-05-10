from . import base_types
from ._Max35Text import Max35Text
from ._RejectionReason68Code import RejectionReason68Code
from ._Status4Code import Status4Code

class SecuritiesCollateralResponse2(base_types._BaseFieldType):

	__slots__ = ["_CollId", "_RspnTp", "_AsstNb", "_RjctnRsn", "_RjctnInf"]
	@property
	def CollId(self):
		return self._CollId

	@CollId.setter
	def CollId(self, value):
		self._CollId = value if type(value) != base_types.auto else self.make_default("CollId")

	@CollId.deleter
	def CollId(self):
		del self._CollId
		self._CollId = None

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

	@property
	def AsstNb(self):
		return self._AsstNb

	@AsstNb.setter
	def AsstNb(self, value):
		self._AsstNb = value if type(value) != base_types.auto else self.make_default("AsstNb")

	@AsstNb.deleter
	def AsstNb(self):
		del self._AsstNb
		self._AsstNb = None

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
	def RjctnInf(self):
		return self._RjctnInf

	@RjctnInf.setter
	def RjctnInf(self, value):
		self._RjctnInf = value if type(value) != base_types.auto else self.make_default("RjctnInf")

	@RjctnInf.deleter
	def RjctnInf(self):
		del self._RjctnInf
		self._RjctnInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnTp', type=Status4Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AsstNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctnRsn', type=RejectionReason68Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctnInf', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

