# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import RejectionReason68Code
from . import Status4Code

class SecuritiesCollateralResponse2(base_types._BaseFieldType):

	__slots__ = ["_AsstNb", "_CollId", "_RjctnInf", "_RjctnRsn", "_RspnTp"]
	@property
	def AsstNb(self):
		return self._AsstNb

	@AsstNb.setter
	def AsstNb(self, value):
		self._AsstNb = value if value is not None else base_types.UninitialisedField(self, 'AsstNb', Max35Text, False)

	@AsstNb.deleter
	def AsstNb(self):
		del self._AsstNb
		self._AsstNb = base_types.UninitialisedField(self, 'AsstNb', Max35Text, False)

	@property
	def CollId(self):
		return self._CollId

	@CollId.setter
	def CollId(self, value):
		self._CollId = value if value is not None else base_types.UninitialisedField(self, 'CollId', Max35Text, False)

	@CollId.deleter
	def CollId(self):
		del self._CollId
		self._CollId = base_types.UninitialisedField(self, 'CollId', Max35Text, False)

	@property
	def RjctnInf(self):
		return self._RjctnInf

	@RjctnInf.setter
	def RjctnInf(self, value):
		self._RjctnInf = value if value is not None else base_types.UninitialisedField(self, 'RjctnInf', Max35Text, False)

	@RjctnInf.deleter
	def RjctnInf(self):
		del self._RjctnInf
		self._RjctnInf = base_types.UninitialisedField(self, 'RjctnInf', Max35Text, False)

	@property
	def RjctnRsn(self):
		return self._RjctnRsn

	@RjctnRsn.setter
	def RjctnRsn(self, value):
		self._RjctnRsn = value if value is not None else base_types.UninitialisedField(self, 'RjctnRsn', RejectionReason68Code, False)

	@RjctnRsn.deleter
	def RjctnRsn(self):
		del self._RjctnRsn
		self._RjctnRsn = base_types.UninitialisedField(self, 'RjctnRsn', RejectionReason68Code, False)

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
		base_types.FieldEntry(name='AsstNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctnInf', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctnRsn', type=RejectionReason68Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnTp', type=Status4Code, min=1, max=1, mutex_group=None, array=False),
	))